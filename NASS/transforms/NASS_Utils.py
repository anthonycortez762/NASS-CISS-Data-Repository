import os
import pandas as pd


def rename_and_union_dfs(raw_directory, file_paths, file_ending, base_file_path, col_name_maps):
    output_dataframes = []

    # For each file path we will read in the relevant csv file, and we will map the column names of the files
    # included in the col_name_maps dictionary
    for file in file_paths:
        output_df = pd.read_csv(os.path.join(raw_directory, file, file_ending), dtype=str)
        if file in col_name_maps.keys():
            output_df = output_df.rename(columns=col_name_maps[file])
        # Here we select the relevant columns using the base_file_path, add a year column, and append each file
        # to a list to then union
        output_df = output_df[col_name_maps[base_file_path].values()]
        output_df['YEAR'] = int(file.split('_')[1])
        output_dataframes.append(output_df)

    final_df = pd.concat(output_dataframes)
    return final_df
