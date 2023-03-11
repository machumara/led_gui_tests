import tkinter as tk
import customtkinter as ctk


class SwitchBtn(ctk.CTkButton):
    def __init__(self, frame, name, width):
        self.name = name
        self.frame = frame
        self.on = False
        self.color = 'Black'
        ctk.CTkButton.__init__(self, self.frame, text=name, width=width, fg_color=self.color, command=self.clicked)

    def clicked(self):
        if self.on:
            self.on = False
            self.color = "Black"
        else:
            self.on = True
            self.color = "Red"
        self.configure(fg_color=self.color)
        self.frame.update()

    # setters
    def set_state(self, state):
        self.on = state

    def set_color(self, color):
        self.color = color

    # getters
    def get_state(self):
        return self.on

    def get_color(self):
        return self.color
