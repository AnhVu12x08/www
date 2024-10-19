import requests

def get_weather(api_key, city):
    base_url = "http://api.weatherapi.com/v1"  # Ensure correct base URL
    endpoint = "/current.json"  # Add specific endpoint for current weather
    params = {
        'q': city,
        'key': api_key
    }

    try:
        response = requests.get(base_url + endpoint, params=params)
        data = response.json()

        if response.status_code == 200:
            main_weather = data['current']['condition']['text']  # Adjusted data structure
            description = data['current']['condition']['text']  # Adjusted data structure
            temperature = data['current']['temp_c']  # Adjusted data structure
            humidity = data['current']['humidity']

            print(f"Weather in {city}: {main_weather} ({description})")
            print(f"Temperature: {temperature}°C")
            print(f"Humidity: {humidity}%")
        else:
            print(f"Error: {data['error']['message']}")  # Handle error message appropriately

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    api_key = 'db4796521a31439bb98164141242101'  # Replace with your actual API key
    city = input("Enter the city name: ")

    get_weather(api_key, city)
