# Import required modules, Global Utils and NASS constants
import os
import pandas as pd
import NASS_Constants
import Global_Utils

# Assign raw and clean directories
nass_raw_directory = '../raw'
nass_clean_directory = '../clean'

# Defining NASS paths from 1979 to 1987 with lists grouped by years with similar schemas
nass_1979_and_1980_paths = ['NASS_1979', 'NASS_1980']
nass_1981_path = 'NASS_1981'
nass_1982_to_1987_paths = ['NASS_1982', 'NASS_1983', 'NASS_1984', 'NASS_1985', 'NASS_1986', 'NASS_1987']
nass_1979_to_1987_paths = ['NASS_1979', 'NASS_1980', 'NASS_1981', 'NASS_1982', 'NASS_1983', 'NASS_1984', 'NASS_1985',
                           'NASS_1986', 'NASS_1987']

# Setting occupant and output filenames
nass_occupant_file_ending = 'occupant.csv'
nass_injury_output_filename = nass_clean_directory + '/NASS_INJURY_CLEANED_1979_TO_1987.csv'

nass_injury_cleaned_dataframes = []


# The NASS 1981 occupant file has different column names than 1982 to 1987 (i.e. 'OAIS1' in 1981 vs 'AIS1' in 1982-1987)
# The clean_nass_1981 function will remove underscores and map certain column names to match their equivalent columns
# from the 1982-1987 NASS files
def clean_nass_1981(df):
    for col_name in df.columns:
        # First we remove underscores from the column names
        # Then some columns are in the format 'OAIS1', 'OAIS2', etc. and need to be renamed to 'AIS1', 'AIS2', etc.
        # Here we remove the last character from the column name. If the shortened column name is in the
        # nass_1981_col_name_map, we replace the prefix with the equivalent prefix from the 1982-1987 files
        # (i.e. 'OAIS' to 'AIS')
        final_col_name = col_name.replace("_", "")
        shortened_col_name = col_name[:-1]
        if shortened_col_name in NASS_Constants.nass_1981_col_name_map.keys():
            final_col_name = col_name.replace(
                shortened_col_name,
                NASS_Constants.nass_1981_col_name_map[shortened_col_name]
            )
        df = df.rename(columns={col_name: final_col_name})
    return df


def clean_nass_injury_files():
    # For each year of NASS we will read in the relevant occupant csv file
    # For NASS 1979 and 1980, we will map their respective column names to match the column names from 1982-1987
    # For NASS 1981 we will use the clean_nass_1981 function to map its columns to match the column names from 1982-1987
    for nass_year in nass_1979_to_1987_paths:
        occupant = pd.read_csv(os.path.join(nass_raw_directory, nass_year, nass_occupant_file_ending), dtype=str)
        if nass_year in nass_1979_and_1980_paths:
            occupant = occupant.rename(columns=NASS_Constants.nass_1979_and_1980_col_name_maps[nass_year])
        elif nass_year == nass_1981_path:
            occupant = clean_nass_1981(occupant)
        # Here we select the relevant columns, add a year column, and append each NASS year to a list to then union
        occupant = occupant[NASS_Constants.nass_1979_and_1980_col_name_maps['NASS_1979'].values()]
        occupant['YEAR'] = int(nass_year.split('_')[1])
        nass_injury_cleaned_dataframes.append(occupant)

    nass_1979_to_1987 = pd.concat(nass_injury_cleaned_dataframes)

    # Unpivot the 6 AIS, ASPECT, BODYREG, LESION, SYSORG, and SOUDAT columns into rows
    unpivoted_nass_1979_to_1987 = pd.wide_to_long(
        nass_1979_to_1987,
        stubnames=['AIS', 'ASPECT', 'BODYREG', 'LESION', 'SYSORG', 'SOUDAT'],
        i=['PSU', 'CASEID', 'YEAR', 'VEHNO', 'OCCNO', ],
        j='INJNO'
    ).reset_index()

    # Filter out injuries where all injury descriptor columns are NaN
    unpivoted_nass_1979_to_1987 = unpivoted_nass_1979_to_1987.dropna(
        subset=['AIS', 'ASPECT', 'BODYREG', 'LESION', 'SYSORG'], how='all')
    final_nass_1979_to_1987 = Global_Utils.clean_column_values(
        unpivoted_nass_1979_to_1987, NASS_Constants.nass_col_specific_value_maps, NASS_Constants.nass_global_value_map)

    final_nass_1979_to_1987.to_csv(nass_injury_output_filename, encoding='utf-8', index=False)


clean_nass_injury_files()
