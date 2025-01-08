from CISS_Injury_Value_Map import ciss_injury_col_specific_value_maps
from CISS_Patient_Value_Map import ciss_patient_col_specific_value_maps

# Injury Constants
injury_join_columns = ['CASEID', 'CASENO', 'VEHNO', 'OCCNO', 'INJNO']
injury_output_columns = injury_join_columns + ['YEAR', 'AISCODE', 'AIS', 'REGION', 'STRUTYPE', 'STRUSPEC', 'INJLEVEL',
                                               'L1', 'L2', 'LDEF']

# Patient Constants
patient_join_columns = ['CASEID', 'PSU', 'CASENO', 'VEHNO', 'OCCNO']
patient_output_columns = patient_join_columns + ['YEAR', 'AGE', 'SEX', 'HEIGHT', 'WEIGHT', 'ROLE', 'PARBELTUSE',
                                                 'PARAIRBAG', 'SEATLOC', 'ENTRAP', 'EYEWEAR', 'HOSPSTAY', 'MOBILITY',
                                                 'MORTALITY', 'TREATMENT', 'EJECTTYPE']
