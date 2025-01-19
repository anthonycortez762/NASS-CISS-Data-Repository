from CISS_Injury_Value_Map import ciss_injury_col_specific_value_maps
from CISS_Patient_Value_Map import ciss_patient_col_specific_value_maps
from CISS_Intrusion_Value_Map import ciss_intrusion_col_specific_value_maps

# CISS Global Constants
ciss_global_value_map = {}

# CISS Injury Constants
injury_base_column_list = ['CASEID', 'CASENO', 'VEHNO', 'OCCNO', 'INJNO']
injury_additional_column_list = ['AISCODE', 'AIS', 'REGION', 'STRUTYPE', 'STRUSPEC', 'INJLEVEL']
injury_localizer_additional_column_list = ['L1', 'L2', 'LDEF']
injury_join_columns_list = [injury_base_column_list]
injury_use_cols_list = [injury_base_column_list + injury_additional_column_list,
                        injury_base_column_list + injury_localizer_additional_column_list]
injury_output_columns = (injury_base_column_list + ['YEAR'] + injury_additional_column_list
                         + injury_localizer_additional_column_list)

# CISS Patient Constants
patient_base_column_list = ['CASEID', 'PSU', 'CASENO']
patient_additional_column_list = ['AGE', 'SEX', 'HEIGHT', 'WEIGHT', 'ROLE', 'PARBELTUSE', 'PARAIRBAG',
                                  'SEATLOC', 'ENTRAP', 'EYEWEAR', 'HOSPSTAY', 'MOBILITY', 'MORTALITY', 'TREATMENT']
patient_join_columns_list = [patient_base_column_list + ['VEHNO', 'OCCNO'], patient_base_column_list + ['VEHNO'],
                             patient_base_column_list]
patient_use_cols_list = [patient_join_columns_list[0] + patient_additional_column_list,
                         patient_join_columns_list[0] + ['EJECTTYPE'],
                         patient_join_columns_list[1] + ['CURBWT', 'DVTOTAL'],
                         patient_base_column_list + ['EVENTS']]
patient_output_columns = patient_join_columns_list[0] + ['YEAR'] + patient_additional_column_list + ['EJECTTYPE',
                                                                                                     'CURBWT', 'DVTOTAL',
                                                                                                     'EVENTS']
intrusion_base_column_list = ['CASEID', 'PSU', 'CASENO', 'VEHNO']
intrusion_additional_column_list = ['INTRUNO', 'INTRUSION', 'INTMAG', 'INTDIRECT']
intrusion_use_cols_list = [intrusion_base_column_list + ['SEATLOC'] + intrusion_additional_column_list]
seat_loc_intrusion_column_list = intrusion_base_column_list + ['YEAR', 'SEATLOC']
intrusion_output_columns = seat_loc_intrusion_column_list + intrusion_additional_column_list
max_intrusion_by_seat_loc_column_map = {'INTMAG_2': 'MAXSEATLOCLONGITUDINALINTMAG',
                                        'INTMAG_3': 'MAXSEATLOCLATERALINTMAG',
                                        'INTRUSION_2': 'MAXSEATLOCLONGITUDINALINTRUSION',
                                        'INTRUSION_3': 'MAXSEATLOCLATERALINTRUSION'}
max_intrusion_by_vehicle_column_map = {'INTMAG_2': 'MAXVEHICLELONGITUDINALINTMAG',
                                       'INTMAG_3': 'MAXVEHICLELATERALINTMAG',
                                       'INTRUSION_2': 'MAXVEHICLELONGITUDINALINTRUSION',
                                       'INTRUSION_3': 'MAXVEHICLELATERALINTRUSION'}

# CISS Encoding Constants
ciss_years_with_wlatin1_encoding = ['2017', '2018', '2019', '2020', '2021']
