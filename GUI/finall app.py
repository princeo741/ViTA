import tkinter as tk
# Import the PhotoImage class from the tkinter module
from tkinter import PhotoImage

import os


# Create the main window
window = tk.Tk()
window.title("ViTA")
window.geometry("450x450")
window.config(bg="white")

# Load the image file
image = PhotoImage(file="GUI/LOGO.png")
# Resize the image while preserving the aspect ratio
image = image.subsample(2, 2)
# Create an image label widget
label = tk.Label(image=image)
# Pack the image label widget to the left of the parent widget
label.pack(side="left")

# Create a button widget
button = tk.Button(window, image=image, bg="white")

# Define a function for each button that runs the corresponding Python file
def run_file_1():
    exec(open('Basic/actions.py').read())

def run_file_2():
    exec(open('Basic/Rock Paper Scissor.py').read())

def run_file_3():
    exec(open('Basic/Simple-Hand-Tracker.py').read())

def run_file_4():
    exec(open('Version 1.1/app.py').read())

# Create the buttons

button1 = tk.Button(text="Actions", bg="beige", command=run_file_1)
button1.configure(height=5, width=20)
button1.pack(pady=10, padx=10)

button2 = tk.Button(text="Rock Paper Scissor", bg="beige", command=run_file_2)
button2.configure(height=5, width=20)
button2.pack(pady=10, padx=10)

button3 = tk.Button(text="Simple-Hand-Tracker", bg="beige", command=run_file_3)
button3.configure(height=5, width=20)
button3.pack(pady=10, padx=10)

button4 = tk.Button(text="ASL", bg="beige", command=run_file_4)
button4.configure(height=5, width=20)
button4.pack(pady=10, padx=10)

# Pack the buttons into the window
button1.pack()
button2.pack()
button3.pack()
button4.pack()
# Run the main loop
window.mainloop()
