import time
import tkinter as tk
import multiprocessing
from tkinter import ttk, messagebox
from threading import *
from src.gui.style._style import STYLE

# Creating a CountDown Class
class CountDown(STYLE):
    def __init__(self, root):
        super().__init__()
        # Create frame
        self.window = root
        self.pause = False  
        
        self.clockWindow = tk.Frame(self.window, background="blue")
        self.clockWindow.grid(row=0, column=0)
        
        self.button_frame = tk.Frame(self.window)
        self.button_frame.grid(row=1, column=0, pady=self.Option_Frame_pady)
        self.Option_Frame_Add_Style(self.button_frame)
        
        # Set default time to be 20 mins
        m = 19*60 
        s = 59       
        self.time_left = m + s
        
        ### Declare variables
        self.minuteString = tk.StringVar()
        self.secondString = tk.StringVar()

        ### Set strings to default value
        self.minuteString.set("20")
        self.secondString.set("00")

        ### Get user input
        minuteTextbox = tk.Label(self.clockWindow, width=3, font=("Calibri", 20, ""), textvariable=self.minuteString)
        secondTextbox = tk.Label(self.clockWindow, width=3, font=("Calibri", 20, ""), textvariable=self.secondString)

        ### Center textboxes
        minuteTextbox.grid(row=0, column=0)
        secondTextbox.grid(row=0, column=1)

        # Begin button
        self.begin_button = tk.Button(self.button_frame, text='Begin', command=self.reset_time)
        self.begin_button.grid(row=0, column=0, padx=self.Option_Button_padx, pady=self.Option_Button_pady)
        self.Option_Button_Add_Style(self.begin_button)
        
        # Pause Button
        self.pause_button = tk.Button(self.button_frame, text="Pause", command=self.pause_time)
        self.pause_button.grid(row=0, column=1, padx=self.Option_Button_padx, pady=self.Option_Button_pady)
        self.Option_Button_Add_Style(self.pause_button)
        
    def reset_time(self, m=19*60, s=59):
        self.pause = False
        self.time_left = m + s
        while self.time_left > 0:
            mins, secs = divmod(self.time_left, 60)
            self.minuteString.set("{0:2d}".format(mins))
            self.secondString.set("{0:2d}".format(secs))
            self.clockWindow.update()
            time.sleep(1)
            self.time_left = self.time_left - 1
            if self.time_left < m+s:
                self.begin_button['text'] = "Reset"
            if self.time_left <= 0:
                messagebox.showinfo('WARNING','TIME IS UP!!!')
            # if the pause button is pressed, the while loop will break
            if self.pause == True:
                break
            
    # Creating a thread to run the show_time function
    def threading(self):
        # Killing a thread through "daemon=True" isn't a good idea
        self.x = Thread(target=self.start_time, daemon=True)
        self.x.start()

    def pause_time(self):
        if self.pause == True:
            self.pause = False    
            self.threading()
            self.pause_button['text'] = "Pause"
        else:
            self.pause = True
            mins, secs = divmod(self.time_left, 60)
            self.minuteString.set("{0:2d}".format(mins))
            self.secondString.set("{0:2d}".format(secs))
            self.clockWindow.update()
            self.pause_button['text'] = "Resume"

    def start_time(self):
        self.pause = False
        while self.time_left > 0:
            mins, secs = divmod(self.time_left, 60)
            self.minuteString.set("{0:2d}".format(mins))
            self.secondString.set("{0:2d}".format(secs))
            self.clockWindow.update()
            # sleep function: for 1 second
            time.sleep(1)
            self.time_left = self.time_left - 1
            if self.time_left <= 0:
                messagebox.showinfo('WARNING','TIME IS UP!!!')
                # Clearing the 'self.button_frame' frame
                # self.Clear_Screen()
            # if the pause button is pressed,
            # the while loop will break
            if self.pause == True:
                break

