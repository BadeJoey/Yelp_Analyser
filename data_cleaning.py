# -*- coding: utf-8 -*-
"""
Created on Sat Jul  3 15:03:32 2021

@author: Joey
"""

import pandas as pd

# Cleaning der Daten

df = pd.read_csv(r"E:\Projekte\Yelp_Analyser\vancouver_yelp_stores.csv")

# Fixen der Nan Values in sinnvolle Werte

df["address"] = df["address"].fillna("")
df["categories"] = df["categories"].fillna("")
df["postal_code"] = df["postal_code"].fillna("")
df["attributes"] = df["attributes"].fillna("{}")
df["hours"] = df["hours"].fillna("{}")


# Entpacken der verschachelten Jsons (Nans müssen gefüllt sein zum klappen)
test2 = pd.json_normalize(df["attributes"].apply(lambda x: eval(x)))
#df = pd.concat([df, pd.json_normalize(df["attributes"].apply(lambda x: eval(x)))], axis=1)