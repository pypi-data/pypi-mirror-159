from typing import Iterable, List
import pandas as pd
from copy import copy
import numpy as np

import naclo
import stse
from stse.dataframes import sync_na_drop
from naclo.__asset_loader import recognized_binarize_options
from naclo.__naclo_util import recognized_options_checker, check_columns_in_df

class Binarize:
    def __init__(self, df:pd.DataFrame, params:dict, options:dict) -> None:
        self.df = df.copy()
        
        self.__options = copy(options)
        recognized_options_checker(options, recognized_binarize_options)
        
        # Params
        self.__structure_col = params['structure_col']
        self.__structure_type = params['structure_type']
        self.__target_col = params['target_col']  # Set to standard_value col if doing unit conversion
        self.__decision_boundary = params['decision_boundary']
        
        # Drop NA structures and targets
        self.df = stse.dataframes.convert_to_nan(self.df)
        self.df.dropna(subset=[self.__structure_col], inplace=True)
        self.df.dropna(subset=[self.__target_col], inplace=True)
        
        # Check all needed columns exist in df
        cols_to_check = [self.__structure_col, self.__target_col]
        if self.__options['convert_units']['run']:
            cols_to_check.append(self.__options['convert_units']['units_col'])
        if self.__options['qualifiers']['run']:
            cols_to_check.append(self.__options['qualifiers']['qualifier_col'])
        check_columns_in_df(self.df, cols_to_check)
    
    def __mol_weights(self) -> List[float]:
        if self.__structure_type == 'smiles':
            mols = naclo.smiles_2_mols(self.df[self.__structure_col])
        elif self.__structure_type == 'mol':
            mols = self.df[self.__structure_col]
        return naclo.mol_stats.mol_weights(mols)
        
    def convert_units(self, output_units) -> pd.DataFrame:
        # target_col == standard_value col in this case
        mws = self.__mol_weights()
        unit_converter = naclo.UnitConverter(values=self.df[self.__target_col],
                                             units=self.df[self.__options['convert_units']['units_col']],
                                             mol_weights=mws)
        if output_units == 'neg_log_molar':
            return unit_converter.to_neg_log_molar()
        elif output_units == 'molar':
            return unit_converter.to_molar()
        elif output_units == 'nanomolar':
            return unit_converter.to_molar()*1e9
        else:
            raise ValueError(f'Unrecognized output units: {output_units}')
        
    def _binarize(self, values:Iterable) -> np.array:
        if self.__options['qualifiers']['run']:
            col = self.__options['qualifiers']['qualifier_col']
            
            self.df, values = sync_na_drop(self.df, col, values, all_na=True)
            
            qualifiers = self.df[col].tolist()
        else:
            qualifiers = None
        
        binarizer = stse.Binarizer(values=values, boundary=self.__decision_boundary,
                                          active_operator=self.__options['active_operator'], qualifiers=qualifiers)
        return binarizer.binarize()
    
    def main(self) -> pd.DataFrame:
        if self.__options['convert_units']['run']:
            # Convert and append units
            output_units = self.__options['convert_units']['output_units']
            converted_values = self.convert_units(output_units).tolist()
            
            self.df[f'{output_units}_{self.__target_col}'] = converted_values
            self.df[f'binarized_{self.__target_col}'] = self._binarize(converted_values)
        else:
            self.df[f'binarized_{self.__target_col}'] = self._binarize(self.df[self.__target_col].tolist())
            
        return self.df
