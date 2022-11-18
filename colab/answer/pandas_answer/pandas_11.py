import pandas as pd
import numpy as np

df_customer = pd.read_csv('https://raw.githubusercontent.com/The-Japan-DataScientist-Society/100knocks-preprocess/master/docker/work/data/customer.csv')
df_product = pd.read_csv('https://raw.githubusercontent.com/The-Japan-DataScientist-Society/100knocks-preprocess/master/docker/work/data/product.csv')
df_receipt = pd.read_csv('https://raw.githubusercontent.com/The-Japan-DataScientist-Society/100knocks-preprocess/master/docker/work/data/receipt.csv')

unit_price_mean = df_product['unit_price'].mean()
unit_cost_mean = df_product['unit_cost'].mean()
df_product_2 = df_product.fillna({'unit_price':unit_price_mean ,'unit_cost':unit_cost_mean})
df_product_2.isnull().sum()
