import NASS_Utils
import NASS_Constants
import Global_Utils
from functools import reduce
import pandas as pd

# Assign raw and clean directories
nass_raw_directory = '../raw'
nass_clean_directory = '../clean'

# Setting output filename
nass_patient_output_filename = nass_clean_directory + '/NASS_PATIENT_CLEANED_1997_TO_2015.csv'
file_endings = [NASS_Constants.nass_1997_to_2015_occupant_file_ending, NASS_Constants.nass_1997_to_2015_vehicle_file_ending, NASS_Constants.nass_1997_to_2015_gen_vehicle_file_ending]

# Using the clean_sas_files to loop through the occupant assessment sas table for each year from
# 1997 to 2015 and combining all these datasets to output an encompassing patient csv dataset 
nass_1997_to_2015_output_dfs = []

for file_ending in file_endings:
    output_df = NASS_Utils.clean_sas_files(nass_raw_directory,
                                            NASS_Constants.nass_1997_to_2015_paths,
                                            file_ending,
                                            NASS_Constants.nass_1997_to_2015_patient_columns_to_convert_to_int,
                                            NASS_Constants.nass_1997_to_2015_patient_output_columns)
    nass_1997_to_2015_output_dfs.append(output_df)

nass_occupant_df_1997_to_2015 = reduce(lambda left, right: pd.merge(left, right, on=['PSU', 'YEAR', 'CASEID', 'VEHNO'], how="left"), nass_1997_to_2015_output_dfs)
nass_occupant_df_1997_to_2015 = nass_occupant_df_1997_to_2015.loc[:, ~nass_occupant_df_1997_to_2015.columns.str.contains("_")]
    
nass_occupant_df_1997_to_2015 = Global_Utils.clean_column_values(nass_occupant_df_1997_to_2015,
                                                                 NASS_Constants.nass_patient_col_specific_value_maps,
                                                                 NASS_Constants.nass_global_value_map)

# Creates BELTUSE column that is binary - either they were properly using an adult seatbelt or not. 
# This will align with CISS column for seatbelt use.
manual_1997_to_2003 = (nass_occupant_df_1997_to_2015['MANUSE']=='Lap and shoulder belt') & (nass_occupant_df_1997_to_2015['MANPROPR']=='Used Properly') & (nass_occupant_df_1997_to_2015['YEAR']<2003) 
automatic_1997_to_2003 = (nass_occupant_df_1997_to_2015['ABELTUSE']=='Belt In Use') & (nass_occupant_df_1997_to_2015['ABLTPROP']=='Used Properly') & (nass_occupant_df_1997_to_2015['YEAR']<2003) 
manual_2003_to_2015 = (nass_occupant_df_1997_to_2015['MANUSE']=='Lap and shoulder belt') & (nass_occupant_df_1997_to_2015['YEAR']>=2003) 
automatic_2003_to_2015 = (nass_occupant_df_1997_to_2015['ABELTUSE']=='Belt In Use') & (nass_occupant_df_1997_to_2015['YEAR']>=2003) 
nass_occupant_df_1997_to_2015['BINARYBELTUSE'] = manual_1997_to_2003 | automatic_1997_to_2003 | manual_2003_to_2015 | automatic_2003_to_2015

nass_occupant_df_1997_to_2015.to_csv(nass_patient_output_filename, encoding='utf-8', index=False)
