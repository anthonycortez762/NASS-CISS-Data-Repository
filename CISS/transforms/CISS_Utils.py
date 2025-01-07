import os
import zipfile
import pandas as pd
from pathlib import Path
import CISS_Constants


def get_file_path(name, filenames):
    for filename in filenames:
        # Comparing name to filename without its file extension (i.e. '.csv')
        if name.upper() == Path(filename).stem.upper():
            return filename


def clean_zip_files(zipped_directory, filename_list, join_columns_list, use_cols_list, output_df_columns):
    output_dataframes = []

    # Iterate over each zip file in the raw directory
    for filename in os.listdir(zipped_directory):
        f = os.path.join(zipped_directory, filename)
        with zipfile.ZipFile(f, 'r') as z:
            # Filenames are not standard in CISS, so we will search through list of filenames from the zip file to
            # find the filepaths for each year and open the relevant files
            filenames = z.namelist()
            output_df = pd.DataFrame()

            # Here we will also determine the file year from the file path and the encoding for each file
            # CISS files from 2017-2021 used latin1 encoding whereas CISS files from 2022 used utf-8 encoding
            file_year = filename.split('_')[1]
            file_encoding = 'latin1' if file_year in CISS_Constants.ciss_years_with_wlatin1_encoding else 'utf-8'

            # Now we will loop through the list of filenames and join the files together
            for index, zipped_file in enumerate(filename_list, start=-1):
                with z.open(get_file_path(zipped_file, filenames)) as opened_file:
                    if output_df.empty:
                        output_df = pd.read_csv(opened_file, dtype=str, encoding=file_encoding)
                    else:
                        output_df = pd.merge(output_df,
                                             pd.read_csv(opened_file, dtype=str, encoding=file_encoding,
                                                         usecols=use_cols_list[index]),
                                             how='left', on=join_columns_list[index])

            output_df['YEAR'] = int(file_year)
            output_df = output_df.filter(output_df_columns)

            output_dataframes.append(output_df)

    # Combine each year's dataframe and return the combined dataframe
    final_df = pd.concat(output_dataframes)
    return final_df


def pivot_and_join_dfs(base_df, unpivoted_df, aggregation_column_list, index_column_list, groupby_column,
                       aggregation_function, column_map, join_columns):
    # First we will create a pivot table to calculate the aggregated metrics
    pivoted_df = pd.pivot_table(unpivoted_df, values=aggregation_column_list, index=index_column_list,
                                columns=groupby_column, aggfunc=aggregation_function)
    # If the pivot table is a MultiIndex we will collapse the newly derived columns
    if isinstance(pivoted_df.columns, pd.MultiIndex):
        pivoted_df.columns = pivoted_df.columns.to_series().str.join('_')

    pivoted_df = pivoted_df.reset_index().rename(columns=column_map)

    # Lastly we will join the aggregated data with the base df
    joined_df = pd.merge(base_df, pivoted_df, how='left', on=join_columns)
    return joined_df
