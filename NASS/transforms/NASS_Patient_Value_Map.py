import Global_Constants

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
            'mapping': {'0': 'None available', '1': 'airbag availability/function not indicated by police', 
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
    ]
}