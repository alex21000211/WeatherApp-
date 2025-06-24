import customtkinter as ctk
from .main_screen import app
from ..read_json import read
from ..weather_data import *

class Info(ctk.CTkFrame):
    def __init__(self, child_master: ctk.CTk):
        ctk.CTkFrame.__init__(
            self,
            master = child_master,
            width = 925,
            height = 800,
            fg_color = "#5DA7B1"
        )
        self.grid(row = 0, column = 1)
        
        self.current_position = ctk.CTkLabel(
            master = self,
            text = 'Поточна позицiя',
            font = ('Roboto Slab', 35, 'bold'),
            text_color = '#FFFFFF'
        )
        self.current_position.place(x = 310, y = 100)
        city_name = read("config.json")["list_city"][0]
        get_info_weather(city_name, "weather_data.json", False)
        self.NAME = ctk.CTkLabel(
            self, 
            text = city_name, 
            text_color = "white",
            font = ('Roboto Slab', 25, 'bold'),
        )
        self.NAME.place(x = 420, y = 145)
        data = read("weather_data.json")
        temp = round(data["main"]["temp"])
        self.TEMP = ctk.CTkLabel(
            self, 
            text = f"{temp}°", 
            text_color = "white",
            font = ('Roboto Slab', 70, 'bold'),
        )
        self.TEMP.place(x = 420, y = 180)
        description = data["weather"][0]["description"].capitalize()
        self.DESCRIPTION = ctk.CTkLabel(
            self, 
            text = description, 
            text_color = "white",
            font = ('Roboto Slab', 25, 'bold'),
        )
        self.DESCRIPTION.place(x = 350, y = 300)
        

info = Info(child_master = app)