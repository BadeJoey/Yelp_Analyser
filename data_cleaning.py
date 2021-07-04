# -*- coding: utf-8 -*-
"""
Created on Sat Jul  3 15:03:32 2021

@author: Joey
"""

import pandas as pd


# Cleaning der Daten

pfad = r"E:\Projekte\Yelp_Analyser\vancouver_yelp_stores.csv"
df = pd.read_csv(pfad)


# Fixen der Nan Values in sinnvolle Werte

df["address"] = df["address"].fillna("")
df["categories"] = df["categories"].fillna("")
df["postal_code"] = df["postal_code"].fillna("")
df["attributes"] = df["attributes"].fillna("{}")
df["hours"] = df["hours"].fillna("{}")


# Entpacken der verschachelten Jsons (Nans müssen gefüllt sein zum klappen)
# Danach viele neue Nans fixen bei Benutzung 

df = pd.concat([df, 
                pd.json_normalize(df["attributes"].apply(lambda x: eval(x)))],
                axis=1)

df = pd.concat([df,
                pd.json_normalize(df["hours"].apply(lambda x: eval(x)))],
                axis=1)


# Bereinigen der durchschnittlichen Sterne
# Eine 5er Bewertung führt zu 5 Sternen ingesamt was ingesamt besser ist als
# ein Restaurant mit 100 5er Bewertung und 1 4er Bewertung. Daher nehmen wir
# an das jedes Geschäft jede Wertung von 1-5 einmal erhalten hat für einen
# faireren Mittelwert

# Alle Wertungen werden einmal hinzugefügt und dann geteilt durch die Anzahl 
# + die 5 neuen Wertungen
values = df.apply(lambda x: ((x["stars"] * x["review_count"])
                                       + 1.0 + 2.0 + 3.0 + 4.0 + 5.0) 
                                       / (x["review_count"] + 5), axis=1)
# Zum einfügen bei einer genauen Position neben Stars und Review_Counts
df.insert(8, "stars_fair", values)


# Einteilen in Geschäfte die Essen anbieten und nur Restaurants

df_food = df[df["categories"].str.contains("food|restaurants", case=False)]
df_restaurants = df[df["categories"].str.contains("restaurant", case=False)]


# Droppen der Felder von geringer Aussagekraft: 
#    BusinessAcceptsBitcoin, HairSpecializesIn, AcceptsInsurance, 
#    AgesAllowed, RestaurantsCounterService

df_food = df_food.drop(columns=["BusinessAcceptsBitcoin", 
                                "HairSpecializesIn", 
                                "AcceptsInsurance", 
                                "AgesAllowed", 
                                "RestaurantsCounterService"])
df_restaurants = df_restaurants.drop(columns=["BusinessAcceptsBitcoin", 
                                              "HairSpecializesIn", 
                                              "AcceptsInsurance", 
                                              "AgesAllowed", 
                                              "RestaurantsCounterService"])


# Speichern der neuen Daten Sets als CSV

df.to_csv("./vancouver_yelp_all_stores.csv", index = False)
df_food.to_csv("./vancouver_yelp_food.csv", index = False)
df_restaurants.to_csv("./vancouver_yelp_restaurants.csv", index = False)