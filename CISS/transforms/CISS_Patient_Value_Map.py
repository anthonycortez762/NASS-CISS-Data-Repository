import Global_Constants

ciss_patient_col_specific_value_maps = {
    'AGE': [
        {
            'ranges': Global_Constants.common_ciss_year_range,
            'mapping': {'0': 'Less than one year old', '999': 'Unknown'}
        }
    ],
    'SEX': [
        {
            'ranges': Global_Constants.common_ciss_year_range,
            'mapping': {'3': 'Female, pregnant - 1st trimester (1st-3rd month)',
                        '4': 'Female, pregnant - 2nd trimester (4th-6th month)',
                        '5': 'Female, pregnant - 3rd trimester (7th-9th month)',
                        '6': 'Female, pregnant - trimester unknown'} | Global_Constants.sex_shared_mapping
        }
    ],
    'HEIGHT': [
        {
            'ranges': Global_Constants.common_ciss_year_range,
            'mapping': {'999': 'Unknown'}
        }
    ],
    'WEIGHT': [
        {
            'ranges': Global_Constants.common_ciss_year_range,
            'mapping': Global_Constants.weight_shared_mapping
        }
    ],
    'ROLE': [
        {
            'ranges': Global_Constants.common_ciss_year_range,
            'mapping': Global_Constants.role_shared_mapping
        }
    ],
    'SEATLOC': [
        {
            'ranges': Global_Constants.common_ciss_year_range,
            'mapping': {'11': 'Front left', '12': 'Front middle', '13': 'Front right', '14': 'Front other',
                        '21': 'Second left', '22': 'Second middle', '23': 'Second right', '24': 'Second other',
                        '31': 'Third left', '32': 'Third middle', '33': 'Third right', '34': 'Third other',
                        '41': 'Fourth left', '42': 'Fourth middle', '43': 'Fourth right', '44': 'Fourth other',
                        '51': 'Fifth left', '52': 'Fifth middle', '53': 'Fifth right', '54': 'Fifth other',
                        '97': 'In or on unenclosed area', '98': 'Other enclosed area', '99': 'Unknown'}
        }
    ],
    'ENTRAP': [
        {
            'ranges': Global_Constants.common_ciss_year_range,
            'mapping': {'2': 'Could not exit vehicle due to jammed doors',
                        '3': 'Could not exit vehicle due to external circumstances (specify)'
                        } | Global_Constants.entrapped_shared_mapping
        }
    ],
    'EJECTTYPE': [
        {
            'ranges': Global_Constants.common_ciss_year_range,
            'mapping': Global_Constants.ejection_shared_mapping
        }
    ],
    'TREATMENT': [
        {
            'ranges': Global_Constants.common_ciss_year_range,
            'mapping': {'1': 'Treatment at scene - non-transported', '2': 'Transported and released',
                        '4': 'Dead on arrival (DOA) at hospital', '5': 'Dead prior to admission',
                        '6': 'Transported to a medical facility - unknown if treated', '7': 'Treatment later'
                        } | Global_Constants.treatment_shared_mapping
        }
    ],
    'HOSPSTAY': [
        {
            'ranges': Global_Constants.common_ciss_year_range,
            'mapping': Global_Constants.hospstay_shared_mapping
        }
    ],
    'MORTALITY': [
        {
            'ranges': Global_Constants.common_ciss_year_range,
            'mapping': {'0': 'Not fatal', '1': 'Fatal', '2': 'Fatal — ruled disease (specify)'}
        }
    ],
    'EYEWEAR': [
        {
            'ranges': Global_Constants.common_ciss_year_range,
            'mapping': {'0': 'No', '1': 'Eyeglasses/sunglasses', '2': 'Contact lenses with sunglasses',
                        '3': 'Contact lenses', '7': 'Other (specify)', '9': 'Unknown'}
        }
    ],
    'MOBILITY': [
        {
            'ranges': Global_Constants.common_ciss_year_range,
            'mapping': {'1': 'Exited from vehicle under own power', '2': 'Exited from vehicle with some assistance',
                        '3': 'Removed from vehicle due to perceived serious injuries',
                        '4': 'Removed from vehicle while unconscious or not oriented to time or place',
                        '5': 'Occupant fatal before removed from vehicle', '6': 'Occupant fully ejected',
                        '8': 'Removed from vehicle for other reasons (specify):', '9': 'Unknown'}
        }
    ],
    'PARAIRBAG': [
        {
            'ranges': Global_Constants.common_ciss_year_range,
            'mapping': {'0': 'No air bag available', '1': 'Deployed', '2': 'Not deployed', '3': 'Unknown if deployed',
                        '7': 'Not reported', '9': 'Police indicated "unknown"'}
        }
    ],
    'PARBELTUSE': [
        {
            'ranges': Global_Constants.common_ciss_year_range,
            'mapping': {'4': 'Belt used, type not specified', '5': 'Child safety seat', '6': 'Automatic belt',
                        '7': 'Other type belt (specify)', '8': 'Police indicated "unknown"', '9': 'Not reported'
                        } | Global_Constants.belt_use_shared_mapping
        }
    ],
    'CURBWT': [
        {
            'ranges': Global_Constants.common_ciss_year_range,
            'mapping': {'9999': 'Unknown'}
        }
    ],
    'DVTOTAL': [
        {
            'ranges': Global_Constants.common_ciss_year_range,
            'mapping': {'999': 'Unknown'}
        }
    ],
}
