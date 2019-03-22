# 3 - Napisać program, który wczytuje dane z plików people.csv oraz planets.csv i generuje JSONA z kluczem "planets",
# który zawiera listę wszystkich planet z pliku planets.csv - dla każdej z planety przedstawiamy wszystkie jej dane oraz
# listę osób (pełne dane każdej osoby), dla których jest to planeta pochodzenia. Tak wygenerowanego JSONa należy zapisać
# do pliku star.json

import csv
import json

file_with_people = 'people.csv'
file_with_planets = 'planets.csv'


def read_csv(file_name):
    helping_dict = {}
    data = []
    with open(file_name, 'r', newline='') as file:
        reader = csv.DictReader(file)
        headers = reader.fieldnames
        for row in reader:
            for header in headers:
                helping_dict[header] = row[header]
            data.append(helping_dict.copy())
    return data


def compare(people, planets):
    for planet in planets:
        planet['residents'] = []
        for pearson in people:
            if pearson['homeworld'] == planet['url']:
                planet['residents'].append(pearson.copy())
    return planets


def write_json(json_data):
    with open('star.json', 'w') as data_file:
        json.dump(json_data, data_file, indent=4)


people_data = read_csv(file_with_people)
planets_data = read_csv(file_with_planets)

new_planets = compare(people_data, planets_data)
print(new_planets)
write_json(new_planets)
