import pandas as pd
import pandas_profiling as pp

df = pd.read_csv('D:\\Shweta\\metabric_data\\brca_metabric_clinical_data.tsv', sep = '\t')

df.to_excel('D:\\Shweta\\metabric_data\\brca_metabric_clinical_data.xlsx', index = False)


profile = pp.ProfileReport(df)
profile.to_file('D:\\Shweta\\metabric_data\\2021_04_03_metabroc_data_profile_report_sk.html')
