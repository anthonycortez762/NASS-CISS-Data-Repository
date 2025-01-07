# Import patient constants and functions
import CISS_Utils
import CISS_Constants
import Global_Utils

# Assign raw and clean directories
patient_raw_zipped_directory = '../raw'
patient_clean_directory = '../clean'

# Setting input file name lists and output filename
patient_base_input_filename_list = ['OCC', 'EJECT', 'GV', 'CRASH']
intrusion_filename_list = ['INTRUSION']
patient_output_filename = patient_clean_directory + '/PATIENT_CLEANED.csv'

# Setting variables for commonly used column names and filter lists
intrusion_column_name = 'INTRUSION'
intrusion_direction_column_name = 'INTDIRECT'
intrusion_value_and_magnitude_column_list = ['INTRUSION', 'INTMAG']
lateral_and_longitudinal_intrusion_directions = ['2', '3']

# Using the clean_zip_files function to join the occupant, eject, gv and crash files for each year in CISS
# and then union each years file into a base patient dataset
ciss_patient_df = CISS_Utils.clean_zip_files(patient_raw_zipped_directory, patient_base_input_filename_list,
                                             CISS_Constants.patient_join_columns_list,
                                             CISS_Constants.patient_use_cols_list,
                                             CISS_Constants.patient_output_columns)

# Using the clean_zip_files function to union each years intrusion file into an intrusion dataset
ciss_intrusion_df = CISS_Utils.clean_zip_files(patient_raw_zipped_directory, intrusion_filename_list,
                                               [], [], CISS_Constants.intrusion_output_columns)

# Filter to lateral and longitudinal intrusions
ciss_intrusion_df = ciss_intrusion_df[ciss_intrusion_df[intrusion_direction_column_name].isin(lateral_and_longitudinal_intrusion_directions)]

# Convert intrusion value and magnitude columns to Int64 and then map unknown and N/A intrusion values and magnitudes
# to null before aggregating
ciss_intrusion_df[intrusion_value_and_magnitude_column_list] = ciss_intrusion_df[intrusion_value_and_magnitude_column_list].astype('Int64')
ciss_intrusion_df = Global_Utils.clean_column_values(ciss_intrusion_df, CISS_Constants.ciss_intrusion_col_specific_value_maps, {})

# Using pivot_and_join_dfs function to calculate the max lateral and longitudinal intrusions by seat location and
# join them into the patient dataframe
ciss_patient_df = CISS_Utils.pivot_and_join_dfs(ciss_patient_df, ciss_intrusion_df,
                                                intrusion_value_and_magnitude_column_list,
                                                CISS_Constants.seat_loc_intrusion_column_list,
                                                intrusion_direction_column_name, 'max',
                                                CISS_Constants.max_intrusion_by_seat_loc_column_map,
                                                CISS_Constants.seat_loc_intrusion_column_list)

# Using pivot_and_join_dfs function to calculate the max lateral and longitudinal intrusions by vehicle and
# join them into the patient dataframe
ciss_patient_df = CISS_Utils.pivot_and_join_dfs(ciss_patient_df, ciss_intrusion_df,
                                                intrusion_value_and_magnitude_column_list,
                                                CISS_Constants.intrusion_base_column_list,
                                                intrusion_direction_column_name, 'max',
                                                CISS_Constants.max_intrusion_by_vehicle_column_map,
                                                CISS_Constants.intrusion_base_column_list)

ciss_patient_df = Global_Utils.clean_column_values(ciss_patient_df, CISS_Constants.ciss_patient_col_specific_value_maps, {})

ciss_patient_df.to_csv(patient_output_filename, encoding='utf-8', index=False)
