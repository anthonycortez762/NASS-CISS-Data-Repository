import os
import zipfile
import pandas as pd
from pathlib import Path


def get_file_path(name, filenames):
    for filename in filenames:
        # Comparing name to filename without its file extension (i.e. '.csv')
        if name.upper() == Path(filename).stem.upper():
            return filename


def clean_column_values(df, column_maps):
    for col_name, col_map in column_maps.items():
        df[col_name] = df[col_name].replace(col_map)


def clean_zip_files(zipped_directory, first_filename, second_filename, join_columns, output_df_columns,
                    output_df_column_maps, output_filename):
    output_dataframes = []

    # Iterate over each zip file in the raw directory
    for filename in os.listdir(zipped_directory):
        f = os.path.join(zipped_directory, filename)
        with zipfile.ZipFile(f, 'r') as z:
            # Filenames are not standard in CISS, so we will search through list of filenames from the zip file to
            # find the filepaths for each year and open the relevant files
            filenames = z.namelist()
            with z.open(get_file_path(first_filename, filenames)) as first_file:
                with z.open(get_file_path(second_filename, filenames)) as second_file:
                    output_df = pd.merge(pd.read_csv(first_file), pd.read_csv(second_file), how='left', on=join_columns)
                    output_df = output_df.filter(output_df_columns)

                    clean_column_values(output_df, output_df_column_maps)
                    output_dataframes.append(output_df)

    # Combine each year's dataframe and write the combined dataframe to a new file
    final_df = pd.concat(output_dataframes)
    final_df.to_csv(output_filename, encoding='utf-8', index=False)