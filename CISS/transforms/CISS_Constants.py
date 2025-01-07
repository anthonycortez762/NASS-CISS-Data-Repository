from CISS_Injury_Value_Map import ciss_injury_col_specific_value_maps
from CISS_Patient_Value_Map import ciss_patient_col_specific_value_maps
from CISS_Intrusion_Value_Map import ciss_intrusion_col_specific_value_maps

# Injury Constants
injury_join_columns_list = [['CASEID', 'CASENO', 'VEHNO', 'OCCNO', 'INJNO']]
injury_use_cols_list = [injury_join_columns_list[0] + ['L1', 'L2', 'LDEF']]
injury_output_columns = injury_join_columns_list[0] + ['YEAR', 'AISCODE', 'AIS', 'REGION', 'STRUTYPE', 'STRUSPEC',
                                                       'INJLEVEL', 'L1', 'L2', 'LDEF']

# Patient Constants
patient_base_column_list = ['CASEID', 'PSU', 'CASENO']
patient_join_columns_list = [patient_base_column_list + ['VEHNO', 'OCCNO'], patient_base_column_list + ['VEHNO'],
                             patient_base_column_list]
patient_use_cols_list = [patient_base_column_list + ['VEHNO', 'OCCNO', 'EJECTTYPE'],
                         patient_base_column_list + ['VEHNO', 'CURBWT', 'DVTOTAL'],
                         patient_base_column_list + ['EVENTS']]
patient_output_columns = patient_join_columns_list[0] + ['YEAR', 'AGE', 'SEX', 'HEIGHT', 'WEIGHT', 'ROLE', 'PARBELTUSE',
                                                         'PARAIRBAG', 'SEATLOC', 'ENTRAP', 'EYEWEAR', 'HOSPSTAY',
                                                         'MOBILITY', 'MORTALITY', 'TREATMENT', 'EJECTTYPE', 'CURBWT',
                                                         'DVTOTAL', 'EVENTS']
intrusion_base_column_list = ['CASEID', 'PSU', 'CASENO', 'VEHNO', 'YEAR']
seat_loc_intrusion_column_list = intrusion_base_column_list + ['SEATLOC']
intrusion_output_columns = seat_loc_intrusion_column_list + ['INTRUNO', 'INTRUSION', 'INTMAG', 'INTDIRECT']
max_intrusion_by_seat_loc_column_map = {'INTMAG_2': 'MAXSEATLOCLONGITUDINALINTMAG',
                                        'INTMAG_3': 'MAXSEATLOCLATERALINTMAG',
                                        'INTRUSION_2': 'MAXSEATLOCLONGITUDINALINTRUSION',
                                        'INTRUSION_3': 'MAXSEATLOCLATERALINTRUSION'}
max_intrusion_by_vehicle_column_map = {'INTMAG_2': 'MAXVEHICLELONGITUDINALINTMAG',
                                       'INTMAG_3': 'MAXVEHICLELATERALINTMAG',
                                       'INTRUSION_2': 'MAXVEHICLELONGITUDINALINTRUSION',
                                       'INTRUSION_3': 'MAXVEHICLELATERALINTRUSION'}

# Encoding Constants
ciss_years_with_wlatin1_encoding = ['2017', '2018', '2019', '2020', '2021']
