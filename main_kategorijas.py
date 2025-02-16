from tkinter import Tk, Label, Button
from PIL import Image, ImageTk
import tkinter as tk
import main
from main import CartManager

from navigation import (go_to_konditorija, go_to_gaļa, go_to_zivis, go_to_augļi, go_to_saldumi, go_to_dārzeņi, go_to_saldējumi,
                        go_to_saldētie_produkti, go_to_rieksti, go_to_maize, go_to_dzērieni, go_to_alkohols)

def main_kategorijas_page():
    logs = Tk()
    logs.title('Kases aparāts')

    logs.resizable(True, True)

    screen_width = logs.winfo_screenwidth()
    screen_height = logs.winfo_screenheight()
    logs.geometry(f"{screen_width}x{screen_height}")

    main.load_test_ui(logs, screen_width, screen_height, go_to_main_kategorijas=lambda win: None , hide_go_to_main=True)

    def resize_image(image_path, width_factor, height_factor):
        img = Image.open(image_path)
        new_width = int(screen_width * width_factor)
        new_height = int(screen_height * height_factor)
        img = img.resize((new_width, new_height), Image.LANCZOS)
        return ImageTk.PhotoImage(img)

    gi = resize_image('Kategorijas/gaļa.png', 0.19, 0.16)
    ki = resize_image('Kategorijas/Konditorija.png', 0.19, 0.16)
    zi = resize_image('Kategorijas/zivis.png', 0.19, 0.16)
    si = resize_image('Kategorijas/saldumi.png', 0.19, 0.16)
    ai = resize_image('Kategorijas/augļi.png', 0.19, 0.16)
    di = resize_image('Kategorijas/dārz.png', 0.19, 0.16)
    sai = resize_image('Kategorijas/saldē.png', 0.19, 0.16)
    salēi = resize_image('Kategorijas/saldētie.png', 0.19, 0.16)
    ri = resize_image('Kategorijas/riekst.png', 0.19, 0.16)
    mi = resize_image('Kategorijas/maiz.png', 0.19, 0.16)
    dzēi = resize_image('Kategorijas/dzēr.png', 0.19, 0.16)
    alki = resize_image('Kategorijas/alk.png', 0.19, 0.16)

    cart_frame = tk.Frame(logs, relief=tk.FLAT, bg='#dadada')
    cart_frame.place(relx=0.7, rely=0.111)

    cart_manager = CartManager(cart_frame)

    gp = Button(logs, image=gi, borderwidth=0, command=lambda: go_to_gaļa(logs))
    gp.place(relx=0.02, rely=0.01)

    kp = Button(logs, image=ki, borderwidth=0, command=lambda: go_to_konditorija(logs))
    kp.place(relx=0.23, rely=0.01)

    zp = Button(logs, image=zi, borderwidth=0, command=lambda: go_to_zivis(logs))
    zp.place(relx=0.44, rely=0.01)

    sp = Button(logs, image=si, borderwidth=0, command=lambda: go_to_saldumi(logs))
    sp.place(relx=0.02, rely=0.20)

    ag = Button(logs, image=ai, borderwidth=0, command=lambda: go_to_augļi(logs))
    ag.place(relx=0.23, rely=0.20)

    dg = Button(logs, image=di, borderwidth=0, command=lambda: go_to_dārzeņi(logs))
    dg.place(relx=0.44, rely=0.20) 

    sap = Button(logs, image=sai, borderwidth=0, command=lambda: go_to_saldējumi(logs))
    sap.place(relx=0.02, rely=0.39)

    salēp = Button(logs, image=salēi, borderwidth=0, command=lambda: go_to_saldētie_produkti(logs))
    salēp.place(relx=0.23, rely=0.39)

    rp = Button(logs, image=ri, borderwidth=0, command=lambda: go_to_rieksti(logs))
    rp.place(relx=0.44, rely=0.39)

    ma = Button(logs, image=mi, borderwidth=0, command=lambda: go_to_maize(logs))
    ma.place(relx=0.02, rely=0.58)

    dzērp = Button(logs, image=dzēi, borderwidth=0, command=lambda: go_to_dzērieni(logs))
    dzērp.place(relx=0.23, rely=0.58)

    alkp = Button(logs, image=alki, borderwidth=0, command=lambda: go_to_alkohols(logs))
    alkp.place(relx=0.44, rely=0.58)

    cart_frame.lift()

    logs.mainloop()

if __name__=='__main__':
    main_kategorijas_page()