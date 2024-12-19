import pandas as pd
import NASS_Utils
import NASS_Constants

# Assign raw and clean directories
nass_raw_directory = 'NASS/raw'
nass_clean_directory = 'NASS/clean'

# Setting output filename
nass_injury_output_filename = nass_clean_directory + '/NASS_INJURY_CLEANED_1997_TO_2015.csv'

# Using the clean_sas_files to loop through the occupant injury sas table for each year from
# 1997 to 2015 and combining all these datasets to output an encompassing injury csv dataset 
NASS_Utils.clean_sas_files(nass_raw_directory, NASS_Constants.nass_1997_to_2015_paths, 
                           NASS_Constants.nass_1997_to_2015_injury_file_ending, 
                           NASS_Constants.nass_1997_to_2015_injury_output_columns,
                           NASS_Constants.nass_injury_col_specific_value_maps,
                           NASS_Constants.nass_global_value_map, nass_injury_output_filename)
