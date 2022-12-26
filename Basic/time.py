import tkinter as tk
import time

# Create the main window
window = tk.Tk()
window.title("Time")
window.geometry("200x50")
window.config(bg="white")

# Create a label widget to display the time
time_label = tk.Label(window, text="", font=("Arial", 18, "bold"))
time_label.pack()

# Update the time label every second
def update_time():
    current_time = time.strftime("%I:%M:%S %p")  # Get the current time in hh:mm:ss AM/PM format
    time_label.configure(text=current_time)
    window.after(1000, update_time)  # Run this function again after 1000 milliseconds (1 second)

update_time()  # Initialize the time label
window.mainloop()
