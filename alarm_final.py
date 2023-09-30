"""
This program is to allow the user to set an alarm in military time with their own alarm sound.
Accepts .mp3 files as audio.

GitHub: @ILYLegend
"""

import tkinter as tk
import time
import pygame.mixer

from tkinter import filedialog

def update_clock():
    """
    Update clock with current time.
    """
    current_time = time.strftime('%H:%M:%S')
    clock_label.config(text=current_time)
    root.after(1000, update_clock)

def set_alarm():
    """
    Set the alarm the user wants.
    """
    alarm_time = entry_alarm.get()
    try:
        alarm_h, alarm_m, alarm_s = map(int, alarm_time.split(':'))
        current_h, current_m, current_s = map(int, time.strftime('%H:%M:%S').split(':'))

        alarm_seconds = (alarm_h - current_h) * 3600 + (alarm_m - current_m) * 60 + (alarm_s - current_s)

        if alarm_seconds <= 0:
            raise ValueError("Invalid time. Please set the alarm for a future time.")

        root.after(alarm_seconds * 1000, trigger_alarm)

        status_label.config(text = f"Alarm set for {alarm_time}")
    except Exception as e:
        status_label.config(text = str(e))

def stop_alarm():
    """
    Stop the alarm.
    """
    alarm_sound.stop()
    status_label.config(text = "Alarm stopped")

def trigger_alarm():
    """
    Have the alarm play when time is reached.
    """
    alarm_sound.play()
    status_label.config(text = "Alarm triggered!")

def change_alarm_sound():
    """
    Allow user to chnage alarm sound.
    """
    global alarm_sound
    file_path = filedialog.askopenfilename(filetypes = [("MP3 Files", "*.mp3")])
    if file_path:
        alarm_sound = pygame.mixer.Sound(file_path)
        status_label.config(text = f"Alarm sound changed")

# Application window
root = tk.Tk()
root.title("Digital Clock with Alarms")

# Clock time styling
clock_label = tk.Label(root, text = "", font = ("Arial", 48))
clock_label.pack()

# Clock 
entry_alarm = tk.Entry(root, font = ("Arial", 24))
entry_alarm.pack()

# Clock alarm set button
set_alarm_button = tk.Button(root, text="Set Alarm", command = set_alarm)
set_alarm_button.pack()

# Stop alarm button
stop_alarm_button = tk.Button(root, text = "Stop Alarm", command = stop_alarm)
stop_alarm_button.pack()

# Change alarm sound button
change_sound_button = tk.Button(root, text = "Change Sound", command = change_alarm_sound)
change_sound_button.pack()

# Display status messages
status_label = tk.Label(root, text = "", font = ("Arial", 18))
status_label.pack()

# Pygmae mixer
pygame.mixer.init()

# Default alarm sound
alarm_sound = pygame.mixer.Sound('alarm.mp3')

# Update clock and run the main loop
update_clock()
root.mainloop()