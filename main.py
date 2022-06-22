from fileinput import close
import tkinter as tk
from turtle import window_width
import webbrowser

my_w = tk.Tk()
my_w.geometry("500x500")  # Size of the window 
my_w.title("Phoenix")  # Adding a title

my_str = tk.StringVar()
l1 = tk.Label(my_w,  textvariable=my_str, width=10 )
l1.grid(row=0,column=1,columnspan=5) 

def show_lan(selected_game):
    my_str.set("Launched")
    def create_window():
        if selected_game == "Quit":
            my_w.quit()
        else:
            webbrowser.open(selected_game)
    create_window()

gamelist = ("Slither.io","Mope.io","Diep.io","Zombs.io", "Quit")
var = 0


for game in gamelist:
    btn = tk.Button(my_w, text=game, command=lambda lan=game:show_lan(lan))
    btn.grid(row=1,column=var)
    var += 1

my_w.mainloop()