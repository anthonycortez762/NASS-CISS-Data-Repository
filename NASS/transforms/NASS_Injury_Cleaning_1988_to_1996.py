import NASS_Constants
import NASS_Utils
import Global_Utils
import pandas as pd

# Assign raw and clean directories
nass_raw_directory = '../raw'
nass_clean_directory = '../clean'

# Setting output filename
nass_injury_output_filename = nass_clean_directory + '/NASS_INJURY_CLEANED_1988_TO_1996.csv'

def is_integer(value):
    try:
        int(value)
        return True
    except ValueError:
        return False

def add_ais_code(injury_file):
    ais_components = ['REGION90', 'STRUTYPE', 'STRUSPEC', 'INJLEVEL', 'AIS']
    print(injury_file['REGION90'].unique())
    injury_file[ais_components] = injury_file[ais_components].applymap(lambda x: str(int(x)) if pd.notna(x) and is_integer(x) else pd.NA)

    injury_file['STRUSPEC'] = injury_file['STRUSPEC'].str.zfill(2)
    injury_file['INJLEVEL'] = injury_file['INJLEVEL'].str.zfill(2)

    injury_file['AISCODE'] = injury_file['REGION90'] + injury_file['STRUTYPE'] + injury_file['STRUSPEC'] + injury_file['INJLEVEL'] + '.' + injury_file['AIS']
    print(injury_file['AISCODE'].head(20))

def clean_nass_injury_files():
    """
    :return:
    """
    nass_injury_df_1988_to_1996 = NASS_Utils.rename_and_union_dfs(
        raw_directory=nass_raw_directory,
        file_paths=NASS_Constants.nass_1988_to_1996_paths,
        file_ending='occupant injury',
        desired_columns=NASS_Constants.injury_cols,
        col_name_maps=NASS_Constants.nass_1988_to_1996_injury_col_name_maps
    )

    add_ais_code(nass_injury_df_1988_to_1996)

    # Filter out injuries where all injury descriptor columns are NaN
    nass_injury_df_1988_to_1996 = nass_injury_df_1988_to_1996.dropna(
        subset=['AIS', 'ASPECT', 'BODYREG', 'LESION', 'SYSORG'], how='all')
    final_nass_injury_df_1988_to_1996 = Global_Utils.clean_column_values(
        nass_injury_df_1988_to_1996,
        NASS_Constants.nass_injury_col_specific_value_maps,
        NASS_Constants.nass_global_value_map
    )    
    final_nass_injury_df_1988_to_1996.to_csv(nass_injury_output_filename, encoding='utf-8', index=False)


clean_nass_injury_files()
