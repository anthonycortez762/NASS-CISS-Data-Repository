nass_patient_col_specific_value_maps = {
    'AGE': [
        {
            'ranges': [
                {'start': 1979, 'end': 1987},
            ],
            'mapping': {'0': 'Less than one year old', '97': '97 years and older', '99': 'Unknown'},
        },
        {
            'ranges': [
                {'start': 1988, 'end': 2009},
            ],
            'mapping': {0: 'Less than one year old', 97: '97 years and older', 'U': 'Unknown'},            
        },
        {
            'ranges': [
                {'start': 2010, 'end': 2015},
            ],
            'mapping': {1: 'Less than one year old', 97: '97 years and older', 'U': 'Unknown'},
        }
    ],
    'SEX': [
        {
            'ranges': [
                {'start': 1979, 'end': 1987},
            ],
            'mapping': {'1': 'Male', '2': 'Female', '9': 'Unknown'},
        },
        {
            'ranges': [
                {'start': 1995, 'end': 2015},
            ],
            'mapping': {1: 'Male', 2: 'Female, not pregnant', 
                        3: 'Female, pregnant - 1st trimester (1st-3rd month)',
                        4: 'Female, pregnant - 2nd trimester (4th-6th month)',
                        5: 'Female, pregnant - 3rd trimester (7th-9th month)', 
                        6: 'Female, pregnant - trimester unknown', 'U': 'Unknown'}
        },
    ],
    'HEIGHT': [
        {
            'ranges': [
                {'start': 1979, 'end': 1987},
            ],
            'mapping': {'99': 'Unknown'},
        },
        {
            'ranges': [
                {'start': 1993, 'end': 2015},
            ],
            'mapping': {220: '219.5 cms and over'},
        }        
    ],
    'WEIGHT': [
        {
            'ranges': [
                {'start': 1979, 'end': 1987},
            ],
            'mapping': {'999': 'Unknown'},
        },
        {
            'ranges': [
                {'start': 1993, 'end': 2015},
            ],
            'mapping': {'150': '149.5 kg and over', 'U': 'Unknown'},
        }
    ],
    'ROLE': [
        {
            'ranges': [
                {'start': 1979, 'end': 1987},
            ],
            'mapping': {'1': 'Driver', '2': 'Passenger', '9': 'Unknown'},
        },
        {
            'ranges': [
                {'start': 1988, 'end': 2015},
            ],
            'mapping': {1: 'Driver', 2: 'Passenger', 'U': 'Unknown'},
        }
    ],
    'BAGAVRPT': [
        {
            'ranges': [
                {'start': 1995, 'end': 2009},
            ],
            'mapping': {0: 'None available', 1: 'airbag availability/function not indicated by police', 
                        2: 'Deployed', 3: 'Not deployed', 4: 'Unknown if deployed', 'U': 'Unknown'}
        },
        {
            'ranges': [
                {'start': 2010, 'end': 2015},
            ],
            'mapping': {0: 'None available', 1: 'Airbag availability/function not indicated by police', 
                        2: 'Deployed', 3: 'Not deployed', 4: 'Unknown if deployed', 7: 'Not reported', 'U': 'Unknown'}
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
        },
        {
            'ranges': [
                {'start': 1991, 'end': 2009},
            ],
            'mapping': {11: 'Front left side', 12: 'Front middle', 13: 'Front right side', 14: 'Front other', 
                        15: 'Front on/in Lap', 21: 'Second left', 22: 'Second middle', 23: 'Second right', 
                        24: 'Second other', 25: 'Second on/in lap', 31: 'Third left', 32: 'Third middle', 
                        33: 'Third right', 34: 'Third other', 35: 'Third on/in lap', 41: 'Fourth left', 
                        42: 'Fourth middle', 43: 'Fourth right', 44: 'Fourth other', 45: 'Fourth on/in lap', 
                        97: 'Unenclosed area', 98: 'Other seat','U': 'Unknown'},
        },
        {
            'ranges': [
                {'start': 2010, 'end': 2015},
            ],
            'mapping': {11: 'Front left side', 12: 'Front middle', 13: 'Front right side', 14: 'Front other', 
                        15: 'Front on/in lap', 19: 'Front row, unknown seat', 21: 'Second left', 22: 'Second middle', 
                        23: 'Second right', 24: 'Second other', 25: 'Second on/in lap', 29: 'Second row, unknown seat', 
                        31: 'Third left', 32: 'Third middle', 33: 'Third right', 34: 'Third other', 
                        35: 'Third on/in lap', 39:'Third row, unknown seat', 41: 'Fourth left', 42: 'Fourth middle', 
                        43: 'Fourth right', 44: 'Fourth other', 45: 'Fourth on/in lap', 49: 'Fourth row, unknown seat', 
                        51: 'Fifth left', 52: 'Fifth middle', 53: 'Fifth right', 54: 'Fifth other', 
                        55: 'Fifth on/in lap', 59: 'Fifth row, unknown seat', 97: 'Unenclosed area', 98: 'Other seat',
                        'U': 'Unknown'},
        },
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
        },
        {
            'ranges': [
                {'start': 1995, 'end': 2006},
            ],
            'mapping': {0: 'Not entrapped', 1: 'Entrapped/Pinned - mechanically restrained', 2: 'Jammed door/Fire', 'U': 'Unknown'},
        },
        {
            'ranges': [
                {'start': 2007, 'end': 2015},
            ],
            'mapping': {0: 'Not entrapped', 1: 'Entrapped/Pinned - mechanically restrained', 2: 'Jammed door/Fire', 
                        3: 'Could not exit due to external circumstances', 'U': 'Unknown'},
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
        },
        {
            'ranges': [
                {'start': 1988, 'end': 2006},
            ],
            'mapping': {0: 'None', 1: 'Complete ejection', 2: 'Partial ejection', 'U': 'Unknown'},
        },
        {
            'ranges': [
                {'start': 2007, 'end': 2015},
            ],
            'mapping': {0: 'None', 1: 'Complete ejection', 2: 'Partial ejection', 3: 'Ejection, unknown degree',
                        'U': 'Unknown'},
        },
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
        {
            'ranges': [
                {'start': 1988, 'end': 2015}
            ],
            'mapping': {0: 'None used/svailable', 1: 'Inoperative', 2: 'Shoulder belt', 3: 'Lap belt', 
                        4: 'Lap and shoulder belt', 5: 'Unknown belt', 8: 'Other belt', 
                        12: 'Shoulder belt with child safety seat', 13: 'Lap belt with child safety seat', 
                        14: 'Lap and shoulder belt with child safety seat', 15: 'Unknown belt with child safety seat', 
                        18: 'Other belt with child safety seat', 'U': 'Unknown if used'},
        }
    ],
    'AUTFNCT': [
        {
            'ranges': [
                {'start': 1979, 'end': 1979},
            ],
            'mapping': {'1': 'None Available', '2': 'Air bag - deployed', '3': 'Air bag - did not deploy',
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