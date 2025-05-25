from extract import extract_weather_data
from load import load_weather_data

def main():
    extract_weather_data()
    load_weather_data()
    print("Done!")

if __name__ == "__main__":
    main()