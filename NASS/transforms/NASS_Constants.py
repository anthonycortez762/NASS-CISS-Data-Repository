import numpy as np
from NASS_Injury_Value_Map import nass_injury_col_specific_value_maps
from NASS_Patient_Value_Map import nass_patient_col_specific_value_maps

nass_global_value_map = {np.nan: None, 'U': 'Unknown', 'A': 'Not applicable'}
nass_1979_path = 'NASS_1979'
nass_1979_to_1987_paths = ['NASS_1979', 'NASS_1980', 'NASS_1981', 'NASS_1982', 'NASS_1983', 'NASS_1984', 'NASS_1985',
                           'NASS_1986', 'NASS_1987']
nass_occupant_file_ending = 'occupant.csv'

# Injury Constants
nass_1979_to_1981_injury_col_name_maps = {
    'NASS_1979': {'H01': 'PSU', 'H02': 'CASEID', 'H06': 'VEHNO', 'O07': 'OCCNO', 'O32': 'AIS1', 'O39': 'AIS2',
                  'O46': 'AIS3', 'O53': 'AIS4', 'O60': 'AIS5', 'O67': 'AIS6', 'O29': 'ASPECT1', 'O36': 'ASPECT2',
                  'O43': 'ASPECT3', 'O50': 'ASPECT4', 'O57': 'ASPECT5', 'O64': 'ASPECT6', 'O28': 'BODYREG1',
                  'O35': 'BODYREG2', 'O42': 'BODYREG3', 'O49': 'BODYREG4', 'O56': 'BODYREG5', 'O63': 'BODYREG6',
                  'O30': 'LESION1', 'O37': 'LESION2', 'O44': 'LESION3', 'O51': 'LESION4', 'O58': 'LESION5',
                  'O65': 'LESION6', 'O31': 'SYSORG1', 'O38': 'SYSORG2', 'O45': 'SYSORG3', 'O52': 'SYSORG4',
                  'O59': 'SYSORG5', 'O66': 'SYSORG6', 'O34': 'SOUDAT1', 'O41': 'SOUDAT2', 'O48': 'SOUDAT3',
                  'O55': 'SOUDAT4', 'O62': 'SOUDAT5', 'O69': 'SOUDAT6'},
    'NASS_1980': {'H01': 'PSU', 'H02': 'CASEID', 'H07': 'VEHNO', 'O08': 'OCCNO', 'O32': 'AIS1', 'O39': 'AIS2',
                  'O46': 'AIS3', 'O53': 'AIS4', 'O60': 'AIS5', 'O67': 'AIS6', 'O29': 'ASPECT1', 'O36': 'ASPECT2',
                  'O43': 'ASPECT3', 'O50': 'ASPECT4', 'O57': 'ASPECT5', 'O64': 'ASPECT6', 'O28': 'BODYREG1',
                  'O35': 'BODYREG2', 'O42': 'BODYREG3', 'O49': 'BODYREG4', 'O56': 'BODYREG5', 'O63': 'BODYREG6',
                  'O30': 'LESION1', 'O37': 'LESION2', 'O44': 'LESION3', 'O51': 'LESION4', 'O58': 'LESION5',
                  'O65': 'LESION6', 'O31': 'SYSORG1', 'O38': 'SYSORG2', 'O45': 'SYSORG3', 'O52': 'SYSORG4',
                  'O59': 'SYSORG5', 'O66': 'SYSORG6', 'O34': 'SOUDAT1', 'O41': 'SOUDAT2', 'O48': 'SOUDAT3',
                  'O55': 'SOUDAT4', 'O62': 'SOUDAT5', 'O69': 'SOUDAT6'},
    'NASS_1981': {'CASE_ID': 'CASEID', 'VEH_NO': 'VEHNO', 'OCC_NO': 'OCCNO', 'OAIS1': 'AIS1', 'OAIS2': 'AIS2',
                  'OAIS3': 'AIS3', 'OAIS4': 'AIS4', 'OAIS5': 'AIS5', 'OAIS6': 'AIS6', 'OASPECT1': 'ASPECT1',
                  'OASPECT2': 'ASPECT2', 'OASPECT3': 'ASPECT3', 'OASPECT4': 'ASPECT4', 'OASPECT5': 'ASPECT5',
                  'OASPECT6': 'ASPECT6', 'OBODYRG1': 'BODYREG1', 'OBODYRG2': 'BODYREG2', 'OBODYRG3': 'BODYREG3',
                  'OBODYRG4': 'BODYREG4', 'OBODYRG5': 'BODYREG5', 'OBODYRG6': 'BODYREG6', 'OLESION1': 'LESION1',
                  'OLESION2': 'LESION2', 'OLESION3': 'LESION3', 'OLESION4': 'LESION4', 'OLESION5': 'LESION5',
                  'OLESION6': 'LESION6', 'OSYSORG1': 'SYSORG1', 'OSYSORG2': 'SYSORG2', 'OSYSORG3': 'SYSORG3',
                  'OSYSORG4': 'SYSORG4', 'OSYSORG5': 'SYSORG5', 'OSYSORG6': 'SYSORG6', 'ODATSOU1': 'SOUDAT1',
                  'ODATSOU2': 'SOUDAT2', 'ODATSOU3': 'SOUDAT3', 'ODATSOU4': 'SOUDAT4', 'ODATSOU5': 'SOUDAT5',
                  'ODATSOU6': 'SOUDAT6'}
}

# Patient Constants
nass_1979_to_1981_patient_col_name_maps = {
    'NASS_1979': {'H01': 'PSU', 'H02': 'CASEID', 'O07': 'OCCNO', 'H06': 'VEHNO', 'O08': 'AGE', 'O09': 'SEX',
                  'O10': 'HEIGHT', 'O11': 'WEIGHT', 'O12': 'ROLE', 'O13': 'SEATPOS', 'O15': 'EJECTION', 'O14': 'ENTRAP',
                  'O20': 'HOSPSTAY', 'O19': 'TREATMNT', 'O24': 'MANUSE', 'O25': 'AUTFNCT'},
    'NASS_1980': {'H01': 'PSU', 'H02': 'CASEID', 'O08': 'OCCNO', 'H07': 'VEHNO', 'O09': 'AGE', 'O10': 'SEX',
                  'O11': 'HEIGHT', 'O12': 'WEIGHT', 'O13': 'ROLE', 'O14': 'SEATPOS', 'O16': 'EJECTION', 'O15': 'ENTRAP',
                  'O21': 'HOSPSTAY', 'O20': 'TREATMNT', 'O24': 'MANUSE', 'O26': 'AUTFNCT'},
    'NASS_1981': {'CASE_ID': 'CASEID', 'OCC_NO': 'OCCNO', 'VEH_NO': 'VEHNO', 'OCC_AGE': 'AGE', 'OSEX': 'SEX', 'OHGT':
                  'HEIGHT', 'OWGT': 'WEIGHT', 'OCC_ROLE': 'ROLE', 'SEAT_POS': 'SEATPOS', 'OHOSPDYS': 'HOSPSTAY',
                  'OTREATMT': 'TREATMNT', 'MAN_REST': 'MANUSE', 'AUT_REST': 'AUTFNCT'}
}
