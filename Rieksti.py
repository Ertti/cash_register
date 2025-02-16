from PIL import Image, ImageTk
import tkinter as tk
import main
from main import CartManager, ProductController

from navigation import go_to_main_kategorijas

def rieksti_page():
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

    k1 = resize_image('Rieksti produkti/Sālīti zemesrieksti.png',  0.19, 0.12)
    k2 = resize_image('Rieksti produkti/Zemesrieksti.png',  0.19, 0.12)
    k3 = resize_image('Rieksti produkti/Valrieksti.png',  0.19, 0.12)
    k4 = resize_image('Rieksti produkti/Pistācijas.png',  0.19, 0.12)
    k5 = resize_image('Rieksti produkti/Zemesrieksti sīpola krējuma apvalkā.png',  0.19, 0.12)
    k6 = resize_image('Rieksti produkti/Zemesrieksti chilli apvalkā.png',  0.19, 0.12)

    # frame for cart
    cart_frame = tk.Frame(logs, relief=tk.RIDGE, bg='#dadada')
    cart_frame.place(relx=0.7, rely=0.111)

    cart_manager = CartManager(cart_frame)

    # PRODUKTS 1

    image_label = tk.Label(logs, image=k1)
    image_label.place(relx=0.02, rely=0.01)
    Sālīti_zemesrieksti = k1

    cena_Sālīti_zemesrieksti = 2.40
    cena_text_SZ = tk.Label(text=f"Cena: €{cena_Sālīti_zemesrieksti:.2f}", font=("Arial", 12))
    cena_text_SZ.place(relx=0.135, rely=0.141)
    daudzums_SZ = tk.Label(text="0", font=("Arial", 12))
    daudzums_SZ.place(relx=0.068, rely=0.14)
    Sālīti_zemesrieksti = ProductController(daudzums_SZ, cart_manager, "Sālīti zemesrieksti 500g", cena_Sālīti_zemesrieksti)

    plus_SZ = tk.Button(text="+", width=3, command=lambda: Sālīti_zemesrieksti.update_amount(1))
    plus_SZ.place(relx=0.09, rely=0.14)
    minus_SZ = tk.Button(text="-", width=3, command=lambda: Sālīti_zemesrieksti.update_amount(-1))
    minus_SZ.place(relx=0.04, rely=0.14)

    # PRODUKTS 2

    image_label = tk.Label(logs, image=k2)
    image_label.place(relx=0.23, rely=0.01)
    Zemesrieksti = k2

    cena_Zemesrieksti = 2.00
    cena_text_Z = tk.Label(text=f"Cena: €{cena_Zemesrieksti:.2f}", font=("Arial", 12))
    cena_text_Z.place(relx=0.345, rely=0.141)
    daudzums_Z = tk.Label(text="0", font=("Arial", 12))
    daudzums_Z.place(relx=0.268, rely=0.14)
    Zemesrieksti = ProductController(daudzums_Z, cart_manager, "Zemesrieksti 500g", cena_Zemesrieksti)

    plus_Z = tk.Button(text="+", width=3, command=lambda: Zemesrieksti.update_amount(1))
    plus_Z.place(relx=0.29, rely=0.14)
    minus_Z = tk.Button(text="-", width=3, command=lambda: Zemesrieksti.update_amount(-1))
    minus_Z.place(relx=0.24, rely=0.14)

    # PRODUKTS 3

    image_label = tk.Label(logs, image=k3)
    image_label.place(relx=0.44, rely=0.01)
    Valrieksti = k3

    cena_Valrieksti = 2.80
    cena_text_v = tk.Label(text=f"Cena: €{cena_Valrieksti:.2f}", font=("Arial", 12))
    cena_text_v.place(relx=0.55, rely=0.141)
    daudzums_v = tk.Label(text="0", font=("Arial", 12))
    daudzums_v.place(relx=0.477, rely=0.14)
    Valrieksti = ProductController(daudzums_v, cart_manager, "Valrieksti 500g", cena_Valrieksti)

    plus_v = tk.Button(text="+", width=3, command=lambda: Valrieksti.update_amount(1))
    plus_v.place(relx=0.5, rely=0.14)
    minus_v = tk.Button(text="-", width=3, command=lambda: Valrieksti.update_amount(-1))
    minus_v.place(relx=0.45, rely=0.14)

    # PRODUKTS 4

    image_label = tk.Label(logs, image=k4)
    image_label.place(relx=0.02, rely=0.20)
    Pistācijas = k4

    cena_Pistācijas = 4.20
    cena_text_P = tk.Label(text=f"Cena: €{cena_Pistācijas:.2f}", font=("Arial", 12))
    cena_text_P.place(relx=0.135, rely=0.33)
    daudzums_P = tk.Label(text="0", font=("Arial", 12))
    daudzums_P.place(relx=0.068, rely=0.329)
    Pistācijas = ProductController(daudzums_P, cart_manager, "Pistācijas 500g", cena_Pistācijas)

    plus_P = tk.Button(text="+", width=3, command=lambda: Pistācijas.update_amount(1))
    plus_P.place(relx=0.09, rely=0.329)
    minus_P = tk.Button(text="-", width=3, command=lambda: Pistācijas.update_amount(-1))
    minus_P.place(relx=0.04, rely=0.329)

    # PRODUKTS 5

    image_label = tk.Label(logs, image=k5)
    image_label.place(relx=0.23, rely=0.20)
    Zemesrieksti_sīpola_krējuma_apvalkā = k5

    cena_Zemesrieksti_sīpola_krējuma_apvalkā = 1.40
    cena_text_Zska = tk.Label(text=f"Cena: €{cena_Zemesrieksti_sīpola_krējuma_apvalkā:.2f}", font=("Arial", 12))
    cena_text_Zska.place(relx=0.345, rely=0.33)
    daudzums_Zska = tk.Label(text="0", font=("Arial", 12))
    daudzums_Zska.place(relx=0.268, rely=0.329)
    Zemesrieksti_sīpola_krējuma_apvalkā = ProductController(daudzums_Zska, cart_manager, "Zemesriek. sīp./krēj. apvalkā 200g", cena_Zemesrieksti_sīpola_krējuma_apvalkā)

    plus_Zska = tk.Button(text="+", width=3, command=lambda: Zemesrieksti_sīpola_krējuma_apvalkā.update_amount(1))
    plus_Zska.place(relx=0.29, rely=0.329)
    minus_Zska = tk.Button(text="-", width=3, command=lambda: Zemesrieksti_sīpola_krējuma_apvalkā.update_amount(-1))
    minus_Zska.place(relx=0.24, rely=0.329)

    # PRODUKTS 6

    image_label = tk.Label(logs, image=k6)
    image_label.place(relx=0.44, rely=0.20)
    Zemesrieksti_chilli_apvalkā = k6

    cena_Zemesrieksti_chilli_apvalkā = 1.40
    cena_text_Zca = tk.Label(text=f"Cena: €{cena_Zemesrieksti_chilli_apvalkā:.2f}", font=("Arial", 12))
    cena_text_Zca.place(relx=0.555, rely=0.33)
    daudzums_Zca = tk.Label(text="0", font=("Arial", 12))
    daudzums_Zca.place(relx=0.477, rely=0.329)
    Zemesrieksti_chilli_apvalkā = ProductController(daudzums_Zca, cart_manager, "Zemesrieksti chilli apvalkā 200g", cena_Zemesrieksti_chilli_apvalkā)

    plus_Zca = tk.Button(text="+", width=3, command=lambda: Zemesrieksti_chilli_apvalkā.update_amount(1))
    plus_Zca.place(relx=0.5, rely=0.329)
    minus_Zca = tk.Button(text="-", width=3, command=lambda: Zemesrieksti_chilli_apvalkā.update_amount(-1))
    minus_Zca.place(relx=0.45, rely=0.329)

    cart_frame.lift()

    logs.mainloop()

if __name__== '__main__':
    rieksti_page()