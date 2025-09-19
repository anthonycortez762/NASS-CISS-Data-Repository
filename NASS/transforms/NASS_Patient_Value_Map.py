import Global_Constants

intrusion_location_map = [
    {
        'ranges': [
            {'start': 1988, 'end': 2015},
        ],
        'mapping': {'11': 'Front Seat Left', '12': 'Front Seat Middle', '13': 'Front Seat Right', 
                    '21': 'Second Seat Left', '22': 'Second Seat Middle', '23': 'Second Seat Right',
                    '31': 'Third Seat Left', '32': 'Third Seat Middle', '33': 'Third Seat Right',
                    '41': 'Fourth Seat Left', '42': 'Fourth Seat Middle', '43': 'Fourth Seat Right',
                    '88': 'Multiple or Other Severe Intrusions', '97': 'Catastrophic', 
                    '98': 'Other Enclosed Area', 'U': 'Unknown'},
    }
]

intrusion_component_map = [
    {
        'ranges': [
            {'start': 1997, 'end': 2009},
        ],
        'mapping': {'1': 'Steering Assembly', '2': 'Instrument Panel Left', '3': 'Instrument Panel Center', 
                    '4': 'Instrument Panel Right', '5': 'Toe Pan', '6': 'A-Pillar', '7': 'B-Pillar', 
                    '8': 'C-Pillar', '9': 'D-Pillar', '10': 'Side Panel', '11': 'Door Panel', 
                    '12': 'Rear Side Panel', '13': 'Roof or Convertible Top', '14': 'Roof Side Rail', 
                    '15': 'Windshield', '16': 'Windshield Header', '17': 'Window Frame',
                    '18': 'Floor Pan', '19': 'Backlight Header', '20': 'Front Seat Back',
                    '21': 'Second Seat Back', '22': 'Third Seat Back', '23': 'Fourth Seat Back',
                    '24': 'Fifth Seat Back', '25': 'Seat Cushion', '26': 'Back Door/Panel',
                    '27': 'Other Component', '30': 'Hood', '31': 'Outside Surface of Vehicle', 
                    '32': 'Other Exterior Object in the Environment', '33': 'Unknown Exterior Object', 
                    '34': 'Grab Handles', '35': 'Door/Forward Upper Quadrants', '36': 'Door/Forward Lower Quadrants',
                    '37': 'Door/Rear Upper Quadrants', '38': 'Door/Rear Lower Quadrants', 
                    '41': 'Door/Undetermined Location', '96': 'Multiple/Other Severe Intrusions',
                    '97': 'Catastrophic', '98': 'Intrusion of Unlisted Component',
                    'U': 'Unknown'},
    },
    {
        'ranges': [
            {'start': 2010, 'end': 2015},
        ],
        'mapping': {'1': 'Steering Assembly', '2': 'Instrument Panel Left', '3': 'Instrument Panel Center', 
                    '4': 'Instrument Panel Right', '5': 'Toe Pan', '6': 'A-Pillar', '7': 'B-Pillar', 
                    '8': 'C-Pillar', '9': 'D-Pillar', '11': 'Door Panel', 
                    '12': 'Side Panel', '13': 'Roof or Convertible Top', '14': 'Roof Side Rail', 
                    '15': 'Windshield', '16': 'Windshield Header', '17': 'Window Frame',
                    '18': 'Floor Pan', '19': 'Backlight Header', '20': 'Front Seat Back',
                    '21': 'Second Seat Back', '22': 'Third Seat Back', '23': 'Fourth Seat Back',
                    '24': 'Fifth Seat Back', '25': 'Seat Cushion', '26': 'Back Door/Panel',
                    '27': 'Other Component', '30': 'Hood', '31': 'Outside Surface of Vehicle', 
                    '32': 'Other Exterior Object in the Environment', '33': 'Unknown Exterior Object', 
                    '34': 'Grab Handles', '35': 'Door/Forward Upper Quadrants', '36': 'Door/Forward Lower Quadrants',
                    '37': 'Door/Rear Upper Quadrants', '38': 'Door/Rear Lower Quadrants', 
                    '41': 'Door/Undetermined Location', '96': 'Multiple/Other Severe Intrusions',
                    '97': 'Catastrophic', '98': 'Intrusion of Unlisted Component',
                    'U': 'Unknown'},
    },
]

