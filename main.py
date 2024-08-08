from tkinter import *

BACKGROUND_COLOR = "#B1DDC6"

window= Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
window.minsize(width=800, height=526)


#importing image 
back= PhotoImage(file="C:\\Users\\mdabr\\OneDrive\\Desktop\\udemy\\word project\\images\\card_back.png")
front= PhotoImage(file="C:\\Users\\mdabr\\OneDrive\\Desktop\\udemy\\word project\\images\\card_front.png")
right = PhotoImage(file="C:\\Users\\mdabr\\OneDrive\\Desktop\\udemy\\word project\\images\\right.png")
wrong = PhotoImage(file= "C:\\Users\\mdabr\\OneDrive\\Desktop\\udemy\\word project\\images\\wrong.png")

#setting background



window.mainloop()