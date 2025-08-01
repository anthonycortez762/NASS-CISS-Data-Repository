import os
import sys

import NASS_Constants
import NASS_Utils
import Global_Utils
import pandas as pd
from functools import reduce

# Assign raw and clean directories
nass_raw_directory = '../raw'
nass_clean_directory = '../clean'

# Setting output filename
nass_patient_output_filename = nass_clean_directory + '/NASS_PATIENT_CLEANED_1988_to_1996.csv'

def merge_dfs_cleanly(left, right, on, how):
    existing_subset = [col for col in on if all(col in df.columns for df in [left, right])]
    # Find overlapping non-key columns
    shared = [col for col in left.columns if col in right.columns and col not in on]

    # Compare overlapping columns
    for col in shared:
        if not left[col].equals(right[col]):
            # If they're not equal, rename columns to avoid conflict
            return pd.merge(left, right, on=existing_subset, how=how, suffixes=('', '_dup'))

    # If all overlapping columns are identical, drop from right and merge
    right_clean = right.drop(columns=shared)
    return pd.merge(left, right_clean, on=existing_subset, how=how)

def clean_nass_patient_files(file_ending):
    # For each year of NASS we will use rename_and_union_dfs to read in the relevant occupant csv file
    # For NASS 1979, 1980 and 1981, we will map their respective column names to match the column names from 1982-1987
    # and union the occupant files from 1979 to 1987 together
    col_name_maps = NASS_Constants.nass_1988_to_1996_patient_col_name_maps
    desired_columns = col_name_maps.keys()
    nass_patient_df_1988_to_1996 = NASS_Utils.rename_and_union_dfs(
        raw_directory=nass_raw_directory,
        file_paths=NASS_Constants.nass_1988_to_1996_paths,
        file_ending=file_ending,
        desired_columns=desired_columns,
        col_name_maps=col_name_maps
    )
    # Rename each column in the dataframe to align with universal value names
    nass_patient_df_1988_to_1996 = Global_Utils.clean_column_values(
        nass_patient_df_1988_to_1996,
        NASS_Constants.nass_patient_col_specific_value_maps,
        NASS_Constants.nass_global_value_map
    )

    return nass_patient_df_1988_to_1996

# Combine each year's NASS patient files into a single dataframe
def compile_annual_nass_patient_files():
    nass_pt_dict_df_1988_to_1996 = {}

    # Loop through each file type in the year folder
    for file_ending in NASS_Constants.nass_1988_to_1996_file_ending_map.keys():        
        current_file = clean_nass_patient_files(file_ending).dropna(axis=1, how='all')
        
        # Remove columns that are entirely 'None'
        current_file = current_file.loc[:, ~(current_file == 'None').all()]
        
        # Specifies which file type each variable comes from if the same variable has different values in different file types
        for col in NASS_Constants.nass_1988_to_1996_file_specific_values:
            new_col_name = col + '_' + NASS_Constants.nass_1988_to_1996_file_ending_map[file_ending]
            if col in current_file.columns:
                current_file.rename(columns={col: new_col_name}, inplace=True)
        nass_pt_dict_df_1988_to_1996[file_ending] = current_file
    
    # Combine dataframes from different file endings into a single dataframe on the shared keys, 'subset'
    subset = ['PSU', 'CASEID', 'VEHNO', 'OCCNO', 'YEAR', 'INJNO', 'ACCSEQ']

    veh_lvl_dfs = [nass_pt_dict_df_1988_to_1996['accident'], nass_pt_dict_df_1988_to_1996['general vehicle'], nass_pt_dict_df_1988_to_1996['interior vehicle'], nass_pt_dict_df_1988_to_1996['exterior vehicle']]
    veh_lvl_merged = reduce(lambda left, right: merge_dfs_cleanly(left, right, on=subset, how='outer'), veh_lvl_dfs)

    all_lvl_dfs = [nass_pt_dict_df_1988_to_1996['occupant assessment'], veh_lvl_merged]
    all_lvl_merged = reduce(lambda left, right: merge_dfs_cleanly(left, right, on=subset, how='outer'), all_lvl_dfs)

    all_lvl_merged.to_csv(nass_patient_output_filename, encoding='utf-8', index=False)

compile_annual_nass_patient_files()