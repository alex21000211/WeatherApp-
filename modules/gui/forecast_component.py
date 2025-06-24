import customtkinter as ctk
from .forecast_frame import *
from ..weather_data import get_info_weather
from ..read_json import read
from .image import *

get_info_weather("Дніпро", "forecast.json", True)
list_weather = read("forecast.json")["list"]

class ForecastComponent(ctk.CTkFrame):
    def __init__(self, master: ctk.CTkScrollableFrame, count: int):
        ctk.CTkFrame.__init__(
            self, 
            master, 
            fg_color="#5DA7B1"
        )
        self.grid(row = 0, column = count, padx = 35)
        data = list_weather[count]
        temp = round(data['main']['temp'])
        self.TEMP = ctk.CTkLabel(
            self, 
            text = f'{temp}°',
            font = ('Inter', 30, 'bold'),
            text_color = "white",

        )
        time = data["dt_txt"]
        time = time[11:16]
        # Зрізи - потрібні щоб з рядка взяти частину за індексом
        # Приклад: "text"[1:3] -> ex
        self.TIME = ctk.CTkLabel(
            self, 
            font = ("Roboto Slab", 22, "bold"),
            text = time,
            text_color = "white"
        )
        self.IMAGE = WeatherImage(
            width = 70,
            height = 70,
            master = self,
            name_json = "forecast.json",
            count = count 
        )
        self.TIME.pack(pady = 15)
        self.IMAGE.pack(pady = 15)
        self.TEMP.pack(pady = 15)
        
for index in range(len(list_weather)):
    comp = ForecastComponent(forecast, index) 
    