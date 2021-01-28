import datetime
from _ast import Lambda
from tkinter import *
import tkinter as tk
from tkinter import filedialog, Text
import os
import time
import requests
from PIL import ImageTk,Image
from PIL import Image
from tkinter import font

from Gmail import mail, SCOPES
#from AtlasSerialComm import liftOff, watch, commConfirm #have to comment this line out when i dont have arduino connected


def functions(text_entry):
    if text_entry == "1":
        print("Watch Activated")
    elif text_entry == "2":
        #commConfirm() #communcation works correctly
        print("Robot Activated")
    elif text_entry == "3":
        print("Checking Emails")
        display_mail()
    else: #if I input a city into the search bar
        city = text_entry #the intended city is the text entry
        get_weather(city) #calls on the get_weather function
#a79e59377305662d95575eec5830f454
#https://api.openweathermap.org/data/2.5/onecall?lat={lat}&lon={lon}&exclude={part}&appid={API key}
def format_response(weather):
    try:
        name = weather['name']
        desc = (weather['weather'][0]['description'])
        temp = (weather['main']['temp'])
        final_str = "City: %s \nCondtions: %s  \nTemperature: %s" % (name, desc, temp)
    except:
        final_str = 'Did you enter a valid city?'
    return final_str
def display_mail():
    mail()




def get_weather(city):
    weather_key = "a79e59377305662d95575eec5830f454"
    url = 'https://api.openweathermap.org/data/2.5/weather'
    params = {'APPID': weather_key, 'q': city, 'units': 'imperial'}
    response = requests.get(url, params=params)
    weather=response.json()
    options['text'] = format_response(weather)

root = tk.Tk()
canvas=Canvas(root, height=700, width=800)
canvas.pack()

#bgimage=Image.open("Altasbackground01.png")
bgimage = tk.PhotoImage(file="Altasbackground01.png")

bglabel=tk.Label(root, image=bgimage)
bglabel.place(x=0,y=0, relwidth=1, relheight=1)
bglabel.place(x=0,y=0, relwidth=1, relheight=1)
frame = tk.Frame(root, bg="#80c1ff", bd=5)
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')
text_entry=Entry(frame, font=40)
text_entry.place(relwidth=0.65, relheight=1)



button=Button(frame, text= "Start", fg="cyan", bg="black", font=40, command=lambda: functions(text_entry.get()))
button.place(relx=0.7, relwidth=0.3,relheight=1)

lframe=Frame(root,bg='#80c1ff', bd=10)
lframe.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')
#label = Label(lframe, text="testing", bg="white")
#label.place(relwidth=1, relheight=1)
options= Label(lframe, text="|| 1: Activate Glasses|| "
                            "2: Activate Robot|| "
                            "3: Check Emails ||"
                            "4: Check Weather|| ", bg="white", font='Calibri')
options.place(relwidth=1, relheight=1)
#print(tk.font.families())
root.mainloop()
