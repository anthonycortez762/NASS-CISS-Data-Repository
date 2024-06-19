def get_file_path(name, filenames):
    for filename in filenames:
        if name.upper() == filename[:-4].upper():
            return filename


def clean_column_values(df, column_maps):
    for col_name, col_map in column_maps.items():
        df[col_name] = df[col_name].replace(col_map)