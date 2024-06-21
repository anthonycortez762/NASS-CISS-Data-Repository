"""
    Injury Table Notes
    - CISS doesn't record the LESION, SYSORG, ASPECT90 and SOUDAT columns from NASS (pgs. 518-520 in Crash Investigation Sampling System, 2021 Analytical User’s Manual)
    - Instead of the LESION and SYSORG columns from NASS, we will keep the STRUTYPE and STRUSPEC columns that cover a lot of the same data
    - We will also pull in the L1, L2, and LDEF columns from the localizer table instead of the ASPECT90 column from NASS to further specify the localization of the injury
    - Users are cautioned that ASPECT90 does not easily map to L1. Users should use caution when comparing. (pg. 515 in Crash Investigation Sampling System, 2021 Analytical User’s Manual)
"""

# Import injury constants and functions
import utils
import constants

# Assign raw and clean directories
injury_raw_zipped_directory = '../raw'
injury_clean_directory = '../clean'

# Setting injury, localizer and output filenames
injury_filename = 'INJURY'
localizer_filename = 'LOCALIZER'
output_filename = injury_clean_directory + '/INJURY_CLEANED.csv'

# Using the clean_zip_files function to join the injury and localizer files for each year in CISS
# and then union each years file into an injury dataset
utils.clean_zip_files(injury_raw_zipped_directory, injury_filename, localizer_filename,
                      constants.injury_join_columns, constants.injury_output_columns,
                      constants.injury_column_maps, output_filename)
