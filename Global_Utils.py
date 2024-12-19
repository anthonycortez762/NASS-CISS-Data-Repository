def clean_column_values(df, col_specific_value_maps, global_value_map):
    for col_name, col_map_list in col_specific_value_maps.items():
        for col_map in col_map_list:
            for map_range in col_map['ranges']:
                df.loc[df['YEAR'].between(map_range['start'], map_range['end']), col_name] = (
                    df.loc[df['YEAR'].between(map_range['start'], map_range['end']), col_name].replace(col_map['mapping'])
                )
    df = df.replace(global_value_map)
    return df
