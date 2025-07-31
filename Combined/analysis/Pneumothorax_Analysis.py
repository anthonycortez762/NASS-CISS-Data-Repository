import pandas as pd
import matplotlib.pyplot as plt

def categorize_injury(aiscode):
    if aiscode in ['442202.2', '442203.4', '442204.5', '442205.3', '442206.5', '442200.3', '442201.4']:
        return 1
    return 0

def categorize_case_wgt(row):
    if row['AISCODE'] in ['442202.2', '442203.4', '442204.5', '442205.3', '442206.5', '442200.3', '442201.4']:
        return row['CASEWGT']
    return 0


# Assign raw and clean directories
injury_clean_directory = '../../CISS/clean/INJURY_CLEANED.csv'
analysis_df = pd.read_csv(injury_clean_directory, dtype={'CASEWGT': float, 'AISCODE': str, 'CASEID': str, 'VEHNO': str, 'OCCNO': str})


analysis_df['PATIENTID'] = analysis_df['CASEID'] + '_' + analysis_df['VEHNO'] + '_' + analysis_df['OCCNO']
analysis_df['PTX'] = analysis_df['AISCODE'].apply(categorize_injury)
analysis_df['PTXCASEWGT'] = analysis_df.apply(categorize_case_wgt, axis=1)

patient_ptx_df = analysis_df.groupby(['PATIENTID', 'YEAR', 'CASEWGT']).agg(
    PTX=('PTX', 'max'),
    PTXCASEWGT=('PTXCASEWGT', 'max')
).reset_index()

graph_df = patient_ptx_df.groupby(['YEAR']).agg(
    TOTALPATIENTS=('PATIENTID', 'count'),
    TOTALCASEWGT=('CASEWGT', 'sum'),
    TOTALPTX=('PTX', 'sum'),
    TOTALPTXCASEWGT=('PTXCASEWGT', 'sum'),
).reset_index()

graph_df.to_csv('/Users/anthonycortez/Downloads/graph_input.csv', index=False)

plt.plot(graph_df['YEAR'], graph_df['TOTALPTX'])
plt.title('CISS Total Yearly Patients with Pneumothorax')
plt.xlabel("Year")
plt.ylabel("Total Patients")

plt.show()
