from tkinter import Tk, Label, Button
from PIL import Image, ImageTk
from tkinter import *


logs = Tk()
logs.title('Kases aparāts')
logs.geometry("1920x1080")


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
gp.place(x=25, y=25)

kp = Button(logs, image=ki, borderwidth=0)
kp.place(x=350, y=25)

zp = Button(logs, image=zi, borderwidth=0)
zp.place(x=675, y=25)

sp = Button(logs, image=si, borderwidth=0)
sp.place(x=25, y=195)

ag = Button(logs, image=ai, borderwidth=0)
ag.place(x=350, y=195)

dg = Button(logs, image=di, borderwidth=0)
dg.place(x=675, y=195) 

sap = Button(logs, image=sai, borderwidth=0)
sap.place(x=25, y=365)

salēp = Button(logs, image=salēi, borderwidth=0)
salēp.place(x=350, y=365)

rp = Button(logs, image=ri, borderwidth=0)
rp.place(x=675, y=365)

ma = Button(logs, image=mi, borderwidth=0)
ma.place(x=25, y=545)

dzērp = Button(logs, image=dzēi, borderwidth=0)
dzērp.place(x=350, y=545)

alkp = Button(logs, image=alki, borderwidth=0)
alkp.place(x=675, y=545)

linl = Label(logs, image=līni)
linl.place(x=0, y=775)

ATp = Button(logs, image=ATi, borderwidth=0)
ATp.place(x=160, y=850)

makp = Button(logs, image=maki, borderwidth=0)
makp.place(x=530, y=850)

sarp = Label(logs, image=sari, borderwidth=0)
sarp.place(x=1080, y=10)

logs.mainloop()
