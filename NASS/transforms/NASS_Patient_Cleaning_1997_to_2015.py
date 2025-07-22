import NASS_Utils
import NASS_Constants

# Assign raw and clean directories
nass_raw_directory = '../raw'
nass_clean_directory = '../clean'

# Setting output filename
nass_patient_output_filename = nass_clean_directory + '/NASS_PATIENT_CLEANED_1997_TO_2015.csv'

# Using the clean_sas_files to loop through the occupant assessment sas table for each year from
# 1997 to 2015 and combining all these datasets to output an encompassing patient csv dataset 
NASS_Utils.clean_sas_files(nass_raw_directory, 
                           NASS_Constants.nass_1997_to_2015_paths, 
                           NASS_Constants.nass_1997_to_2015_occupant_file_ending, 
                           NASS_Constants.nass_1997_to_2015_patient_output_columns,
                           NASS_Constants.nass_patient_col_specific_value_maps,
                           NASS_Constants.nass_global_value_map, 
                           nass_patient_output_filename)
