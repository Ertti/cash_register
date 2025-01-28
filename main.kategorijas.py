from tkinter import Tk, Label, Button
from PIL import Image, ImageTk
from tkinter import *


logs = Tk()
logs.title('Kases aparāts')

screen_width = logs.winfo_screenwidth()
screen_height = logs.winfo_screenheight()
logs.geometry(f"{screen_width}x{screen_height}")

gi = PhotoImage(file="gaļa.png")
ki = PhotoImage(file='Konditorija.png')
zi = PhotoImage(file='zivis.png')
si = PhotoImage(file='saldumi.png')
ai = PhotoImage(file='augļi.png')
di = PhotoImage(file='dārz.png')
sai = PhotoImage(file='saldē.png')
salēi = PhotoImage(file='saldē.png')
ri = PhotoImage(file='saldētie.png')
mi = PhotoImage(file='maiz.png')
dzēi = PhotoImage(file='dzēr.png')
alki = PhotoImage(file='alk.png')
līni = PhotoImage(file='4v.png')  
ATi = PhotoImage(file='b.png')
maki = PhotoImage(file='MAKSĀT.png')
sari = PhotoImage(file='SAR.png')

gp = Button(logs, image=gi, borderwidth=0)
gp.place(relx=0.02, rely=0.01)

kp = Button(logs, image=ki, borderwidth=0)
kp.place(relx=0.23, rely=0.01)

zp = Button(logs, image=zi, borderwidth=0)
zp.place(relx=0.44, rely=0.01)

sp = Button(logs, image=si, borderwidth=0)
sp.place(relx=0.02, rely=0.20)

ag = Button(logs, image=ai, borderwidth=0)
ag.place(relx=0.23, rely=0.20)

dg = Button(logs, image=di, borderwidth=0)
dg.place(relx=0.44, rely=0.20) 

sap = Button(logs, image=sai, borderwidth=0)
sap.place(relx=0.02, rely=0.39)

salēp = Button(logs, image=salēi, borderwidth=0)
salēp.place(relx=0.23, rely=0.39)

rp = Button(logs, image=ri, borderwidth=0)
rp.place(relx=0.44, rely=0.39)

ma = Button(logs, image=mi, borderwidth=0)
ma.place(relx=0.02, rely=0.58)

dzērp = Button(logs, image=dzēi, borderwidth=0)
dzērp.place(relx=0.23, rely=0.58)

alkp = Button(logs, image=alki, borderwidth=0)
alkp.place(relx=0.44, rely=0.58)

linl = Label(logs, image=līni)
linl.place(relx=0.5, rely=0)

ATp = Button(logs, image=ATi, borderwidth=0)
ATp.place(relx=0.6, rely=0.30)

makp = Button(logs, image=maki, borderwidth=0)
makp.place(relx=0.6, rely=0.60)

sarp = Label(logs, image=sari, borderwidth=0)
sarp.place(relx=0.67, rely=0.01)

logs.mainloop()