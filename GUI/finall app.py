import tkinter as tk
import os


# Create the main window
window = tk.Tk()
window.title("ViTA")

# Define a function for each button that runs the corresponding Python file
def run_file_1():
    exec(open('Basic/actions.py').read())

def run_file_2():
    exec(open('Basic/Rock Paper Scissor.py').read())

def run_file_3():
    exec(open('Basic/Simple-Hand-Tracker.py').read())


# Create the buttons
button1 = tk.Button(text="Actions", command=run_file_1)
button1.configure(height=5, width=20)
button1.pack(pady=10, padx=10)



button2 = tk.Button(text="Rock Paper Scissor", command=run_file_2)
button2.configure(height=5, width=20)
button2.pack(pady=10, padx=10)

button3 = tk.Button(text="Simple-Hand-Tracker", command=run_file_3)
button3.configure(height=5, width=20)
button3.pack(pady=10, padx=10)

# Pack the buttons into the window
button1.pack()
button2.pack()
button3.pack()

# Run the main loop
window.mainloop()
