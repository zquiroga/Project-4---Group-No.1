# Vehicle Price Prediction in Australia
Project4 - UWA/edX Data Analytics Bootcamp

## Table of Contents

1. [Introduction](#introduction)
   1. [Overview](#overview)
   2. [Objective](#objective)
2. [Features](#features)
3. [Approach](#approach)
   1. [Methodology](#methodology)
   2. [Structure](#structure)
   3. [Scripts](#scripts)
4. [Repository Structure](#repository-structure)
5. [Data Sources and Copyright](#data-sources-and-copyright)
   1. [Data Sources](#data-sources)
   2. [Copyright Notice](#copyright-notice)
6. [Conclusion](#conclusion)
7. [References](#references)


## Introduction

### Overview



### Objective


## Getting Started

### Prerequisites



### Installation



### Running the Application




## Features



## Approach

### Methodology





### Structure



## Coding 



## Repository Structure
- Root Directory: Contains the main application files like index.html, Jupyter notebooks (01_ASX_Top10_Dataframes_Historic.ipynb, etc.), and the Flask script app_solution.
- Streamlit App Directory:
   - [Main website](Streamlit-App/app.py)  
     The main root of the website is to select between the "Predict" and "Explore" pages.
   - [Predict page](Streamlit-App/predict_page.py)  
     Page for data input from users to predict vehicle prices
     
- Pickle-files Directory:
   - [Random Forest Regressor model saved](Pickle-files/random_model_steps.pkl)  
   - [Decision Tree Regressor model saved](Pickle-files/saved_steps.pkl)  
- Resources Directory:
   - [Australian Vehicle Prices.csv](Resources/Australian_Vehicle_Prices.csv)  
     Original dataset found in Kaggle. 
   - [Brands and models.csv](Resources/unique_brands.csv)  
     Table created to filter car models by brand on the Streamlit app.
  
## Data Sources and Copyright  
### Data Sources
- [Australian Vehicle Prices](https://www.kaggle.com/datasets/nelgiriyewithana/australian-vehicle-prices/code)
  This dataset contains the latest information on car prices in Australia for 2023. It covers various brands, models, types, and features of cars sold in the Australian market. The dataset includes information such as brand, year, model, car/suv, title, used/new, transmission, engine, drive type, fuel type, fuel consumption, kilometres, colour (exterior/interior), location, cylinders in the engine, body type, doors, seats, and price. The dataset has over 16,000 records of car listings from various online platforms in Australia.

### Copyright Notice
The data used on this web application is the property of the respective data providers. The information provided by this application is for informational/educational purposes only and is not intended for trading advice. We do not hold any responsibility for financial decisions made based on the information provided by our website.  

## Conclusions
- The Decision Tree Regressor model and the Random Forest Regressor model allowed us to predict vehicle prices based on a dataset with the latest information on car prices in Australia for 2023.  
- Even though the predictions showed scores of 99% and 98% for both models respectively, the mean squared error is significantly different ($338 and $2053) and might be relevant when buying cars with a low budget (below $10,000).  
- As shown on the [Data Engineering](Data-Engineering.ipynb) file, the main feature used by both models is the year of manufacture (almost 50%), followed by litres of the motor, kilometres, model and brand in that order. It is debatable as when buying a car in real life, features like "Used or New" or "Transmission" of the car tend to change the price of a car but they are not used by the models.

## References
- https://github.com/patrickloeber/ml-app-salaryprediction

