![In Progress](https://badgen.net/badge/status/in-progress/yellow)
#### Links
- [Introduction](#introduction)
  - [English Version](#english)
  - [Deutsche Version](#deutsch)
 - [File Description](#files)
 - [Data Collection and Cleaning](#data-collection-and-cleaning)
 - [EDA Exploratory Data Analysis](#eda-exploratory-data-analysis)

# Yelp Analyser

## Introduction
### English
This Project explores the public [Yelp Dataset](https://www.yelp.com/dataset). It collects the data from the dataset and cleans it. The data will be filtered to only show stores in Vancouver, Canada. Furthermore, we look at restaurants in Vancouver and explore some interesting dependencies between the variables.

### Deutsch
Dieses Projekt erforscht das öffentliche [Yelp Dataset](https://www.yelp.com/dataset). Es sammelt die Daten aus dem Datensatz und bereinigt diese. Die Daten werden gefiltert, um nur Geschäfte in Vancouver, Kanada, anzuzeigen. Außerdem schauen wir uns Restaurants in Vancouver an und untersuchen einige interessante Abhängigkeiten zwischen den Variablen.

### Files
#### CSV
1. `vancouver_yelp_stores.csv`      - All stores in __Vancouver, Canada__
2. `vancouver_yelp_all_stores.csv`  - As 1. but __cleaned__
3. `vancouver_yelp_food.csv`        - As 2. but only where __food__ is served
4. `vancouver_yelp_restaurants.csv` - As 3. but only considered __restaurants__
#### Code
1. `data_collection.py` - Collecting the data from open yelp database
2. `data_cleaning.py`- Cleaning the data and filtering to only include Vancouver
3. `data_eda.ipynb` - Exploring the data and finding intresting connections

# Data Collection and Cleaning
The Collection is straightforward since the dataset from Yelp is already well build. We filter only to show stores in Vancouver. <br/><br/>
The Cleaning part __fills the obvious NaNs__ of the dataset and also unpack some nested JSON Columns. We also add a new column with __a more fair star rating__.<br/>
Currently, a store having one 5-star rating is on average better than a store with two thousand 5-star ratings and one 4-star rating. To make this more fair, we add every rating from 1 to 5 one time to each store before we take the average. This way, restaurants with low number of ratings are more influenced than restaurants with a lot of good ratings.
```python
df.apply(lambda x: ((x["stars"] * x["review_count"]) + 1.0 + 2.0 + 3.0 + 4.0 + 5.0) / (x["review_count"] + 5), axis=1)
```

# EDA Exploratory Data Analysis
It became clear through exploration there was still some cleaning to do in the EDA itself. We also created some dummy variables out of the categories of food the restaurants sells. Some categories were grouped like `'Japanese|SushiBars|Ramen'` all under Japanese. The opening times on weekdays and weekend were also calculated for each restaurant, given opening hours were provided.
<br/>
<br/>
Before we look at the Heat Map, we can see the `Pandas.describe()` of the numerical values.
<br/>
<br/>
![Describe](https://github.com/BadeJoey/Yelp_Analyser/blob/master/Images/describe.JPG)
<br/>
<br/>
Heat Map:<br/>
![Heat Map](https://github.com/BadeJoey/Yelp_Analyser/blob/master/Images/heatmap.JPG)
<br/>
<br/>
It shows a correlation between weekday hours and weekend hours, which is not surprising to think a restaurant that is long open during the weekdays will also be during the weekend. There also seems to be a weaker correlation between price range and review counts. We can see in this Pivot Table that especially the price range of 3 (which is more luxurious but still affordable) gets a lot of reviews.
<br/>
<br/>
![Price Range Box](https://github.com/BadeJoey/Yelp_Analyser/blob/master/Images/price_range_box.JPG)
![Price Range - Review Count](https://github.com/BadeJoey/Yelp_Analyser/blob/master/Images/price_review.JPG)
<br/>

---

Restaurants that have alcohol on the menu also show to get more reviews. It doesn't seem to affect the stars that are given.
<br/>
<br/>
![Alcohol Count](https://github.com/BadeJoey/Yelp_Analyser/blob/master/Images/alc_count.JPG)
![Alcohol Stars](https://github.com/BadeJoey/Yelp_Analyser/blob/master/Images/alc_stars.JPG)
![Alcohol Categories](https://github.com/BadeJoey/Yelp_Analyser/blob/master/Images/alc_cat.JPG)
<br/>

---

Fast food restaurants have on average less stars than non-fast food restaurants. They also get less reviews.
<br/>
<br/>
![Alcohol Count](https://github.com/BadeJoey/Yelp_Analyser/blob/master/Images/alc_count.JPG)
