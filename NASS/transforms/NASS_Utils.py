import os
import sys
import pandas as pd
import numpy as np
import math

# Add the root directory to sys.path
# sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
import Global_Utils

def is_float(x):
    try:
        return isinstance(x, float) or (float(x) == float(x))  # This still catches strings like "1.0"
    except (ValueError, TypeError):
        return False

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
        output_df = pd.read_csv(os.path.join(raw_directory, file, file_ending), dtype=str)
        if file in col_name_maps.keys():
            output_df = output_df.rename(columns=col_name_maps[file])
        # Here we select the relevant columns using the base_file_path, add a year column, and append each file
        # to a list to then union
        output_df = output_df[desired_columns]
        output_df['YEAR'] = int(file.split('_')[1])
        output_dataframes.append(output_df)

    final_df = pd.concat(output_dataframes)
    return final_df


def remove_space(df, columns_to_clean):
    for column in columns_to_clean:
        # Remove empty space preceding any string values
        if df[column].apply(lambda x: isinstance(x, str)).any():
            df[column] = df[column].apply(lambda x: x.lstrip() if isinstance(x, str) else x)
    return df

def add_ais_code(injury_file):
    ais_components = ['REGION90', 'STRUTYPE', 'STRUSPEC', 'INJLEVEL', 'AIS']
    print(injury_file.head(20))
    injury_file[ais_components] = injury_file[ais_components].applymap(lambda x: str(int(x)) if pd.notna(x) and not x == "<NA>" else pd.NA)

    injury_file['STRUSPEC'] = injury_file['STRUSPEC'].str.zfill(2)
    injury_file['INJLEVEL'] = injury_file['INJLEVEL'].str.zfill(2)

    injury_file['AISCODE'] = injury_file['REGION90'] + injury_file['STRUTYPE'] + injury_file['STRUSPEC'] + injury_file['INJLEVEL'] + '.' + injury_file['AIS']


def clean_sas_files(raw_directory, file_paths, file_ending, output_df_columns, output_df_column_maps, global_value_map, output_filename):
    output_dataframes = []
    
    for file in file_paths:
        output_df = pd.read_sas(os.path.join(raw_directory, file, file_ending), encoding='cp1252')
        # Converts float values to integers if whole numbers, then converts all columns to string type
        output_df = output_df.replace({np.nan: pd.NA})
        for col in output_df.columns:
            output_df[col] = output_df[col].map(lambda x: int(x) if is_float(x) and not pd.isna(x) and float(x).is_integer() else x)  
            if output_df[col].map(lambda x: pd.isna(x) or isinstance(x, int)).all():
                output_df[col] = output_df[col].astype("Int64")
        output_df = output_df.astype(str)
        # Harmonize column names (Neded for 2001 to 2010 where BODY, LESION and SYSORG are not upper case)
        output_df.columns = [col.upper() if not col.isupper() else col for col in output_df.columns]
        output_df = output_df.filter(output_df_columns)

        remove_space(output_df, output_df.columns.to_list())
        output_df['YEAR'] = int(file.split('_')[1])
        output_dataframes.append(output_df)

    final_df = pd.concat(output_dataframes)

    final_nass_injury_df_1997_to_2015 = Global_Utils.clean_column_values(final_df, output_df_column_maps, global_value_map)

    if set(['REGION90', 'STRUTYPE', 'STRUSPEC', 'INJLEVEL', 'AIS']).issubset(final_nass_injury_df_1997_to_2015.columns):
        add_ais_code(final_nass_injury_df_1997_to_2015)

    print(final_nass_injury_df_1997_to_2015.head(20))
    print(final_nass_injury_df_1997_to_2015['AISCODE'].head(20))

    final_nass_injury_df_1997_to_2015.to_csv(output_filename, encoding='utf-8', index=False)