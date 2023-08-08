#GUI import and framework
from tkinter import *
import tkinter as tk
#Game import
import numberGuess as game

#Window creation
window = tk.Tk()

#Title of Window
greeting = tk.Label(text="Welcome to Number Guesser!")
greeting.pack()
# label = tk.Label(text="Hello, Tkinter",
#                   fg="white",
#                   bg="black",
#                   width=10,
#                   height=10)
# label.pack()
button = tk.Button(text="Play Number Guesser?!",
                    width=25,
                    height=5,
                    fg="black",
                    bg="blue",
                    activebackground="red",
                    command=game.play_Game
)
button.pack()

#Root of window, generate and maintain GUI window
window.geometry("1280x800")
window.mainloop()