intrusion_magnitude_map = [
    {
        'ranges': [
            {'start': 1997, 'end': 2015},
        ],
        'mapping': {'1': '> 3 cm but < 8 cm', '2': '> 8 cm but < 15 cm', '3': '> 15 cm but < 30 cm', 
                    '4': '> 30 cm but < 46 cm', '5': '> 46 cm but < 61 cm', '6': '> 61 cm', 
                    '7': 'Catastrophic', '8': 'Multiple/Severe Other Intrusions', 'U': 'Unknown'},
    },
]

dominant_crush_direction_map = [
    {
        'ranges': [
            {'start': 1997, 'end': 2015},
        ],
        'mapping': {'1': 'Vertical', '2': 'Longitudinal', '3': 'Lateral', '7': 'Catastrophic', 
                    '8': 'Multiple/Severe Other Intrusions', 'U': 'Unknown'},
    }
]    

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
            'mapping': {'0': 'Less than one year old', '97': '97 years and older', 'U': 'Unknown'},            
        },
        {
            'ranges': [
                {'start': 2010, 'end': 2015},
            ],
            'mapping': {'1': 'Less than one year old', '97': '97 years and older', 'U': 'Unknown'},
        }
    ],
    'SEX': [
        {
            'ranges': [
                {'start': 1979, 'end': 1987},
            ],
            'mapping': Global_Constants.sex_shared_mapping,
        },
        {
            'ranges': [
                {'start': 1995, 'end': 2015},
            ],
            'mapping': {'1': 'Male', '2': 'Female, not pregnant', 
                        '3': 'Female, pregnant - 1st trimester (1st-3rd month)',
                        '4': 'Female, pregnant - 2nd trimester (4th-6th month)',
                        '5': 'Female, pregnant - 3rd trimester (7th-9th month)', 
                        '6': 'Female, pregnant - trimester unknown', 'U': 'Unknown'}
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
            'mapping': {'220': '219.5 cms and over'},
        }        
    ],
    'WEIGHT': [
        {
            'ranges': [
                {'start': 1979, 'end': 1987},
            ],
            'mapping': Global_Constants.weight_shared_mapping,
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
            'mapping': Global_Constants.role_shared_mapping,
        },
        {
            'ranges': [
                {'start': 1988, 'end': 2015},
            ],
            'mapping': {'1': 'Driver', '2': 'Passenger', 'U': 'Unknown'},
        }
    ],
    'BAGAVRPT': [
        {
            'ranges': [
                {'start': 1995, 'end': 2009},
            ],
            'mapping': {'0': 'None available', '1': 'Airbag availability/function not indicated by police',
                        '2': 'Deployed', '3': 'Not deployed', '4': 'Unknown if deployed', 'U': 'Unknown'}
        },
        {
            'ranges': [
                {'start': 2010, 'end': 2015},
            ],
            'mapping': {'0': 'None available', '1': 'Airbag availability/function not indicated by police', 
                        '2': 'Deployed', '3': 'Not deployed', '4': 'Unknown if deployed', '7': 'Not reported', 'U': 'Unknown'}
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
                        '14': 'In or on unenclosed area', '15': 'In or on trailing unit', '99': 'Unknown'},
        },
        {
            'ranges': [
                {'start': 1991, 'end': 2009},
            ],
            'mapping': {'11': 'Front left side', '12': 'Front middle', '13': 'Front right side', '14': 'Front other', 
                        '15': 'Front on/in Lap', '21': 'Second left', '22': 'Second middle', '23': 'Second right', 
                        '24': 'Second other', '25': 'Second on/in lap', '31': 'Third left', '32': 'Third middle', 
                        '33': 'Third right', '34': 'Third other', '35': 'Third on/in lap', '41': 'Fourth left', 
                        '42': 'Fourth middle', '43': 'Fourth right', '44': 'Fourth other', '45': 'Fourth on/in lap', 
                        '97': 'Unenclosed area', '98': 'Other seat','U': 'Unknown'},
        },
        {
            'ranges': [
                {'start': 2010, 'end': 2015},
            ],
            'mapping': {'11': 'Front left side', '12': 'Front middle', '13': 'Front right side', '14': 'Front other', 
                        '15': 'Front on/in lap', '19': 'Front row, unknown seat', '21': 'Second left', '22': 'Second middle', 
                        '23': 'Second right', '24': 'Second other', '25': 'Second on/in lap', '29': 'Second row, unknown seat', 
                        '31': 'Third left', '32': 'Third middle', '33': 'Third right', '34': 'Third other', 
                        '35': 'Third on/in lap', '39':'Third row, unknown seat', '41': 'Fourth left', '42': 'Fourth middle', 
                        '43': 'Fourth right', '44': 'Fourth other', '45': 'Fourth on/in lap', '49': 'Fourth row, unknown seat', 
                        '51': 'Fifth left', '52': 'Fifth middle', '53': 'Fifth right', '54': 'Fifth other', 
                        '55': 'Fifth on/in lap', '59': 'Fifth row, unknown seat', '97': 'Unenclosed area', '98': 'Other seat',
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
            'mapping': Global_Constants.entrapped_shared_mapping
        },
        {
            'ranges': [
                {'start': 1995, 'end': 2006},
            ],
            'mapping': {'0': 'Not entrapped', '1': 'Entrapped/Pinned - mechanically restrained', '2': 'Jammed door/Fire', 'U': 'Unknown'},
        },
        {
            'ranges': [
                {'start': 2007, 'end': 2015},
            ],
            'mapping': {'0': 'Not entrapped', '1': 'Entrapped/Pinned - mechanically restrained', '2': 'Jammed door/Fire', 
                        '3': 'Could not exit due to external circumstances', 'U': 'Unknown'},
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
            'mapping': Global_Constants.ejection_shared_mapping
        },
        {
            'ranges': [
                {'start': 1988, 'end': 2006},
            ],
            'mapping': {'0': 'None', '1': 'Complete ejection', '2': 'Partial ejection', 'U': 'Unknown'},
        },
        {
            'ranges': [
                {'start': 2007, 'end': 2015},
            ],
            'mapping': {'0': 'None', '1': 'Complete ejection', '2': 'Partial ejection', '3': 'Ejection, unknown degree',
                        'U': 'Unknown'},
        },
    ],
    'EYEWEAR': [
        {
            'ranges': [
                {'start': 1995, 'end': 2015},
            ],
            'mapping': {'0': 'Not Equip/Avail', '1': 'No', '2': 'Eye/Sun Glasses', '3': 'Contact Lenses',
                        '4': 'Deploy/Unk Eyew', '7': 'Not Deployed', '8': 'Unk If Deployed', 'U': 'Unknown'},
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
            'mapping': {'1': 'Fatal', '2': 'Fatal - ruled disease nonfatal', '4': 'Transported and released',
                        '5': 'Treatment at scene - nontransported', '6': 'Treatment later'
                        } | Global_Constants.treatment_shared_mapping,
        },
        {
            'ranges': [
                {'start': 1988, 'end': 2015},
            ],
            'mapping': {'0': 'No Treatment', '1': 'Fatal', '2': 'Fatal - Ruled Disease',
                        '3': 'Hospitalized', '4': 'Transported and Released', '5': 'Treatment at Scene - Not Transported',
                        '6': 'Treatment - Later', '7': 'Treatment - Other', '8': 'Transported - Unknown Treatment',
                        'N': 'Not Collected', 'U': 'Unknown'},
        }
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
            'mapping': Global_Constants.hospstay_shared_mapping,
        },
        {
            'ranges': [
                {'start': 1988, 'end': 2015},
            ],
            'mapping': {'0': 'Not Hospitalized', '61': '61 Days or More', 'U': 'Unknown'},
        }
    ],
    'MANUSE': [
        {
            'ranges': [
                {'start': 1979, 'end': 1979},
            ],
            'mapping': {'1': 'None (includes unavailability)', '2': 'Lap and shoulder belt', '3': 'Lap belt',
                        '4': 'Shoulder harness', '5': 'Helmet', '6': 'Child safety seat - in proper use',
                        '7': 'Other restraint used', '9': 'Unknown'},
        },
        {
            'ranges': [
                {'start': 1980, 'end': 1981},
            ],
            'mapping': {'4': 'Child safety seat - in proper use', '5': 'Helmet', '8': 'Other restraint used',
                        '9': 'Unknown'} | Global_Constants.belt_use_shared_mapping,
        },
        {
            'ranges': [
                {'start': 1982, 'end': 1987},
            ],
            'mapping': {'4': 'Helmet', '5': 'Child safety seat - in proper use',
                        '6': 'Child safety seat - used improperly', '7': 'Child safety seat - unknown if used properly',
                        '8': 'Other restraint used', '9': 'Unknown'} | Global_Constants.belt_use_shared_mapping,
        },
        {
            'ranges': [
                {'start': 1988, 'end': 2015}
            ],
            'mapping': {'0': 'None used/available', '1': 'Inoperative', '2': 'Shoulder belt', '3': 'Lap belt', 
                        '4': 'Lap and shoulder belt', '5': 'Unknown belt', '8': 'Other belt', 
                        '12': 'Shoulder belt with child safety seat', '13': 'Lap belt with child safety seat', 
                        '14': 'Lap and shoulder belt with child safety seat', '15': 'Unknown belt with child safety seat', 
                        '18': 'Other belt with child safety seat', 'U': 'Unknown if used'},
        }
    ],
    'AUTFNCT': [
        {
            'ranges': [
                {'start': 1979, 'end': 1979},
            ],
            'mapping': {'1': 'None available', '2': 'Air bag - deployed', '3': 'Air bag - did not deploy',
                        '4': 'Passive belt', '5': 'Other restraint', '9': 'Unknown'},
        },
        {
            'ranges': [
                {'start': 1980, 'end': 1987},
            ],
            'mapping': {'0': 'Not equipped', '1': 'Automatic belt in use', '2': 'Automatic belt not in use',
                        '3': 'Air bag - deployed', '4': 'Air bag - did not deploy', '9': 'Unknown'},
        }
    ],
    'BAGAVAIL': [
        {
            'ranges': [
                {'start': 1991, 'end': 2015},
            ],
            'mapping': {'0': 'Not equipped or available', '1': 'Airbag available', '2': 'Airbag disconnected',
                        '3': 'Bag not reinstalled', 'U': 'Unknown'},
        }
    ],
    'BAGDEPLY': [
        {
            'ranges': [
                {'start': 1991, 'end': 1994},
            ],
            'mapping': {'0': 'Not Equipped/Available', '1': 'Bag Deployed', '2': 'Bag Deployed - Inadvertently Prior to Impact',
                        '3': 'Bag Deployed - Accident Sequence Undetermined', '4': 'Nondeployed', '5': 'Unknown if Deployed',
                        '6': 'Bag Deployed - Noncollision Event', 'U': 'Unknown'},
        },
        {
            'ranges': [
                {'start': 1995, 'end': 2015},
            ],
            'mapping': {'0': 'Not Equipped/Available', '1': 'Bag Deployed', '2': 'Bag Deployed - Inadvertently Prior to Impact',
                        '3': 'Bag Deployed - Accident Sequence Undetermined', '7': 'Nondeployed', '5': 'Unknown if Deployed',
                        '4': 'Bag Deployed - Noncollision Event', 'U': 'Unknown'},
        }
    ],
    'PARUSE': [
        {
            'ranges': [
                {'start': 1988, 'end': 1993},
            ],
            'mapping': {'0': 'None Used', '1': 'Not Indicated', '2': 'Shoulder Belt',
                        '3': 'Lap Belt', '4': 'Lap/Shoulder', '5': 'Belt Used - Type Unknown',
                        '6': 'Child Seat', '7': 'Other or Automatic Belt', '8': 'Restrained - Type Unknown',
                        'U': 'Unknown'},
        },
        {
            'ranges': [
                {'start': 1994, 'end': 2015},
            ],
            'mapping': {'0': 'None Used', '1': 'Not Indicated', '2': 'Shoulder Belt',
                        '3': 'Lap Belt', '4': 'Lap/Shoulder', '5': 'Belt Used - Type Unknown',
                        '6': 'Child Seat', '7': 'Automatic Belt', '8': 'Other Type Belt',
                        '10': 'Not Reported', 'U': 'Unknown'},
        }
    ],
    'MANAVAIL': [
        {
            'ranges': [
                {'start': 1988, 'end': 2015},
            ],
            'mapping': {'0': 'Not Available', '1': 'Removed/Destroyed', '2': 'Shoulder Belt',
                        '3': 'Lap Belt', '4': 'Lap and Shoulder', '5': 'Type Unknown',
                        '6': 'Shoulder Belt/Lap Destroyed', '7': 'Lap Belt/Shoulder Destroyed', '8': 'Other Belt',
                        'U': 'Unknown'},
        }
    ],
    'ABELTAVL': [
        {
            'ranges': [
                {'start': 1991, 'end': 2009},
            ],
            'mapping': {'0': 'Not Equipped/Available', '1': '2 Point Belts', '2': '3 Point Belts',
                        '3': 'Unknown Type Belts', '4': 'Belts Destroyed', 'U': 'Unknown'},
        }
    ],
    'ABELTUSE': [
        {
            'ranges': [
                {'start': 1991, 'end': 2009},
            ],
            'mapping': {'0': 'Not Equipped/Not Available', '1': 'Belt In Use', '2': 'Belt Not In Use',
                        '3': 'Belt Use Unknown', 'U': 'Unknown'},
        }
    ],
    'MANFAIL': [
        {
            'ranges': [
                {'start': 1988, 'end': 1989},
            ],
            'mapping': {'0': 'None Used or Available', '1': 'No Failure', '2': 'Manual Belt Failure',
                        'U': 'Unknown'},
        },
        {
            'ranges': [
                {'start': 1990, 'end': 2015},
            ],
            'mapping': {'0': 'None Used', '1': 'Not Indicated', '2': 'Torn Webbing',
                        '3': 'Broken Buckle or Latch', '4': 'Upper Anchorage Separation', 
                        '5': 'Other Anchorage Separation', '6': 'Broken Retractor', '7': 'Combination', 
                        '8': 'Other Failure','U': 'Unknown'},
        }
    ],
    'ABLTFAIL': [
        {
            'ranges': [
                {'start': 1991, 'end': 2009},
            ],
            'mapping': {'0': 'Not Used or Available', '1': 'No Belt Failure', '2': 'Torn Webbing',
                        '3': 'Broken Buckle or Latch', '4': 'Upper Anchorage Separation', 
                        '5': 'Other Anchorage Separation', '6': 'Broken Retractor', '7': 'Combination', 
                        '8': 'Other Failure','U': 'Unknown', '10': 'Structural Failure'},
        }
    ],
    'POSTURE': [
        {
            'ranges': [
                {'start': 1988, 'end': 1992},
            ],
            'mapping': {'0': 'Normal Posture', '1': 'Abnormal Posture', 'U': 'Unknown'},
        },
        {
            'ranges': [
                {'start': 1993, 'end': 2015},
            ],
            'mapping': {'0': 'Normal Posture', '1': 'Kneeling on Seat', '2': 'Lying On Seat',
                        '3': 'Kneeling in Front of Seat', '4': 'Sitting Sideways', '5': 'Sitting on Console',
                        '6': 'Lying on Seat Back', '7': 'Bracing With Feet', '8': 'Other Abnormal Posture',
                        'U': 'Unknown'},
        }
    ],
    'OCCMOBIL': [
        {
            'ranges': [
                {'start': 1995, 'end': 2015},
            ],
            'mapping': {'0': 'Occupant Fatal', '1': 'Removed Unconscious', '2': 'Removed Injured',
                        '3': 'Exited w/ Assist', '4': 'Exited Own Power', '5': 'Fully Ejected',
                        '8': 'Removed from vehicle for other reasons', 'U': 'Unknown'},
        }
    ],
    'DEATH': [
        {
            'ranges': [
                {'start': 1988, 'end': 2015},
            ],
            'mapping': {'0': 'Not Fatal', '96': 'Fatal - Ruled Disease', 'U': 'Unknown'},
        }
    ],
    'MEDFACIL': [
        {
            'ranges': [
                {'start': 1988, 'end': 2015},
            ],
            'mapping': {'0': 'Not Medical Facility', '1': 'Trauma Center', '2': 'Hospital',
                        '3': 'Medical Clinic', '4': 'Physician Office', '5': 'Later at Facility',
                        '8': 'Other', 'U': 'Unknown'},
        }
    ],
    'CAUSE1': [
        {
            'ranges': [
                {'start': 1988, 'end': 2015},
            ],
            'mapping': {'0': 'Not Fatal', '96': 'No Specific Injury', '97': 'Other Result',
                        'U': 'Unknown'},
        }
    ],
    'CAUSE2': [
        {
            'ranges': [
                {'start': 1988, 'end': 2015},
            ],
            'mapping': {'0': 'Not Fatal', '96': 'No Specific Injury', '97': 'Other Result',
                        'U': 'Unknown'},
        }
    ],
    'CAUSE3': [
        {
            'ranges': [
                {'start': 1988, 'end': 2015},
            ],
            'mapping': {'0': 'Not Fatal', '96': 'No Specific Injury', '97': 'Other Result',
                        'U': 'Unknown'},
        }
    ],
    'INJNUM': [
        {
            'ranges': [
                {'start': 1988, 'end': 2015},
            ],
            'mapping': {'0': 'No Recorded Injuries', '97': 'Injured, Details Unknown',
                        'U': 'Unknown if Injured'},
        }
    ],
    'MAIS': [
        {
            'ranges': [
                {'start': 1988, 'end': 2015},
            ],
            'mapping': {'0': 'Not Injured', '1': 'Minor Injury', '2': 'Moderate Injury',
                        '3': 'Serious Injury', '4': 'Severe Injury', '5': 'Critical Injury', 
                        '6': 'Maximum Injury', '7': 'Injured, Unknown Severity',
                        'U': 'Unknown if Injured'},
        }
    ],
    'INJSEV': [
        {
            'ranges': [
                {'start': 1988, 'end': 2015},
            ],
            'mapping': {'0': 'No Injury', '1': 'Possible Injury', '2': 'Nonincapacitating',
                        '3': 'Incapacitating', '4': 'Killed', '5': 'Severity Unknown', 
                        '6': 'Died Prior', 'U': 'Unknown'},
        }
    ],
    'WORKDAYS': [
        {
            'ranges': [
                {'start': 1988, 'end': 2015},
            ],
            'mapping': {'0': 'No Work Days Lost', '61': '61 Days or More', '62': 'Fatally Injured',
                        '97': 'Not Working Prior', 'U': 'Unknown'},
        }
    ],
    'MANPROPR': [
        {
            'ranges': [
                {'start': 1993, 'end': 2002},
            ],
            'mapping': {'0': 'None Used/Available', '1': 'Used Properly', '2': 'Used Properly with Child Seat',
                        '3': 'Shoulder Belt Under Arm', '4': 'Shoulder Belt Behind Seat',
                        '5': 'Around >1 Person', '6': 'Belt on Abdomen', '7': 'Improper Use w/ Child Seat',
                        '8': 'Other Improper Use', 'U': 'Unknown'},
        }
    ],
    'ABLTPROP': [
        {
            'ranges': [
                {'start': 1993, 'end': 2002},
            ],
            'mapping': {'0': 'None Equipped/Available', '1': 'Used Properly', '2': 'Used Properly with Child Seat',
                        '3': 'Shoulder Belt Under Arm', '4': 'Shoulder Belt Behind Seat',
                        '5': 'Around >1 Person', '6': 'Belt on Abdomen', '7': 'Improper Use w/ Child Seat',
                        '8': 'Other Improper Use', 'U': 'Unknown'},
        }
    ],
    'INLOC1': intrusion_location_map,
    'INLOC2': intrusion_location_map,
    'INLOC3': intrusion_location_map,
    'INLOC4': intrusion_location_map,
    'INLOC5': intrusion_location_map,
    'INLOC6': intrusion_location_map,
    'INLOC7': intrusion_location_map,
    'INLOC8': intrusion_location_map,
    'INLOC9': intrusion_location_map,
    'INLOC10': intrusion_location_map,
    'INCOMP1': intrusion_component_map,
    'INCOMP2': intrusion_component_map,
    'INCOMP3': intrusion_component_map,
    'INCOMP4': intrusion_component_map,
    'INCOMP5': intrusion_component_map,
    'INCOMP6': intrusion_component_map,
    'INCOMP7': intrusion_component_map,
    'INCOMP8': intrusion_component_map,
    'INCOMP9': intrusion_component_map,
    'INCOMP10': intrusion_component_map,
    'INMAG1': intrusion_magnitude_map,
    'INMAG2': intrusion_magnitude_map,
    'INMAG3': intrusion_magnitude_map,
    'INMAG4': intrusion_magnitude_map,
    'INMAG5': intrusion_magnitude_map,
    'INMAG6': intrusion_magnitude_map,
    'INMAG7': intrusion_magnitude_map,
    'INMAG8': intrusion_magnitude_map,
    'INMAG9': intrusion_magnitude_map,
    'INMAG10': intrusion_magnitude_map,
    'CDRIR1': dominant_crush_direction_map,
    'CDRIR2': dominant_crush_direction_map,
    'CDRIR3': dominant_crush_direction_map,
    'CDRIR4': dominant_crush_direction_map,
    'CDRIR5': dominant_crush_direction_map,
    'CDRIR6': dominant_crush_direction_map,
    'CDRIR7': dominant_crush_direction_map,
    'CDRIR8': dominant_crush_direction_map,
    'CDRIR9': dominant_crush_direction_map,
    'CDRIR10': dominant_crush_direction_map,
}