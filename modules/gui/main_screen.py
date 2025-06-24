import customtkinter as ctk
from ..read_json import *

config = read('config.json')
#Створюємо клас для додатку
class App(ctk.CTk):
    def __init__(self, name: str, width: int, height: int):
        ctk.CTk.__init__(
            self = self,
            fg_color = config['color']
        )
        #Задаємо назву додатку
        self.title(string = name)

        # winfo_screenwidth, winfo_screenheight - отримують розмір екрану
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        x = int((screen_width - width) / 2)
        y = int((screen_height - height) / 2)

        #Задаєемо розмір вікна
        self.geometry(f'{width}x{height}+{x}+{y}')
        
app = App(name = config['name'], width = config['width'], height = config['height'])

