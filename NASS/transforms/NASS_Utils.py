import os

import NASS_Constants
import pandas as pd

def get_file_endings_nass_1988_to_1996(file_content, year):
    file_content_mapped = NASS_Constants.nass_1988_to_1996_file_ending_map[file_content]
    return file_content_mapped + year + '.csv'

def rename_and_union_dfs(raw_directory, file_paths, file_ending, desired_columns, col_name_maps):
    """
    :param raw_directory:
    :param file_paths:
    :param file_ending:
    :param desired_columns:
    :param col_name_maps:
    :return: union of dataframes, each containing NASS data for a particular year
    """
    output_dataframes = []

    # For each file path we will read in the relevant csv file, and we will map the column names of the files
    # included in the col_name_maps dictionary
    for file in file_paths:
        # Apply correct file name for the year's naming convention
        if file in NASS_Constants.nass_1988_to_1996_paths:
            file_ending_fixed = get_file_endings_nass_1988_to_1996(file_ending, file.split('_')[1])
        else: file_ending_fixed = file_ending
        output_df = pd.read_csv(os.path.join(raw_directory, file, file_ending_fixed), dtype=str)
        if file in col_name_maps.keys():
            output_df = output_df.rename(columns=col_name_maps[file])
        # Here we select the relevant columns using the base_file_path, add a year column, and append each file
        # to a list to then union
        output_df = output_df.reindex(columns=desired_columns)
        output_df['YEAR'] = int(file.split('_')[1])
        output_dataframes.append(output_df)

    final_df = pd.concat(output_dataframes)
    return final_df
