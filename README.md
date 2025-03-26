# API_JSON_user_choice_weather_program
Simple Weather Data Fetcher using OpenWeatherMap API and JSON allowing user to input location.

This Python program fetches and displays the current weather for a user-specified city using the OpenWeatherMap API. It allows the user to choose between metric (°C) and imperial (°F) units for temperature display. The program handles API responses, validates user input, and prints the temperature, daily high, and low values in the selected unit system.

##  This code demonstrates object-oriented programming principles by encapsulating city-specific weather data and behavior within the City class. ##

The program retrieves weather data from the OpenWeatherMap API and presents it in a user-friendly format. 

Users can input different location parameters to access weather details, including:
- City name
- Latitude and Longitude (geographical coordinates to retrieve location-specific weather details)


# To use this program, sign up for a free API key at OpenWeatherMap at https://home.openweathermap.org/users/sign_up.
Once you have the API key, it can be used to request weather data via the OpenWeatherMap API endpoints.
Example API Request Format: https://pro.openweathermap.org/data/2.5/forecast/climate?lat={lat}&lon={lon}&appid={API_KEY}

The program will use the requests library to make the API call and the json library to parse the JSON response.

# The provided code is a program that models weather data for different cities using a City class. 
- The code includes functionality to print temperature information for two cities: London and Malaga. 
- It uses formatted strings (f-strings) to display the data in a user-friendly format.
- The City class has an __init__ method that initializes the city object with a name, latitude, longitude, and units (defaulting to "metric").
- It also highlights the use of f-strings for clean and readable output formatting.
