"""
    Injury Table Notes
    - CISS doesn't record the LESION, SYSORG, ASPECT90 and SOUDAT columns from NASS (pgs. 518-520 in Crash Investigation Sampling System, 2021 Analytical User’s Manual)
    - Instead of the LESION and SYSORG columns from NASS, we will keep the STRUTYPE and STRUSPEC columns that cover a lot of the same data
    - We will also pull in the L1, L2, and LDEF columns from the localizer table instead of the ASPECT90 column from NASS to further specify the localization of the injury
    - Users are cautioned that ASPECT90 does not easily map to L1. Users should use caution when comparing. (pg. 515 in Crash Investigation Sampling System, 2021 Analytical User’s Manual)
"""

# Import injury constants and functions
import CISS_Utils
import CISS_Constants
import Global_Utils

# Assign raw and clean directories
injury_raw_zipped_directory = '../raw'
injury_clean_directory = '../clean'

# Setting the list of input filenames and the output filename
injury_input_filename_list = ['INJURY', 'LOCALIZER']
injury_output_filename = injury_clean_directory + '/INJURY_CLEANED.csv'

# Using the clean_zip_files function to join the injury and localizer files for each year in CISS
# and then union each years file into an injury dataset
ciss_injury_df = CISS_Utils.clean_zip_files(injury_raw_zipped_directory, injury_input_filename_list,
                                            CISS_Constants.injury_join_columns_list,
                                            CISS_Constants.injury_use_cols_list, CISS_Constants.injury_output_columns)

ciss_injury_df = Global_Utils.clean_column_values(ciss_injury_df, CISS_Constants.ciss_injury_col_specific_value_maps, {})

ciss_injury_df.to_csv(injury_output_filename, encoding='utf-8', index=False)
