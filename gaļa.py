import tkinter as tk
from PIL import Image, ImageTk
import main
from main import CartManager, ProductController

from navigation import go_to_main_kategorijas

def Gaļa_page():
    logs = tk.Tk()
    logs.title('Kases aparāts')

    logs.resizable(True, True)

    screen_width = logs.winfo_screenwidth()
    screen_height = logs.winfo_screenheight()
    logs.geometry(f"{screen_width}x{screen_height}")

    main.load_test_ui(logs, screen_width, screen_height, go_to_main_kategorijas)

    def resize_image(image_path, width_factor, height_factor):
        img = Image.open(image_path)
        new_width = int(screen_width * width_factor)
        new_height = int(screen_height * height_factor)
        img = img.resize((new_width, new_height), Image.LANCZOS)
        return ImageTk.PhotoImage(img)

    k1 = resize_image('Gaļas produkti/Vistas maltā gaļa 500g.png', 0.19, 0.12)
    k2 = resize_image('Gaļas produkti/Maltā tītara gaļa 500g.png', 0.19, 0.12)
    k3 = resize_image('Gaļas produkti/Maltā cūkgaļa 500g.png', 0.19, 0.12)
    k4 = resize_image('Gaļas produkti/Cūkgaļas karbonāde 1kg.png', 0.19, 0.12)
    k5 = resize_image('Gaļas produkti/Cūkgaļas šķiņķis 1kg.png', 0.19, 0.12)
    k6 = resize_image('Gaļas produkti/Cūkgaļas šķiņķis 500g.png', 0.19, 0.12)
    k7 = resize_image('Gaļas produkti/Vistas šķiņķis 500g.png', 0.19, 0.12)
    k8 = resize_image('Gaļas produkti/Vistas fileja 1kg.png', 0.19, 0.12)
    k9 = resize_image('Gaļas produkti/Vistas_fileja_500g.png', 0.19, 0.12)
    
    # frame for cart
    cart_frame = tk.Frame(logs, relief=tk.RIDGE, bg='#dadada')
    cart_frame.place(relx=0.7, rely=0.111)

    cart_manager = CartManager(cart_frame)

    # PRODUKTS 1

    image_label = tk.Label(logs, image=k1)
    image_label.place(relx=0.02, rely=0.01)
    Vistasmaltā = k1

    cena_Vistasmaltā = 0.25
    cena_text_Vistasmaltā = tk.Label(text=f"Cena: €{cena_Vistasmaltā:.2f}", font=("Arial", 12))
    cena_text_Vistasmaltā.place(relx=0.135, rely=0.141)
    daudzums_Vistasmaltā = tk.Label(text="0", font=("Arial", 12))
    daudzums_Vistasmaltā.place(relx=0.068, rely=0.14)
    Vistasmaltā = ProductController(daudzums_Vistasmaltā, cart_manager, "Vistas maltā gaļa 500g", cena_Vistasmaltā)

    plus_Vistasmaltā = tk.Button(text="+", width=3, command=lambda: Vistasmaltā.update_amount(1))
    plus_Vistasmaltā.place(relx=0.09, rely=0.14)
    minus_Vistasmaltā = tk.Button(text="-", width=3, command=lambda: Vistasmaltā.update_amount(-1))
    minus_Vistasmaltā.place(relx=0.04, rely=0.14)

    # PRODUKTS 2

    image_label = tk.Label(logs, image=k2)
    image_label.place(relx=0.23, rely=0.01)
    Maltātītara = k2

    cena_Maltātītara = 1.19
    cena_text_Maltātītara = tk.Label(text=f"Cena: €{cena_Maltātītara:.2f}", font=("Arial", 12))
    cena_text_Maltātītara.place(relx=0.345, rely=0.141)
    daudzums_Maltātītara = tk.Label(text="0", font=("Arial", 12))
    daudzums_Maltātītara.place(relx=0.268, rely=0.14)
    Maltātītara = ProductController(daudzums_Maltātītara, cart_manager, "Maltā tītara gaļa 500g", cena_Maltātītara)

    plus_Maltātītara = tk.Button(text="+", width=3, command=lambda: Maltātītara.update_amount(1))
    plus_Maltātītara.place(relx=0.29, rely=0.14)
    minus_Maltātītara = tk.Button(text="-", width=3, command=lambda: Maltātītara.update_amount(-1))
    minus_Maltātītara.place(relx=0.24, rely=0.14)

    # PRODUKTS 3

    image_label = tk.Label(logs, image=k3)
    image_label.place(relx=0.44, rely=0.01)
    Maltācūkgaļa = k3

    cena_Maltācūkgaļa = 0.55
    cena_text_Maltācūkgaļa = tk.Label(text=f"Cena: €{cena_Maltācūkgaļa:.2f}", font=("Arial", 12))
    cena_text_Maltācūkgaļa.place(relx=0.555, rely=0.141)
    daudzums_Maltācūkgaļa = tk.Label(text="0", font=("Arial", 12))
    daudzums_Maltācūkgaļa.place(relx=0.477, rely=0.14)
    Maltācūkgaļa = ProductController(daudzums_Maltācūkgaļa, cart_manager, "Maltā cūkgaļa 500g", cena_Maltācūkgaļa)

    plus_Maltācūkgaļa = tk.Button(text="+", width=3, command=lambda: Maltācūkgaļa.update_amount(1))
    plus_Maltācūkgaļa.place(relx=0.5, rely=0.14)
    minus_Maltācūkgaļa = tk.Button(text="-", width=3, command=lambda: Maltācūkgaļa.update_amount(-1))
    minus_Maltācūkgaļa.place(relx=0.45, rely=0.14)

    #PRODUKTS 4

    image_label = tk.Label(logs, image=k4)
    image_label.place(relx=0.02, rely=0.20)
    Cūkgaļaskarbonāde = k4

    cena_Cūkgaļaskarbonāde = 1.50
    cena_text_Cūkgaļaskarbonāde = tk.Label(text=f"Cena: €{cena_Cūkgaļaskarbonāde:.2f}", font=("Arial", 12))
    cena_text_Cūkgaļaskarbonāde.place(relx=0.135, rely=0.33)
    daudzums_Cūkgaļaskarbonāde = tk.Label(text="0", font=("Arial", 12))
    daudzums_Cūkgaļaskarbonāde.place(relx=0.068, rely=0.329)
    Cūkgaļaskarbonāde = ProductController(daudzums_Cūkgaļaskarbonāde, cart_manager, "Cūkgaļas karbonāde 1kg", cena_Cūkgaļaskarbonāde)

    plus_Cūkgaļaskarbonāde = tk.Button(text="+", width=3, command=lambda: Cūkgaļaskarbonāde.update_amount(1))
    plus_Cūkgaļaskarbonāde.place(relx=0.09, rely=0.329)
    minus_Cūkgaļaskarbonāde = tk.Button(text="-", width=3, command=lambda: Cūkgaļaskarbonāde.update_amount(-1))
    minus_Cūkgaļaskarbonāde.place(relx=0.04, rely=0.329)
    
    #PRODUKTS 5

    image_label = tk.Label(logs, image=k5)
    image_label.place(relx=0.23, rely=0.20)
    Cūkgaļasšķiņķis = k5

    cena_Cūkgaļasšķiņķis = 0.75
    cena_text_Cūkgaļasšķiņķis = tk.Label(text=f"Cena: €{cena_Cūkgaļasšķiņķis:.2f}", font=("Arial", 12))
    cena_text_Cūkgaļasšķiņķis.place(relx=0.345, rely=0.33)
    daudzums_Cūkgaļasšķiņķis = tk.Label(text="0", font=("Arial", 12))
    daudzums_Cūkgaļasšķiņķis.place(relx=0.268, rely=0.329)
    Cūkgaļasšķiņķis = ProductController(daudzums_Cūkgaļasšķiņķis, cart_manager, "Cūkgaļas šķiņķis 1kg", cena_Cūkgaļasšķiņķis)

    plus_Cūkgaļasšķiņķis = tk.Button(text="+", width=3, command=lambda: Cūkgaļasšķiņķis.update_amount(1))
    plus_Cūkgaļasšķiņķis.place(relx=0.29, rely=0.329)
    minus_Cūkgaļasšķiņķis = tk.Button(text="-", width=3, command=lambda: Cūkgaļasšķiņķis.update_amount(-1))
    minus_Cūkgaļasšķiņķis.place(relx=0.24, rely=0.329)

    #PRODUKTS 6

    image_label = tk.Label(logs, image=k6)
    image_label.place(relx=0.44, rely=0.20)
    Cūkgaļasšķiņķis05 = k6

    cena_Cūkgaļasšķiņķis05 = 1.60
    cena_text_Cūkgaļasšķiņķis05 = tk.Label(text=f"Cena: €{cena_Cūkgaļasšķiņķis05:.2f}", font=("Arial", 12))
    cena_text_Cūkgaļasšķiņķis05.place(relx=0.555, rely=0.33)
    daudzums_Cūkgaļasšķiņķis05 = tk.Label(text="0", font=("Arial", 12))
    daudzums_Cūkgaļasšķiņķis05.place(relx=0.477, rely=0.329)
    Cūkgaļasšķiņķis05 = ProductController(daudzums_Cūkgaļasšķiņķis05, cart_manager, "Cūkgaļas šķiņķis 500g", cena_Cūkgaļasšķiņķis05)

    plus_Cūkgaļasšķiņķis05 = tk.Button(text="+", width=3, command=lambda: Cūkgaļasšķiņķis05.update_amount(1))
    plus_Cūkgaļasšķiņķis05.place(relx=0.5, rely=0.329)
    minus_Cūkgaļasšķiņķis05 = tk.Button(text="-", width=3, command=lambda: Cūkgaļasšķiņķis05.update_amount(-1))
    minus_Cūkgaļasšķiņķis05.place(relx=0.45, rely=0.329)

    #PRODUKTS 7

    image_label = tk.Label(logs, image=k7)
    image_label.place(relx=0.02, rely=0.39)
    Vistasšķiņķis = k7

    cena_Vistasšķiņķis = 1.20
    cena_text_Vistasšķiņķis = tk.Label(text=f"Cena: €{cena_Vistasšķiņķis:.2f}", font=("Arial", 12))
    cena_text_Vistasšķiņķis.place(relx=0.135, rely=0.52)
    daudzums_Vistasšķiņķis = tk.Label(text="0", font=("Arial", 12))
    daudzums_Vistasšķiņķis.place(relx=0.068, rely=0.519)
    Vistasšķiņķis = ProductController(daudzums_Vistasšķiņķis, cart_manager, "Vistas šķiņķis 500g", cena_Vistasšķiņķis)

    plus_Vistasšķiņķis = tk.Button(text="+", width=3, command=lambda: Vistasšķiņķis.update_amount(1))
    plus_Vistasšķiņķis.place(relx=0.09, rely=0.519)
    minus_Vistasšķiņķis = tk.Button(text="-", width=3, command=lambda: Vistasšķiņķis.update_amount(-1))
    minus_Vistasšķiņķis.place(relx=0.04, rely=0.519)

