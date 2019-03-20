# 1 - Korzystając z swapi pobrać listę "ludzi" (nie muszą być wszystkie osoby, wystarczy kilka), dane:
#
# Imię (name)
# Wzrost
# Płeć
# Id planety "pochodzenia" Powyższe dane zapisać w pliku people.csv
# 2 - Korzystając z swapi pobrać listę planet, dane:
#
# Nazwa
# Klimat
# Populacja
# Id (można odczytać z pola 'url') Powyższe dane zapisać planets.csv

from urllib.parse import urljoin
import csv
import requests
API_URL = 'https://swapi.co/api/people'
people_url = urljoin(API_URL, 'people/')
planets_url = urljoin(API_URL, 'planets/')

file_name = 'planets.csv'
people_dict_keys = {'name': [], 'height': [], 'gender': [], 'homeworld': []}
planets_dict_keys = {'name': [], 'climate': [], 'population': [], 'url': []}


def data_download(url, dict_info):
    response = requests.get(url)
    data = response.json()
    print(data['results'])
    stuff_info = []     #list of dicts containing data on people or planets
    for result in data['results']:
        for key_name in dict_info.keys():
            dict_info[key_name] = result.get(key_name)

        stuff_info.append(dict_info.copy())
        print(stuff_info)
    return stuff_info


def save_as_csv(data, name_of_file):
    with open(name_of_file, 'w') as file:
        writer = csv.DictWriter(file, fieldnames=data[0].keys())
        writer.writeheader()
        writer.writerows(data)


# w zależności od argumentów funkcji zostaną wczytane osoby lub planety
stuff_data = data_download(planets_url, planets_dict_keys)
save_as_csv(stuff_data, file_name)
