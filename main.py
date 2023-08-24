from tkinter import Tk, ttk
from tkinter import *

from PIL import  Image, ImageTk

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

main = Frame(window, width=368, height = 300, bg = color2 )
main.grid(row =1, column=0)

#top frame
icon = Image.open('images/convertericon.png')
icon = icon.resize((40, 40))
icon = ImageTk.PhotoImage(icon)
app_name = Label(top, image = icon, compound= LEFT, text ="Ugyen's Currency Converter", height = 5, padx=13, pady=30, anchor=CENTER, font=('Arial 16 bold'), bg=color4, fg=color5)
app_name.place(x=0,y=0)

window.mainloop()