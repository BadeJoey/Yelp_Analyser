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
Before we start, let's look at `Pandas.describe()` of the numerical values.
<br/>
<br/>
![Describe](https://github.com/BadeJoey/Yelp_Analyser/blob/master/Images/describe.JPG)
<br/>

## Basic Analysis
### Number of Restaurants
First let's see where most restaurants are in Vancouver.
<br/>
<br/>
![Map Count](https://github.com/BadeJoey/Yelp_Analyser/blob/master/Images/map_count.JPG)
<br/>
<br/>
We can see that the __West End__ and especially __Downtown__ have the highest number of restaurants. This fits with the reputation of this neigborhoods since Downtown is famous for its __buzzing nightlife and restaurant scene__.

### Review Counts
The review distrubtion has a tail that goes to the __max value of 2302 reviews__. Its important to point out that we have a log scale for the y-axis so the curve is much steeper in a normal scale.
<br/>
<br/>
![Review Count](https://github.com/BadeJoey/Yelp_Analyser/blob/master/Images/review_count.JPG)
<br/>
<br/>
We see that the __mean of reviews__ is __not__ heavy dependent on the postal code. But still there is a __slight increase__ in the expected __downtown area__. Keep in mind that the __review count doesn't necessarily__ say anything about the __number of customers__. 
<br/>
<br/>
![Map Review](https://github.com/BadeJoey/Yelp_Analyser/blob/master/Images/map_review.JPG)

###Stars and Price
Star, Fair Stars and Price Range all seem to be __normally distributed with a negativ skew__.
<br/>
<br/>
![Stars and Price Count](https://github.com/BadeJoey/Yelp_Analyser/blob/master/Images/star_fair_price.JPG)
<br/>
<br/>
The Map also shows an even distribution. The __Downtime Eastside__ shows a little __higher mean__. This semms to be connected to the Japanese Restaurants in the Area which has higher ratings as we will later see.
<br/>
<br/>
![Map Star](https://github.com/BadeJoey/Yelp_Analyser/blob/master/Images/map_star.JPG)
<br/>
<br/>
Also the Price seems to even out over all the Areas.
<br/>
<br/>
![Map Price](https://github.com/BadeJoey/Yelp_Analyser/blob/master/Images/map_price.JPG)
<br/>
<br/>
Here another visualitation of boxplots for reviews, stars, fair stars and price range. 
<br/>
<br/>
![Stars Review Price](https://github.com/BadeJoey/Yelp_Analyser/blob/master/Images/star_fair_price_review.JPG)

## Correlation

### Heat Map
![Heat Map](https://github.com/BadeJoey/Yelp_Analyser/blob/master/Images/with_population_corr.JPG)
<br/>
<br/>
The strongest correlation is shown between weekday hours and weekend hours, which is not surprising to think a restaurant that is long open during the weekdays will also be during the weekend.
<br/>
<br/>
![Weekday Weekend Correlation](https://github.com/BadeJoey/Yelp_Analyser/blob/master/Images/week_end_corr.JPG)
<br/>
There also seems to be a correlation between price range/review counts and star/review counts. We can see this more clearly in the following graphes.

### Does a higher price or better ratings give you more reviews?
![Price Range - Review](https://github.com/BadeJoey/Yelp_Analyser/blob/master/Images/review_price_corr.JPG)
<br/>
<br/>
The price range of the restaurants does affect the review count strongly. It peaks at the price range of 3 the second highest in Yelp. The reason for this could be that these restaurants are still afforadable for working class people or maybe with the expactation that comes with the price.
<br/>
<br/>
![Stars - Review Count](https://github.com/BadeJoey/Yelp_Analyser/blob/master/Images/review_star_corr.JPG)
<br/>
<br/>
The same can be said for stars. They also peak at the second-highest value of 4-stars, but then fall stronger at 5 stars. A 4-star rating could also be achieved though a combination of 3- and 5-star reviews also our graphs before showed that the median of stars given is 4, which would explain the more ratings. Were, 5-Star ratings can only be achieved when all people rate with 5-stars, which is unlikely.
<br/>
<br/>
![All together - Price - Stars - Review](https://github.com/BadeJoey/Yelp_Analyser/blob/master/Images/stars_price_review.JPG)
<br/>
<br/>
Combining these 3 together, we can see that the highest review count can be achieved with price rating of 3 and current stars of 4.5. So your restaurant should be exclusive but not luxurious and the higher your ratings the better.

### Higher Price better Ratings?
The Heat Map shows no Correlation between price and stars. But if we look closer at these two together, it shows that with higher price, you at least narrow down your ratings to a higher median and mean. You won't be scored 2-stars in total, but you are also missing out on the 5-star perfect rating, which likely comes from high expectations with this kind of price tag.
<br/>
<br/>
![Price with Stars](https://github.com/BadeJoey/Yelp_Analyser/blob/master/Images/stars_price.JPG)


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
