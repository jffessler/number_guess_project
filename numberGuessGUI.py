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
                    text="Play Number Guesser?!",
                    width=15,
                    height=2,
                    fg="black",
                    bg="white",
                    activebackground="red",
                    # command=game.play_Game 
                    ).pack()

frame1 = tk.Frame(window,bg="skyblue3", width=400,height=500)
# frame1.place(x=640, y=400)
frame1.pack(fill='both',expand='yes')
# frame2 = Frame(window,width=25,height=25)

L1 = tk.Label(frame1,text="Lower Bound").pack(side=LEFT)
E1 = tk.Entry(frame1,bd=5).pack(side=RIGHT)
# L2 = Label(frame2,text="Upper Bound").pack(side=LEFT)
# E2 = Entry(frame2,bd=5).pack(side=RIGHT)


#Close window loop
quitButton = tk.Button(window, text= "Quit", command=window.quit).pack(side=BOTTOM)
#Root of window, generate and maintain GUI window
window.geometry("1280x800")
window.mainloop()