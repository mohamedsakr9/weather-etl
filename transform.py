import pandas as pd
import json

def transform_weather_data():
    # Load data
    with open('weather_data.json', 'r') as f:
        data = json.load(f)
    
    # Create DataFrame
    df = pd.DataFrame(data)
    
    # Add temperature category
    df['temp_category'] = df['temperature'].apply(lambda x: 'Hot' if x > 20 else 'Cold')
    
    # Simple aggregation
    avg_temp = df['temperature'].mean()
    summary = {'average_temperature': avg_temp, 'total_cities': len(df)}
    
    return df, summary

if __name__ == "__main__":
    df, summary = transform_weather_data()
    print(f"Transformed {len(df)} records")
    print(f"Average temperature: {summary['average_temperature']:.1f}°C")