from PIL import Image, ImageTk
import tkinter as tk
import main
from main import CartManager, ProductController

from navigation import go_to_main_kategorijas

def dzērieni_page():
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

    k1 = resize_image('Dzērieni produkti/kola.png',  0.19, 0.12)
    k2 = resize_image('Dzērieni produkti/fanta.png',  0.19, 0.12)
    k3 = resize_image('Dzērieni produkti/sprite.png',  0.19, 0.12)
    k4 = resize_image('Dzērieni produkti/kvass.png',  0.19, 0.12)
    k5 = resize_image('Dzērieni produkti/multiaugļu sula.png',  0.19, 0.12)
    k6 = resize_image('Dzērieni produkti/apelsīnu sula.png',  0.19, 0.12)

    # frame for cart
    cart_frame = tk.Frame(logs, relief=tk.RIDGE, bg='#dadada')
    cart_frame.place(relx=0.7, rely=0.111)

    cart_manager = CartManager(cart_frame)

    # PRODUKTS 1

    image_label = tk.Label(logs, image=k1)
    image_label.place(relx=0.02, rely=0.01)
    kola = k1

    cena_kola = 1.99
    cena_text_kola = tk.Label(text=f"Cena: €{cena_kola:.2f}", font=("Arial", 12))
    cena_text_kola.place(relx=0.135, rely=0.141)
    daudzums_kola = tk.Label(text="0", font=("Arial", 12))
    daudzums_kola.place(relx=0.068, rely=0.14)
    kola = ProductController(daudzums_kola, cart_manager, "Kola 1.5l.", cena_kola)

    plus_kola = tk.Button(text="+", width=3, command=lambda: kola.update_amount(1))
    plus_kola.place(relx=0.09, rely=0.14)
    minus_kola = tk.Button(text="-", width=3, command=lambda: kola.update_amount(-1))
    minus_kola.place(relx=0.04, rely=0.14)

    # PRODUKTS 2

    image_label = tk.Label(logs, image=k2)
    image_label.place(relx=0.23, rely=0.01)
    fanta = k2

    cena_fanta = 1.99
    cena_text_fanta = tk.Label(text=f"Cena: €{cena_fanta:.2f}", font=("Arial", 12))
    cena_text_fanta.place(relx=0.345, rely=0.141)
    daudzums_fanta = tk.Label(text="0", font=("Arial", 12))
    daudzums_fanta.place(relx=0.268, rely=0.14)
    fanta = ProductController(daudzums_fanta, cart_manager, "Fanta 1.5l.", cena_fanta)

    plus_fanta = tk.Button(text="+", width=3, command=lambda: fanta.update_amount(1))
    plus_fanta.place(relx=0.29, rely=0.14)
    minus_fanta = tk.Button(text="-", width=3, command=lambda: fanta.update_amount(-1))
    minus_fanta.place(relx=0.24, rely=0.14)

    # PRODUKTS 3

    image_label = tk.Label(logs, image=k3)
    image_label.place(relx=0.44, rely=0.01)
    sprite = k3

    cena_sprite = 1.99
    cena_text_sprite = tk.Label(text=f"Cena: €{cena_sprite:.2f}", font=("Arial", 12))
    cena_text_sprite.place(relx=0.55, rely=0.141)
    daudzums_sprite = tk.Label(text="0", font=("Arial", 12))
    daudzums_sprite.place(relx=0.477, rely=0.14)
    sprite = ProductController(daudzums_sprite, cart_manager, "Sprite 1.5l.", cena_sprite)

    plus_sprite = tk.Button(text="+", width=3, command=lambda: sprite.update_amount(1))
    plus_sprite.place(relx=0.5, rely=0.14)
    minus_sprite = tk.Button(text="-", width=3, command=lambda: sprite.update_amount(-1))
    minus_sprite.place(relx=0.45, rely=0.14)

    # PRODUKTS 4

    image_label = tk.Label(logs, image=k4)
    image_label.place(relx=0.02, rely=0.20)
    kvass = k4

    cena_kvass = 1.75
    cena_text_kvass = tk.Label(text=f"Cena: €{cena_kvass:.2f}", font=("Arial", 12))
    cena_text_kvass.place(relx=0.135, rely=0.33)
    daudzums_kvass = tk.Label(text="0", font=("Arial", 12))
    daudzums_kvass.place(relx=0.068, rely=0.329)
    kvass = ProductController(daudzums_kvass, cart_manager, "Kvass 1.5l.", cena_kvass)

    plus_kvass = tk.Button(text="+", width=3, command=lambda: kvass.update_amount(1))
    plus_kvass.place(relx=0.09, rely=0.329)
    minus_kvass = tk.Button(text="-", width=3, command=lambda: kvass.update_amount(-1))
    minus_kvass.place(relx=0.04, rely=0.329)

    # PRODUKTS 5

    image_label = tk.Label(logs, image=k5)
    image_label.place(relx=0.23, rely=0.20)
    Multiaugļu_sula = k5

    cena_Multiaugļu_sula = 0.99
    cena_text_msula = tk.Label(text=f"Cena: €{cena_Multiaugļu_sula:.2f}", font=("Arial", 12))
    cena_text_msula.place(relx=0.345, rely=0.33)
    daudzums_msula = tk.Label(text="0", font=("Arial", 12))
    daudzums_msula.place(relx=0.268, rely=0.329)
    Multiaugļu_sula = ProductController(daudzums_msula, cart_manager, "Multiaugļu sula 2l.", cena_Multiaugļu_sula)

    plus_msula = tk.Button(text="+", width=3, command=lambda: Multiaugļu_sula.update_amount(1))
    plus_msula.place(relx=0.29, rely=0.329)
    minus_msula = tk.Button(text="-", width=3, command=lambda: Multiaugļu_sula.update_amount(-1))
    minus_msula.place(relx=0.24, rely=0.329)

    # PRODUKTS 6

    image_label = tk.Label(logs, image=k6)
    image_label.place(relx=0.44, rely=0.20)
    apelsīnu_sula = k6

    cena_apelsīnu_sula = 1.40
    cena_text_asula = tk.Label(text=f"Cena: €{cena_apelsīnu_sula:.2f}", font=("Arial", 12))
    cena_text_asula.place(relx=0.555, rely=0.33)
    daudzums_asula = tk.Label(text="0", font=("Arial", 12))
    daudzums_asula.place(relx=0.477, rely=0.329)
    apelsīnu_sula = ProductController(daudzums_asula, cart_manager, "Apelsīnu sula 2l.", cena_apelsīnu_sula)

    plus_asula = tk.Button(text="+", width=3, command=lambda: apelsīnu_sula.update_amount(1))
    plus_asula.place(relx=0.5, rely=0.329)
    minus_asula = tk.Button(text="-", width=3, command=lambda: apelsīnu_sula.update_amount(-1))
    minus_asula.place(relx=0.45, rely=0.329)

    cart_frame.lift()

    logs.mainloop()

if __name__== '__main__':
    dzērieni_page()