# Import required modules, constants and functions
import os
import zipfile
import pandas as pd
import utils
import constants

# Assign raw and clean directories
raw_zipped_directory = '../raw'
clean_directory = '../clean'

# Initialize a list that will be used to collect each years dataframe and the output filename
output_dataframes = []
output_filename = clean_directory + '/PATIENT_CLEANED.csv'


def clean_patient_files():
    # Iterate over each zip file in the raw directory
    for filename in os.listdir(raw_zipped_directory):
        f = os.path.join(raw_zipped_directory, filename)
        with zipfile.ZipFile(f, 'r') as z:
            # The filenames are not standard in CISS, so we will check the filepath for each year and open the occupant
            # and eject files
            filenames = z.namelist()
            path_to_occupant_csv = utils.get_file_path('OCC', filenames)
            path_to_eject_csv = utils.get_file_path('EJECT', filenames)
            with z.open(path_to_occupant_csv) as f:
                with z.open(path_to_eject_csv) as g:
                    occupant = pd.read_csv(f)
                    eject = pd.read_csv(g)

                    patient = pd.merge(occupant, eject, how='left', on=['CASEID', 'PSU', 'CASENO', 'VEHNO', 'OCCNO'])
                    patient = patient.filter(
                        ['CASEID', 'OCCNO', 'VEHNO', 'AGE', 'SEX', 'HEIGHT', 'WEIGHT', 'ROLE', 'PARBELTUSE',
                         'PARAIRBAG', 'SEATLOC', 'ENTRAP', 'EYEWEAR', 'HOSPSTAY', 'MOBILITY', 'MORTALITY', 'TREATMENT',
                         'EJECTTYPE'])

                    utils.clean_column_values(patient, constants.patient_column_maps)

                    output_dataframes.append(patient)

    # Combine each year's dataframe and write the combined dataframe to a new file
    final_df = pd.concat(output_dataframes)
    final_df.to_csv(output_filename, encoding='utf-8', index=False)


clean_patient_files()
