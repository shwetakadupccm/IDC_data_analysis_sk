import pandas as pd
import os


def get_value_count_for_each_column(folder, file):
    df_path = os.path.join(folder, file)
    df = pd.read_excel(df_path)
    df_cols = df.columns
    writer = pd.ExcelWriter('D:/Shweta/799_cases/2021_03_30_value_counts.xlsx',
                            engine='xlsxwriter')

    unique_value_count_list = []
    for col in df_cols:
        col_value_counts = df[col].value_counts()
        col_value_counts = col_value_counts.reset_index()
        print(col_value_counts)
        if len(col) >= 31:
            col = col[0:31]
        else:
            col = col
        col_value_counts.to_excel(writer, sheet_name=col, index=False)
        unique_value_count_list.append(col_value_counts)
    writer.save()
    output_df = pd.DataFrame(unique_value_count_list, columns=df_cols)
    return unique_value_count_list, output_df

##

idc_dat = pd.read_excel('D:\\Shweta\\799_cases\\2021_02_09_799_cases_Orchids2010_2018_rb_dk.xlsx')

survivor_1 = ['Survivor: Lost to follow.up', 'Survivor: Disease free', 'Survivor: With recurrence',
              'Survivor: metastatic disease', 'Survivor: with Mets', 'Survivor: primary surgery not done',
              'Survivor: with disease', 'Survivor: with recurrence']

deceased_0 = ['Deceased']


survival_status = []
for value in idc_dat.last_follow_up_status:
    if value in survivor_1:
        survival_status.append(1)
    elif value ==  'Deceased':
        survival_status.append(0)
    else:
        survival_status.append('NA')

import statsmodels.api as sm

x = idc_dat['age_at_diagnosis']
y = pd.Series(survival_status)

model = sm.OLS(y, x, missing='drop')

idc_dat.dtypes

