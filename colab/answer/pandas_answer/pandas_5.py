import pandas as pd
import numpy as np

df_customer = pd.read_csv('https://raw.githubusercontent.com/The-Japan-DataScientist-Society/100knocks-preprocess/master/docker/work/data/customer.csv')
df_product = pd.read_csv('https://raw.githubusercontent.com/The-Japan-DataScientist-Society/100knocks-preprocess/master/docker/work/data/product.csv')
df_receipt = pd.read_csv('https://raw.githubusercontent.com/The-Japan-DataScientist-Society/100knocks-preprocess/master/docker/work/data/receipt.csv')

df_receipt_only_member = df_receipt[~df_receipt["customer_id"].str.startswith("Z")]
customer_id_only_member_sum = df_receipt_only_member.groupby('customer_id').sum()
customer_id_only_member_mean = customer_id_only_member_sum.mean()
customer_id_only_member_meanup = customer_id_only_member_sum[customer_id_only_member_sum["amount"]>=customer_id_only_member_mean["amount"]]
customer_id_only_member_meanup[["amount"]].head()
