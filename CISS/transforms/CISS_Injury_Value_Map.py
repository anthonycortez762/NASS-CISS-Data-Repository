import Global_Constants

ciss_injury_col_specific_value_maps = {
    'AIS': [
        {
            'ranges': Global_Constants.common_ciss_year_range,
            'mapping': {'3': 'Serious injury', '4': 'Severe injury', '9': 'Injury, unknown severity'
                        } | Global_Constants.ais_shared_mapping
        }
    ],
    'REGION': [
        {
            'ranges': Global_Constants.common_ciss_year_range,
            'mapping': {'0': 'Other trauma', '1': 'Head', '2': 'Face', '3': 'Neck', '4': 'Thorax', '5': 'Abdomen',
                        '6': 'Spine', '7': 'Upper extremity', '8': 'Lower extremity', '9': 'Unspecified'}
        }
    ]
}
