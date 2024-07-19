import numpy as np

nass_global_value_map = {np.nan: None, 'U': 'Unknown', 'A': 'Not Applicable'}
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

nass_injury_col_specific_value_maps = {'AIS': [
    {
        'ranges': [
            {'start': 1979, 'end': 1987},
        ],
        'mapping': {'0': 'Not Injured', '1': 'Minor Injury', '2': 'Moderate Injury', '3': 'Severe Injury',
                    '4': 'Serious Injury', '5': 'Critical Injury', '6': 'Maximum Injury',
                    '7': 'Injury, Unknown Severity', '9': 'Unknown if injured'},
    }
], 'ASPECT': [
    {
        'ranges': [
            {'start': 1979, 'end': 1987},
        ],
        'mapping': {'R': 'Right', 'L': 'Left', 'B': 'Bilateral', 'C': 'Central', 'A': 'Anterior - front',
                    'P': 'Posterior - back', 'S': 'Superior - upper', 'I': 'Inferior - lower', 'W': 'Whole Region',
                    'U': 'Injured, unknown aspect', '0': 'Not Injured', '8': 'Not applicable',
                    '9': 'Unknown if injured'},
    }
], 'SYSORG': [
    {
        'ranges': [
            {'start': 1979, 'end': 1987},
        ],
        'mapping': {'W': 'All systems in region', 'A': 'Arteries - veins', 'B': 'Brain', 'D': 'Digestive', 'E': 'Ears',
                    'O': 'Eye', 'H': 'Heart', 'U': 'Injured, unknown system', 'I': 'Integumentary', 'J': 'Joints',
                    'K': 'Kidneys', 'L': 'Liver', 'M': 'Muscles', 'N': 'Nervous system', 'P': 'Pulmonary - lungs',
                    'R': 'Respiratory', 'S': 'Skeletal', 'C': 'Spinal cord', 'Q': 'Spleen',
                    'T': 'Thyroid, other endocrine gland', 'G': 'Urogenital', 'V': 'Vertebrae', '0': 'Not injured',
                    '8': 'Not applicable', '9': 'Unknown if injured'},
    }
], 'BODYREG': [
    {
        'ranges': [
            {'start': 1979, 'end': 1987},
        ],
        'mapping': {'H': 'Head - skull', 'F': 'Face', 'N': 'Neck - cervical spine', 'S': 'Shoulder',
                    'X': 'Upper limb(s) (whole or unknown part)', 'A': 'Arm (upper)', 'E': 'Elbow', 'R': 'Forearm',
                    'W': 'Wrist - hand', 'C': 'Chest', 'M': 'Abdomen', 'B': 'Back - thoracolumbar spine',
                    'P': 'Pelvic - hip', 'Y': 'Lower limb(s) (whole or unknown part)', 'T': 'Thigh', 'K': 'Knee',
                    'L': 'Leg (lower)', 'Q': 'Ankle - foot', 'O': 'Whole body', 'U': 'Injured, unknown region',
                    '0': 'Not injured', '8': 'Not applicable', '9': 'Unknown if injured'},
    }
], 'LESION': [
    {
        'ranges': [
            {'start': 1979, 'end': 1979},
        ],
        'mapping': {'L': 'Laceration', 'C': 'Contusion', 'A': 'Abrasions', 'F': 'Fractures', 'P': 'Pain',
                    'K': 'Concussion', 'H': 'Hemorrhage', 'V': 'Avulsion', 'R': 'Rupture', 'S': 'Sprains',
                    'D': 'Dislocations', 'N': 'Crushing', 'M': 'Amputation', 'B': 'Burn', 'X': 'Asphyxia', 'O': 'Other',
                    'U': 'Injured, unknown lesion', '8': 'Not applicable', '9': 'Unknown if injured'},
    },
    {
        'ranges': [
            {'start': 1980, 'end': 1987},
        ],
        'mapping': {'Z': 'Fracture and dislocation', 'T': 'Strain', 'E': 'Total severence',
                    'G': 'Detachment, separation', 'L': 'Laceration', 'C': 'Contusion', 'A': 'Abrasion',
                    'F': 'Fracture', 'P': 'Perforation, puncture', 'K': 'Concussion', 'V': 'Avulsion', 'R': 'Rupture',
                    'S': 'Sprain', 'D': 'Dislocation', 'N': 'Crushing', 'M': 'Amputation', 'B': 'Burn', 'O': 'Other',
                    'U': 'Injured, unknown lesion', '0': 'Not injured', '9': 'Unknown if injured'},
    }
], 'SOUDAT': [
    {
        'ranges': [
            {'start': 1979, 'end': 1979},
        ],
        'mapping': {'1': 'Autopsy Records', '2': 'Medical or Hospital Records', '3': 'Treating Physician',
                    '4': 'Interviewee', '5': 'EMS Personnel', '6': 'Police', '7': 'Other source', '8': 'Not applicable',
                    '9': 'Unknown'}
    },
    {
        'ranges': [
            {'start': 1980, 'end': 1980},
            {'start': 1982, 'end': 1987},
        ],
        'mapping': {'0': 'Not injured', '1': 'Autopsy Records', '2': 'Medical or Hospital Records',
                    '3': 'Emergency room records only', '4': 'Private physician', '5': 'Lay coroner report',
                    '6': 'EMS personnel', '7': 'Interviewee', '8': 'Other source', '9': 'Police'}
    },
    {
        'ranges': [
            {'start': 1981, 'end': 1981},
        ],
        'mapping': {'0': 'Not injured', '1': 'Autopsy Records', '2': 'Medical or Hospital Records',
                    '3': 'Treating Physician', '4': 'Interviewee', '5': 'EMS Personnel', '6': 'Police',
                    '7': 'Other source', '9': 'Unknown'}
    }
]}

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

