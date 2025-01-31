import tkinter as tk
from PIL import Image, ImageTk
from tkinter import Tk, Label, Button

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

kon1 = resize_image('Konditorijas produkti/Virtulis zemeņu.png', 0.19, 0.12)
kon2 = resize_image('Konditorijas produkti/Virtulis šokolādes.png', 0.19, 0.12)
kon3 = resize_image('Konditorijas produkti/Magoņmaizīte.png', 0.19, 0.12)
kon4 = resize_image('Konditorijas produkti/Kanēļmaizīte.png', 0.19, 0.12)
kon5 = resize_image('Konditorijas produkti/Kivimaizīte.png', 0.19, 0.12)
kon6 = resize_image('Konditorijas produkti/Buliona pīrādziņš.png', 0.19, 0.12)
kon7 = resize_image('Konditorijas produkti/Pica.png', 0.19, 0.12)
kon8 = resize_image('Konditorijas produkti/Cīsiņš mīklā.png', 0.19, 0.12)
kon9 = resize_image('Konditorijas produkti/Ķiploku bagete.png', 0.19, 0.12)
līni = resize_image('Main/4v.png', 0.65, 0.002)
ATi = resize_image('Main/b.png', 0.14, 0.12)
maki = resize_image('Main/MAKSĀT.png', 0.24, 0.12)
sari = resize_image('Main/SAR.png', 0.3, 0.95)
tīr = resize_image('Main/notīr.png', 0.25, 0.08)

k1 = tk.Label(logs, image=kon1)
k1.place(relx=0.02, rely=0.01)

k2 = tk.Label(logs, image=kon2)
k2.place(relx=0.23, rely=0.01)

k3 = tk.Label(logs, image=kon3)
k3.place(relx=0.44, rely=0.01)

k4 = tk.Label(logs, image=kon4)
k4.place(relx=0.02, rely=0.20)

k5 = tk.Label(logs, image=kon5)
k5.place(relx=0.23, rely=0.20)

k6 = tk.Label(logs, image=kon6)
k6.place(relx=0.44, rely=0.20)

k7 = tk.Label(logs, image=kon7)
k7.place(relx=0.02, rely=0.39)

k8 = tk.Label(logs, image=kon8)
k8.place(relx=0.23, rely=0.39)

k9 = tk.Label(logs, image=kon9)
k9.place(relx=0.44, rely=0.39)

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