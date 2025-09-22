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

    # Loop through each file type in the year folder and place in dictionary
    for file_ending in NASS_Constants.nass_1988_to_1996_file_ending_map.keys():        
        current_file = clean_nass_patient_files(file_ending).dropna(axis=1, how='all')
        nass_pt_dict_df_1988_to_1996[file_ending] = current_file
    
    # Remove redundant columns
    file_w_redundant_col = ['interior vehicle', 'occupant assessment']
    cols_to_drop = ["PSUWGT", "NATWGT", "RATWGT", "STRATIF", "VERSION"]
    for file in file_w_redundant_col:
        existing_cols = [col for col in cols_to_drop if col in nass_pt_dict_df_1988_to_1996[file].columns]
        nass_pt_dict_df_1988_to_1996[file] = nass_pt_dict_df_1988_to_1996[file].drop(columns = existing_cols, axis=1)

    # Combine dataframes from different file endings into a single dataframe on the shared keys
    dfs = [nass_pt_dict_df_1988_to_1996['occupant assessment'], 
                    nass_pt_dict_df_1988_to_1996['general vehicle'], 
                    nass_pt_dict_df_1988_to_1996['interior vehicle']]
    
    nass_patient_df_1988_to_1996 = reduce(lambda left, right: pd.merge(left, right, on=['PSU', 'CASEID', 'VEHNO', 'YEAR'], how='left'), dfs)

    # Add Binary Seatbelt Variable
    manual = (nass_patient_df_1988_to_1996['MANUSE']=='Lap and shoulder belt') & (nass_patient_df_1988_to_1996['MANPROPR']=='Used Properly')
    automatic = (nass_patient_df_1988_to_1996['ABELTUSE']=='Automatic belt in use') & (nass_patient_df_1988_to_1996['ABLTPROP']=='Used Properly')
    nass_patient_df_1988_to_1996['BINARYBELTUSE'] = (manual | automatic)

    nass_patient_df_1988_to_1996.to_csv(nass_patient_output_filename, encoding='utf-8', index=False)

compile_annual_nass_patient_files()