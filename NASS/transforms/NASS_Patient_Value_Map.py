import Global_Constants

intrusion_location_map = {
            'ranges': [
                {'start': 1988, 'end': 1996},
            ],
            'mapping': {'11': 'Front Seat Left', '12': 'Front Seat Middle', '13': 'Front Seat Right', 
                        '21': 'Second Seat Left', '22': 'Second Seat Middle', '23': 'Second Seat Right',
                        '31': 'Third Seat Left', '32': 'Third Seat Middle', '33': 'Third Seat Right',
                        '41': 'Fourth Seat Left', '42': 'Fourth Seat Middle', '43': 'Fourth Seat Right',
                        '97': 'Catastrophic', '98': 'Other Enclosed Area', '99': 'Unknown'},
        }

intrusion_component_map_1988_to_1994 = {
            'ranges': [
                {'start': 1988, 'end': 1994},
            ],
            'mapping': {'1': 'Steering Assembly', '2': 'Instrument Panel Left', '3': 'Instrument Panel Center', 
                        '4': 'Instrument Panel Right', '5': 'Toe Pan', '6': 'A-Pillar', '7': 'B-Pillar', 
                        '8': 'C-Pillar', '9': 'D-Pillar', '10': 'Door Panel', '11': 'Side Panel', 
                        '12': 'Roof or Convertible Top', '13': 'Roof Side Rail', '14': 'Windshield', 
                        '15': 'Windshield Header', '16': 'Window Frame', '17': 'Floor Plan',
                        '18': 'Backlight Header', '19': 'Front Seat Back', '20': 'Second Seat Back',
                        '21': 'Third Seat Back', '22': 'Fourth Seat Back', '23': 'Fifth Seat Back',
                        '24': 'Seat Cushion', '25': 'Back Panel or Door Surface', '26': 'Other Interior Compartments',
                        '27': 'Side Panel Forward of the Panel A', '28': 'Side Panel Rear of the A Pillar', 
                        '30': 'Hood', '31': 'Outside Surface of Vehicle', '32': 'Other Exterior Object in the Environment',
                        '33': 'Unknown Exterior Object', '97': 'Catastrophic', '98': 'Intrusion of Unlisted Component',
                        '99': 'Unknown'
                        },
        }

intrusion_component_map_1995_to_1996 = {
            'ranges': [
                {'start': 1995, 'end': 1996},
            ],
            'mapping': {'1': 'Steering Assembly', '2': 'Instrument Panel Left', '3': 'Instrument Panel Center', 
                        '4': 'Instrument Panel Right', '5': 'Toe Pan', '6': 'A-Pillar', '7': 'B-Pillar', 
                        '8': 'C-Pillar', '9': 'D-Pillar', '10': 'Door Panel', '11': 'Side Panel', 
                        '12': 'Side Panel Rear of the B Pillar', '13': 'Roof Side Rail', '14': 'Windshield', 
                        '15': 'Windshield Header', '16': 'Window Frame', '17': 'Floor Plan',
                        '18': 'Backlight Header', '19': 'Front Seat Back', '20': 'Second Seat Back',
                        '21': 'Third Seat Back', '22': 'Fourth Seat Back', '23': 'Fifth Seat Back',
                        '24': 'Seat Cushion', '25': 'Back Panel or Door Surface', '26': 'Other Interior Compartments',
                        '27': 'Side Panel Forward of the Panel A', '28': 'Side Panel Rear of the A Pillar', 
                        '30': 'Hood', '31': 'Outside Surface of Vehicle', '32': 'Other Exterior Object in the Environment',
                        '33': 'Unknown Exterior Object', '97': 'Catastrophic', '98': 'Intrusion of Unlisted Component',
                        '99': 'Unknown'
                        },
            }

intrusion_magnitude_1988_to_1992 = {
            'ranges': [
                {'start': 1988, 'end': 1992},
            ],
            'mapping': {'1': '> 1 inch but < 3 inches', '2': '> 3 inches but < 6 inches', '3': '> 6 inches but < 12 inches', 
                        '4': '> 12 inches but < 18 inches', '5': '> 18 inches but < 24 inches', '6': '> 24 inches', 
                        '7': 'Catastrophic', '9': 'Unknown'
                        },
            }

