import customtkinter as ctk
from .main_screen import app

# master - параметр який відповідає за батьківський елемент (той до якого кріпиться)
# CTkScrollableFrame - створює елемент з прокруткою
class VerticalMenu(ctk.CTkScrollableFrame):
    def __init__ (self, master_ch: ctk.CTk, width_ch: int, height_ch: int, **kwargs):
        ctk.CTkScrollableFrame.__init__(
            self = self,
            master = master_ch,
            width = width_ch,
            height = height_ch,
            fg_color = "#096C82",
            **kwargs
        )
        self.grid(row=0, column=0)
        # grid - розміщює елемент за сіткою (row, column)
        # self.pack(padx=10, pady=10)
        # pack - розміщює елемент за отступами (padx, pady)
        # self.place(x=0, y=0)
        # place - розміщює елемент за координатами

menu = VerticalMenu(app, 275, 800)

# **kwargs - дозволяє приймати будь які параметри
# *args - дозволяє приймати параметри без імен