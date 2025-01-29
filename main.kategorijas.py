from tkinter import Tk, Label, Button
from PIL import Image, ImageTk
import tkinter as tk

logs = Tk()
logs.title('Kases aparāts')

logs.resizable(True, True)

screen_width = logs.winfo_screenwidth()
screen_height = logs.winfo_screenheight()
logs.geometry(f"{screen_width}x{screen_height}")

def resize_image(image_path, width_factor, height_factor):
    img = Image.open(image_path)
    new_width = int(screen_width * width_factor)
    new_height = int(screen_height * height_factor)
    img = img.resize((new_width, new_height), Image.LANCZOS)
    return ImageTk.PhotoImage(img)

gi = resize_image('gaļa.png', 0.19, 0.16)
ki = resize_image('Konditorija.png', 0.19, 0.16)
zi = resize_image('zivis.png', 0.19, 0.16)
si = resize_image('saldumi.png', 0.19, 0.16)
ai = resize_image('augļi.png', 0.19, 0.16)
di = resize_image('dārz.png', 0.19, 0.16)
sai = resize_image('saldē.png', 0.19, 0.16)
salēi = resize_image('saldē.png', 0.19, 0.16)
ri = resize_image('saldētie.png', 0.19, 0.16)
mi = resize_image('maiz.png', 0.19, 0.16)
dzēi = resize_image('dzēr.png', 0.19, 0.16)
alki = resize_image('alk.png', 0.19, 0.16)
līni = resize_image('4v.png', 0.65, 0.002)
ATi = resize_image('b.png', 0.14, 0.12)
maki = resize_image('MAKSĀT.png', 0.24, 0.12)
sari = resize_image('SAR.png', 0.3, 0.95)
tīr = resize_image('notīr.png', 0.25, 0.08)

gp = Button(logs, image=gi, borderwidth=0)
gp.place(relx=0.02, rely=0.01, )

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
linl.place(relx=0, rely=0.8)

ATp = Button(logs, image=ATi, borderwidth=0)
ATp.place(relx=0.1, rely=0.83)

makp = Button(logs, image=maki, borderwidth=0)
makp.place(relx=0.35, rely=0.83)

sarp = Label(logs, image=sari, borderwidth=0)
sarp.place(relx=0.67, rely=0.01)

notī = Button(logs, image=tīr, borderwidth=0, fg='light grey')
notī.place(relx=0.7, rely=0.86)

logs.mainloop()