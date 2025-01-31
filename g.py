from tkinter import Tk, Label, Button
from PIL import Image, ImageTk
import tkinter as tk
logs = tk.Tk()
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

gaļa1 = resize_image('Vistas_fileja_500g.png',  0.19, 0.12)
gaļa2 = resize_image('Vistas fileja 1kg.png',  0.19, 0.12)
gaļa3 = resize_image('Vistas šķiņķis 500g.png',  0.19, 0.12)
gaļa4 = resize_image('Vistas maltā gaļa 500g.png',  0.19, 0.12)
gaļa5 = resize_image('Maltā cūkgaļa 500g.png',  0.19, 0.12)
gaļa6 = resize_image('Maltā tītara gaļa 500g.png',  0.19, 0.12)
gaļa7 = resize_image('Cūkgaļas šķiņķis 500g.png',  0.19, 0.12)
gaļa8 = resize_image('Cūkgaļas šķiņķis 1kg.png',  0.19, 0.12)
gaļa9 = resize_image('Cūkgaļas karbonāde 1kg.png', 0.19, 0.12)
līni = resize_image('4v.png', 0.65, 0.002)
ATi = resize_image('b.png', 0.14, 0.12)
maki = resize_image('MAKSĀT.png', 0.24, 0.12)
sari = resize_image('SAR.png', 0.3, 0.95)
tīr = resize_image('notīr.png', 0.25, 0.08)
image_label = tk.Label(logs, image=gaļa1)
image_label.place(relx=0.02, rely=0.01)

image_label = tk.Label(logs, image=gaļa2)
image_label.place(relx=0.23, rely=0.01)

image_label = tk.Label(logs, image=gaļa3)
image_label.place(relx=0.44, rely=0.01)

image_label = tk.Label(logs, image=gaļa4)
image_label.place(relx=0.02, rely=0.20)

image_label = tk.Label(logs, image=gaļa5)
image_label.place(relx=0.23, rely=0.20)

image_label = tk.Label(logs, image=gaļa6)
image_label.place(relx=0.44, rely=0.20)

image_label = tk.Label(logs, image=gaļa7)
image_label.place(relx=0.02, rely=0.39)

image_label = tk.Label(logs, image=gaļa8)
image_label.place(relx=0.23, rely=0.39)

image_label = tk.Label(logs, image=gaļa9)
image_label.place(relx=0.44, rely=0.39)

linl = Label(logs, image=līni)
linl.place(relx=0, rely=0.8)

ATp = Button(logs, image=ATi, borderwidth=0)
ATp.place(relx=0.1, rely=0.83)

makp = Button(logs, image=maki, borderwidth=0)
makp.place(relx=0.35, rely=0.83)

sarp = Label(logs, image=sari, borderwidth=0)
sarp.place(relx=0.67, rely=0.01)

notī = Button(logs, image=tīr, borderwidth=0, bg='#dadada')
notī.place(relx=0.7, rely=0.86)

logs.mainloop()