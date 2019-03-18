# ## Zadanie podstawowe
#
# Korzystając z open Open Weather Map:
# - Założyć darmowe konto w serwisie w celu pozyskania klucza: https://openweathermap.org/appid
# - Wykorzystać dostępne API do stworzenia skryptu, który wypisze podstawowe informacja pogodowe dla wybranych miast
# - Obsłużyć sytuacje, w których usługa będzie niedostępna/wystąpi błąd
#
# ## Zadanie zaawansowane
#
# Rozbudować skrypt o:
# - Możliwość wprowadzenia nazwy miasta przez użytkownika (np. parametr skryptu)
# - Obsłużyć sytuacje, w której podane miasto nie istnieje
# - Wygenerować plik html przedstawiający dane o pogodzie
# - W wygenerowanym pliku html wyświetlić również ikonę pogodową

import requests
import logging
from requests import HTTPError, ConnectionError
import webbrowser
address = 'http://api.openweathermap.org/data/2.5/weather?q={city}&APPID=c7e0f3235174d068624c60a848f56198&units=metric'


# zapytanie musi być w formie api.openweathermap.org/data/2.5/weather?q={city name}


def handle_request(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
    except ConnectionError as error:
        logging.error(f'An error during handling the request {error}')
        return None
    except HTTPError:
        logging.error('The city doesnt exist')
        return None
    except Exception as error:
        logging.error(f'An error during handling the request {error}')
    return 1


def show_results(url):
    response = requests.get(url)
    city_data = response.json()
    print("Weather in %s: \n"
          "\tTemperature: %2.2fC \n"
          "\tWeather: %s \n"
          "\tHumidity: %s \n"
          "\tPressure: %shPa" % (city_data['name'], city_data['main']['temp'],
                                 city_data['weather'][0]['main'], city_data['main']['humidity'],
                                 city_data['main']['pressure']))


def input_city(url):
    city = input('Input city name: ').replace(' ', '+')
    new_url = url.replace('{city}', city)
    return new_url


def create_html(url):
    response = requests.get(url)
    city_data = response.json()

    icon_url = "http://openweathermap.org/img/w/" + city_data['weather'][0]['icon'] + '.png'

    html_data = """<!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>Weather in {}</title>
    </head>
    <body>
    <h1>Weather in {}</h1>
    <img src={} >
    <p>Weather: {} <br>
    Temperature: {}C <br>
    Wind speed: {} <br>
    Pressure: {}hPa <br>
    Humidity: {}%</p>
    </body>
    </html>"""

    html_data = html_data.format(city_data['name'],
                                 city_data['name'], icon_url,
                                 city_data['weather'][0]['main'],
                                 city_data['main']['temp'],
                                 city_data['wind']['speed'],
                                 city_data['main']['pressure'],
                                 city_data['main']['humidity'])

    file = open("weather.html", 'w+')
    file.write(html_data)
    webbrowser.open_new_tab("weather.html")


address = input_city(address)
process_response = handle_request(address)
if process_response == 1:
    #show_results(address)
    create_html(address)
