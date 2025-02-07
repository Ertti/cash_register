import tkinter as tk
from PIL import Image, ImageTk
import main
from main import CartManager, ProductController

from navigation import go_to_main_kategorijas

def Saldumi_page():
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

    kon1 = resize_image('SaldaisPop.png', 0.19, 0.12)
    kon2 = resize_image('VafelesŠok.png', 0.19, 0.12)
    kon3 = resize_image('ŽelejasKonf.png', 0.19, 0.12)
    kon4 = resize_image('BārbelaŠok.png', 0.19, 0.12)
    kon5 = resize_image('PienaŠok.png', 0.19, 0.12)
    kon6 = resize_image('TumšāŠok.png', 0.19, 0.12)

    # frame for cart
    cart_frame = tk.Frame(logs, relief=tk.RIDGE, bg='#dadada')
    cart_frame.place(relx=0.7, rely=0.111)

    cart_manager = CartManager(cart_frame)

    # PRODUKTS 1

    k1 = tk.Label(logs, image=kon1)
    k1.place(relx=0.02, rely=0.01)
    Saldias_z = kon1

    cena_saldaispop_z = 0.90
    cena_text_sz = tk.Label(text=f"Cena: €{cena_saldaispop_z:.2f}", font=("Arial", 12))
    cena_text_sz.place(relx=0.135, rely=0.141)
    daudzums_sz = tk.Label(text="0", font=("Arial", 12))
    daudzums_sz.place(relx=0.068, rely=0.14)
    Saldias_z = ProductController(daudzums_sz, cart_manager, "Saldias Popkorns", cena_saldaispop_z)

    plus_Saldias = tk.Button(text="+", width=3, command=lambda: Saldias_z.update_amount(1))
    plus_Saldias.place(relx=0.09, rely=0.14)
    minus_Saldias = tk.Button(text="-", width=3, command=lambda: Saldias_z.update_amount(-1))
    minus_Saldias.place(relx=0.04, rely=0.14)

    # PRODUKTS 2

    k2 = tk.Label(logs, image=kon2)
    k2.place(relx=0.23, rely=0.01)
    vafel_š = kon2

    cena_vafel_š = 1.00
    cena_text_vaš = tk.Label(text=f"Cena: €{cena_vafel_š:.2f}", font=("Arial", 12))
    cena_text_vaš.place(relx=0.345, rely=0.141)
    daudzums_vaš = tk.Label(text="0", font=("Arial", 12))
    daudzums_vaš.place(relx=0.268, rely=0.14)
    vafel_š = ProductController(daudzums_vaš, cart_manager, "Vafeles Šokolāde", cena_vafel_š)

    plus_vš = tk.Button(text="+", width=3, command=lambda: vafel_š.update_amount(1))
    plus_vš.place(relx=0.29, rely=0.14)
    minus_vš = tk.Button(text="-", width=3, command=lambda: vafel_š.update_amount(-1))
    minus_vš.place(relx=0.24, rely=0.14)

    # PRODUKTS 3

    k3 = tk.Label(logs, image=kon3)
    k3.place(relx=0.44, rely=0.01)
    ŽelejasKonf = kon3

    cena_žel = 0.60
    cena_text_zel = tk.Label(text=f"Cena: €{ cena_žel:.2f}", font=("Arial", 12))
    cena_text_zel.place(relx=0.555, rely=0.141)
    daudzums_magm = tk.Label(text="0", font=("Arial", 12))
    daudzums_magm.place(relx=0.477, rely=0.14)
    ŽelejasKonf = ProductController(daudzums_magm, cart_manager, "Želejas Konfekete", cena_žel)

    plus_želk = tk.Button(text="+", width=3, command=lambda: ŽelejasKonf.update_amount(1))
    plus_želk.place(relx=0.5, rely=0.14)
    minus_želk = tk.Button(text="-", width=3, command=lambda: ŽelejasKonf.update_amount(-1))
    minus_želk.place(relx=0.45, rely=0.14)

    #PRODUKTS 4

    k4 = tk.Label(logs, image=kon4)
    k4.place(relx=0.02, rely=0.20)
    BārbelesŠok = kon4

    cena_BārbelesŠok  = 0.60
    cena_text_barb = tk.Label(text=f"Cena: €{cena_BārbelesŠok :.2f}", font=("Arial", 12))
    cena_text_barb.place(relx=0.135, rely=0.33)
    daudzums_barb = tk.Label(text="0", font=("Arial", 12))
    daudzums_barb.place(relx=0.068, rely=0.329)
    BārbelesŠok = ProductController(daudzums_barb, cart_manager, "Bārbeles Šokolāde", cena_BārbelesŠok )

    plus_barbš = tk.Button(text="+", width=3, command=lambda: BārbelesŠok.update_amount(1))
    plus_barbš.place(relx=0.09, rely=0.329)
    minus_barbš = tk.Button(text="-", width=3, command=lambda: BārbelesŠok.update_amount(-1))
    minus_barbš.place(relx=0.04, rely=0.329)
    
    #PRODUKTS 5

    k5 = tk.Label(logs, image=kon5)
    k5.place(relx=0.23, rely=0.20)
    Pienašok = kon5

    cena_text_pienš = 0.75
    cena_text_pienš = tk.Label(text=f"Cena: €{cena_text_pienš:.2f}", font=("Arial", 12))
    cena_text_pienš.place(relx=0.345, rely=0.33)
    daudzums_pienš = tk.Label(text="0", font=("Arial", 12))
    daudzums_pienš.place(relx=0.268, rely=0.329)
    Pienašok = ProductController(daudzums_pienš, cart_manager, "Piena Šokolāde 100g", cena_text_pienš)

    plus_peinš = tk.Button(text="+", width=3, command=lambda: Pienašok.update_amount(1))
    plus_peinš.place(relx=0.29, rely=0.329)
    minus_peinš = tk.Button(text="-", width=3, command=lambda: Pienašok.update_amount(-1))
    minus_peinš.place(relx=0.24, rely=0.329)

    #PRODUKTS 6

    k6 = tk.Label(logs, image=kon6)
    k6.place(relx=0.44, rely=0.20)
    Tšok = kon6

    cena_Tšok = 0.70
    cena_text_Tšok = tk.Label(text=f"Cena: €{cena_Tšok:.2f}", font=("Arial", 12))
    cena_text_Tšok.place(relx=0.555, rely=0.33)
    daudzums_bulp = tk.Label(text="0", font=("Arial", 12))
    daudzums_bulp.place(relx=0.477, rely=0.329)
    Tšok = ProductController(daudzums_bulp, cart_manager, "Buliona pīrādziņš", cena_Tšok)

    plus_Tšok = tk.Button(text="+", width=3, command=lambda: Tšok.update_amount(1))
    plus_Tšok.place(relx=0.5, rely=0.329)
    minus_Tšok = tk.Button(text="-", width=3, command=lambda: Tšok.update_amount(-1))
    minus_Tšok.place(relx=0.45, rely=0.329)


    cart_frame.lift()

    logs.mainloop()

if __name__== '__main__':
    Saldumi_page()