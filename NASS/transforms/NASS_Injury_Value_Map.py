import Global_Constants

soudat_shared_mapping = {'1': 'Autopsy records', '2': 'Medical or hospital records', '3': 'Treating physician',
                         '4': 'Interviewee', '5': 'EMS personnel', '6': 'Police', '7': 'Other source', '9': 'Unknown'}

nass_injury_col_specific_value_maps = {'AIS': [
    {
        'ranges': [
            {'start': 1979, 'end': 1987},
        ],
        'mapping': {'0': 'Not injured', '3': 'Severe injury', '4': 'Serious injury', '7': 'Injury, unknown severity',
                    '9': 'Unknown if injured'} | Global_Constants.ais_shared_mapping
    }
    {
        'ranges': [
            {'start': 1988, 'end': 2015},
        ],
        'mapping': {'1': 'Minor Injury', '2': 'Moderate Injury', '3': 'Serious Injury', '4': 'Severe Injury', 
                    '5': 'Critical Injury', '6': 'Maximum Injury', '7': 'Injury, Unknown Severity'},
    }    
], 'ASPECT': [
    {
        'ranges': [
            {'start': 1979, 'end': 1987},
        ],
        'mapping': {'R': 'Right', 'L': 'Left', 'B': 'Bilateral', 'C': 'Central', 'A': 'Anterior - front',
                    'P': 'Posterior - back', 'S': 'Superior - upper', 'I': 'Inferior - lower', 'W': 'Whole region',
                    'U': 'Injured, unknown aspect', '0': 'Not injured', '8': 'Not applicable',
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
    },
    {
        'ranges': [
            {'start': 1995, 'end': 2015},
        ],
        'mapping': {'A': 'Arteries - Veins', 'B': 'Brain', 'C': 'Spinal Cord', 'D': 'Digestive', 'E': 'Ears', 
                    'G': 'Urogenital', 'H': 'Heart', 'I': 'Integumentary', 'J': 'Joints', 'K': 'Kidneys', 'L': 'Liver', 
                    'M': 'Muscles', 'N': 'Nervous System', 'O': 'Eye', 'P': 'Pulmonary - Lungs', 'Q': 'Spleen', 
                    'R': 'Respiratory', 'S': 'Skeletal', 'T': 'Thyroid', 'U': 'Injured/Unknown System', 
                    'V': 'Vertebrae', 'W': 'All Systems in Region'},
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
    },
    {
        'ranges': [
            {'start': 1995, 'end': 2015},
        ],
        'mapping': {'A': 'Arm', 'B': 'Back', 'C': 'Chest', 'E': 'Elbow', 'F': 'Face', 'H': 'Head', 'K': 'Knee', 
                    'L': 'Leg/Lower', 'M': 'Abdomen', 'N': 'Neck', 'P': 'Pelvic/Hip', 'Q': 'Ankle/Foot', 
                    'R': 'Forearm', 'S': 'Shoulder', 'T': 'Thigh', 'U': 'Injured, unknown region', 'W': 'Wrist/Hand', 
                    'X': 'Upper Limbs', 'Y': 'Lower Limbs'},
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
    },
    {
        'ranges': [
            {'start': 1995, 'end': 2015},
        ],
        'mapping': {'A': 'Abrasion', 'B': 'Burn', 'C': 'Contusion', 'D': 'Dislocation', 'E': 'Total Severance', 
                    'F': 'Fracture', 'G': 'Detachment', 'K': 'Concussion', 'L': 'Laceration', 'M': 'Amputation', 
                    'N': 'Crush', 'O': 'Other', 'P': 'Perforation, puncture', 'R': 'Rupture', 'S': 'Sprain', 
                    'T': 'Strain', 'U': 'Injured, unknown Lesion', 'V': 'Avulsion'}
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
        'mapping': {'0': 'Not injured', '1': 'Autopsy records', '2': 'Medical or hospital records',
                    '3': 'Emergency room records only', '4': 'Private physician', '5': 'Lay coroner report',
                    '6': 'EMS personnel', '7': 'Interviewee', '8': 'Other source', '9': 'Police'}
    },
    {
        'ranges': [
            {'start': 1981, 'end': 1981},
        ],
        'mapping': {'0': 'Not injured'} | soudat_shared_mapping
    },
    {
        'ranges': [
            {'start': 1988, 'end': 2006},
        ],
        'mapping': {1: 'Autopsy Records', 2: 'Medical or Hospital Records', 3: 'Emergency Room Records', 
                    4: 'Private Physician or Clinic', 5: 'Lay Coroner Report', 6: 'EMS Personnel', 7: 'Interviewee', 
                    8: 'Other Source', 9: 'Police'}
    },
    {
        'ranges': [
            {'start': 2007, 'end': 2015},
        ],
        'mapping': {2: 'Medical or Hospital Records', 3: 'Emergency Room Records', 4: 'Private Physician or Clinic', 
                    5: 'Lay Coroner Report', 6: 'EMS Personnel', 7: 'Interviewee', 8: 'Other Source', 9: 'Police', 
                    16: 'Internal Autopsy', 17: 'External Autopsy'}
    }
], 'ASPECT90': [
    {
        'ranges': [
            {'start': 1993, 'end': 2008},
        ],
        'mapping': {0: 'Whole Region', 1: 'Right', 2: 'Left', 3: 'Bilateral', 4: 'Central', 5: 'Anterior', 6: 'Posterior', 
                    7: 'Superior', 8: 'Inferior'}
    },
    {
        'ranges': [
            {'start': 2009, 'end': 2015},
        ],
        'mapping': {0: 'Whole Region', 1: 'Right', 2: 'Left', 3: 'Bilateral', 4: 'Central', 5: 'Anterior/Front/Ventral', 
                    6: 'Posterior/Back/Dorsal', 7: 'Superior/Upper', 8: 'Inferior/Lower'}
    }    
]}