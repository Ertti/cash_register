from tkinter import Tk, Label, Button, PhotoImage
from PIL import Image, ImageTk  

logs = Tk()
logs.geometry('1920x1080')
def load_resized_image(file_path, width, height):
    img = Image.open(file_path)  
    img_resized = img.resize((width, height), Image.ANTIALIAS) 
    return ImageTk.PhotoImage(img_resized)  

gi = load_resized_image("gaļa.png", 100, 100)  
gp = Button(logs, image=gi, borderwidth=0)
gp.place(x=100, y=50)

ki = load_resized_image('Konditorija.png', 100, 100)
kp = Button(logs, image=ki, borderwidth=0)
kp.place(x=370, y=50)

zi = load_resized_image('zivis.png', 100, 100)
zp = Button(logs, image=zi, borderwidth=0)
zp.place(x=640, y=50)

si = load_resized_image('saldumi.png', 100, 100)
sp = Button(logs, image=si, borderwidth=0)
sp.place(x=100, y=200)

ai = load_resized_image('augļi.png', 100, 100)
ag = Button(logs, image=ai, borderwidth=0)
ag.place(x=370, y=200)

di = load_resized_image('dārz.png', 100, 100)
dg = Button(logs, image=di, borderwidth=0)
dg.place(x=640, y=200)

sai = load_resized_image('saldē.png', 100, 100)
sap = Button(logs, image=sai, borderwidth=0)
sap.place(x=100, y=350)

salēi = load_resized_image('saldētie.png', 100, 100)
salēp = Button(logs, image=salēi, borderwidth=0)
salēp.place(x=370, y=350)

ri = load_resized_image('riekst.png', 100, 100)
rp = Button(logs, image=ri, borderwidth=0)
rp.place(x=640, y=350)

mi = load_resized_image('maiz.png', 100, 100)
ma = Button(logs, image=mi, borderwidth=0)
ma.place(x=100, y=500)

dzēi = load_resized_image('dzēr.png', 100, 100)
dzērp = Button(logs, image=dzēi, borderwidth=0)
dzērp.place(x=370, y=500)

alki = load_resized_image('alk.png', 100, 100)
alkp = Button(logs, image=alki, borderwidth=0)
alkp.place(x=640, y=500)

līni = PhotoImage(file='v4.png')  
linl = Label(logs, image=līni)
linl.place(x=0, y=600)

ATi = load_resized_image('b.png', 100, 100)
ATp = Button(logs, image=ATi, borderwidth=0)
ATp.place(x=160, y=680)

maki = load_resized_image('MAKSĀT.png', 100, 100)
makp = Button(logs, image=maki, borderwidth=0)
makp.place(x=650, y=680)
sari = load_resized_image('SAR.png', 100 100)
sarp = Button(logs, image=sari, borderwidth=0)
sarp.place(x=680, y=30)

logs.mainloop()
