import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df_details = pd.read_csv('data/clean/df_details.csv')
df_vivareal = pd.read_csv('data/clean/df_vivareal.csv')
df_merge = pd.read_csv('data/clean/df_merge.csv')


df_details_ilhota = df_details[df_details['Address'].isin(['Ilhota'])]
plt.figure(figsize=(20, 10))
plt.subplot(1,2,1)
aux1 = df_details_ilhota[['number_of_bathrooms', 'ad_id']].groupby('number_of_bathrooms').count().reset_index()
plt.title('Number of properties by number of bathrooms')
sns.barplot(data=aux1, x="number_of_bathrooms", y="ad_id")

plt.subplot(1,2,2)
aux2 = df_details_ilhota[['number_of_bedrooms', 'ad_id']].groupby('number_of_bedrooms').count().reset_index()
plt.title('Number of properties by number of bedrooms')
sns.barplot(data=aux2, x="number_of_bedrooms", y="ad_id")
plt.show()