from fileinput import close
import tkinter as tk 
from turtle import window_width
import webbrowser

root = tk.Tk()
root.geometry("500x500")  # Size of the window 
root.title("Phoenix")  # Adding a title

my_str = tk.StringVar()
l1 = tk.Label(root,  textvariable=my_str, width=25)
l1.grid(row=0,column=1,columnspan=5)
my_str.set("Click on the text to run a game!")

def show_lan(selected_game):
    my_str.set("Launched")
    def create_window():
        if selected_game == "Quit":
            root.quit()
        else:
            webbrowser.open(selected_game)
    create_window()

gamelist = ("Slither.io","Mope.io","Diep.io","Zombs.io", "Quit")
var = 0


for game in gamelist:
    btn = tk.Button(root, text=game, command=lambda lan=game:show_lan(lan), relief=tk.FLAT, bd=0, borderwidth=0.5)
    btn.grid(row=1,column=var)
    var += 1

root.mainloop()