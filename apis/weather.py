import requests, json
import config
# Make you config.py in root
# And add like below
# open_weather_api_key = '1234567890'
# https://openweathermap.org/
open_weather_api_key = config.open_weather_api_key

# base_url variable to store url
base_url = "http://api.openweathermap.org/data/2.5/weather?"



def get_weather(city_name):
    complete_url = base_url + "appid=" + open_weather_api_key + "&q=" + city_name
    # print(complete_url)
    response = requests.get(complete_url)

    x = response.json()

    if x["cod"] != "404":

        icon = x['weather'][0]['icon']
        if icon == '01n':
            icon = '01d'
        icon_url = 'http://openweathermap.org/img/wn/{}@2x.png'.format(icon)
        y = x["main"]

        current_temperature = y["temp"] - 273.0

        current_pressure = y["pressure"]
        # icon = y['icon']
        # print(icon)
        current_humidiy = y["humidity"]

        z = x["weather"]

        weather_description = z[0]["description"]
        if weather_description == 'clear sky':
            weather = '맑음'
            icon = 'assets/Sun.png'
        elif weather_description == 'few clouds' or 'scattered clouds' or 'broken clouds':
            weather = '구름'
            icon = 'assets/Cloud.png'
        elif weather_description == 'shower rain' or 'rain':
            weather = '비'
            icon = 'assets/Rain.png'
        elif weather_description == 'thunderstorm':
            weather = '번개'
            icon = 'assets/Storm.png'
        elif weather_description == 'mist':
            weather = '안개'
            icon = 'assets/Haze.png'
        elif weather_description == 'snow':
            weather = '눈'
            icon = 'assets/Snow.png'
        return int(current_temperature), weather, icon
        # print(" Temperature (in kelvin unit) = " +
        #       str(current_temperature) +
        #       "\n atmospheric pressure (in hPa unit) = " +
        #       str(current_pressure) +
        #       "\n humidity (in percentage) = " +
        #       str(current_humidiy) +
        #       "\n description = " +
        #       str(weather_description))

    else:
        print(" City Not Found ")

if __name__ == '__main__':
    get_weather("Ulsan")