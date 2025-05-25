import os
import requests
import json

def extract_weather_data():
    api_key = os.getenv('OPENWEATHER_API_KEY')
    cities = ["London", "Paris", "Tokyo"]
    data = []
    
    for city in cities:
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
        response = requests.get(url)
        
        if response.status_code == 200:
            weather = response.json()
            data.append({
                'city': weather['name'],
                'temperature': weather['main']['temp'],
                'humidity': weather['main']['humidity']
            })
    
    with open('weather_data.json', 'w') as f:
        json.dump(data, f)
    
    return data

if __name__ == "__main__":
    data = extract_weather_data()
    print(f"Extracted {len(data)} records")