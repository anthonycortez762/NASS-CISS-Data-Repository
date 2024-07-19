import NASS_Constants
import NASS_Utils
import Global_Utils

# Assign raw and clean directories
nass_raw_directory = '../raw'
nass_clean_directory = '../clean'

# Setting output filename
nass_patient_output_filename = nass_clean_directory + '/NASS_PATIENT_CLEANED_1979_to_1987.csv'


def clean_nass_patient_files():
    # For each year of NASS we will use rename_and_union_dfs to read in the relevant occupant csv file
    # For NASS 1979, 1980 and 1981, we will map their respective column names to match the column names from 1982-1987
    # and union the occupant files from 1979 to 1987 together
    nass_patient_df_1979_to_1987 = NASS_Utils.rename_and_union_dfs(nass_raw_directory,
                                                                   NASS_Constants.nass_1979_to_1987_paths,
                                                                   NASS_Constants.nass_occupant_file_ending,
                                                                   NASS_Constants.nass_1979_path,
                                                                   NASS_Constants.nass_1979_to_1981_patient_col_name_maps)

    nass_patient_df_1979_to_1987 = Global_Utils.clean_column_values(nass_patient_df_1979_to_1987,
                                                                    NASS_Constants.nass_patient_col_specific_value_maps,
                                                                    NASS_Constants.nass_global_value_map)

    nass_patient_df_1979_to_1987.to_csv(nass_patient_output_filename, encoding='utf-8', index=False)


clean_nass_patient_files()
