import customtkinter as ctk
from .side_bar import menu
from ..read_json import *
from ..weather_data import get_info_weather
from datetime import datetime, timezone, timedelta

list_city = read('config.json')["list_city"]

class CityFrame(ctk.CTkFrame):
    def __init__(self, city_name: str, master_ch: ctk.CTkScrollableFrame):
        ctk.CTkFrame.__init__(
            self,
            master = master_ch,
            width = 236,
            height = 100,
            border_width = 2,
            border_color = "#b5d3d9",
            corner_radius = 20,
            fg_color = "#096C82"
        ) 
        self.pack(pady = 20)
        get_info_weather(city_name, "weather_data.json", False)
        self.DATA = read("weather_data.json")
        temp = round(self.DATA['main']['temp'])
        temp_min = round(self.DATA['main']['temp_min'])
        temp_max = round(self.DATA['main']['temp_max'])

        timez = timedelta(seconds=self.DATA['timezone'])
        # 
        time = (datetime.now(timezone.utc) + timez).strftime("%H:%M")
        # 
        
        description = self.DATA['weather'][0]['description'].capitalize()
        # CTkLabel - создает текст
        self.TEMP = ctk.CTkLabel(
            text = f"{temp}°",
            master = self,
            font = ("Roboto Slab", 50, "bold"),
            text_color = "#FFFFFF"
        )
        self.TEMP.place(x = 230, y = 5, anchor = "ne")
        self.CITY = ctk.CTkLabel(
            master = self,
            font = ("Roboto Slab", 16, "bold"),
            text = str(self.DATA["name"]),
            text_color = '#FFFFFF'
        )
        self.CITY.place(x = 15, y = 12)
        self.TIME = ctk.CTkLabel(
            master = self,
            font = ("Roboto Slab", 12, "bold"),
            text = time,
            text_color = '#FFFFFF',
            height = 18
        )
        self.TIME.place(x = 15, y = 33)
        self.DESC = ctk.CTkLabel(
            master = self,
            font = ("Roboto Slab", 12),
            text = description,
            text_color = '#b5d3d9'
        )
        self.DESC.place(x = 15, y = 65)
        self.TEMP_MIN_MAX = ctk.CTkLabel(
            master = self,
            font = ("Roboto Slab", 12),
            text = f"макс: {temp_max}°, мін: {temp_min}°",
            text_color = '#b5d3d9'
        )
        self.TEMP_MIN_MAX.place(x = 225, y = 65, anchor = "ne")

for city_name in list_city:
    city = CityFrame(city_name, menu)