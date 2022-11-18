import pandas as pd
import numpy as np

df_customer = pd.read_csv('https://raw.githubusercontent.com/The-Japan-DataScientist-Society/100knocks-preprocess/master/docker/work/data/customer.csv')
df_product = pd.read_csv('https://raw.githubusercontent.com/The-Japan-DataScientist-Society/100knocks-preprocess/master/docker/work/data/product.csv')
df_receipt = pd.read_csv('https://raw.githubusercontent.com/The-Japan-DataScientist-Society/100knocks-preprocess/master/docker/work/data/receipt.csv')

df_receipt_only_member = df_receipt[~df_receipt["customer_id"].str.startswith("Z")]
customer_id_only_member_sum = df_receipt_only_member.groupby('customer_id').sum()

df_customer_only_member = df_customer[~df_customer["customer_id"].str.startswith("Z")]
customer_amount = pd.merge(df_customer_only_member, customer_id_only_member_sum, on = 'customer_id', how='left')
custor_aount.fillna({'amountmem':0}).dropna(axis=1).query('gender_cd == 1').head()
