import os
import pandas as pd
import NASS_Constants


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


def add_ais_code(df):
    df['AISCODE'] = (df['REGION90'] + df['STRUTYPE'] + df['STRUSPEC'].str.zfill(2) + df['INJLEVEL'].str.zfill(2) + '.'
                     + df['AIS'])
    return df


def clean_sas_files(raw_directory, file_paths, file_ending, columns_to_convert_to_int, output_df_columns):
    output_dataframes = []
    
    for file in file_paths:
        output_df = pd.read_sas(os.path.join(raw_directory, file, file_ending), encoding='cp1252')
        # Harmonize column names (Needed for 2001 to 2010 where BODY, LESION and SYSORG are not upper case)
        output_df.columns = [col.upper() if not col.isupper() else col for col in output_df.columns]

        # Converts float values to integers if whole numbers, then converts all columns to string type
        for col in columns_to_convert_to_int:
            output_df[col] = (output_df[col].astype("Int64").astype(str).replace(
                              NASS_Constants.nass_1997_to_2015_null_values, None))
        output_df = output_df.astype(str).replace(NASS_Constants.nass_1997_to_2015_null_values, None)

        output_df = output_df.filter(output_df_columns)
        remove_space(output_df, output_df.columns.to_list())
        output_df['YEAR'] = int(file.split('_')[1])
        output_dataframes.append(output_df)

    final_df = pd.concat(output_dataframes)

    return final_df
