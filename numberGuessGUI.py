#GUI import and framework
from tkinter import *
import tkinter as tk
#Game import
import numberGuess as game

#Window creation
window = Tk()

#Title of Window
greeting = tk.Label(text="Welcome to Number Guesser!").pack()

# Function call button
button = tk.Button(window,
                    text="Play Number Guesser?! \n Click \n Return to Script CLI",
                    width=50,
                    height=25,
                    fg="black",
                    bg="white",
                    activebackground="red",
                    command=game.play_Game,
                    # command = window.quit
                    ).pack()

frame1 = tk.Frame(window,bg="skyblue3", width=300,height=200)
# frame1.place(x=640, y=400)
frame1.pack(fill='both',expand='yes')
L1 = tk.Label(frame1,text="Lower Bound").pack()
E1 = tk.Entry(frame1,bd=5).pack()

# frame2 = Frame(window,width=25,height=25)
# L2 = Label(frame2,text="Upper Bound").pack(side=LEFT)
# E2 = Entry(frame2,bd=5).pack(side=RIGHT)


#Close window loop
quitButton = tk.Button(window, text= "Quit", command=window.quit).pack(side=BOTTOM)
#Root of window, generate and maintain GUI window
window.geometry("1280x800")
window.mainloop()