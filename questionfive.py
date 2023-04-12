import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df_details = pd.read_csv('data/clean/df_details.csv')
df_vivareal = pd.read_csv('data/clean/df_vivareal.csv')
df_merge = pd.read_csv('data/clean/df_merge.csv')

df_merge_ilhota = df_merge[df_merge['Address'].isin(['Ilhota'])]
aux = df_merge_ilhota['price'].mean()
print(np.round(aux, 2))

df_igpm = pd.DataFrame({'year': 2024, 'revenue': 50*30352.44}, index=[0])
for k in np.arange(2025, 2027, 1):
    df = pd.DataFrame({'year': [k], 'revenue': df_igpm[df_igpm['year'] == k-1 ]['revenue']*1.0786}, index=[0])
    df_igpm = pd.concat([df_igpm, df], axis=0)

df_igpm.to_csv('data/clean/five/df_igpm.csv')