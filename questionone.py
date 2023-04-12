import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df_details = pd.read_csv('data/clean/df_details.csv')
df_vivareal = pd.read_csv('data/clean/df_vivareal.csv')
df_merge = pd.read_csv('data/clean/df_merge.csv')

plt.figure(figsize=(25, 10))
aux1 = df_merge[['Address', 'price']].groupby('Address').mean().sort_values('price', ascending=False).reset_index()
plt.title('Average rent amount')
sns.barplot(data=aux1, x="Address", y="price")
plt.show()

plt.subplot(1,2,1)
aux2 = df_vivareal[['address_neighborhood', 'sale_price']].groupby('address_neighborhood').mean().sort_values('sale_price', ascending=False).reset_index()
plt.title('Average property value by neighborhood')
plt.xticks(rotation =20)
sns.barplot(data=aux2, x="address_neighborhood", y="sale_price")
plt.subplot(1,2,2)
aux3 = df_vivareal[['unit_type', 'sale_price']].groupby('unit_type').mean().sort_values('sale_price', ascending=False).reset_index()
plt.xticks(rotation =20)
plt.title('Average property value by type')
sns.barplot(data=aux3, x="unit_type", y="sale_price")
plt.show()

df = df_vivareal[['address_neighborhood', 'unit_type', 'sale_price']]
df= df[df['address_neighborhood'] == 'Ilhota']
aux4 = df[['unit_type', 'sale_price']].groupby('unit_type').mean().reset_index()
plt.title('Average property value by type in the Ilhota neighborhood')
sns.barplot(data=aux4, x="unit_type", y="sale_price")
plt.show()

df_neigh_price = pd.DataFrame(columns=['ADDRESS', 'APARTMENT', 'FLAT', 'HOME', 'ALLOTMENT'])
waterfront = ['Canto da Praia', 'Morretes', 'Meia Praia', 'Centro', 'Ilhota']
for k in np.arange(len(waterfront)):
    df = df_vivareal[['address_neighborhood', 'unit_type', 'sale_price']]
    df= df[df['address_neighborhood'] == waterfront[k]]
    a = df[['unit_type', 'sale_price']].groupby('unit_type').mean().T
    a['ADDRESS'] = waterfront[k]
    df_neigh_price = pd.concat([df_neigh_price, a], axis=0).sort_values('ALLOTMENT').reset_index(drop=True)

df_neigh_price.to_csv('data/clean/one/df_neigh_price.csv')