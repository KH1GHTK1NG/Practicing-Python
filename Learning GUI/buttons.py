# button = you vlivk it, then it does stuff

from tkinter import *

count = 0

def click():
    global count
    count+=1
    count_label.config(text=count)
    

window = Tk()
button = Button(window, text='Click ME')
button.config(command=click)
button.config(font=('Ink Free', 50, 'bold'))
button.config(bg='#ff6200')
button.config(fg='yellow')
button.config(activebackground='#FF0000')
button.config(activeforeground='#fffb1f')
image = PhotoImage(file="Learning GUI\\img\\arrow_basic_e.png")
button.config(image=image)
button.config(compound='top')
#button.config(state=DISABLED) # Disable a button


count_label = Label(window, text=count)
count_label.config(font=('Monospace', 50))
count_label.pack()
button.pack()

window.mainloop()