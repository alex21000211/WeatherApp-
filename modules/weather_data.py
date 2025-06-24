import requests
from .write_json import write
# requests - модуль для відправки запитів
# get - отримує дані за посиланням
api_key = "f45b384d06f8d6558d2f50d57cd3220f"

def get_info_weather(city_name: str, file_name: str, forecast: bool):
    if forecast:
        url = f'https://api.openweathermap.org/data/2.5/forecast?q={city_name}&appid={api_key}&lang=ua&units=metric'
    else:
        url = f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}&lang=ua&units=metric'

    print(city_name)
    data = requests.get(url)
    if data.status_code == 200:
        write(file_name, data.json())
    else:
        print("Error - ",data.status_code)
        