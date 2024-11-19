import json
import requests
from pprint import pprint


def find_mismatched_data(url, file_name):
    response = requests.get(url)
    planets = response.json()
    with open(file_name, 'r') as file:
        file_data = json.load(file)

    mismatches = []

    for key in planets:
        if key not in file_data:
            mismatches.append({'url_data': {key: planets[key]}, 'file_data': None})
        elif planets[key] != file_data[key]:
            mismatches.append({'url_data': {key: planets[key]}, 'file_data': {key: file_data[key]}})

    for key in file_data:
        if key not in planets:
            mismatches.append({'url_data': None, 'file_data': {key: file_data[key]}})
        elif planets.get(key) != file_data[key]:
            mismatches.append({'url_data': {key: planets.get(key)}, 'file_data': {key: file_data[key]}})

    return mismatches


if __name__ == "__main__":
    url = "https://swapi.dev/api/planets/"
    file_name = "planets.json"

    pprint(find_mismatched_data(url, file_name))
