import requests

class City:
    def __init__(self, name, units="metric"):
        self.name = name
        self.units = units
        self.get_data()

    def get_data(self):
        try:
            # Fetch weather data for the city
            response = requests.get(
                f"https://api.openweathermap.org/data/2.5/weather?units={self.units}&q={self.name}&appid={API_KEY}"  ## enter your API key in place of: {API_KEY} ##
            )
            response.raise_for_status()  # Raise an error for bad responses
        except requests.exceptions.RequestException as e:
            print(f"An error occurred: {e}")
            return

        self.response_json = response.json()
        self.temp = self.response_json["main"]["temp"]
        self.temp_min = self.response_json["main"]["temp_min"]
        self.temp_max = self.response_json["main"]["temp_max"]

    def temp_print(self):
        unit_symbol = "C" if self.units == "metric" else "F"
        print(f"The weather in {self.name} is {self.temp}° {unit_symbol}")
        print(f"Today's High: {self.temp_max}°{unit_symbol}")
        print(f"Today's Low: {self.temp_min}°{unit_symbol}")


# Allow the user to input a city name
city_name = input("Enter the name of the city: ")
unit_choice = input("Enter the unit system (metric for °C, imperial for °F): ").strip().lower()

# Validate unit choice
if unit_choice not in ["metric", "imperial"]:
    print("Invalid unit system. Defaulting to metric (°C).")
    unit_choice = "metric"

# Create a City instance for the user-selected city
user_city = City(city_name, units=unit_choice)
user_city.temp_print()
