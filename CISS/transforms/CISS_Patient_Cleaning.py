# Import patient constants and functions
import utils
import constants

# Assign raw and clean directories
patient_raw_zipped_directory = '../raw'
patient_clean_directory = '../clean'

# Setting occupant, eject and output filenames
occupant_filename = 'OCC'
eject_filename = 'EJECT'
output_filename = patient_clean_directory + '/PATIENT_CLEANED.csv'

# Using the clean_zip_files function to join the occupant and eject files for each year in CISS
# and then union each years file into a patient dataset
utils.clean_zip_files(patient_raw_zipped_directory, occupant_filename, eject_filename,
                      constants.patient_join_columns, constants.patient_output_columns,
                      constants.patient_column_maps, output_filename)
