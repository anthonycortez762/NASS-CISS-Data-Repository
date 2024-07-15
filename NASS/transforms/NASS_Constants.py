import numpy as np

nass_col_specific_value_maps = {'AIS': [
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

nass_global_value_map = {np.nan: None, 'U': 'Unknown', 'A': 'Not Applicable'}

nass_1979_and_1980_col_name_maps = {
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
                  'O55': 'SOUDAT4', 'O62': 'SOUDAT5', 'O69': 'SOUDAT6'}
}

nass_1981_col_name_map = {'OAIS': 'AIS', 'OASPECT': 'ASPECT', 'OBODYRG': 'BODYREG', 'OLESION': 'LESION',
                          'OSYSORG': 'SYSORG', 'ODATSOU': 'SOUDAT'}
