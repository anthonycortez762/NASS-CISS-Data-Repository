import NASS_Constants
import NASS_Utils
import Global_Utils

# Assign raw and clean directories
nass_raw_directory = '../raw'
nass_clean_directory = '../clean'

# Setting output filename
nass_injury_output_filename = nass_clean_directory + '/NASS_INJURY_CLEANED_1988_TO_1996.csv'


def clean_nass_injury_files():
    """
    :return:
    """
    nass_injury_df_1988_to_1996 = NASS_Utils.rename_and_union_dfs(
        raw_directory=nass_raw_directory,
        file_paths=NASS_Constants.nass_1988_to_1996_paths,
        file_ending=NASS_Constants.nass_oi_file_ending,
        desired_columns=NASS_Constants.injury_cols,
        col_name_maps=NASS_Constants.nass_1988_to_1996_injury_col_name_maps
    )

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
