import streamlit as st
import pickle
import numpy as np
import warnings
warnings.filterwarnings("ignore")
import datetime as dt


st.set_page_config(
    page_title="Bike Rental Prediction",
    page_icon="🚲",
    layout="centered"
)

st.markdown("""
<style>

/* ===== BACKGROUND ===== */
.stApp {
    background: linear-gradient(135deg, #020617, #030712);
    color: #e5e7eb;
    font-family: 'Segoe UI', sans-serif;
}

/* ===== TITLE ===== */
h1 {
    color: #22d3ee;
    text-align: center;
    text-shadow: 0 0 15px #22d3ee;
}

/* ===== INPUT CARDS ===== */
div[data-testid="stContainer"] {
    background-color: #020617;
    padding: 18px;
    border-radius: 16px;
    box-shadow: 0 0 25px rgba(34, 211, 238, 0.12);
}

/* ===== BUTTON ===== */
.stButton > button {
    background: linear-gradient(90deg, #22d3ee, #38bdf8);
    color: black;
    border-radius: 16px;
    font-weight: bold;
    font-size: 18px;
    padding: 12px 26px;
    border: none;
    box-shadow: 0 0 20px rgba(34,211,238,0.6);
}
.stButton > button:hover {
    transform: scale(1.07);
}

/* ===== BOMBO ANSWER BOX ===== */
div[data-testid="stSuccess"] {
    background: radial-gradient(circle, #22d3ee, #0284c7);
    color: black;
    font-size: 28px;
    font-weight: 900;
    text-align: center;
    padding: 25px;
    border-radius: 20px;
    box-shadow: 0 0 40px rgba(34,211,238,0.9);
    animation: pulse 1.5s infinite;
}

/* ===== GLOW ANIMATION ===== */
@keyframes pulse {
    0% { box-shadow: 0 0 20px #22d3ee; }
    50% { box-shadow: 0 0 50px #38bdf8; }
    100% { box-shadow: 0 0 20px #22d3ee; }
}

</style>
""", unsafe_allow_html=True)

st.title("🚲 Bike Rental Demand Prediction")
st.write("Predict total bike rentals based on weather and time conditions.")

# ---------------- LOAD MODEL & SCALER ----------------
with open("bike_rental_model.pkl", "rb") as file:
    model = pickle.load(file)

with open("scaler.pkl", "rb") as file:
    scaler = pickle.load(file)





# ---------------- DATE & TIME ----------------
date = st.date_input(
    "Select Date",
    min_value=dt.date(2011, 1, 1),
    max_value=dt.date(2030, 12, 31),
    value=dt.date(2012, 6, 15)
)
hr = st.slider("Hour", 0, 23, 12)

day = date.day
month = date.month
year = date.year
weekday = date.weekday()
dayofweek = weekday

yr = 1 if year >= 2012 else 0
mnth = month
instant = 1

# ---------------------------------- WEATHER INPUTS ------------------------------------#
temp = st.slider("Temperature (normalized)", 0.0, 1.0, 0.5)
temp_c = round(temp * 41, 1)
st.caption(f"🌡️ Approx Temperature: {temp_c} °C")


atemp = st.slider("Feels Like Temperature (normalized)", 0.0, 1.0, 0.5)
atemp_c = round(atemp * 50, 1)
st.caption(f"🌡️ Feels Like: {atemp_c} °C")


hum = st.slider("Humidity (normalized)", 0.0, 1.0, 0.5)
hum_percent = int(hum * 100)
st.caption(f"💧 Approx Humidity: {hum_percent}%")


windspeed = st.slider("Wind Speed (normalized)", 0.0, 1.0, 0.3)
wind_kmh = round(windspeed * 67, 1)
st.caption(f"🌬️ Approx Wind Speed: {wind_kmh} km/h")

#-------------------------------------------------------------------------------------------------#


# ---------------------------------------------- SEASON ------------------------------------------#
season = st.selectbox("Season", ["Spring", "Summer", "Winter", "Fall"])

season_springer = 1 if season == "Spring" else 0
season_summer = 1 if season == "Summer" else 0
season_winter = 1 if season == "Winter" else 0

#------------------------------------------------------------------------------------------------#

# ------------------------------------------- WEATHER -------------------------------------------#
weather = st.selectbox("Weather", ["Clear", "Mist", "Light Snow", "Heavy Rain"])

weathersit_Heavy_Rain = 1 if weather == "Heavy Rain" else 0
weathersit_Light_Snow = 1 if weather == "Light Snow" else 0
weathersit_Mist = 1 if weather == "Mist" else 0


# ---------------- HOLIDAY / WORKDAY ----------
holiday = st.selectbox("Holiday", ["No", "Yes"])
workingday = st.selectbox("Working Day", ["No", "Yes"])

holiday_Yes = 1 if holiday == "Yes" else 0
workingday_Working_Day_space = 1 if workingday == "Yes" else 0

# # ---------------- FIXED VALUES ----------------
# casual = 49
# registered = 151

# ---------------- INPUT ARRAY (23 FEATURES) ---
input_data = np.array([[
    instant,                     # 1
    yr,                          # 2
    mnth,                        # 3
    hr,                          # 4
    weekday,                     # 5
    temp,                        # 6
    atemp,                       # 7
    hum,                         # 8
    windspeed,                   # 9
    # casual,                      # 10
    # registered,                  # 11
    day,                         # 12
    month,                       # 13
    year,                        # 14
    dayofweek,                   # 15
    season_springer,             # 16
    season_summer,               # 17
    season_winter,               # 18
    holiday_Yes,                 # 19
    workingday_Working_Day_space,# 20
    weathersit_Heavy_Rain,       # 21
    weathersit_Light_Snow,       # 22
    weathersit_Mist              # 23
]])

# ---------------- PREDICTION -----------------
if st.button("Predict Bike Rentals"):
    input_scaled = scaler.transform(input_data)
    prediction = model.predict(input_scaled)
    st.success(f"Estimated Bike Rentals: {int(prediction[0])}")