intrusion_magnitude_1993_to_1996 = {
            'ranges': [
                {'start': 1993, 'end': 1996},
            ],
            'mapping': {'1': '> 3 cm but < 8 cm', '2': '> 8 cm but < 15 cm', '3': '> 15 cm but < 30 cm', 
                        '4': '> 30 cm but < 46 cm', '5': '> 46 cm but < 61 cm', '6': '> 24 inches', 
                        '7': 'Catastrophic', '9': 'Unknown'
                        },
            }

dominant_crush_direction = {
            'ranges': [
                {'start': 1988, 'end': 1996},
            ],
            'mapping': {'1': 'Vertical', '2': 'Longitudinal', '3': 'Lateral', '7': 'Catastrophic', '9': 'Unknown'},
}

nass_patient_col_specific_value_maps = {
    'AGE': [
        {
            'ranges': [
                {'start': 1979, 'end': 1996},
            ],
            'mapping': {'0': 'Less than one year old', '97': '97 years and older', '99': 'Unknown'},
        }
    ],
    'SEX': [
        {
            'ranges': [
                {'start': 1979, 'end': 1994},
            ],
            'mapping': Global_Constants.sex_shared_mapping,
        },
        {
            'ranges': [
                {'start': 1994, 'end': 1996},
            ],
            'mapping': {'1': 'Male', '2': 'Female, Not Reported Pregnant', '3': 'Female Pregnant - 1st Trimester',
                        '4': 'Female Pregnant - 2nd Trimester', '5': 'Female Pregnant - 3rd Trimester', 
                        '6': 'Female Pregnant - Trimester Unknown', '9': 'Unknown'},
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
            'mapping': Global_Constants.weight_shared_mapping,
        }
    ],
    'ROLE': [
        {
            'ranges': [
                {'start': 1979, 'end': 1996},
            ],
            'mapping': Global_Constants.role_shared_mapping,
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
                {'start': 1988, 'end': 1996},
            ],
            'mapping': {'11': 'Front, Left Side', '12': 'Front, Middle', '13': 'Front, Right Side', '14': 'Front, Other', '15': 'Front, On Lap of Other Occupant',
                        '21': 'Second Seat, Left Side', '22': 'Second Seat, Middle', '23': 'Second Seat, Right Side', '24': 'Second Seat, Other', '25': 'Second Seat, On Lap of Other Occupant',
                        '31': 'Third Seat, Left Side', '32': 'Third Seat, Middle', '33': 'Third Seat, Right Side', '34': 'Third Seat, Other', '35': 'Third Seat, On Lap of Other Occupant',
                        '41': 'Fourth Seat, Left Side', '42': 'Fourth Seat, Middle', '43': 'Fourth Seat, Right Side', '44': 'Fourth Seat, Other', '45': 'Fourth Seat, On Lap of Other Occupant',
                        '97': 'Unenclosed Area', '98': 'Other Seat', '99': 'Unknown'
                        },
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
            'mapping': Global_Constants.entrapped_shared_mapping
        },
        {
            'ranges': [
                {'start': 1988, 'end': 1996},
            ],
            'mapping': {'0': 'Not Entrapped', '1': 'Entrapped', '2': 'Could Not Exit Due To Jam, Fire, Etc', '9': 'Unknown'},
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
                {'start': 1980, 'end': 1996},
            ],
            'mapping': Global_Constants.ejection_shared_mapping
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
                {'start': 1988, 'end': 1994},
            ],
            'mapping': {'1': 'Fatal', '2': 'Fatal - ruled disease', '3': 'Hospitalized',
                        '4': 'Transported and released', '5': 'Treatment at scene - nontransported', '6': 'Treatment later'
                        } | Global_Constants.treatment_shared_mapping,
        },
        {
            'ranges': [
                {'start': 1995, 'end': 1996},
            ],
            'mapping': {'1': 'Fatal', '2': 'Fatal - ruled disease', '3': 'Hospitalized',
                        '4': 'Transported and released', '5': 'Treatment at scene - nontransported', '6': 'Treatment later',
                        '7': 'Treatment - Other', '8': 'Transported to Medical Facility, Treatment Unknown', '9': 'Unknown'}
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
                {'start': 1982, 'end': 1996},
            ],
            'mapping': Global_Constants.hospstay_shared_mapping,
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
                {'start': 1988, 'end': 1996},
            ],
            'mapping': {'0': 'None, Unavailable or Destroyed', '1': 'Inoperative', '2': 'Shoulder belt',
                        '3': 'Lap belt', '4': 'Lap and shoulder belt', '5': 'Belt used - type unknown',
                        '8': 'Other belt used', '12': 'Shoulder belt w/ child safety seat',
                        '13': 'Lap belt w/ child safety seat', '14': 'Lap and shoulder w/ child safety seat', 
                        '15': 'Belt used w/ child safety seat-type unknown', '18': 'Other belt used w/ child safety seat',
                        '99': 'Unknown'},
        },
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
        },
        {
            'ranges': [
                {'start': 1988, 'end': 1990},
            ],
            'mapping': {'0': 'Not equipped', '1': 'Automatic belt in use', '2': 'Automatic belt not in use',
                        '3': 'Automatic Belt Use Unknown', '4': 'Air Bag Deployed During Crash', 
                        '5': 'Airbag Deployed Prior to Crash', '6': 'Deployed, Sequence Unknown',
                        '7': 'Nondeployed', '8': 'Unknown if Deployed', '9': 'Unknown'},
        }
    ],
    'AUTFAIL': [
        {
            'ranges': [
                {'start': 1988, 'end': 1996},
            ],
            'mapping': {'0': 'Not Equipped/Not Available', '1': 'No', '2': 'Yes', '9': 'Unknown'},
        }
    ],
    'PARUSE': [
        {
            'ranges': [
                {'start': 1988, 'end': 1996},
            ],
            'mapping': {'0': 'None', '1': 'Not Recorded', '2': 'Shoulder Belt', '3': 'Lap Belt', '4': 'Lap and Shoulder Belt',
                        '5': 'Belt Used, Type Not Specified', '6': 'Child Safety Seat', '7': 'Other or Automatic Restraint',
                        '8': 'Restrained, Type Unknown', '9': 'Unknown'},
        }
    ],
    'OCCMOBIL': [
        {
            'ranges': [
                {'start': 1988, 'end': 1996},
            ],
            'mapping': {'0': 'Occupant Fatal Before Removed', '1': 'Removed Unconscious/Disoriented', '2': 'Removed Due To Injury', 
                        '3': 'Exited Vehicle with Some Assistance', '4': 'Exited Vehicle Under Own Power',
                        '5': 'Occupant Fully Ejected', '8': 'Removed From Vehicle - Other Reason', '9': 'Unknown'},
        }
    ],
    'DEATH': [
        {
            'ranges': [
                {'start': 1988, 'end': 1996},
            ],
            'mapping': {'0': 'Not Fatal', '96': 'Fatal - Ruled Disease', '99': 'Unknown'},
        }
    ],
    'BAGDEPLY': [
        {
            'ranges': [
                {'start': 1991, 'end': 1994},
            ],
            'mapping': {'0': 'Not equipped', '1': 'Air Bag Deployed During Crash', 
                        '2': 'Airbag Deployed Prior to Crash', '3': 'Deployed, Sequence Unknown',
                        '4': 'Nondeployed', '5': 'Unknown if Deployed', '6': 'Deployed - Noncollision Event', '9': 'Unknown'},
        },
        {
            'ranges': [
                {'start': 1995, 'end': 1996},
            ],
            'mapping': {'0': 'Not equipped', '1': 'Air Bag Deployed During Crash', 
                        '2': 'Airbag Deployed Prior to Crash', '3': 'Deployed, Sequence Unknown', '4': 'Deployed - Noncollision Event',
                        '5': 'Unknown if Deployed', '7': 'Nondeployed', '9': 'Unknown'},
        }
    ],
    'ABELTUSE': [
        {
            'ranges': [
                {'start': 1991, 'end': 1996},
            ],
            'mapping': {'0': 'Not equipped', '1': 'Automatic belt in use', '2': 'Automatic belt not in use',
                        '3': 'Automatic Belt Use Unknown', '9': 'Unknown'},
        }
    ],
    'POSTURE': [
        {
            'ranges': [
                {'start': 1988, 'end': 1992},
            ],
            'mapping': {'0': 'Normal Posture', '1': 'Abnormal Posture', '9': 'Unknown'},
        },
        {
            'ranges': [
                {'start': 1992, 'end': 1996},
            ],
            'mapping': {'0': 'Normal Posture', '1': 'Kneeling Or Standing On Seat', '2': 'Lying on or Across Seat',
                        '3': 'Kneel/Stand/Sitting in Front of Seat', '4': 'Sitting Sideways', '5': 'Sitting on Console',
                        '6': 'Lying in Reclined Seat Position', '7': 'Bracing Feet or Hands on Surface', 
                        '8': 'Other Abnormal Position', '9': 'Unknown'},
        }
    ],
    'MANAVAIL': [
        {
            'ranges': [
                {'start': 1988, 'end': 1996},
            ],
            'mapping': {'0': 'Not Available', '1': 'Belt Removed/Destroyed', '2': 'Shoulder Belt', '3': 'Lap Belt',
                        '4': 'Lap and Shoulder Belt', '5': 'Belt Available - Type Unknown', '6': 'Shoulder Belt (Lap Destroyed/Removed)',
                        '7': 'Lap Belt (Shoulder Destroyed/Removed)', '8': 'Other Belt', '9': 'Unknown'},
        },
    ],
    'MANFAIL': [
        {
            'ranges': [
                {'start': 1988, 'end': 1989},
            ],
            'mapping': {'0': 'Not Used or Not Available', '1': 'No Manual Belt Failures', '2': 'Manual Belt Failures', '9': 'Unknown'},
        },
        {
            'ranges': [
                {'start': 1990, 'end': 1996},
            ],
            'mapping': {'0': 'Not Used or Not Available', '1': 'No Manual Belt Failures', '2': 'Torn Webbing', '3': 'Broken Buckle or Latchplate',
                        '4': 'Upper Anchorage Separated', '5': 'Other Anchorage Separated', '6': 'Broken Retractor',
                        '7': 'Combination of Above', '8': 'Other Manual Belt Failure', '9': 'Unknown'},
        },
    ],
    'MANFAIL': [
        {
            'ranges': [
                {'start': 1988, 'end': 1989},
            ],
            'mapping': {'0': 'Not Used or Not Available', '1': 'No Manual Belt Failures', '2': 'Manual Belt Failures', '9': 'Unknown'},
        },
        {
            'ranges': [
                {'start': 1990, 'end': 1996},
            ],
            'mapping': {'0': 'Not Used or Not Available', '1': 'No Manual Belt Failures', '2': 'Torn Webbing', '3': 'Broken Buckle or Latchplate',
                        '4': 'Upper Anchorage Separated', '5': 'Other Anchorage Separated', '6': 'Broken Retractor',
                        '7': 'Combination of Above', '8': 'Other Manual Belt Failure', '9': 'Unknown'},
        },
    ],
    'MAIS': [
        {
            'ranges': [
                {'start': 1988, 'end': 1996},
            ],
            'mapping': {'0': 'Not Injured', '1': 'Minor Injury', '2': 'Moderate Injury', '3': 'Serious Injury',
                        '4': 'Severe Injury', '5': 'Critical Injury', '6': 'Maximum (Untreatable) Injury',
                        '7': 'Injury, Severity Unknown', '9': 'Unknown if Injured'},
        },
    ],
    'AUTAVAIL': [
        {
            'ranges': [
                {'start': 1988, 'end': 1990},
            ],
            'mapping': {'0': 'Not Equipped/Not Available', '1': 'Airbag', '2': 'Airbag Disconnected', '3': 'Airbag not Reinstalled',
                        '4': '2Point Automatic Belts', '5': '3Point Automatic Belts', '6': 'Automatic Belts Destroyed/Inoperative',
                        '9': 'Unknown'},
        },
    ],
    'BAGAVAIL': [
        {
            'ranges': [
                {'start': 1991, 'end': 1996},
            ],
            'mapping': {'0': 'Not Equipped/Not Available', '1': 'Airbag', '2': 'Airbag Disconnected', '3': 'Airbag not Reinstalled',
                        '9': 'Unknown'},
        },
    ],
    'ABELTAVL': [
        {
            'ranges': [
                {'start': 1991, 'end': 1996},
            ],
            'mapping': {'0': 'Not Equipped/Not Available', '1': '2Point Automatic Belts', '2': '3Point Automatic Belts', 
                        '4': 'Automatic Belts Destroyed/Inoperative', '3': 'Automatic Belt Type Unknown',
                        '9': 'Unknown'},
        },
    ],
    'MEDFACIL': [
        {
            'ranges': [
                {'start': 1988, 'end': 1996},
            ],
            'mapping': {'0': 'Not Treated at a Medical Facility', '1': 'Trauma Center', '2': 'Hospital', 
                        '3': 'Medical Clinic', '4': "Physician's Office", '5': 'Treatment Later At Medical Facility', 
                        '8': 'Other', '9': 'Unknown'},
        }
    ],
    'INJSEV': [
        {
            'ranges': [
                {'start': 1988, 'end': 1996},
            ],
            'mapping': {'0': 'No Injury', '1': 'Possible Injury', '2': 'Non-Incapacitating Injury', 
                        '3': 'Incapacitating Injury', '4': 'Killed', '5': 'Injury, Severity Unknown', 
                        '6': 'Died Prior to Accident', '9': 'Unknown'},
        }
    ],
    'WORKDAYS': [
        {
            'ranges': [
                {'start': 1988, 'end': 1996},
            ],
            'mapping': {'61': '61 or More Days Lost', '62': 'Fatally Injured', '97': 'Not Working Prior to Accident', 
                        '99': 'Unknown'},
        }
    ],
    'INLOC1': [intrusion_location_map],
    'INLOC2': [intrusion_location_map],
    'INLOC3': [intrusion_location_map],
    'INLOC4': [intrusion_location_map],
    'INLOC5': [intrusion_location_map],
    'INLOC6': [intrusion_location_map],
    'INLOC7': [intrusion_location_map],
    'INLOC8': [intrusion_location_map],
    'INLOC9': [intrusion_location_map],
    'INLOC10': [intrusion_location_map],

    'INCOMP1': [intrusion_component_map_1988_to_1994, intrusion_component_map_1995_to_1996],
    'INCOMP2': [intrusion_component_map_1988_to_1994, intrusion_component_map_1995_to_1996],
    'INCOMP3': [intrusion_component_map_1988_to_1994, intrusion_component_map_1995_to_1996],
    'INCOMP4': [intrusion_component_map_1988_to_1994, intrusion_component_map_1995_to_1996],
    'INCOMP5': [intrusion_component_map_1988_to_1994, intrusion_component_map_1995_to_1996],
    'INCOMP6': [intrusion_component_map_1988_to_1994, intrusion_component_map_1995_to_1996],
    'INCOMP7': [intrusion_component_map_1988_to_1994, intrusion_component_map_1995_to_1996],
    'INCOMP8': [intrusion_component_map_1988_to_1994, intrusion_component_map_1995_to_1996],
    'INCOMP9': [intrusion_component_map_1988_to_1994, intrusion_component_map_1995_to_1996],
    'INCOMP10': [intrusion_component_map_1988_to_1994, intrusion_component_map_1995_to_1996],

    'CDRIR1': [dominant_crush_direction],
    'CDRIR2': [dominant_crush_direction],
    'CDRIR3': [dominant_crush_direction],
    'CDRIR4': [dominant_crush_direction],
    'CDRIR5': [dominant_crush_direction],
    'CDRIR6': [dominant_crush_direction],
    'CDRIR7': [dominant_crush_direction],
    'CDRIR8': [dominant_crush_direction],
    'CDRIR9': [dominant_crush_direction],
    'CDRIR10': [dominant_crush_direction],

    'INMAG1': [intrusion_magnitude_1988_to_1992, intrusion_magnitude_1993_to_1996],
    'INMAG2': [intrusion_magnitude_1988_to_1992, intrusion_magnitude_1993_to_1996],
    'INMAG3': [intrusion_magnitude_1988_to_1992, intrusion_magnitude_1993_to_1996],
    'INMAG4': [intrusion_magnitude_1988_to_1992, intrusion_magnitude_1993_to_1996],
    'INMAG5': [intrusion_magnitude_1988_to_1992, intrusion_magnitude_1993_to_1996],
    'INMAG6': [intrusion_magnitude_1988_to_1992, intrusion_magnitude_1993_to_1996],
    'INMAG7': [intrusion_magnitude_1988_to_1992, intrusion_magnitude_1993_to_1996],
    'INMAG8': [intrusion_magnitude_1988_to_1992, intrusion_magnitude_1993_to_1996],
    'INMAG9': [intrusion_magnitude_1988_to_1992, intrusion_magnitude_1993_to_1996],
    'INMAG10': [intrusion_magnitude_1988_to_1992, intrusion_magnitude_1993_to_1996],
}