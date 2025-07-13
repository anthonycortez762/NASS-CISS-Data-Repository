import numpy as np
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from NASS_Injury_Value_Map import nass_injury_col_specific_value_maps
from NASS_Patient_Value_Map import nass_patient_col_specific_value_maps

nass_global_value_map = {np.nan: None, 'U': 'Unknown', 'A': 'Not applicable'}
nass_1979_path = 'NASS_1979'
nass_1979_to_1987_paths = ['NASS_1979', 'NASS_1980', 'NASS_1981', 'NASS_1982', 'NASS_1983', 'NASS_1984', 'NASS_1985',
                           'NASS_1986', 'NASS_1987']
nass_1988_to_1996_paths = ['NASS_1988', 'NASS_1989', 'NASS_1990', 'NASS_1991', 'NASS_1992', 'NASS_1993', 'NASS_1994',
                           'NASS_1995', 'NASS_1996']
nass_occupant_file_ending = 'occupant.csv'
nass_oi_file_ending = 'oi.csv'

# Desired injury column names 1988-1996
injury_cols = ["PSU", "CASEID", "VEHNO", "OCCNO", "INJNO", "AIS", "ASPECT", "BODYREG", "LESION", "SYSORG", "SOUDAT", "REGION90", "STRUTYPE", "STRUSPEC", "INJLEVEL", "RATWGT", "YEAR"]

# Injury Constants for 1979 to 1981
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

# Injury Constants for 1988 to 1996
nass_1988_to_1996_injury_col_name_maps = {
    'NASS_1993': {'ASPECT90': 'ASPECT'},
    'NASS_1994': {'ASPECT90': 'ASPECT'},
    'NASS_1995': {'ASPECT90': 'ASPECT'},
    'NASS_1996': {'ASPECT90': 'ASPECT'}
}

# Patient Constants for 1979 to 1981
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

nass_1988_to_1996_patient_col_name_maps = {
    'CASEID': 'CASEID', 'PSU': 'PSU', 'VEHNO': 'VEHNO', 'OCCNO': 'OCCNO', 'AGE': 'AGE', 'SEX': 'SEX', 'HEIGHT': 'HEIGHT', 
    'WEIGHT': 'WEIGHT', 'ROLE': 'ROLE', 'PARUSE': 'PARBELTUSE', 'SEATPOS': 'SEATLOC', 'ENTRAP': 'ENTRAP', 'HOSPSTAY': 'HOSPSTAY',    
    'OCCMOBIL': 'MOBILITY', 'DEATH': 'MORTALITY', 'TREATMNT': 'TREATMENT', 'EJECTION': 'EJECTTYPE', 'CURBWGT': 'CURBWT', 'DVTOTAL': 'DVTOTAL',
    'EVENTS': 'EVENTS', 'BAGAVAIL': 'BAGAVAIL', 'ABELTAVL': 'ABELTAVL', 'INJSEV': 'INJSEV', 
    
    'MANUSE': 'MANUSE', 'AUTFNCT': 'AUTFNCT', 'BAGDEPLY': 'PARAIRBAG', 'YEAR': 'YEAR', 'POSTURE': 'POSTURE', 
    'MANAVAIL': 'MANAVAIL', 'MANPROPER': 'MANPROPER', 'MANFAIL': 'MANFAIL', 'AUTAVAIL': 'AUTAVAIL', 'ABELTUSE': 'ABELTUSE', 'AUTFAIL': 'AUTFAIL', 
    'MEDFACIL': 'MEDFACIL', 'WORKDAYS': 'WORKDAYS', 'CAUSE1': 'CAUSE1', 'CAUSE2': 'CAUSE2', 'CAUSE3': 'CAUSE3', 'INJNUM': 'INJNUM', 
    'PSUWGT': 'PSUWGT', 'NATWGT': 'NATWGT', 'RATWGT': 'RATWGT', 'STRATIF': 'STRATIF', 'MAIS': 'MAIS', 'ISS': 'ISS', 'VERSION': 'VERSION',
    'INJNO': 'INJNO', 'ACCSEQ': 'ACCSEQ',

    'INLOC1': 'INLOC1', 'INCOMP1': 'INCOMP1', 'INMAG1': 'INMAG1', 'CDRIR1': 'CDRIR1', 
    'INLOC2': 'INLOC2', 'INCOMP2': 'INCOMP2', 'INMAG2': 'INMAG2', 'CDRIR2': 'CDRIR2', 
    'INLOC3': 'INLOC3', 'INCOMP3': 'INCOMP3', 'INMAG3': 'INMAG3', 'CDRIR3': 'CDRIR3', 
    'INLOC4': 'INLOC4', 'INCOMP4': 'INCOMP4', 'INMAG4': 'INMAG4', 'CDRIR4': 'CDRIR4', 
    'INLOC5': 'INLOC5', 'INCOMP5': 'INCOMP5', 'INMAG5': 'INMAG5', 'CDRIR5': 'CDRIR5', 
    'INLOC6': 'INLOC6', 'INCOMP6': 'INCOMP6', 'INMAG6': 'INMAG6', 'CDRIR6': 'CDRIR6', 
    'INLOC7': 'INLOC7', 'INCOMP7': 'INCOMP7', 'INMAG7': 'INMAG7', 'CDRIR7': 'CDRIR7', 
    'INLOC8': 'INLOC8', 'INCOMP8': 'INCOMP8', 'INMAG8': 'INMAG8', 'CDRIR8': 'CDRIR8', 
    'INLOC9': 'INLOC9', 'INCOMP9': 'INCOMP9', 'INMAG9': 'INMAG9', 'CDRIR9': 'CDRIR9', 
    'INLOC10': 'INLOC10', 'INCOMP10': 'INCOMP10', 'INMAG10': 'INMAG10', 'CDRIR10': 'CDRIR10',
}

nass_1988_to_1996_file_ending_map = {
    'accident': 'accident', 'event': 'event', 
    'general vehicle': 'gv', 'exterior vehicle': 've', 'interior vehicle': 'vi',
    'occupant assessment': 'oa', 'occupant injury': 'oi', 
}

nass_1988_to_1996_file_specific_values = ['PSUWGT', 'NATWGT', 'RATWGT', 'STRATIF', 'VERSION']