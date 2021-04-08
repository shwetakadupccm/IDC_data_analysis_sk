import pandas as pd
import numpy as np
import os
from sklearn.preprocessing import LabelEncoder
import statsmodels.api as sm
from statsmodels.formula.api import ols
from scipy.stats import shapiro

df = pd.read_excel('D:\\Shweta\\799_cases\\2021_04_05_799_cases_2010_2018_sk.xlsx', sheet_name='799_IDC')

lb = LabelEncoder()

############################################################################################

def encode_the_all_columns(folder, file):
    df_path = os.path.join(folder, file)
    df = pd.read_excel(df_path)
    df2 = df.select_dtypes(include=['object'])
    df_cols = df2.columns
    col_list = ['file_number', 'patient_name', 'biopsy_date', 'surgery_date', 'last_follow_up_date',
                'recurrence_date', 'subtype']

    for col in df_cols:
        df[col] = df[col].fillna('None')
        if col in col_list:
            continue
        df[col] = df[col].astype('str')
        df[col] = lb.fit_transform(df[col])
    return df

# idc_encoded_data = encode_the_all_columns('D:\\Shweta\\799_cases', '2021_04_05_799_cases_2010_2018_sk.xlsx')

# df_melt = pd.melt(idc_encoded_data, id_vars=['subtype'],
#                   value_vars= ['age_at_diagnosis', 'menopause_status', 'ihc_report',
#                                'er_status', 'er%', 'pr_status', 'pr%', 'her2_grade', 'fish_status',
#                                'nact', 'tumour_grade', 'Pathology_tumour_status_or_tumour_dimensions',
#                                'pT', 'lymph_node_status', 'pN', 'act', 'rt_status', 'last_follow_up_status',
#                                'recurrence_site_local_distant', 'laterality', 'her2_status'])
#
# sns.boxplot(x='subtype', y='value', hue='variable', data=df_melt, palette='Set3')

#### one way

# age_df_melt = pd.melt(idc_encoded_data.reset_index(), id_vars = ['subtype'], value_vars=['age_at_diagnosis'])

# model_one_way = ols('value ~ subtype', data=age_df_melt).fit()
# anova_table_one_way = sm.stats.anova_lm(model_one_way, typ=2)

def get_anova_table_for_each_column(folder, file):
    encoded_df = encode_the_all_columns(folder, file)
    df_cols = encoded_df.columns
    col_list = ['file_number', 'patient_name', 'biopsy_date', 'surgery_date', 'last_follow_up_date',
                'recurrence_date', 'subtype']

    shapiro_test_p_values = []
    anova_lst = []

    for col in df_cols:
        if col in col_list:
            continue

        statisic, shapiro_p_value = shapiro(encoded_df[col])
        shapiro_output_lst = np.append(col, shapiro_p_value)
        shapiro_test_p_values.append(shapiro_output_lst)
        shapiro_df = pd.DataFrame(shapiro_test_p_values, columns=['variable', 'shapiro_p_value'])

        if shapiro_p_value > 0.05:
            melt_df = pd.melt(encoded_df, id_vars=['subtype'], value_vars=[col])
            model = ols('value ~ subtype', data=melt_df).fit()
            anova_table = sm.stats.anova_lm(model, typ=2)
            p_value = anova_table['PR(>F)'][0]
            output_lst = np.append(col, p_value)
            anova_lst.append(output_lst)
            anova_df = pd.DataFrame(anova_lst, columns=['variable', 'p-value'])
        else:
            print('data is not normal')
    return anova_df, anova_lst, shapiro_df


# anova_df, anova_lst, shapiro_df = get_anova_table_for_each_column('D:\\Shweta\\799_cases', '2021_04_05_799_cases_2010_2018_sk.xlsx')

