import json
from transform import transform_weather_data

def load_weather_data():
    df, summary = transform_weather_data()
    
    # Save CSV
    df.to_csv('weather_output.csv', index=False)
    
    # Save summary
    with open('weather_summary.json', 'w') as f:
        json.dump(summary, f)
    
    print(f"Saved {len(df)} records to weather_output.csv")
    return len(df)

if __name__ == "__main__":
    load_weather_data()