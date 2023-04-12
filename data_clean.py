#### Imports

import time
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from geopy.geocoders import Nominatim

#### Loading Data

columns_av = ['airbnb_listing_id', 'price', 'ano', 'mes', 'dia']

columns_details = ['ad_id', 'number_of_bathrooms', 'number_of_bedrooms',
                   'number_of_beds', 'latitude', 'longitude', 'ano', 'mes', 'dia']

columns_vivareal = ['listing_id', 'business_types', 'unit_type',
                   'property_type', 'usage_type', 'sale_price', 'bathrooms',
                   'bedrooms', 'suites', 'address_neighborhood', 'property_type']

columns_mesh = ['airbnb_listing_id', 'latitude', 'longitude']


df_details = pd.read_csv('data/Details_Data.csv', usecols=columns_details)
df_mesh = pd.read_csv('data/Mesh_Ids_Data_Itapema.csv', usecols=columns_mesh)
df_vivareal = pd.read_csv('data/Vivareal_Itapema.csv', usecols=columns_vivareal)
df_av = pd.read_csv('data/Price_AV_Itapema.csv', usecols=columns_av)

df_av = df_av.sample(30000, random_state=42)


#### Helper Functions

# Removing scientific notation
pd.set_option('display.float_format', lambda x: '%.2f' %x)

# creating suburbs
def create_suburb(df):
    lat=df['latitude'].to_list()
    lon=df['longitude'].to_list()
    # Creating a zip with latitudes and longitudes
    coords=list(zip(lat,lon)) 

    geolocator = Nominatim(user_agent="test_app") 
    full_suburb=[]
    for i in range(len(coords)):
        try:
            location = geolocator.reverse(coords[i])
            suburb=location.raw['address']['suburb']
            full_suburb.append(suburb)
        except:
            full_suburb.append('NA')

        time.sleep(1)
    #Creating dataframe with all the suburbs
    suburb=pd.DataFrame(data=full_suburb , columns=['Address'])
    return suburb


#### Check and Treatment NAs

# Dataframe Details
aux1 = np.round(df_details['number_of_bedrooms'].median(), 2)
df_details['number_of_bedrooms'].fillna(aux1, inplace=True)

aux2 = np.round(df_details['number_of_beds'].median(), 2)
df_details['number_of_beds'].fillna(aux2, inplace=True)

df_details['number_of_bathrooms'].fillna(1, inplace=True)

# Dataframe Vivareal
df_vivareal['bathrooms'].fillna(1, inplace=True)

aux3 = np.round(df_vivareal['bedrooms'].median(), 2)
df_vivareal['bedrooms'].fillna(aux1, inplace=True)

df_vivareal['suites'].fillna(0, inplace=True)

aux4 = np.round(df_vivareal['sale_price'].median(), 2)
df_vivareal['sale_price'].fillna(aux2, inplace=True)

df_vivareal.dropna(inplace=True)

# Dataframe AV
df_av.dropna(inplace=True)


#### Check and Change Data Types

# Dataframe Details
df_details['number_of_bedrooms'] = df_details['number_of_bedrooms'].astype(int)
df_details['number_of_beds'] = df_details['number_of_beds'].astype(int)
df_details['number_of_bathrooms'] = df_details['number_of_bathrooms'].astype(int)

# Dataframe Vivareal
df_vivareal['bathrooms'] = df_vivareal['bathrooms'].astype(int)
df_vivareal['bedrooms'] = df_vivareal['bedrooms'].astype(int)
df_vivareal['suites'] = df_vivareal['suites'].astype(int)


#### Feature Engineering

# Rows filtering
df_mesh.drop_duplicates(inplace=True)
df_details.drop_duplicates(inplace=True)
df_av.drop_duplicates(inplace=True)
df_vivareal.drop_duplicates(inplace=True)

df_vivareal = df_vivareal[df_vivareal['business_types'] != '["RENTAL"]']

# merge dataframes df_av and df_mesh
df_merge = df_av.merge(df_mesh, on='airbnb_listing_id', how='left')

# uniformity of presentation of data
df_vivareal['address_neighborhood'] = df_vivareal['address_neighborhood'].replace({'Meia praia': 'Meia Praia', 'meia praia': 'Meia Praia', 'MEIA PRAIA': 'Meia Praia', 
                                                                                   'Meia Praia - Frente Mar': 'Meia Praia', 'MORRETES': 'Morretes', 'itapema': 'Itapema', 
                                                                                   'ITAPEMA': 'Itapema', 'Varzea': 'Várzea', 'Alto Sao Bento': 'Alto São Bento',
                                                                                   'Tabuleiro': 'Tabuleiro dos Oliveiras', 'Praia Mar': 'Jardim Praia Mar'})

df_vivareal['business_types'] = df_vivareal['business_types'].replace({'["RENTAL", "SALE"]': '["SALE", "RENTAL"]'})

df_vivareal['unit_type'] = df_vivareal['unit_type'].replace({'COMMERCIAL_BUILDING': 'COMMERCIAL_PROPERTY', 'COMMERCIAL_ALLOTMENT_LAND': 'COMMERCIAL_PROPERTY', 
                                                             'BUSINESS': 'COMMERCIAL_PROPERTY', 'BUILDING': 'COMMERCIAL_PROPERTY', 
                                                             'SHED_DEPOSIT_WAREHOUSE': 'COMMERCIAL_PROPERTY', 'OFFICE': 'COMMERCIAL_PROPERTY', 
                                                             'ALLOTMENT_LAND': 'RESIDENTIAL_ALLOTMENT_LAND', 'RESIDENTIAL_BUILDING': 'APARTMENT', 
                                                             'FARM': 'COUNTRY_HOUSE', 'TWO_STORY_HOUSE': 'HOME', 'CONDOMINIUM': 'APARTMENT' })

# Defining neighborhood of df_merge from lat and lon
suburb_merge = create_suburb(df_merge)
df_merge = pd.concat([df_merge, suburb_merge], axis=1)

# Defining neighborhood of df_details from lat and lon
suburb_details = create_suburb(df_details)
df_details = pd.concat([df_details, suburb_details], axis=1)

# Adjusting new datafrmes
df_merge.dropna(inplace=True)
df_details.dropna(inplace=True)
df_details['number_of_bathrooms'] = df_details['number_of_bathrooms'].astype(int)
df_details['number_of_bedrooms'] = df_details['number_of_bedrooms'].astype(int)

#filtering for neighborhoods Canto da Praia, Morretes, Meia Praia, Centro e Ilhota
waterfront = ['Canto da Praia', 'Morretes', 'Meia Praia', 'Centro', 'Ilhota']
df_details = df_details[df_details['Address'].isin(waterfront)]
df_vivareal = df_vivareal[df_vivareal['address_neighborhood'].isin(waterfront)]
df_vivareal = df_vivareal[df_vivareal['unit_type'].isin(['APARTMENT', 'RESIDENTIAL_ALLOTMENT_LAND', 'FLAT', 'HOME'])]
df_vivareal = df_vivareal.replace({'RESIDENTIAL_ALLOTMENT_LAND':'ALLOTMENT'})
df_merge = df_merge[df_merge['Address'].isin(waterfront)]

# export clean dataframes
df_details.to_csv('data/clean/df_details.csv')
df_merge.to_csv('data/clean/df_merge.csv')
df_vivareal.to_csv('data/clean/df_vivareal.csv')