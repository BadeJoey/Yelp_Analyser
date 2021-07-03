# -*- coding: utf-8 -*-
"""
Created on Sat Jul  3 15:03:32 2021

@author: Joey
"""

import pandas as pd

# Cleaning der Daten

test = pd.read_csv(r"E:\Projekte\Yelp_Analyser\vancouver_yelp_stores.csv")

test.columns

test["stars"].value_counts()
test["stars"].mean()
test["stars"].median()
test["stars"].mode()
test["stars"].isna().sum()


test["review_count"].value_counts()
test["review_count"].mean()
test["review_count"].median()
test["review_count"].mode()
test["review_count"].isna().sum()

test["review_count"].where(test["stars"] == 5.0,).groupby(test["review_count"]).transform('max')

test.describe()