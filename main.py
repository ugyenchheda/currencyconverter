from tkinter import Tk, ttk
from tkinter import *

from PIL import  Image, ImageTk

import requests
import json

color1 = "blue"
color2 = "orange"
color3 = "black"
color4 = "white"
color5 = "#3b474d"

window = Tk()
window.geometry('368x360')
window.title("Ugyen's Currency Converter")
window.configure(bg=color4)
window.resizable(height= FALSE, width=FALSE)

#frames
top = Frame(window, width=368, height= 60, bg = color3)
top.grid(row = 0,column=0)

main = Frame(window, width=368, height = 300, bg = color4 )
main.grid(row =1, column=0)

def convert():
    url = "https://currency-converter18.p.rapidapi.com/api/v1/convert"
    currency_from = comboFrom.get()
    currency_to = comboTo.get()
    amount = value.get()

    querystring = {"from": currency_from, "to": currency_to, "amount": amount}

    headers = {
        "X-RapidAPI-Key": "970b8bb5e5mshb75460a8d5c5c60p17afb3jsnd738436ab2d3",
        "X-RapidAPI-Host": "currency-converter18.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)

    data = json.loads(response.text)
    
    if data['success']:
        converted_amount = data['result']['convertedAmount']
        formatted = "{:,.2f}".format(converted_amount)
        result["text"] = format(formatted)
    else:
        result["text"] = format(data['validationMessage'])

#top frame
icon = Image.open('images/convertericon.png')
icon = icon.resize((40, 40))
icon = ImageTk.PhotoImage(icon)
app_name = Label(top, image = icon, compound= LEFT, text ="Ugyen's Currency Converter", height = 5, padx=13, pady=30,relief="solid", anchor=CENTER, font=('Arial 16 bold'), bg=color2, fg=color4)
app_name.place(x=0,y=0)

#main frame
result = Label(main, text="",width=21, height=2, padx=4, pady=10, anchor=CENTER, relief="solid", font=('Ivy 15 bold'), bg=color4, fg=color3)
result.place(x=50,y=15)

from_label = Label(main,width=21, text ="From", height = 5, padx=0, pady=0,relief="flat", anchor=NW, font=('Ivy 12'), bg=color4, fg=color3)
from_label.place(x=50, y=100)

currency = ['EUR', 'AUD', 'USD', 'NPR', 'INR']
comboFrom = ttk.Combobox(main, width=10, justify=CENTER, font=("Ivy 12 "))
comboFrom['values'] =(currency)
comboFrom.place(x=50, y=125)

to_label = Label(main,width=21, text ="To", height = 5, padx=0, pady=0,relief="flat", anchor=NW, font=('Ivy 12'), bg=color4, fg=color3)
to_label.place(x=200, y=100)

comboTo =ttk.Combobox(main, width=10, justify=CENTER, font=("Ivy 12"))
comboTo['values'] = (currency)
comboTo.place(x=200, y=125)

value = Entry(main, width=29, justify=CENTER, font=("Ivy 12 bold"), relief="solid")
value.place(x=50, y=170)

button =Button(main, text="Convert", width=25, padx=5, height=1, bg=color2, fg=color4, font=("Ivy 12 bold"), justify=CENTER, command=convert)
button.place(x=50, y=210)
window.mainloop()