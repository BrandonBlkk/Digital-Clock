import tkinter as tk
from time import strftime

def update_time():
    string_time = strftime('%H:%M:%S %p')
    label.config(text=string_time)
    label.after(1000, update_time)  # Update time every 1000 milliseconds (1 second)

# Create the main window
root = tk.Tk()
root.title("Digital Clock")

# Set the font and size for the clock
label_font = ('calibri', 40, 'bold')

# Create a label to display the time
label = tk.Label(root, font=label_font, background='black', foreground='white')
label.pack(anchor='center')

# Run the update_time function to initialize the clock
update_time()

# Set the size of the window and run the Tkinter main loop
root.mainloop()
