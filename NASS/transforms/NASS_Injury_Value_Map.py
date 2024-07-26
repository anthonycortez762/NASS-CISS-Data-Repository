import Global_Constants

soudat_shared_mapping = {'1': 'Autopsy Records', '2': 'Medical or Hospital Records', '3': 'Treating Physician',
                         '4': 'Interviewee', '5': 'EMS Personnel', '6': 'Police', '7': 'Other source', '9': 'Unknown'}

nass_injury_col_specific_value_maps = {'AIS': [
    {
        'ranges': [
            {'start': 1979, 'end': 1987},
        ],
        'mapping': {'0': 'Not Injured', '3': 'Severe Injury', '4': 'Serious Injury', '7': 'Injury, Unknown Severity',
                    '9': 'Unknown if injured'} | Global_Constants.ais_shared_mapping
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
        'mapping': {'8': 'Not applicable'} | soudat_shared_mapping
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
        'mapping': {'0': 'Not injured'} | soudat_shared_mapping
    }
]}