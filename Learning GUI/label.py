from tkinter import *

#label = an area widget that holds text and/or an image within a window

window = Tk()
window.geometry("420x420")

photo = PhotoImage(file="Learning GUI\\img\\arrow_basic_e.png")


label = Label(window, 
              text="Sup Nigga", 
              font=('Arial', 40,'bold'), 
              fg="green", 
              bg="black",
              relief=RAISED,
              bd=10,
              padx=20,
              pady=20,
              image=photo,
              compound='bottom')
label.pack()
#label.place(x=0, y=0)

window.mainloop()