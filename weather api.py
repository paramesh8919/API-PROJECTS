# Import necessary libraries

import requests

import json



# Function to fetch weather data from API

def fetch_weather_data(location):

    api_key = 'your_api_key_here'  # Replace with your actual API key

    base_url = 'https://api.openweathermap.org/data/2.5/weather'



    # Handling different location input types (city name or coordinates)

    if location.isdigit():  # Assuming input is coordinates (latitude, longitude)

        params = {'lat': location.split(',')[0], 'lon': location.split(',')[1], 'appid': api_key, 'units': 'metric'}

    else:  # Assuming input is city name

        params = {'q': location, 'appid': api_key, 'units': 'metric'}



    try:

        response = requests.get(base_url, params=params)

        data = response.json()



        if response.status_code == 200:

            return data  # Return JSON data received from API

        else:

            print(f"Error fetching data: {data['message']}")

            return None



    except requests.exceptions.RequestException as e:

        print(f"Error fetching data: {e}")

        return None



# Function to display weather data

def display_weather_data(data):

    if data:

        # Extracting relevant weather information

        temperature = data['main']['temp']

        weather_desc = data['weather'][0]['description']

        humidity = data['main']['humidity']

        wind_speed = data['wind']['speed']



        # Displaying weather information

        print(f"Temperature: {temperature} °C")

        print(f"Weather: {weather_desc}")

        print(f"Humidity: {humidity}%")

        print(f"Wind Speed: {wind_speed} m/s")

    else:

        print("No weather data available.")



# Main function to run the application

def main():

    location = input("Enter city name or coordinates (latitude,longitude): ")

    weather_data = fetch_weather_data(location)

    display_weather_data(weather_data)

if __name__ == "__main__":
    main()
