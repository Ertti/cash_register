from PIL import Image, ImageTk
import tkinter as tk
import main
from main import CartManager, ProductController

from navigation import go_to_main_kategorijas

def Saldētie_prod_page():
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

    k1 = resize_image('Sald. produkti/Pelmeņi 500g.png',  0.19, 0.12)
    k2 = resize_image('Sald. produkti/Pelmeņi 1kg.png',  0.19, 0.12)
    k3 = resize_image('Sald. produkti/Mīkla.png',  0.19, 0.12)
    k4 = resize_image('Sald. produkti/Dārzeņi.png',  0.19, 0.12)
    k5 = resize_image('Sald. produkti/Zirņi.png',  0.19, 0.12)
    k6 = resize_image('Sald. produkti/Peperoni pica.png',  0.19, 0.12)

    # frame for cart
    cart_frame = tk.Frame(logs, relief=tk.RIDGE, bg='#dadada')
    cart_frame.place(relx=0.7, rely=0.111)

    cart_manager = CartManager(cart_frame)

    # PRODUKTS 1

    image_label = tk.Label(logs, image=k1)
    image_label.place(relx=0.02, rely=0.01)
    Pelmeņi_500g = k1

    cena_Pelmeņi_500g = 0.80
    cena_text_p500 = tk.Label(text=f"Cena: €{cena_Pelmeņi_500g:.2f}", font=("Arial", 12))
    cena_text_p500.place(relx=0.135, rely=0.141)
    daudzums_p500 = tk.Label(text="0", font=("Arial", 12))
    daudzums_p500.place(relx=0.068, rely=0.14)
    Pelmeņi_500g = ProductController(daudzums_p500, cart_manager, "Pelmeņi 500g", cena_Pelmeņi_500g)

    plus_p500 = tk.Button(text="+", width=3, command=lambda: Pelmeņi_500g.update_amount(1))
    plus_p500.place(relx=0.09, rely=0.14)
    minus_p500 = tk.Button(text="-", width=3, command=lambda: Pelmeņi_500g.update_amount(-1))
    minus_p500.place(relx=0.04, rely=0.14)

    # PRODUKTS 2

    image_label = tk.Label(logs, image=k2)
    image_label.place(relx=0.23, rely=0.01)
    Pelmeņi_1kg = k2

    cena_Pelmeņi_1kg = 1.50
    cena_text_p1 = tk.Label(text=f"Cena: €{cena_Pelmeņi_1kg:.2f}", font=("Arial", 12))
    cena_text_p1.place(relx=0.345, rely=0.141)
    daudzums_p1 = tk.Label(text="0", font=("Arial", 12))
    daudzums_p1.place(relx=0.268, rely=0.14)
    Pelmeņi_1kg = ProductController(daudzums_p1, cart_manager, "Pelmeņi 1kg", cena_Pelmeņi_1kg)

    plus_p1 = tk.Button(text="+", width=3, command=lambda: Pelmeņi_1kg.update_amount(1))
    plus_p1.place(relx=0.29, rely=0.14)
    minus_p1 = tk.Button(text="-", width=3, command=lambda: Pelmeņi_1kg.update_amount(-1))
    minus_p1.place(relx=0.24, rely=0.14)

    # PRODUKTS 3

    image_label = tk.Label(logs, image=k3)
    image_label.place(relx=0.44, rely=0.01)
    Mīkla = k3

    cena_Mīkla = 1.90
    cena_text_Mīkla = tk.Label(text=f"Cena: €{cena_Mīkla:.2f}", font=("Arial", 12))
    cena_text_Mīkla.place(relx=0.55, rely=0.141)
    daudzums_Mīkla = tk.Label(text="0", font=("Arial", 12))
    daudzums_Mīkla.place(relx=0.477, rely=0.14)
    Mīkla = ProductController(daudzums_Mīkla, cart_manager, "Mīkla 500g", cena_Mīkla)

    plus_Mīkla = tk.Button(text="+", width=3, command=lambda: Mīkla.update_amount(1))
    plus_Mīkla.place(relx=0.5, rely=0.14)
    minus_Mīkla = tk.Button(text="-", width=3, command=lambda: Mīkla.update_amount(-1))
    minus_Mīkla.place(relx=0.45, rely=0.14)

    # PRODUKTS 4

    image_label = tk.Label(logs, image=k4)
    image_label.place(relx=0.02, rely=0.20)
    Dārzeņi = k4

    cena_Dārzeņi = 2.90
    cena_text_Dārzeņi = tk.Label(text=f"Cena: €{cena_Dārzeņi:.2f}", font=("Arial", 12))
    cena_text_Dārzeņi.place(relx=0.135, rely=0.33)
    daudzums_Dārzeņi = tk.Label(text="0", font=("Arial", 12))
    daudzums_Dārzeņi.place(relx=0.068, rely=0.329)
    Dārzeņi = ProductController(daudzums_Dārzeņi, cart_manager, "Dārzeņi 500g", cena_Dārzeņi)

    plus_Dārzeņi = tk.Button(text="+", width=3, command=lambda: Dārzeņi.update_amount(1))
    plus_Dārzeņi.place(relx=0.09, rely=0.329)
    minus_Dārzeņi = tk.Button(text="-", width=3, command=lambda: Dārzeņi.update_amount(-1))
    minus_Dārzeņi.place(relx=0.04, rely=0.329)

    # PRODUKTS 5

    image_label = tk.Label(logs, image=k5)
    image_label.place(relx=0.23, rely=0.20)
    Zirņi = k5

    cena_Zirņi = 1.80
    cena_text_Zirņi = tk.Label(text=f"Cena: €{cena_Zirņi:.2f}", font=("Arial", 12))
    cena_text_Zirņi.place(relx=0.345, rely=0.33)
    daudzums_Zirņi = tk.Label(text="0", font=("Arial", 12))
    daudzums_Zirņi.place(relx=0.268, rely=0.329)
    Zirņi = ProductController(daudzums_Zirņi, cart_manager, "Zirņi 500g", cena_Zirņi)

    plus_Zirņi = tk.Button(text="+", width=3, command=lambda: Zirņi.update_amount(1))
    plus_Zirņi.place(relx=0.29, rely=0.329)
    minus_Zirņi = tk.Button(text="-", width=3, command=lambda: Zirņi.update_amount(-1))
    minus_Zirņi.place(relx=0.24, rely=0.329)

    # PRODUKTS 6

    image_label = tk.Label(logs, image=k6)
    image_label.place(relx=0.44, rely=0.20)
    Peperoni_pica = k6

    cena_Peperoni_pica = 1.45
    cena_text_pp = tk.Label(text=f"Cena: €{cena_Peperoni_pica:.2f}", font=("Arial", 12))
    cena_text_pp.place(relx=0.555, rely=0.33)
    daudzums_pp = tk.Label(text="0", font=("Arial", 12))
    daudzums_pp.place(relx=0.477, rely=0.329)
    Peperoni_pica = ProductController(daudzums_pp, cart_manager, "Peperoni pica 250g", cena_Peperoni_pica)

    plus_pp = tk.Button(text="+", width=3, command=lambda: Peperoni_pica.update_amount(1))
    plus_pp.place(relx=0.5, rely=0.329)
    minus_pp = tk.Button(text="-", width=3, command=lambda: Peperoni_pica.update_amount(-1))
    minus_pp.place(relx=0.45, rely=0.329)
    
    cart_frame.lift()

    logs.mainloop()

if __name__== '__main__':
    Saldētie_prod_page()