from PIL import Image, ImageTk
import tkinter as tk
import main
from main import CartManager, ProductController

from navigation import go_to_main_kategorijas

def maize_page():
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

    k1 = resize_image('Maizes produkti/Baltmaize.png',  0.19, 0.12)
    k2 = resize_image('Maizes produkti/Rupjmaiz.png',  0.19, 0.12)
    k3 = resize_image('Maizes produkti/Saldskābmaize.png',  0.19, 0.12)

    # frame for cart
    cart_frame = tk.Frame(logs, relief=tk.RIDGE, bg='#dadada')
    cart_frame.place(relx=0.7, rely=0.111)

    cart_manager = CartManager(cart_frame)

    # PRODUKTS 1

    image_label = tk.Label(logs, image=k1)
    image_label.place(relx=0.02, rely=0.01)
    Baltmaize = k1

    cena_Baltmaize = 0.99
    cena_text_Baltmaize = tk.Label(text=f"Cena: €{cena_Baltmaize:.2f}", font=("Arial", 12))
    cena_text_Baltmaize.place(relx=0.135, rely=0.141)
    daudzums_Baltmaize = tk.Label(text="0", font=("Arial", 12))
    daudzums_Baltmaize.place(relx=0.068, rely=0.14)
    Baltmaize = ProductController(daudzums_Baltmaize, cart_manager, "Baltmaize 250g", cena_Baltmaize)

    plus_Baltmaize = tk.Button(text="+", width=3, command=lambda: Baltmaize.update_amount(1))
    plus_Baltmaize.place(relx=0.09, rely=0.14)
    minus_Baltmaize = tk.Button(text="-", width=3, command=lambda: Baltmaize.update_amount(-1))
    minus_Baltmaize.place(relx=0.04, rely=0.14)

    # PRODUKTS 2

    image_label = tk.Label(logs, image=k2)
    image_label.place(relx=0.23, rely=0.01)
    Rupjmaiz = k2

    cena_Rupjmaiz = 1.45
    cena_text_Rupjmaiz = tk.Label(text=f"Cena: €{cena_Rupjmaiz:.2f}", font=("Arial", 12))
    cena_text_Rupjmaiz.place(relx=0.345, rely=0.141)
    daudzums_Rupjmaiz = tk.Label(text="0", font=("Arial", 12))
    daudzums_Rupjmaiz.place(relx=0.268, rely=0.14)
    Rupjmaiz = ProductController(daudzums_Rupjmaiz, cart_manager, "Rupjmaize 250g", cena_Rupjmaiz)

    plus_Rupjmaiz = tk.Button(text="+", width=3, command=lambda: Rupjmaiz.update_amount(1))
    plus_Rupjmaiz.place(relx=0.29, rely=0.14)
    minus_Rupjmaiz = tk.Button(text="-", width=3, command=lambda: Rupjmaiz.update_amount(-1))
    minus_Rupjmaiz.place(relx=0.24, rely=0.14)

    # PRODUKTS 3

    image_label = tk.Label(logs, image=k3)
    image_label.place(relx=0.44, rely=0.01)
    Saldskābmaize = k3

    cena_Saldskābmaize = 2.85
    cena_text_Saldskm = tk.Label(text=f"Cena: €{cena_Saldskābmaize:.2f}", font=("Arial", 12))
    cena_text_Saldskm.place(relx=0.55, rely=0.141)
    daudzums_Saldskm = tk.Label(text="0", font=("Arial", 12))
    daudzums_Saldskm.place(relx=0.477, rely=0.14)
    Saldskābmaize = ProductController(daudzums_Saldskm, cart_manager, "Saldskābmaize 500g", cena_Saldskābmaize)

    plus_Saldskm = tk.Button(text="+", width=3, command=lambda: Saldskābmaize.update_amount(1))
    plus_Saldskm.place(relx=0.5, rely=0.14)
    minus_Saldskm = tk.Button(text="-", width=3, command=lambda: Saldskābmaize.update_amount(-1))
    minus_Saldskm.place(relx=0.45, rely=0.14)

    cart_frame.lift()

    logs.mainloop()

if __name__== '__main__':
    maize_page()