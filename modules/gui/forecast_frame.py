import customtkinter as ctk
from .main_screen import app


class FrameForecast(ctk.CTkScrollableFrame):
    def __init__(self, master: ctk.CTk):
        ctk.CTkScrollableFrame.__init__(
            self, 
            master,
            width = 800,
            height = 240,
            fg_color = "#5DA7B1",
            border_width = 5,
            border_color = "white",
            corner_radius = 20,
            orientation = "horizontal"
        )
        self.place(x = 325, y = 430)

forecast = FrameForecast(app)