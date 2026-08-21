# Bike sharing data analysis
## About the project

This project analyzes the bike sharing dataset.
The dataset contains information about bike rentals together with time, weather, season, working/non-working day. 
The goal of project was to practice complete data analysis and ML workflow:
-loading and validating data;
-exploratory data analysis(EDA)
-feature engineering
-encoding and scaling
-train/test splitting
-implementing KNN
-evaluating model performance
-error analysis

The target variable is 'cnt', which represents total number of bike rentals

## Dataset
The main dataset that was used is: data/row/hour.csv

Dataset includes hourly information and such columns - instant, dteday, season, yr, mnth, hr, holiday, weekday, workingday, weathersit, temp, atemp, hum, windspeed, casual, registered, cnt. 

## Project structure

Bike-Sharing-Project/
│
├── data/
│   ├── raw/
│   │   ├── hour.csv
│   │   └── day.csv
│   └── processed/
│       ├── hour_features.csv
│       ├── X_train.csv
│       ├── X_test.csv
│       ├── y_train.csv
│       └── y_test.csv
│
├── notebooks/
│   ├── 02_eda.ipynb
│   ├── 03_feature_engineering.ipynb
│   ├── 04_data_preparation.ipynb
│   └── 05_knn.ipynb
│
├── source/
│   ├── load_data.py
│   ├── validate_data.py
│   └── transform_data.py
│
├── tests/
│   ├── test_validate_data.py
│   └── test_transform_data.py
│
├── cli.py
└── README.md

## Data loading

The first part of project was built on opening and validating data. The project includes: open(), csv.DictReader, functions for counting rows and columns, checking missing values and column names, identify categorical and numerical columns. 
Data validation was conducted in validate_data.py. Examples: validation of hour, month, season, weather. 

## Exploratory data analysis(EDA)

For EDA analysis it was investigated how bike demand changes by different factors. I explored how factors influence on rental activity. Factors that I used: hour, days off and working days, season, weather.

## Feature enginnering

In transform_data.py I created several new features from original data. 
time_of_day: hour was transformed into 4 groups(Morning, afternoon, evening, night)
high_demand: binary feature created
rush_hour: binary feature identifying typical working day rush-hours(morning: 7-9, evening: 17-19)
These features were added to dataset and saved to data/processed/hour_features.csv

## Preparing data for KNN

The target is 'cnt'
Model receives X and predict y(X-info given to model, y-value to predict).
Features that can give straight answer were deleted, id column - was deleted also. High_demand was removed because it rises from cnt.

## Encoding categorical features

KNN works only with numerical values so encoding was used to calculate distances between observations. 
For eg: time_of_day was transformed into columns - time_of_day_Morning, time_of_day_Afternoon, time_of_day_Evening, time_of_day_Night. Values are represented as 0 and 1. 

## Feature scaling

KNN uses distances and some features have different numerical ranges which will spoil results and influence on Euclidian distance. We scale features with formula: z = (x - mean) / standard deviation.

## Train/test split

Data was divided into training and testing sets(80/20). Testing data is used to evaluate predictions on unseen data. 

## KNN regression 
KNN was implemented from scratch without using libraries. 
Steps: 1) Test point

2) Calculate distance to every training point

3) Sort distances

4) Select K nearest neighbors

5) Take their target values

6) Calculate their average

7) Prediction

The distance metric: Euclidian distance

## Choosing K

Through different expirements I chose the best K, it is 5

## Model evaluation

3 metrics were used

MAE(Mean Absolute Error) - average absolute difference between real value and predicted one. 
MAE = average(|actual - prediction|)
For selected K, MAE is about 75, so this means that predicted model differs from actual by 75 rentals. 

RMSE(Root Mean Squarred Error) - gives more weight to large errors.
RMSE = sqrt(average((actual - prediction)^2))
I got around 107.

R² - measures how much of variation in target is explained by model. 
R²≈0.76

## Baseline

A simple baseline was calculated. Baseline predicts the mean training for every test observation. This provides simple reference point for evaluating whether KNN provides useful predictions.

## Error analysis

After generating predictions, individual prediction errors were analyzed.
For every test observation, project stores - actualprediction,error,index,hr,workingday,season,weathersit,time_of_day. This analysis was saved to data/processed/knn_error_analysis.csv