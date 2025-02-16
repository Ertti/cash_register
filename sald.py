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

    k1 = resize_image('Saldumu produkti/SaldaisPop.png', 0.19, 0.12)
    k2 = resize_image('Saldumu produkti/VafelesŠok.png', 0.19, 0.12)
    k3 = resize_image('Saldumu produkti/ŽelejasKonf.png', 0.19, 0.12)
    k4 = resize_image('Saldumu produkti/BārbelaŠok.png', 0.19, 0.12)
    k5 = resize_image('Saldumu produkti/PienaŠok.png', 0.19, 0.12)
    k6 = resize_image('Saldumu produkti/TumšāŠok.png', 0.19, 0.12)

    # frame for cart
    cart_frame = tk.Frame(logs, relief=tk.RIDGE, bg='#dadada')
    cart_frame.place(relx=0.7, rely=0.111)

    cart_manager = CartManager(cart_frame)

    # PRODUKTS 1

    image_label = tk.Label(logs, image=k1)
    image_label.place(relx=0.02, rely=0.01)
    Saldias_Popkorns = k1

    cena_Saldias_Popkorns = 1.50
    cena_text_sz = tk.Label(text=f"Cena: €{cena_Saldias_Popkorns:.2f}", font=("Arial", 12))
    cena_text_sz.place(relx=0.135, rely=0.141)
    daudzums_sz = tk.Label(text="0", font=("Arial", 12))
    daudzums_sz.place(relx=0.068, rely=0.14)
    Saldias_Popkorns = ProductController(daudzums_sz, cart_manager, "Saldias Popkorns", cena_Saldias_Popkorns)

    plus_sz = tk.Button(text="+", width=3, command=lambda: Saldias_Popkorns.update_amount(1))
    plus_sz.place(relx=0.09, rely=0.14)
    minus_sz = tk.Button(text="-", width=3, command=lambda: Saldias_Popkorns.update_amount(-1))
    minus_sz.place(relx=0.04, rely=0.14)

    # PRODUKTS 2

    image_label = tk.Label(logs, image=k2)
    image_label.place(relx=0.23, rely=0.01)
    Vafeles_Šokolādes = k2

    cena_Vafeles_Šokolādes = 1.00
    cena_text_vaš = tk.Label(text=f"Cena: €{cena_Vafeles_Šokolādes:.2f}", font=("Arial", 12))
    cena_text_vaš.place(relx=0.345, rely=0.141)
    daudzums_vaš = tk.Label(text="0", font=("Arial", 12))
    daudzums_vaš.place(relx=0.268, rely=0.14)
    Vafeles_Šokolādes = ProductController(daudzums_vaš, cart_manager, "Vafeles Šokolādes", cena_Vafeles_Šokolādes)

    plus_vaš = tk.Button(text="+", width=3, command=lambda: Vafeles_Šokolādes.update_amount(1))
    plus_vaš.place(relx=0.29, rely=0.14)
    minus_vaš = tk.Button(text="-", width=3, command=lambda: Vafeles_Šokolādes.update_amount(-1))
    minus_vaš.place(relx=0.24, rely=0.14)

    # PRODUKTS 3

    image_label = tk.Label(logs, image=k3)
    image_label.place(relx=0.44, rely=0.01)
    ŽelejasKonf = k3

    cena_ŽelejasKonf = 0.60
    cena_text_zel = tk.Label(text=f"Cena: €{ cena_ŽelejasKonf:.2f}", font=("Arial", 12))
    cena_text_zel.place(relx=0.555, rely=0.141)
    daudzums_zel = tk.Label(text="0", font=("Arial", 12))
    daudzums_zel.place(relx=0.477, rely=0.14)
    ŽelejasKonf = ProductController(daudzums_zel, cart_manager, "Želejas Konfekete", cena_ŽelejasKonf)

    plus_zel = tk.Button(text="+", width=3, command=lambda: ŽelejasKonf.update_amount(1))
    plus_zel.place(relx=0.5, rely=0.14)
    minus_zel = tk.Button(text="-", width=3, command=lambda: ŽelejasKonf.update_amount(-1))
    minus_zel.place(relx=0.45, rely=0.14)

    #PRODUKTS 4

    image_label = tk.Label(logs, image=k4)
    image_label.place(relx=0.02, rely=0.20)
    Bārbeles_kon = k4

    cena_Bārbeles_kon  = 0.60
    cena_text_barb = tk.Label(text=f"Cena: €{cena_Bārbeles_kon :.2f}", font=("Arial", 12))
    cena_text_barb.place(relx=0.135, rely=0.33)
    daudzums_barb = tk.Label(text="0", font=("Arial", 12))
    daudzums_barb.place(relx=0.068, rely=0.329)
    Bārbeles_kon = ProductController(daudzums_barb, cart_manager, "Bārbeles konfektes", cena_Bārbeles_kon )

    plus_barb = tk.Button(text="+", width=3, command=lambda: Bārbeles_kon.update_amount(1))
    plus_barb.place(relx=0.09, rely=0.329)
    minus_barb = tk.Button(text="-", width=3, command=lambda: Bārbeles_kon.update_amount(-1))
    minus_barb.place(relx=0.04, rely=0.329)
    
    #PRODUKTS 5

    image_label = tk.Label(logs, image=k5)
    image_label.place(relx=0.23, rely=0.20)
    Pienašok = k5

    cena_Pienašok = 0.75
    cena_text_pienš = tk.Label(text=f"Cena: €{cena_Pienašok:.2f}", font=("Arial", 12))
    cena_text_pienš.place(relx=0.345, rely=0.33)
    daudzums_pienš = tk.Label(text="0", font=("Arial", 12))
    daudzums_pienš.place(relx=0.268, rely=0.329)
    Pienašok = ProductController(daudzums_pienš, cart_manager, "Piena Šokolāde 100g", cena_Pienašok)

    plus_pienš = tk.Button(text="+", width=3, command=lambda: Pienašok.update_amount(1))
    plus_pienš.place(relx=0.29, rely=0.329)
    minus_pienš = tk.Button(text="-", width=3, command=lambda: Pienašok.update_amount(-1))
    minus_pienš.place(relx=0.24, rely=0.329)

    #PRODUKTS 6

    image_label = tk.Label(logs, image=k6)
    image_label.place(relx=0.44, rely=0.20)
    Tumšā_šokolāde = k6

    cena_Tumšā_šokolāde = 0.70
    cena_text_Tšok = tk.Label(text=f"Cena: €{cena_Tumšā_šokolāde:.2f}", font=("Arial", 12))
    cena_text_Tšok.place(relx=0.555, rely=0.33)
    daudzums_bulp = tk.Label(text="0", font=("Arial", 12))
    daudzums_bulp.place(relx=0.477, rely=0.329)
    Tumšā_šokolāde = ProductController(daudzums_bulp, cart_manager, "Tumšā šokolāde", cena_Tumšā_šokolāde)

    plus_Tšok = tk.Button(text="+", width=3, command=lambda: Tumšā_šokolāde.update_amount(1))
    plus_Tšok.place(relx=0.5, rely=0.329)
    minus_Tšok = tk.Button(text="-", width=3, command=lambda: Tumšā_šokolāde.update_amount(-1))
    minus_Tšok.place(relx=0.45, rely=0.329)


    cart_frame.lift()

    logs.mainloop()

if __name__== '__main__':
    Saldumi_page()