import requests
import pandas as pd
from config import API_KEY, CITY
from datetime import datetime   
import time

from database import insert_data

# ---------- FETCH ----------
def fetch_weather():
    url = f"https://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric"
    
    response = requests.get(url)
    data = response.json()
    
    return data

# ---------- CLEAN ----------
def clean_data(data):
    cleaned = {
        "city": data["name"],
        "temperature": data["main"]["temp"],
        "feels_like": data["main"]["feels_like"],
        "humidity": data["main"]["humidity"],
        "pressure": data["main"]["pressure"],
        "weather": data["weather"][0]["description"],
        "wind_speed": data["wind"]["speed"],
        "timestamp": datetime.now()
    }
    return cleaned



# ---------- AUTOMATION LOOP ----------
while True:
    weather_data = fetch_weather()
    
    if weather_data:
        cleaned_data = clean_data(weather_data)
        insert_data(cleaned_data)
        
        df = pd.DataFrame([cleaned_data])
        print("✅ Data inserted")
        print(df)
    
    time.sleep(3600) 