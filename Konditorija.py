import tkinter as tk
from PIL import Image, ImageTk
import main
from main import CartManager, ProductController

from navigation import go_to_main_kategorijas

def konditorija_page():
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

    kon1 = resize_image('Konditorijas produkti/Virtulis zemeņu.png', 0.19, 0.12)
    kon2 = resize_image('Konditorijas produkti/Virtulis šokolādes.png', 0.19, 0.12)
    kon3 = resize_image('Konditorijas produkti/Magoņmaizīte.png', 0.19, 0.12)
    kon4 = resize_image('Konditorijas produkti/Kanēļmaizīte.png', 0.19, 0.12)
    kon5 = resize_image('Konditorijas produkti/Kivimaizīte.png', 0.19, 0.12)
    kon6 = resize_image('Konditorijas produkti/Buliona pīrādziņš.png', 0.19, 0.12)
    kon7 = resize_image('Konditorijas produkti/Pica.png', 0.19, 0.12)
    kon8 = resize_image('Konditorijas produkti/Cīsiņš mīklā.png', 0.19, 0.12)
    kon9 = resize_image('Konditorijas produkti/Ķiploku bagete.png', 0.19, 0.12)

    # frame for cart
    cart_frame = tk.Frame(logs, relief=tk.RIDGE, bg='#dadada')
    cart_frame.place(relx=0.7, rely=0.111)

    cart_manager = CartManager(cart_frame)

    # PRODUKTS 1

    k1 = tk.Label(logs, image=kon1)
    k1.place(relx=0.02, rely=0.01)
    virtulis_z = kon1

    cena_virtulis_z = 0.55
    cena_text_vz = tk.Label(text=f"Cena: €{cena_virtulis_z:.2f}", font=("Arial", 12))
    cena_text_vz.place(relx=0.135, rely=0.141)
    daudzums_vz = tk.Label(text="0", font=("Arial", 12))
    daudzums_vz.place(relx=0.068, rely=0.14)
    virtulis_z = ProductController(daudzums_vz, cart_manager, "Virtulis zemeņu", cena_virtulis_z)

    plus_vz = tk.Button(text="+", width=3, command=lambda: virtulis_z.update_amount(1))
    plus_vz.place(relx=0.09, rely=0.14)
    minus_vz = tk.Button(text="-", width=3, command=lambda: virtulis_z.update_amount(-1))
    minus_vz.place(relx=0.04, rely=0.14)

    # PRODUKTS 2

    k2 = tk.Label(logs, image=kon2)
    k2.place(relx=0.23, rely=0.01)
    virtulis_š = kon2

    cena_virtulis_š = 0.55
    cena_text_vš = tk.Label(text=f"Cena: €{cena_virtulis_š:.2f}", font=("Arial", 12))
    cena_text_vš.place(relx=0.345, rely=0.141)
    daudzums_vš = tk.Label(text="0", font=("Arial", 12))
    daudzums_vš.place(relx=0.268, rely=0.14)
    virtulis_š = ProductController(daudzums_vš, cart_manager, "Virtulis šokolādes", cena_virtulis_š)

    plus_vš = tk.Button(text="+", width=3, command=lambda: virtulis_š.update_amount(1))
    plus_vš.place(relx=0.29, rely=0.14)
    minus_vš = tk.Button(text="-", width=3, command=lambda: virtulis_š.update_amount(-1))
    minus_vš.place(relx=0.24, rely=0.14)

    # PRODUKTS 3

    k3 = tk.Label(logs, image=kon3)
    k3.place(relx=0.44, rely=0.01)
    magoņmaizīte = kon3

    cena_magoņmaizīte = 0.60
    cena_text_magm = tk.Label(text=f"Cena: €{cena_magoņmaizīte:.2f}", font=("Arial", 12))
    cena_text_magm.place(relx=0.555, rely=0.141)
    daudzums_magm = tk.Label(text="0", font=("Arial", 12))
    daudzums_magm.place(relx=0.477, rely=0.14)
    magoņmaizīte = ProductController(daudzums_magm, cart_manager, "Magoņmaizīte", cena_magoņmaizīte)

    plus_magm = tk.Button(text="+", width=3, command=lambda: magoņmaizīte.update_amount(1))
    plus_magm.place(relx=0.5, rely=0.14)
    minus_magm = tk.Button(text="-", width=3, command=lambda: magoņmaizīte.update_amount(-1))
    minus_magm.place(relx=0.45, rely=0.14)

    #PRODUKTS 4

    k4 = tk.Label(logs, image=kon4)
    k4.place(relx=0.02, rely=0.20)
    kanēļmaizīte = kon4

    cena_kanēļmaizīte = 0.60
    cena_text_kanm = tk.Label(text=f"Cena: €{cena_kanēļmaizīte:.2f}", font=("Arial", 12))
    cena_text_kanm.place(relx=0.135, rely=0.33)
    daudzums_kanm = tk.Label(text="0", font=("Arial", 12))
    daudzums_kanm.place(relx=0.068, rely=0.329)
    kanēļmaizīte = ProductController(daudzums_kanm, cart_manager, "Kanēļmaizīte", cena_kanēļmaizīte)

    plus_kanm = tk.Button(text="+", width=3, command=lambda: kanēļmaizīte.update_amount(1))
    plus_kanm.place(relx=0.09, rely=0.329)
    minus_kanm = tk.Button(text="-", width=3, command=lambda: kanēļmaizīte.update_amount(-1))
    minus_kanm.place(relx=0.04, rely=0.329)
    
    #PRODUKTS 5

    k5 = tk.Label(logs, image=kon5)
    k5.place(relx=0.23, rely=0.20)
    kivimaizīte = kon5

    cena_kivimaizīte = 0.75
    cena_text_kivim = tk.Label(text=f"Cena: €{cena_kivimaizīte:.2f}", font=("Arial", 12))
    cena_text_kivim.place(relx=0.345, rely=0.33)
    daudzums_kivim = tk.Label(text="0", font=("Arial", 12))
    daudzums_kivim.place(relx=0.268, rely=0.329)
    kivimaizīte = ProductController(daudzums_kivim, cart_manager, "Kivimaizīte", cena_kivimaizīte)

    plus_kivim = tk.Button(text="+", width=3, command=lambda: kivimaizīte.update_amount(1))
    plus_kivim.place(relx=0.29, rely=0.329)
    minus_kivim = tk.Button(text="-", width=3, command=lambda: kivimaizīte.update_amount(-1))
    minus_kivim.place(relx=0.24, rely=0.329)

    #PRODUKTS 6

    k6 = tk.Label(logs, image=kon6)
    k6.place(relx=0.44, rely=0.20)
    bulionapīrādziņš = kon6

    cena_bulionapīrādziņš = 0.70
    cena_text_bulp = tk.Label(text=f"Cena: €{cena_bulionapīrādziņš:.2f}", font=("Arial", 12))
    cena_text_bulp.place(relx=0.555, rely=0.33)
    daudzums_bulp = tk.Label(text="0", font=("Arial", 12))
    daudzums_bulp.place(relx=0.477, rely=0.329)
    bulionapīrādziņš = ProductController(daudzums_bulp, cart_manager, "Buliona pīrādziņš", cena_bulionapīrādziņš)

    plus_bulp = tk.Button(text="+", width=3, command=lambda: bulionapīrādziņš.update_amount(1))
    plus_bulp.place(relx=0.5, rely=0.329)
    minus_bulp = tk.Button(text="-", width=3, command=lambda: bulionapīrādziņš.update_amount(-1))
    minus_bulp.place(relx=0.45, rely=0.329)

    #PRODUKTS 7

    k7 = tk.Label(logs, image=kon7)
    k7.place(relx=0.02, rely=0.39)
    pica = kon7

    cena_pica = 1.00
    cena_text_pica = tk.Label(text=f"Cena: €{cena_pica:.2f}", font=("Arial", 12))
    cena_text_pica.place(relx=0.135, rely=0.52)
    daudzums_pica = tk.Label(text="0", font=("Arial", 12))
    daudzums_pica.place(relx=0.068, rely=0.519)
    pica = ProductController(daudzums_pica, cart_manager, "pica", cena_pica)

    plus_pica = tk.Button(text="+", width=3, command=lambda: pica.update_amount(1))
    plus_pica.place(relx=0.09, rely=0.519)
    minus_pica = tk.Button(text="-", width=3, command=lambda: pica.update_amount(-1))
    minus_pica.place(relx=0.04, rely=0.519)

    #PRODUKTS 8

    k8 = tk.Label(logs, image=kon8)
    k8.place(relx=0.23, rely=0.39)
    cīsiņšmīklā = kon8

    cena_cīsiņšmīklā = 0.75
    cena_text_cīsm = tk.Label(text=f"Cena: €{cena_cīsiņšmīklā:.2f}", font=("Arial", 12))
    cena_text_cīsm.place(relx=0.345, rely=0.52)
    daudzums_cīsm = tk.Label(text="0", font=("Arial", 12))
    daudzums_cīsm.place(relx=0.268, rely=0.519)
    cīsiņšmīklā = ProductController(daudzums_cīsm, cart_manager, "Cīsiņš mīklā", cena_cīsiņšmīklā)

    plus_cīsm = tk.Button(text="+", width=3, command=lambda: cīsiņšmīklā.update_amount(1))
    plus_cīsm.place(relx=0.29, rely=0.519)
    minus_cīsm = tk.Button(text="-", width=3, command=lambda: cīsiņšmīklā.update_amount(-1))
    minus_cīsm.place(relx=0.24, rely=0.519)

    #PRODUKTS 9

    k9 = tk.Label(logs, image=kon9)
    k9.place(relx=0.44, rely=0.39)
    Ķiplokubagete = kon9

    cena_Ķiplokubagete = 0.80
    cena_text_ķipb = tk.Label(text=f"Cena: €{cena_Ķiplokubagete:.2f}", font=("Arial", 12))
    cena_text_ķipb.place(relx=0.555, rely=0.52)
    daudzums_ķipb = tk.Label(text="0", font=("Arial", 12))
    daudzums_ķipb.place(relx=0.477, rely=0.519)
    Ķiplokubagete = ProductController(daudzums_bulp, cart_manager, "Ķiploku bagete", cena_Ķiplokubagete)

    plus_ķipb = tk.Button(text="+", width=3, command=lambda: Ķiplokubagete.update_amount(1))
    plus_ķipb.place(relx=0.5, rely=0.519)
    minus_ķipb = tk.Button(text="-", width=3, command=lambda: Ķiplokubagete.update_amount(-1))
    minus_ķipb.place(relx=0.45, rely=0.519)

    cart_frame.lift()

    logs.mainloop()

if __name__== '__main__':
    konditorija_page()