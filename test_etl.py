
def test_api_response():
    """Simple test - check if API returns expected data"""
    import requests
    import os
    
    api_key = os.getenv('OPENWEATHER_API_KEY', 'test')
    url = f"http://api.openweathermap.org/data/2.5/weather?q=London&appid={api_key}&units=metric"
    
    try:
        response = requests.get(url)
        if response.status_code == 200:
            print("✅ API test passed")
            return True
        else:
            print("❌ API test failed")
            return False
    except:
        print("❌ API test error")
        return False

def test_transform():
    """Simple test - check temperature categorization"""
    def categorize_temp(temp):
        return 'Hot' if temp > 20 else 'Cold'
    
    assert categorize_temp(25) == 'Hot'
    assert categorize_temp(15) == 'Cold'
    print("✅ Transform test passed")

if __name__ == "__main__":
    test_api_response()
    test_transform()