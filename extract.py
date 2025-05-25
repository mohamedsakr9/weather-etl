import os
import requests
import json

def extract_weather_data():
    api_key = os.getenv('WEATHER_API_KEY')  # Keep this line
    if not api_key:
        print("❌ No API key found! Set WEATHER_API_KEY environment variable")
        return []
        
    cities = ["London", "Paris", "Tokyo"]
    data = []
    
    for city in cities:
        # Use the variable, not hardcoded key
        url = f"http://api.weatherapi.com/v1/current.json?key={api_key}&q={city}"
        response = requests.get(url)
        
        if response.status_code == 200:
            weather = response.json()
            data.append({
                'city': weather['location']['name'],
                'temperature': weather['current']['temp_c'],
                'humidity': weather['current']['humidity']
            })
            print(f"✅ {city}: {weather['current']['temp_c']}°C")
        else:
            print(f"❌ Failed for {city}")
    
    with open('weather_data.json', 'w') as f:
        json.dump(data, f)
    
    print(f"Saved {len(data)} records")
    return data

if __name__ == "__main__":
    extract_weather_data()