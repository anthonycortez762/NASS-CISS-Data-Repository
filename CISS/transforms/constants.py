# Injury Constants
injury_column_maps = {
    'AIS': {1: 'Minor Injury', 2: 'Moderate Injury', 3: 'Serious Injury', 4: 'Severe Injury', 5: 'Critical Injury',
            6: 'Maximum Injury', 9: 'Injured, Unknown Severity'},
    'REGION': {0: 'Other Trauma', 1: 'Head', 2: 'Face', 3: 'Neck', 4: 'Thorax', 5: 'Abdomen', 6: 'Spine',
               7: 'Upper Extremity', 8: 'Lower Extremity', 9: 'Unspecified'}
}

# Patient Constants
patient_column_maps = {
    'AGE': {0: 'Less than 1 year old', 999: 'Unknown'},
    'SEX': {1: 'Male', 2: 'Female', 3: 'Female, pregnant - 1st trimester (1st-3rd month)',
            4: 'Female, pregnant - 2nd trimester (4th-6th month)',
            5: 'Female, pregnant - 3rd trimester (7th-9th month)', 6: 'Female, pregnant - trimester unknown',
            9: 'Unknown'},
    'HEIGHT': {999: 'Unknown'},
    'WEIGHT': {999: 'Unknown'},
    'ROLE': {1: 'Driver', 2: 'Passenger', 9: 'Unknown'},
    'PARBELTUSE': {0: 'None used', 1: 'Shoulder belt', 2: 'Lap belt', 3: 'Lap and shoulder belt',
                   4: 'Belt used, type not specified', 5: 'Child safety seat', 6: 'Automatic belt',
                   7: 'Other type belt (specify)', 8: 'Police indicated "unknown"', 9: 'Not Reported'},
    'PARAIRBAG': {0: 'No Air Bag Available', 1: 'Deployed', 2: 'Not Deployed', 3: 'Unknown if deployed',
                  7: 'Not Reported', 9: 'Police indicated "Unknown"'},
    'SEATLOC': {11: 'Front Left', 12: 'Front middle', 13: 'Front right', 14: 'Front other', 21: 'Second left',
                22: 'Second middle', 23: 'Second right', 24: 'Second other', 31: 'Third left', 32: 'Third middle',
                33: 'Third right', 34: 'Third other', 41: 'Fourth left', 42: 'Fourth middle', 43: 'Fourth right',
                44: 'Fourth other', 51: 'Fifth left', 52: 'Fifth middle', 53: 'Fifth right', 54: 'Fifth other',
                97: 'In or on unenclosed area', 98: 'Other enclosed area', 99: 'Unknown'},
    'ENTRAP': {0: 'Not entrapped/exit not inhibited', 1: 'Entrapped/pinned — mechanically restrained',
               2: 'Could not exit vehicle due to jammed doors',
               3: 'Could not exit vehicle due to external circumstances (specify)', 9: 'Unknown'},
    'EYEWEAR': {0: 'No', 1: 'Eyeglasses/sunglasses', 2: 'Contact lenses with sunglasses', 3: 'Contact lenses',
                7: 'Other (specify)', 9: 'Unknown'},
    'HOSPSTAY': {0: 'Not hospitalized', 61: '61 days or more', 99: 'Unknown'},
    'MOBILITY': {1: 'Exited from vehicle under own power', 2: 'Exited from vehicle with some assistance',
                 3: 'Removed from vehicle due to perceived serious injuries',
                 4: 'Removed from vehicle while unconscious or not oriented to time or place',
                 5: 'Occupant fatal before removed from vehicle', 6: 'Occupant fully ejected',
                 8: 'Removed from vehicle for other reasons (specify):', 9: 'Unknown'},
    'MORTALITY': {0: 'Not Fatal', 1: 'Fatal', 2: 'Fatal — ruled disease (specify)'},
    'TREATMENT': {0: 'No treatment', 1: 'Treatment at scene - non-transported', 2: 'Transported and released',
                  3: 'Hospitalization', 4: 'Dead on Arrival (DOA) at hospital', 5: 'Dead Prior To Admission',
                  6: 'Transported to a medical facility - unknown if treated', 7: 'Treatment later',
                  8: 'Treatment - other (specify)', 9: 'Unknown'},
    'EJECTTYPE': {0: 'Not Ejected', 1: 'Ejected, Totally', 2: 'Ejected, Partially', 3: 'Ejection - Unknown Degree',
                  9: 'Unknown'}
}