#PRODUKTS 8

    image_label = tk.Label(logs, image=k8)
    image_label.place(relx=0.23, rely=0.39)
    Vistasfileja1 = k8

    cena_Vistasfileja1 = 1.25
    cena_text_Vistasfileja1 = tk.Label(text=f"Cena: €{cena_Vistasfileja1:.2f}", font=("Arial", 12))
    cena_text_Vistasfileja1.place(relx=0.345, rely=0.52)
    daudzums_Vistasfileja1 = tk.Label(text="0", font=("Arial", 12))
    daudzums_Vistasfileja1.place(relx=0.268, rely=0.519)
    Vistasfileja1 = ProductController(daudzums_Vistasfileja1, cart_manager, "Vistas fileja 1kg", cena_Vistasfileja1)

    plus_Vistasfileja1 = tk.Button(text="+", width=3, command=lambda: Vistasfileja1.update_amount(1))
    plus_Vistasfileja1.place(relx=0.29, rely=0.519)
    minus_Vistasfileja1 = tk.Button(text="-", width=3, command=lambda: Vistasfileja1.update_amount(-1))
    minus_Vistasfileja1.place(relx=0.24, rely=0.519)

 #PRODUKTS 9

    image_label = tk.Label(logs, image=k8)
    image_label.place(relx=0.23, rely=0.39)
    Vistas_fileja_500g = k8

    cena_Vistas_fileja_500g = 1.25
    cena_text_Vistas_fileja_500g = tk.Label(text=f"Cena: €{cena_Vistas_fileja_500g:.2f}", font=("Arial", 12))
    cena_text_Vistas_fileja_500g.place(relx=0.345, rely=0.52)
    daudzums_Vistas_fileja_500g = tk.Label(text="0", font=("Arial", 12))
    daudzums_Vistas_fileja_500g.place(relx=0.268, rely=0.519)
    Vistas_fileja_500g = ProductController(daudzums_Vistas_fileja_500g, cart_manager, "Vistas_fileja_500g", cena_Vistas_fileja_500g)

    plus_Vistas_fileja_500g = tk.Button(text="+", width=3, command=lambda: Vistas_fileja_500g.update_amount(1))
    plus_Vistas_fileja_500g.place(relx=0.29, rely=0.519)
    minus_Vistas_fileja_500g = tk.Button(text="-", width=3, command=lambda: Vistas_fileja_500g.update_amount(-1))
    minus_Vistas_fileja_500g.place(relx=0.24, rely=0.519)

    cart_frame.lift()

    logs.mainloop()

if __name__== '__main__':
    Gaļa_page()