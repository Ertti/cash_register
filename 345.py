from tkinter import *

logs = Tk()
logs.title('Kases aparāts')
logs.geometry("1920x1080")

poga = PhotoImage(file="poga.png")

img = Button(logs, image = poga, borderwidth=0)

img.pack()

logs.mainloop()