nass_patient_col_specific_value_maps = {
    'AGE': [
        {
            'ranges': [
                {'start': 1979, 'end': 1987},
            ],
            'mapping': {'0': 'Less than one year old', '97': '97 years and older', '99': 'Unknown'},
        }
    ],
    'SEX': [
        {
            'ranges': [
                {'start': 1979, 'end': 1987},
            ],
            'mapping': {'1': 'Male', '2': 'Female', '9': 'Unknown'},
        }
    ],
    'HEIGHT': [
        {
            'ranges': [
                {'start': 1979, 'end': 1987},
            ],
            'mapping': {'99': 'Unknown'},
        }
    ],
    'WEIGHT': [
        {
            'ranges': [
                {'start': 1979, 'end': 1987},
            ],
            'mapping': {'999': 'Unknown'},
        }
    ],
    'ROLE': [
        {
            'ranges': [
                {'start': 1979, 'end': 1987},
            ],
            'mapping': {'1': 'Driver', '2': 'Passenger', '9': 'Unknown'},
        }
    ],
    'SEATPOS': [
        {
            'ranges': [
                {'start': 1979, 'end': 1987},
            ],
            'mapping': {'1': 'Front seat-left side', '2': 'Front seat-middle', '3': 'Front seat-right side',
                        '4': 'Second seat-left side', '5': 'Second seat-middle', '6': 'Second seat-right side',
                        '7': 'Third seat-left side', '8': 'Third seat-middle', '9': 'Third seat-right side',
                        '10': 'Front seat-additional passenger', '11': 'Second seat or beyond-additional passenger',
                        '12': 'Truck-tractor sleeping section', '13': 'Other enclosed area',
                        '14': 'In or on Unenclosed area', '15': 'In or on trailing unit', '99': 'Unknown'},
        }
    ],
    'ENTRAP': [
        {
            'ranges': [
                {'start': 1979, 'end': 1979},
            ],
            'mapping': {'1': 'Not entrapped', '2': 'Entrapped', '8': 'Not applicable', '9': 'Unknown'},
        },
        {
            'ranges': [
                {'start': 1980, 'end': 1987},
            ],
            'mapping': {'0': 'Not entrapped', '1': 'Entrapped', '9': 'Unknown'},
        }
    ],
    'EJECTION': [
        {
            'ranges': [
                {'start': 1979, 'end': 1979},
            ],
            'mapping': {'1': 'None', '2': 'Partial ejection', '3': 'Complete ejection', '4': 'Ejection, unknown degree',
                        '8': 'Not applicable', '9': 'Unknown'},
        },
        {
            'ranges': [
                {'start': 1980, 'end': 1987},
            ],
            'mapping': {'0': 'None', '1': 'Complete ejection', '2': 'Partial ejection', '3': 'Ejection, unknown degree',
                        '9': 'Unknown'},
        }
    ],
    'TREATMNT': [
        {
            'ranges': [
                {'start': 1979, 'end': 1981},
            ],
            'mapping': {'1': 'Fatal', '2': 'Hospitalization', '3': 'Transported and released', '4': 'Treatment-other',
                        '5': 'No treatment', '9': 'Unknown'},
        },
        {
            'ranges': [
                {'start': 1982, 'end': 1984},
            ],
            'mapping': {'1': 'Fatal', '2': 'Fatal - ruled disease Nonfatal', '3': 'Hospitalization',
                        '4': 'Transported and released', '5': 'Treatment-other', '6': 'No treatment', '9': 'Unknown'},
        },
        {
            'ranges': [
                {'start': 1985, 'end': 1987},
            ],
            'mapping': {'0': 'No treatment', '1': 'Fatal', '2': 'Fatal - ruled disease Nonfatal', '3': 'Hospitalization'
                        ,'4': 'Transported and released', '5': 'Treatment at scene - nontransported',
                        '6': 'Treatment later', '8': 'Treatment-other', '9': 'Unknown'},
        },
    ],
    'HOSPSTAY': [
        {
            'ranges': [
                {'start': 1979, 'end': 1981},
            ],
            'mapping': {'31': '31 days or more', '98': 'Not applicable', '99': 'Unknown'},
        },
        {
            'ranges': [
                {'start': 1982, 'end': 1987},
            ],
            'mapping': {'61': '61 days or more', '99': 'Unknown'},
        }
    ],
    'MANUSE': [
        {
            'ranges': [
                {'start': 1979, 'end': 1979},
            ],
            'mapping': {'1': 'None (includes unavailability)', '2': 'Lap belt and shoulder belt', '3': 'Lap belt',
                        '4': 'Shoulder harness', '5': 'Helmet', '6': 'Child safety seat - in proper use',
                        '7': 'Other restraint used', '9': 'Unknown'},
        },
        {
            'ranges': [
                {'start': 1980, 'end': 1981},
            ],
            'mapping': {'0': 'None used - vehicle occupant', '1': 'Shoulder belt', '2': 'Lap belt',
                        '3': 'Lap belt and shoulder belt', '4': 'Child safety seat - in proper use', '5': 'Helmet',
                        '8': 'Other restraint used', '9': 'Unknown'},
        },
        {
            'ranges': [
                {'start': 1982, 'end': 1987},
            ],
            'mapping': {'0': 'None used - vehicle occupant', '1': 'Shoulder belt', '2': 'Lap belt',
                        '3': 'Lap belt and shoulder belt', '4': 'Helmet', '5': 'Child safety seat - in proper use',
                        '6': 'Child safety seat - used improperly', '7': 'Child safety seat - unknown if used properly',
                        '8': 'Other restraint used', '9': 'Unknown'},
        },
    ],
    'AUTFNCT': [
        {
            'ranges': [
                {'start': 1979, 'end': 1979},
            ],
            'mapping': {'1': 'None Availabile', '2': 'Air bag - deployed', '3': 'Air bag - did not deploy',
                        '4': 'Passive belt', '5': 'Other restraint', '9': 'Unknown'},
        },
        {
            'ranges': [
                {'start': 1980, 'end': 1987},
            ],
            'mapping': {'0': 'Not equipped', '1': 'Automatic belt in use', '2': 'Automatic belt not in use',
                        '3': 'Air bag - deployed', '4': 'Air bag - did not deploy', '9': 'Unknown'},
        }
    ]
}
