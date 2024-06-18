"""
    Injury Table Notes
    - CISS doesn't record the LESION, SYSORG, ASPECT90 and SOUDAT columns from NASS (pgs. 518-520 in Crash Investigation Sampling System, 2021 Analytical User’s Manual)
    - Instead of the LESION and SYSORG columns from NASS, we will keep the STRUTYPE and STRUSPEC columns that cover a lot of the same data
    - We will also pull in the L1, L2, and LDEF columns from the localizer table instead of the ASPECT90 column from NASS to further specify the localization of the injury
    - Users are cautioned that ASPECT90 does not easily map to L1. Users should use caution when comparing. (pg. 515 in Crash Investigation Sampling System, 2021 Analytical User’s Manual)
"""

# Import required modules
import os
import zipfile
import pandas as pd

# Assign raw and clean directories
raw_zipped_directory = '../raw'
clean_directory = '../clean'

# Initialize a list that will be used to collect each years dataframe and the output filename
output_dataframes = []
output_filename = clean_directory + '/INJURY_CLEANED.csv'

# Initialize the maps to convert AIS and body region from numbers to their descriptors
ais_map = {1: 'Minor Injury', 2: 'Moderate Injury', 3: 'Serious Injury', 4: 'Severe Injury', 5: 'Critical Injury',
           6: 'Maximum Injury', 9: 'Injured, Unknown Severity'}
region_map = {0: 'Other Trauma', 1: 'Head', 2: 'Face', 3: 'Neck', 4: 'Thorax', 5: 'Abdomen', 6: 'Spine',
              7: 'Upper Extremity', 8: 'Lower Extremity', 9: 'Unspecified'}


def clean_ciss():
    # Iterate over each zip file in the raw directory
    for filename in os.listdir(raw_zipped_directory):
        f = os.path.join(raw_zipped_directory, filename)
        with zipfile.ZipFile(f, 'r') as z:
            # The filenames are not standard in CISS, so we will check the filepath for each year and open the injury
            # and localizer files
            filenames = z.namelist()
            path_to_injury_csv = get_file_path('INJURY', filenames)
            path_to_localizer_csv = get_file_path('LOCALIZER', filenames)
            with z.open(path_to_injury_csv) as f:
                with z.open(path_to_localizer_csv) as g:
                    # Filter to the columns we will use from the localizer table
                    localizer = pd.read_csv(g)
                    localizer_cleaned = localizer.filter(
                        ['CASEID', 'CASENO', 'VEHNO', 'OCCNO', 'INJNO', 'L1', 'L2', 'LDEF'])

                    # Filter to columns we will use from the injury table and convert the AIS and REGION columns to
                    # their descriptors
                    injury = pd.read_csv(f)
                    injury_cleaned = injury.filter(
                        ['CASEID', 'CASENO', 'VEHNO', 'OCCNO', 'INJNO', 'AIS', 'REGION', 'STRUTYPE', 'STRUSPEC',
                         'INJLEVEL'])
                    injury_cleaned['AIS'] = injury_cleaned['AIS'].replace(ais_map)
                    injury_cleaned['REGION'] = injury_cleaned['REGION'].replace(region_map)

                    # Join the injury and localizer tables and add the dataframe to the output_dataframes list
                    injury_joined = pd.merge(injury_cleaned, localizer_cleaned, how='left',
                                             on=['CASEID', 'CASENO', 'VEHNO', 'OCCNO', 'INJNO'])
                    output_dataframes.append(injury_joined)

    # Combine each year's dataframe and write the combined dataframe to a new file
    final_df = pd.concat(output_dataframes)
    final_df.to_csv(output_filename, encoding='utf-8', index=False)


def get_file_path(substring, filenames):
    for name in filenames:
        if substring.upper() in name.upper():
            return name


clean_ciss()
