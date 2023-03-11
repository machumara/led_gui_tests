import tkinter as tk
from tkinter import colorchooser
import customtkinter as ctk


class SwitchBtn(ctk.CTkButton):
    def __init__(self, frame, name, width):
        self.name = name
        self.frame = frame
        self.on = False
        self.color = 'Black'
        self.color_pick = 'Red'
        ctk.CTkButton.__init__(self, self.frame, text=name, width=width, fg_color=self.color, command=self.clicked)
        self.bind("<Button-3>", self.pick_color)

    def pick_color(self, event):
        self.color_pick = colorchooser.askcolor()[1]
        if self.on:
            self.configure(fg_color=self.color_pick)
            self.frame.update()
        print(self.on)

    def clicked(self):
        if self.on:
            self.on = False
            self.color = "Black"
        else:
            self.on = True
            self.color = self.color_pick
        self.configure(fg_color=self.color)
        self.frame.update()
        print(self.on)

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
