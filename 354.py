from tkinter import Tk, Label, Button, PhotoImage
from tkinter import *
logs = Tk()
gi = PhotoImage(file="gaļa.png")
gp = Button(logs, image=gi, borderwidth=0)
gp.place(x=100, y=50)

ki = PhotoImage(file='Konditorija.png')
kp = Button(logs, image=ki, borderwidth=0)
kp.place(x=370, y=50)

zi = PhotoImage(file='zivis.png')
zp = Button(logs, image=zi, borderwidth=0)
zp.place(x=640, y=50)

si = PhotoImage(file='saldumi.png')
sp = Button(logs, image=si, borderwidth=0)
sp.place(x=100, y=200)

ai = PhotoImage(file='augļi.png')
ag = Button(logs, image=ai, borderwidth=0)
ag.place(x=370, y=200)

di = PhotoImage(file='dārz.png')
dg = Button(logs, image=di, borderwidth=0)
dg.place(x=640, y=200)

sai = PhotoImage(file='saldē.png')
sap = Button(logs, image=sai, borderwidth=0)
sap.place(x=100, y=350)

salēi = PhotoImage(file='saldētie.png')
salēp = Button(logs, image=salēi, borderwidth=0)
salēp.place(x=370, y=350)

ri = PhotoImage(file='riekst.png')
rp = Button(logs, image=ri, borderwidth=0)
rp.place(x=640, y=350)

mi = PhotoImage(file='maiz.png')
ma = Button(logs, image=mi, borderwidth=0)
ma.place(x=100, y=500)

dzēi = PhotoImage(file='dzēr.png')
dzērp = Button(logs, image=dzēi, borderwidth=0)
dzērp.place(x=370, y=500)

alki = PhotoImage(file='alk.png')
alkp = Button(logs, image=alki, borderwidth=0)
alkp.place(x=640, y=500)

līni = PhotoImage(file='v4.png')
linl = Label(logs, image=līni)
linl.place(x=0, y=600)

ATi = PhotoImage(file='b.png')
ATp = Button(logs, image=ATi, borderwidth=0)
ATp.place(x=160, y=680)

maki = PhotoImage(file='MAKSĀT.png')
makp = Button(logs, image=maki, borderwidth=0)
makp.place(x=650, y=680)

logs.mainloop()
