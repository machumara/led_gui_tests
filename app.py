import tkinter as tk
import customtkinter as ctk
from switch_btn import SwitchBtn


class App:
    def __init__(self):
        self.num_of_buttons = 0
        self.switch_buttons: list[SwitchBtn] = []

        # set look
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")

        # set main window
        self.window = ctk.CTk()
        self.window.geometry("720x480")
        self.window.title("GUI Test")

        # *****INPUT*****

        # set frame for input
        self.input_frame = ctk.CTkFrame(self.window, border_width=5)

        # input title
        self.input_title = ctk.CTkLabel(self.input_frame, text="Enter num of buttons")
        self.input_title.grid(padx=10, pady=10)

        # input
        self.input = ctk.CTkEntry(self.input_frame, width=100, height=40)
        self.input.grid()

        # go button
        go_btn = ctk.CTkButton(self.input_frame, text="GO", command=self.add_buttons)
        go_btn.grid(padx=10, pady=10)

        self.input_frame.place(relx=0.5, rely=0.2, anchor=ctk.CENTER)

        # *****BUTTONS*****
        # btn frame
        self.btn_frame = ctk.CTkFrame(self.window)

    # add buttons
    def add_buttons(self):
        self.num_of_buttons = int(self.input.get())
        for i in range(self.num_of_buttons):
            # bt = ctk.CTkButton(self.btn_frame, text=str(i+1), width=25, fg_color='black')
            self.switch_buttons.append(SwitchBtn(self.btn_frame, str(i+1), 25))
            self.switch_buttons[i].grid(row=0, column=i)
        self.btn_frame.place(relx=0.5, rely=0.5, anchor=ctk.CENTER)

    # run app
    def run(self):
        self.window.mainloop()