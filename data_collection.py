# -*- coding: utf-8 -*-
"""
Created on Fri Jul  2 16:04:47 2021

@author: Joey
"""

import pandas as pd

# Einlesen der Yelp Datenbank

path = "E:\Projekte\Yelp_Analyser\yelp_academic_dataset_business.json"

data = pd.read_json(path, lines=True)


# Filtern der Geschäfte in Vancouver

data_vancouver = data[data["city"].str.lower() == "vancouver"]

# Cleaning der Daten

# data_vancouver.to_csv("vancouver_yelp_stores.csv", index = False)

# test = pd.read_csv("vancouver_yelp_stores.csv")