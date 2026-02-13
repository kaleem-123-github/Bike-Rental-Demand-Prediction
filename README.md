# 🚲 Bike Rental Demand Prediction

A Machine Learning web application that predicts the total number of bike rentals based on weather conditions, time, and seasonal factors.

Built using:
- Python
- Scikit-learn
- Streamlit
- Random Forest Regressor

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

## 📌 Project Overview

This project predicts hourly bike rental demand using environmental and temporal features such as:

- Date
- Hour
- Temperature
- Feels-like Temperature
- Humidity
- Wind Speed
- Season
- Weather Condition
- Holiday
- Working Day

The goal is to help bike-sharing businesses estimate demand and optimize resource allocation.

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

## 🧠 Model Information

Model Used:
- Random Forest Regressor (Tuned)

Performance Metrics:

- MAE: 23.64
- RMSE: 40.02
- R² Score: 0.949

Best Parameters:
- n_estimators: 200
- max_depth: None
- min_samples_split: 2
- min_samples_leaf: 1

The model was trained on historical bike rental data.

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

## ⚠️ Model File Notice

The trained model file (`bike_rental_model.pkl`) is **not included in this repository**.

Reason:
GitHub has a file size limit of 100MB, and the trained model exceeds this limit.

If you would like access to the trained model file, please feel free to contact me and I will share it directly.

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

## 📊 Features Used

The model uses the following engineered features:

- Season (Encoded)
- Weather Condition (Encoded)
- Holiday
- Working Day
- Hour
- Normalized Temperature (0–1 scale)
- Normalized Feels-like Temperature (0–1 scale)
- Humidity (0–1 scale)
- Wind Speed (0–1 scale)
- Date-based features (Year, Month, Day)

Note:
Some weather features are normalized between 0 and 1 as per the original dataset format.

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

## 💻 Streamlit Web App

The application allows users to:

- Select a date
- Choose hour (0–23)
- Adjust weather conditions
- Modify environmental factors
- Instantly get predicted bike rentals

To run locally:

```bash
pip install -r requirements.txt
streamlit run app.py



