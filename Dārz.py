import tkinter as tk
from PIL import Image, ImageTk
import main
from main import CartManager, ProductController

from navigation import go_to_main_kategorijas

def Daŗzeņi_page():
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

    kon1 = resize_image('sīpol.png', 0.19, 0.12)
    kon2 = resize_image('kāpo.png', 0.19, 0.12)
    kon3 = resize_image('ķiploki.png', 0.19, 0.12)
    kon4 = resize_image('kartupeļi.png', 0.19, 0.12)
    kon5 = resize_image('burk.png', 0.19, 0.12)
    kon6 = resize_image('Lgurķ.png', 0.19, 0.12)
    kon7 = resize_image('tomāti.png', 0.19, 0.12)
    

    # frame for cart
    cart_frame = tk.Frame(logs, relief=tk.RIDGE, bg='#dadada')
    cart_frame.place(relx=0.7, rely=0.111)

    cart_manager = CartManager(cart_frame)

    # PRODUKTS 1

    k1 = tk.Label(logs, image=kon1)
    k1.place(relx=0.02, rely=0.01)
    sīpol = kon1

    cena_sīpol = 0.22
    cena_text_sīpol = tk.Label(text=f"Cena: €{cena_sīpol:.2f}", font=("Arial", 12))
    cena_text_sīpol.place(relx=0.135, rely=0.141)
    daudzums_sīpol = tk.Label(text="0", font=("Arial", 12))
    daudzums_sīpol.place(relx=0.068, rely=0.14)
    sīpol = ProductController(daudzums_sīpol, cart_manager, "Sīpoli", cena_sīpol)

    plus_sīpol = tk.Button(text="+", width=3, command=lambda: sīpol.update_amount(1))
    plus_sīpol.place(relx=0.09, rely=0.14)
    minus_sīpol = tk.Button(text="-", width=3, command=lambda: sīpol.update_amount(-1))
    minus_sīpol.place(relx=0.04, rely=0.14)

    # PRODUKTS 2

    k2 = tk.Label(logs, image=kon2)
    k2.place(relx=0.23, rely=0.01)
    kāpo = kon2

    cena_kāpo = 0.22
    cena_text_kāpo = tk.Label(text=f"Cena: €{sīpol:.2f}", font=("Arial", 12))
    cena_text_kāpo.place(relx=0.345, rely=0.141)
    daudzums_kāpo = tk.Label(text="0", font=("Arial", 12))
    daudzums_kāpo.place(relx=0.268, rely=0.14)
    kāpo = ProductController(daudzums_kāpo, cart_manager, "Kāposti", cena_kāpo)

    plus_kāpo = tk.Button(text="+", width=3, command=lambda: kāpo.update_amount(1))
    plus_kāpo.place(relx=0.29, rely=0.14)
    minus_kāpo = tk.Button(text="-", width=3, command=lambda: kāpo.update_amount(-1))
    minus_kāpo.place(relx=0.24, rely=0.14)

    # PRODUKTS 3

    k3 = tk.Label(logs, image=kon3)
    k3.place(relx=0.44, rely=0.01)
    ķiploki = kon3

    cena_ķiploki = 0.60
    cena_text_ķiploki = tk.Label(text=f"Cena: €{cena_ķiploki:.2f}", font=("Arial", 12))
    cena_text_ķiploki.place(relx=0.555, rely=0.141)
    daudzums_ķiploki = tk.Label(text="0", font=("Arial", 12))
    daudzums_ķiploki.place(relx=0.477, rely=0.14)
    ķiploki = ProductController(daudzums_ķiploki, cart_manager, "Ķiploki", cena_ķiploki)

    plus_ķiploki = tk.Button(text="+", width=3, command=lambda: ķiploki.update_amount(1))
    plus_ķiploki.place(relx=0.5, rely=0.14)
    minus_ķiploki = tk.Button(text="-", width=3, command=lambda: ķiploki.update_amount(-1))
    minus_ķiploki.place(relx=0.45, rely=0.14)

    #PRODUKTS 4

    k4 = tk.Label(logs, image=kon4)
    k4.place(relx=0.02, rely=0.20)
    kartupeļi = kon4

    cena_kartupeļi = 0.60
    cena_text_kartupeļi = tk.Label(text=f"Cena: €{cena_kartupeļi:.2f}", font=("Arial", 12))
    cena_text_kartupeļi.place(relx=0.135, rely=0.33)
    daudzums_kartupeļi = tk.Label(text="0", font=("Arial", 12))
    daudzums_kartupeļi.place(relx=0.068, rely=0.329)
    kartupeļi = ProductController(daudzums_kartupeļi, cart_manager, "Kartupeļi", cena_kartupeļi)

    plus_kartupeļi = tk.Button(text="+", width=3, command=lambda: kartupeļi.update_amount(1))
    plus_kartupeļi.place(relx=0.09, rely=0.329)
    minus_kartupeļi = tk.Button(text="-", width=3, command=lambda: kartupeļi.update_amount(-1))
    minus_kartupeļi.place(relx=0.04, rely=0.329)
    
    #PRODUKTS 5

    k5 = tk.Label(logs, image=kon5)
    k5.place(relx=0.23, rely=0.20)
    burk = kon5

    cena_burk = 0.75
    cena_text_burk = tk.Label(text=f"Cena: €{cena_burk:.2f}", font=("Arial", 12))
    cena_text_burk.place(relx=0.345, rely=0.33)
    daudzums_burk = tk.Label(text="0", font=("Arial", 12))
    daudzums_burk.place(relx=0.268, rely=0.329)
    burk = ProductController(daudzums_burk, cart_manager, "Burkāni", cena_burk)

    plus_burk = tk.Button(text="+", width=3, command=lambda: burk.update_amount(1))
    plus_burk.place(relx=0.29, rely=0.329)
    minus_burk = tk.Button(text="-", width=3, command=lambda: burk.update_amount(-1))
    minus_burk.place(relx=0.24, rely=0.329)

    #PRODUKTS 6

    k6 = tk.Label(logs, image=kon6)
    k6.place(relx=0.44, rely=0.20)
    Lgurķ = kon6

    cena_Lgurķ = 0.70
    cena_text_Lgurķ = tk.Label(text=f"Cena: €{cena_Lgurķ:.2f}", font=("Arial", 12))
    cena_text_Lgurķ.place(relx=0.555, rely=0.33)
    daudzums_Lgurķ = tk.Label(text="0", font=("Arial", 12))
    daudzums_Lgurķ.place(relx=0.477, rely=0.329)
    Lgurķ = ProductController(daudzums_Lgurķ, cart_manager, "Lauku gurķi", cena_Lgurķ)

    plus_Lgurķ = tk.Button(text="+", width=3, command=lambda: Lgurķ.update_amount(1))
    plus_Lgurķ.place(relx=0.5, rely=0.329)
    minus_Lgurķ = tk.Button(text="-", width=3, command=lambda: Lgurķ.update_amount(-1))
    minus_Lgurķ.place(relx=0.45, rely=0.329)

    #PRODUKTS 7

    k7 = tk.Label(logs, image=kon7)
    k7.place(relx=0.02, rely=0.39)
    tomāti = kon7

    cena_tomāti = 1.00
    cena_text_tomāti = tk.Label(text=f"Cena: €{cena_tomāti:.2f}", font=("Arial", 12))
    cena_text_tomāti.place(relx=0.135, rely=0.52)
    daudzums_tomāti = tk.Label(text="0", font=("Arial", 12))
    daudzums_tomāti.place(relx=0.068, rely=0.519)
    tomāti = ProductController(daudzums_tomāti, cart_manager, "Tomāti", cena_tomāti)

    plus_tomāti = tk.Button(text="+", width=3, command=lambda: tomāti.update_amount(1))
    plus_tomāti.place(relx=0.09, rely=0.519)
    minus_tomāti = tk.Button(text="-", width=3, command=lambda: tomāti.update_amount(-1))
    minus_tomāti.place(relx=0.04, rely=0.519)


    cart_frame.lift()

    logs.mainloop()

if __name__== '__main__':
    Daŗzeņi_page()