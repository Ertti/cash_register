from PIL import Image, ImageTk
import tkinter as tk
import main
from main import CartManager, ProductController

from navigation import go_to_main_kategorijas

def alkohols_page():
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

    k1 = resize_image('Alkohols produkti/Sarkanvīns.png',  0.19, 0.12)
    k2 = resize_image('Alkohols produkti/Baltvīns.png',  0.19, 0.12)
    k3 = resize_image('Alkohols produkti/Šampanietis.png',  0.19, 0.12)
    k4 = resize_image('Alkohols produkti/Viskijs.png',  0.19, 0.12)

    # frame for cart
    cart_frame = tk.Frame(logs, relief=tk.RIDGE, bg='#dadada')
    cart_frame.place(relx=0.7, rely=0.111)

    cart_manager = CartManager(cart_frame)

    # PRODUKTS 1

    image_label = tk.Label(logs, image=k1)
    image_label.place(relx=0.02, rely=0.01)
    Sarkanvīns = k1

    cena_Sarkanvīns = 13.99
    cena_text_Sarkanvīns = tk.Label(text=f"Cena: €{cena_Sarkanvīns:.2f}", font=("Arial", 12))
    cena_text_Sarkanvīns.place(relx=0.135, rely=0.141)
    daudzums_Sarkanvīns = tk.Label(text="0", font=("Arial", 12))
    daudzums_Sarkanvīns.place(relx=0.068, rely=0.14)
    Sarkanvīns = ProductController(daudzums_Sarkanvīns, cart_manager, "Sarkanvīns 0.75l.", cena_Sarkanvīns)

    plus_Sarkanvīns = tk.Button(text="+", width=3, command=lambda: Sarkanvīns.update_amount(1))
    plus_Sarkanvīns.place(relx=0.09, rely=0.14)
    minus_Sarkanvīns = tk.Button(text="-", width=3, command=lambda: Sarkanvīns.update_amount(-1))
    minus_Sarkanvīns.place(relx=0.04, rely=0.14)

    # PRODUKTS 2

    image_label = tk.Label(logs, image=k2)
    image_label.place(relx=0.23, rely=0.01)
    Baltvīns = k2

    cena_Baltvīns = 7.99
    cena_text_Baltvīns = tk.Label(text=f"Cena: €{cena_Baltvīns:.2f}", font=("Arial", 12))
    cena_text_Baltvīns.place(relx=0.345, rely=0.141)
    daudzums_Baltvīns = tk.Label(text="0", font=("Arial", 12))
    daudzums_Baltvīns.place(relx=0.268, rely=0.14)
    Baltvīns = ProductController(daudzums_Baltvīns, cart_manager, "Baltvīns 0.75l.", cena_Baltvīns)

    plus_Baltvīns = tk.Button(text="+", width=3, command=lambda: Baltvīns.update_amount(1))
    plus_Baltvīns.place(relx=0.29, rely=0.14)
    minus_Baltvīns = tk.Button(text="-", width=3, command=lambda: Baltvīns.update_amount(-1))
    minus_Baltvīns.place(relx=0.24, rely=0.14)

    # PRODUKTS 3

    image_label = tk.Label(logs, image=k3)
    image_label.place(relx=0.44, rely=0.01)
    Šampanietis = k3

    cena_Šampanietis = 20.99
    cena_text_Šampanietis = tk.Label(text=f"Cena: €{cena_Šampanietis:.2f}", font=("Arial", 12))
    cena_text_Šampanietis.place(relx=0.55, rely=0.141)
    daudzums_Šampanietis = tk.Label(text="0", font=("Arial", 12))
    daudzums_Šampanietis.place(relx=0.477, rely=0.14)
    Šampanietis = ProductController(daudzums_Šampanietis, cart_manager, "Šampanietis 0.75l.", cena_Šampanietis)

    plus_Šampanietis = tk.Button(text="+", width=3, command=lambda: Šampanietis.update_amount(1))
    plus_Šampanietis.place(relx=0.5, rely=0.14)
    minus_Šampanietis = tk.Button(text="-", width=3, command=lambda: Šampanietis.update_amount(-1))
    minus_Šampanietis.place(relx=0.45, rely=0.14)

    # PRODUKTS 4

    image_label = tk.Label(logs, image=k4)
    image_label.place(relx=0.02, rely=0.20)
    Viskijs = k4

    cena_Viskijs = 39.99
    cena_text_Viskijs = tk.Label(text=f"Cena: €{cena_Viskijs:.2f}", font=("Arial", 12))
    cena_text_Viskijs.place(relx=0.135, rely=0.33)
    daudzums_Viskijs = tk.Label(text="0", font=("Arial", 12))
    daudzums_Viskijs.place(relx=0.068, rely=0.329)
    Viskijs = ProductController(daudzums_Viskijs, cart_manager, "Viskijs 0.7l.", cena_Viskijs)

    plus_Viskijs = tk.Button(text="+", width=3, command=lambda: Viskijs.update_amount(1))
    plus_Viskijs.place(relx=0.09, rely=0.329)
    minus_Viskijs = tk.Button(text="-", width=3, command=lambda: Viskijs.update_amount(-1))
    minus_Viskijs.place(relx=0.04, rely=0.329)

    cart_frame.lift()

    logs.mainloop()

if __name__== '__main__':
    alkohols_page()