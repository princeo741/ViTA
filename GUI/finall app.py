import tkinter as tk
from tkinter import PhotoImage # Import the PhotoImage class from the tkinter module
import os
import time

# Create the main window
window = tk.Tk()
window.title("ViTA")
window.geometry("600x455")
window.config(bg="white")

image = PhotoImage(file="GUI/LOGO.png") # Load the image file
image = image.subsample(1, 1) # Resize the image while preserving the aspect ratio
label = tk.Label(image=image) # Create an image label widget
label.pack(side="left") # Pack the image label widget to the left of the parent widget

# Create a label widget to display the time
time_label = tk.Label(window, text="", font=("Arial", 18, "bold"))
time_label.pack()


# Create a button widget
button = tk.Button(window, image=image, bg="white")

# Update the time label every second
def update_time():
    current_time = time.strftime("%I:%M:%S %p")  # Get the current time in hh:mm:ss AM/PM format
    time_label.configure(text=current_time)
    window.after(1000, update_time)  # Run this function again after 1000 milliseconds (1 second)

update_time()  # Initialize the time label

# Define a function for each button that runs the corresponding Python file
def run_file_1():
    exec(open('Basic/actions.py').read())

def run_file_2():
    exec(open('Basic/Rock Paper Scissor.py').read())

def run_file_3():
    exec(open('Basic/Simple-Hand-Tracker.py').read())

def run_file_4():
    exec(open('Version 1.1/app.py').read())

def run_file_5():
    exec(open('User Guide/GIT ReadMe.py').read())
# Create the buttons

button1 = tk.Button(text="Actions", bg="beige", activebackground="light blue", command=run_file_1)
button1.configure(height=5, width=20)
button1.pack(pady=5, padx=5)
button1.config(font=("Playfair", 8, "bold"))
button1.config(borderwidth=2, relief="groove")

button2 = tk.Button(text="Rock Paper Scissor", bg="beige", activebackground="light blue", command=run_file_2)
button2.configure(height=5, width=20)
button2.pack(pady=5, padx=5)
button2.config(font=("Playfair", 8, "bold"))
button2.config(borderwidth=2, relief="groove")

button3 = tk.Button(text="Simple-Hand-Tracker", bg="beige", activebackground="light blue", command=run_file_3)
button3.configure(height=5, width=20)
button3.pack(pady=5, padx=5)
button3.config(font=("Playfair", 8, "bold"))
button3.config(borderwidth=2, relief="groove")

button4 = tk.Button(text="ASL", bg="beige", activebackground="light blue", command=run_file_4)
button4.configure(height=5, width=20)
button4.pack(pady=5, padx=5)
button4.config(font=("Playfair", 8, "bold"))
button4.config(borderwidth=2, relief="groove")

button5 = tk.Button(text="About Us", bg="beige", activebackground="light blue", command=run_file_5)
button5.configure(height=2, width=20)
button5.pack(pady=5, padx=5)
button5.config(font=("Playfair", 8, "bold", "italic"))
button5.config(borderwidth=2, relief="groove")


# Pack the buttons into the window
button1.pack()
button2.pack()
button3.pack()
button4.pack()
button4.pack()
# Run the main loop
window.mainloop()
