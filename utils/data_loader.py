from dotenv import load_dotenv
import os
import requests

load_dotenv()

API_KEY = os.getenv("API_KEY")
API_URL = os.getenv("API_URL")
DAYS = 1
LANG = 'ru'
aqi = 'yes'

def load_data(city):
    response = requests.get(API_URL, params= {'key': API_KEY, 'q': city, 'days': DAYS, 'aqi': aqi,'lang': LANG}) 
    if response.status_code == 200:
        data = response.json()
    # Обработка данных
    else:
        print("Ошибка:", response.status_code, response.text)    

    location = data['location']
    forecast_hours = data['forecast']['forecastday'][0]['hour']
    city_name = location['name']
    current = data['current']
    hours = [h['time'][-5:] for h in forecast_hours]
    co = [h['air_quality']['co'] for h in forecast_hours]  #оксид углерода (CO), или угарный газ
    no2 = [h['air_quality']['no2'] for h in forecast_hours]   #Диоксид азота (NO2) в воздухе 
    o3 = [h['air_quality']['o3'] for h in forecast_hours]   #Озон (O3) в воздухе
    so2 = [h['air_quality']['so2'] for h in forecast_hours]   #Концентрация углекислого газа (CO2)
    pm2_5 = [h['air_quality']['pm2_5'] for h in forecast_hours]  #микроскопические частицы
    pm10 = [h['air_quality']['pm10'] for h in forecast_hours]  #крупная пыль, споры плесени, пыльца

    co_curr = current['air_quality']['co']
    no2_curr = current['air_quality']['no2']
    o3_curr = current['air_quality']['o3']  
    so2_curr = current['air_quality']['so2']  
    pm2_5_curr = current['air_quality']['pm2_5']
    pm10_curr = current['air_quality']['pm10']


    return{"location": location,
           "city_name": city_name,
           "hours": hours,
           "co": co,
           "no2": no2,
           "o3": o3,
           "so2": so2,
           "pm2_5": pm2_5,
           "pm10": pm10,
           "co_curr": co_curr,
           "no2_curr": no2_curr,
           "o3_curr": o3_curr,
           "so2_curr": so2_curr,
           "pm2_5_curr": pm2_5_curr,
           "pm10_curr": pm10_curr
           }

    print(hours, co, no2, o3, so2, pm2_5, pm10, co_curr, no2_curr, o3_curr, so2_curr, pm2_5_curr, pm10_curr)
