from PIL import Image, ImageTk
import tkinter as tk
import main
from main import CartManager, ProductController

from navigation import go_to_main_kategorijas

def zivis_page():
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

    ziv1 = resize_image('Zivis/Lasis 1kg.png',  0.19, 0.12)
    ziv2 = resize_image('Zivis/Lasis 500g.png',  0.19, 0.12)
    ziv3 = resize_image('Zivis/Omāras.png',  0.19, 0.12)
    ziv4 = resize_image('Zivis/Skumbrija.png',  0.19, 0.12)
    ziv5 = resize_image('Zivis/Šprotes.png',  0.19, 0.12)

    # frame for cart
    cart_frame = tk.Frame(logs, relief=tk.RIDGE, bg='#dadada')
    cart_frame.place(relx=0.7, rely=0.111)

    cart_manager = CartManager(cart_frame)

    # PRODUKTS 1

    image_label = tk.Label(logs, image=ziv1)
    image_label.place(relx=0.02, rely=0.01)
    Lasis_1kg = ziv1

    cena_Lasis_1kg = 12.99
    cena_text_l1 = tk.Label(text=f"Cena: €{cena_Lasis_1kg:.2f}", font=("Arial", 12))
    cena_text_l1.place(relx=0.135, rely=0.141)
    daudzums_l1 = tk.Label(text="0", font=("Arial", 12))
    daudzums_l1.place(relx=0.068, rely=0.14)
    Lasis_1kg = ProductController(daudzums_l1, cart_manager, "Lasis 1kg", cena_Lasis_1kg)

    plus_l1 = tk.Button(text="+", width=3, command=lambda: Lasis_1kg.update_amount(1))
    plus_l1.place(relx=0.09, rely=0.14)
    minus_l1 = tk.Button(text="-", width=3, command=lambda: Lasis_1kg.update_amount(-1))
    minus_l1.place(relx=0.04, rely=0.14)

    # PRODUKTS 2

    image_label = tk.Label(logs, image=ziv2)
    image_label.place(relx=0.23, rely=0.01)
    Lasis_500g = ziv2

    cena_Lasis_500g = 6.99
    cena_text_l500 = tk.Label(text=f"Cena: €{cena_Lasis_500g:.2f}", font=("Arial", 12))
    cena_text_l500.place(relx=0.345, rely=0.141)
    daudzums_l500 = tk.Label(text="0", font=("Arial", 12))
    daudzums_l500.place(relx=0.268, rely=0.14)
    Lasis_500g = ProductController(daudzums_l500, cart_manager, "Lasis 500g", cena_Lasis_500g)

    plus_l500 = tk.Button(text="+", width=3, command=lambda: Lasis_500g.update_amount(1))
    plus_l500.place(relx=0.29, rely=0.14)
    minus_l500 = tk.Button(text="-", width=3, command=lambda: Lasis_500g.update_amount(-1))
    minus_l500.place(relx=0.24, rely=0.14)

    # PRODUKTS 3

    image_label = tk.Label(logs, image=ziv3)
    image_label.place(relx=0.44, rely=0.01)
    Omārs = ziv3

    cena_Omārs = 7.50
    cena_text_Omārs = tk.Label(text=f"Cena: €{cena_Omārs:.2f}", font=("Arial", 12))
    cena_text_Omārs.place(relx=0.55, rely=0.141)
    daudzums_Omārs = tk.Label(text="0", font=("Arial", 12))
    daudzums_Omārs.place(relx=0.477, rely=0.14)
    Omārs = ProductController(daudzums_Omārs, cart_manager, "Omārs", cena_Omārs)

    plus_Omārs = tk.Button(text="+", width=3, command=lambda: Omārs.update_amount(1))
    plus_Omārs.place(relx=0.5, rely=0.14)
    minus_Omārs = tk.Button(text="-", width=3, command=lambda: Omārs.update_amount(-1))
    minus_Omārs.place(relx=0.45, rely=0.14)

    # PRODUKTS 4

    image_label = tk.Label(logs, image=ziv4)
    image_label.place(relx=0.02, rely=0.20)
    Skumbrija = ziv4

    cena_Skumbrija = 2.99
    cena_text_skumb = tk.Label(text=f"Cena: €{cena_Skumbrija:.2f}", font=("Arial", 12))
    cena_text_skumb.place(relx=0.135, rely=0.33)
    daudzums_skumb = tk.Label(text="0", font=("Arial", 12))
    daudzums_skumb.place(relx=0.068, rely=0.329)
    Skumbrija = ProductController(daudzums_skumb, cart_manager, "Skumbrija", cena_Skumbrija)

    plus_skumb = tk.Button(text="+", width=3, command=lambda: Skumbrija.update_amount(1))
    plus_skumb.place(relx=0.09, rely=0.329)
    minus_skumb = tk.Button(text="-", width=3, command=lambda: Skumbrija.update_amount(-1))
    minus_skumb.place(relx=0.04, rely=0.329)

    # PRODUKTS 5

    image_label = tk.Label(logs, image=ziv5)
    image_label.place(relx=0.23, rely=0.20)
    Šprotes = ziv5

    cena_Šprotes = 1.10
    cena_text_Šprotes = tk.Label(text=f"Cena: €{cena_Šprotes:.2f}", font=("Arial", 12))
    cena_text_Šprotes.place(relx=0.345, rely=0.33)
    daudzums_Šprotes = tk.Label(text="0", font=("Arial", 12))
    daudzums_Šprotes.place(relx=0.268, rely=0.329)
    Šprotes = ProductController(daudzums_Šprotes, cart_manager, "Šprotes", cena_Šprotes)

    plus_Šprotes = tk.Button(text="+", width=3, command=lambda: Šprotes.update_amount(1))
    plus_Šprotes.place(relx=0.29, rely=0.329)
    minus_Šprotes = tk.Button(text="-", width=3, command=lambda: Šprotes.update_amount(-1))
    minus_Šprotes.place(relx=0.24, rely=0.329)

    cart_frame.lift()

    logs.mainloop()

if __name__== '__main__':
    zivis_page()