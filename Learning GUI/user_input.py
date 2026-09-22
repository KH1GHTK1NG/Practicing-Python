# entry widget = textbox that accepts a single line of user input

from tkinter import *

def submit():
    username = entry.get()
    print(f"Hello {username}")

def delete():
    entry.delete(0,END) # Delete Line of txt

def backspace():
    entry.delete(len(entry.get())-1, END) # Delete last character

window = Tk()

Submit = Button(window, text="Submit", command=submit)
Submit.pack(side=RIGHT)

Delete = Button(window, text="Delete", command=delete)
Delete.pack(side=RIGHT)

Backspace = Button(window, text="Backspace", command=backspace)
Backspace.pack(side=RIGHT)

entry = Entry()
entry.config(font=('Ink Free', 50),
             bg='Blue',
             fg='green',
             width=10)

#entry.insert(0, "Spongebob") # To add Default text
#entry.config(state=DISABLED) # To disable 
#entry.config(show="*") # For things like passwords
entry.pack()
window.mainloop()