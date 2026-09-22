from tkinter import *

# Difference between Windows and Widgets:
# Widgets = GUI elements like buttons, labels, text boxes, etc.
# Windows = serves as container to hold or contain widgets. It is the main window of the application.

window = Tk()  # Create a window
window.title("My First GUI")  # Set the title of the window
window.geometry("400x300")  # Set the size of the window (width x height)
window.config(background="blue")

window.mainloop()  # Start the GUI , listen to events and wait for user interaction


#icon = PhotoImage(file="Learning GUI\\icon.png")  # Load an icon image
#window.iconphoto(True, icon)  # Set the icon of the window