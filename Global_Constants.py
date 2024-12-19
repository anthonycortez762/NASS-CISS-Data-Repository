import datetime

max_year = datetime.MAXYEAR
common_ciss_year_range = [{'start': 2017, 'end': max_year}]

ais_shared_mapping = {'1': 'Minor injury', '2': 'Moderate injury', '5': 'Critical injury', '6': 'Maximum injury'}
sex_shared_mapping = {'1': 'Male', '2': 'Female', '9': 'Unknown'}
weight_shared_mapping = {'999': 'Unknown'}
role_shared_mapping = {'1': 'Driver', '2': 'Passenger', '9': 'Unknown'}
entrapped_shared_mapping = {'0': 'Not entrapped', '1': 'Entrapped', '9': 'Unknown'}
ejection_shared_mapping = {'0': 'None', '1': 'Complete ejection', '2': 'Partial ejection',
                           '3': 'Ejection, unknown degree', '9': 'Unknown'}
treatment_shared_mapping = {'0': 'No treatment', '3': 'Hospitalization', '8': 'Treatment-other', '9': 'Unknown'}
hospstay_shared_mapping = {'61': '61 days or more', '99': 'Unknown'}
belt_use_shared_mapping = {'0': 'None used', '1': 'Shoulder belt', '2': 'Lap belt', '3': 'Lap and shoulder belt'}
intrusion_shared_mapping = {'997': 'Catastrophic'}
