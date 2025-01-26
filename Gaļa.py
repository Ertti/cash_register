import tkinter as tk
from PIL import Image, ImageTk

logs = tk.Tk()
logs.title('Kases aparāts')
logs.geometry("1920x1080")

gaļa1 = Image.open('Gaļas produkti/Vistas_fileja_500g.png')
gaļa1 = ImageTk.PhotoImage(gaļa1)

image_label = tk.Label(logs, image=gaļa1)
image_label.place(x=25, y=25)

gaļa2 = Image.open('Gaļas produkti/Vistas fileja 1kg.png')
gaļa2 = ImageTk.PhotoImage(gaļa2)

image_label = tk.Label(logs, image=gaļa2)
image_label.place(x=350, y=25)

gaļa3 = Image.open('Gaļas produkti/Vistas šķiņķis 500g.png')
gaļa3 = ImageTk.PhotoImage(gaļa3)

image_label = tk.Label(logs, image=gaļa3)
image_label.place(x=675, y=25)

gaļa4 = Image.open('Gaļas produkti/Vistas maltā gaļa 500g.png')
gaļa4 = ImageTk.PhotoImage(gaļa4)

image_label = tk.Label(logs, image=gaļa4)
image_label.place(x=25, y=175)

gaļa5 = Image.open('Gaļas produkti/Maltā cūkgaļa 500g.png')
gaļa5 = ImageTk.PhotoImage(gaļa5)

image_label = tk.Label(logs, image=gaļa5)
image_label.place(x=350, y=175)

gaļa6 = Image.open('Gaļas produkti/Maltā tītara gaļa 500g.png')
gaļa6 = ImageTk.PhotoImage(gaļa6)

image_label = tk.Label(logs, image=gaļa6)
image_label.place(x=675, y=175)

gaļa7 = Image.open('Gaļas produkti/Cūkgaļas šķiņķis 500g.png')
gaļa7 = ImageTk.PhotoImage(gaļa7)

image_label = tk.Label(logs, image=gaļa7)
image_label.place(x=25, y=325)

gaļa8 = Image.open('Gaļas produkti/Cūkgaļas šķiņķis 1kg.png')
gaļa8 = ImageTk.PhotoImage(gaļa8)

image_label = tk.Label(logs, image=gaļa8)
image_label.place(x=350, y=325)

gaļa9 = Image.open('Gaļas produkti/Cūkgaļas karbonāde 1kg.png')
gaļa9 = ImageTk.PhotoImage(gaļa9)

image_label = tk.Label(logs, image=gaļa9)
image_label.place(x=675, y=325)

logs.mainloop()