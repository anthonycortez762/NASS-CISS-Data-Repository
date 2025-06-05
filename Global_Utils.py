import pandas as pd

def clean_column_values(df, col_specific_value_maps, global_value_map):
    # Avoids warnings about downcasting
    pd.set_option('future.no_silent_downcasting', True)
    for col_name, col_map_list in col_specific_value_maps.items():
        # Check if the column exists in the DataFrame
        if col_name in df.columns:
            #Avoids warnings about data type changes by converting to object
            df[col_name] = df[col_name].astype(object)
            for col_map in col_map_list:
                for map_range in col_map['ranges']:
                    # Apply replacement mapping only for the rows within the specified range
                    mask = df['YEAR'].between(map_range['start'], map_range['end'])
                    if mask.any():  # Ensure there are rows in the specified range
                        df.loc[mask, col_name] = (
                            df.loc[mask, col_name].replace(col_map['mapping'])
                        )
                        
    # Apply global value map to all columns
    df = df.replace(global_value_map)
    return df
