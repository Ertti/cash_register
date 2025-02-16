from PIL import Image, ImageTk
import tkinter as tk
import main
from main import CartManager, ProductController

from navigation import go_to_main_kategorijas

def dārzeņi_page():
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

    k1 = resize_image('Dārzeņu produkti/Sīpoli.png',  0.19, 0.12)
    k2 = resize_image('Dārzeņu produkti/Burkāni.png',  0.19, 0.12)
    k3 = resize_image('Dārzeņu produkti/Kāposts.png',  0.19, 0.12)
    k4 = resize_image('Dārzeņu produkti/Kartupeļi.png',  0.19, 0.12)
    k5 = resize_image('Dārzeņu produkti/Ķiploki.png',  0.19, 0.12)
    k6 = resize_image('Dārzeņu produkti/Lauku gurķi.png',  0.19, 0.12)
    k7 = resize_image('Dārzeņu produkti/Tomāti.png',  0.19, 0.12)
   
    # frame for cart
    cart_frame = tk.Frame(logs, relief=tk.RIDGE, bg='#dadada')
    cart_frame.place(relx=0.7, rely=0.111)

    cart_manager = CartManager(cart_frame)

    # PRODUKTS 1

    image_label = tk.Label(logs, image=k1)
    image_label.place(relx=0.02, rely=0.01)
    Sīpoli = k1

    cena_Sīpoli = 0.65
    cena_text_Sīpoli = tk.Label(text=f"Cena: €{cena_Sīpoli:.2f}/kg", font=("Arial", 12))
    cena_text_Sīpoli.place(relx=0.135, rely=0.141)
    daudzums_Sīpoli = tk.Label(text="0", font=("Arial", 12))
    daudzums_Sīpoli.place(relx=0.068, rely=0.14)
    Sīpoli = ProductController(daudzums_Sīpoli, cart_manager, "Sīpoli", cena_Sīpoli)

    plus_Sīpoli = tk.Button(text="+", width=3, command=lambda: Sīpoli.update_amount(1))
    plus_Sīpoli.place(relx=0.09, rely=0.14)
    minus_Sīpoli = tk.Button(text="-", width=3, command=lambda: Sīpoli.update_amount(-1))
    minus_Sīpoli.place(relx=0.04, rely=0.14)

    # PRODUKTS 2

    image_label = tk.Label(logs, image=k2)
    image_label.place(relx=0.23, rely=0.01)
    Burkāni = k2

    cena_Burkāni = 1.20
    cena_text_Burkāni = tk.Label(text=f"Cena: €{cena_Burkāni:.2f}/kg", font=("Arial", 12))
    cena_text_Burkāni.place(relx=0.345, rely=0.141)
    daudzums_Burkāni = tk.Label(text="0", font=("Arial", 12))
    daudzums_Burkāni.place(relx=0.268, rely=0.14)
    Burkāni = ProductController(daudzums_Burkāni, cart_manager, "Burkāni", cena_Burkāni)

    plus_Burkāni = tk.Button(text="+", width=3, command=lambda: Burkāni.update_amount(1))
    plus_Burkāni.place(relx=0.29, rely=0.14)
    minus_Burkāni = tk.Button(text="-", width=3, command=lambda: Burkāni.update_amount(-1))
    minus_Burkāni.place(relx=0.24, rely=0.14)

    # PRODUKTS 3

    image_label = tk.Label(logs, image=k3)
    image_label.place(relx=0.44, rely=0.01)
    Kāposts = k3

    cena_Kāposts = 1.50
    cena_text_Kāposts = tk.Label(text=f"Cena: €{cena_Kāposts:.2f}/kg", font=("Arial", 12))
    cena_text_Kāposts.place(relx=0.55, rely=0.141)
    daudzums_Kāposts = tk.Label(text="0", font=("Arial", 12))
    daudzums_Kāposts.place(relx=0.477, rely=0.14)
    Kāposts = ProductController(daudzums_Kāposts, cart_manager, "Kāposts", cena_Kāposts)

    plus_Kāposts = tk.Button(text="+", width=3, command=lambda: Kāposts.update_amount(1))
    plus_Kāposts.place(relx=0.5, rely=0.14)
    minus_Kāposts = tk.Button(text="-", width=3, command=lambda: Kāposts.update_amount(-1))
    minus_Kāposts.place(relx=0.45, rely=0.14)

    # PRODUKTS 4

    image_label = tk.Label(logs, image=k4)
    image_label.place(relx=0.02, rely=0.20)
    Kartupeļi = k4

    cena_Kartupeļi = 0.95
    cena_text_Kartupeļi = tk.Label(text=f"Cena: €{cena_Kartupeļi:.2f}/kg", font=("Arial", 12))
    cena_text_Kartupeļi.place(relx=0.135, rely=0.33)
    daudzums_Kartupeļi = tk.Label(text="0", font=("Arial", 12))
    daudzums_Kartupeļi.place(relx=0.068, rely=0.329)
    Kartupeļi = ProductController(daudzums_Kartupeļi, cart_manager, "Kartupeļi", cena_Kartupeļi)

    plus_Kartupeļi = tk.Button(text="+", width=3, command=lambda: Kartupeļi.update_amount(1))
    plus_Kartupeļi.place(relx=0.09, rely=0.329)
    minus_Kartupeļi = tk.Button(text="-", width=3, command=lambda: Kartupeļi.update_amount(-1))
    minus_Kartupeļi.place(relx=0.04, rely=0.329)

    # PRODUKTS 5

    image_label = tk.Label(logs, image=k5)
    image_label.place(relx=0.23, rely=0.20)
    Ķiploki = k5

    cena_Ķiploki = 0.90
    cena_text_Ķiploki = tk.Label(text=f"Cena: €{cena_Ķiploki:.2f}/kg", font=("Arial", 12))
    cena_text_Ķiploki.place(relx=0.345, rely=0.33)
    daudzums_Ķiploki = tk.Label(text="0", font=("Arial", 12))
    daudzums_Ķiploki.place(relx=0.268, rely=0.329)
    Ķiploki = ProductController(daudzums_Ķiploki, cart_manager, "Ķiploki", cena_Ķiploki)

    plus_Ķiploki = tk.Button(text="+", width=3, command=lambda: Ķiploki.update_amount(1))
    plus_Ķiploki.place(relx=0.29, rely=0.329)
    minus_Ķiploki = tk.Button(text="-", width=3, command=lambda: Ķiploki.update_amount(-1))
    minus_Ķiploki.place(relx=0.24, rely=0.329)

    # PRODUKTS 6

    image_label = tk.Label(logs, image=k6)
    image_label.place(relx=0.44, rely=0.20)
    Lauku_gurķi = k6

    cena_Lauku_gurķi = 1.10
    cena_text_lauku_g = tk.Label(text=f"Cena: €{cena_Lauku_gurķi:.2f}/kg", font=("Arial", 12))
    cena_text_lauku_g.place(relx=0.555, rely=0.33)
    daudzums_lauku_g = tk.Label(text="0", font=("Arial", 12))
    daudzums_lauku_g.place(relx=0.477, rely=0.329)
    Lauku_gurķi = ProductController(daudzums_lauku_g, cart_manager, "Lauku gurķi", cena_Lauku_gurķi)

    plus_lauku_g = tk.Button(text="+", width=3, command=lambda: Lauku_gurķi.update_amount(1))
    plus_lauku_g.place(relx=0.5, rely=0.329)
    minus_lauku_g = tk.Button(text="-", width=3, command=lambda: Lauku_gurķi.update_amount(-1))
    minus_lauku_g.place(relx=0.45, rely=0.329)

    # PRODUKTS 7

    image_label = tk.Label(logs, image=k7)
    image_label.place(relx=0.02, rely=0.39)
    Tomāti = k7

    cena_Tomāti = 1.35
    cena_text_Tomāti = tk.Label(text=f"Cena: €{cena_Tomāti:.2f}/kg", font=("Arial", 12))
    cena_text_Tomāti.place(relx=0.135, rely=0.52)
    daudzums_Tomāti = tk.Label(text="0", font=("Arial", 12))
    daudzums_Tomāti.place(relx=0.068, rely=0.519)
    Tomāti = ProductController(daudzums_Tomāti, cart_manager, "Tomāti", cena_Tomāti)

    plus_Tomāti = tk.Button(text="+", width=3, command=lambda: Tomāti.update_amount(1))
    plus_Tomāti.place(relx=0.09, rely=0.519)
    minus_Tomāti = tk.Button(text="-", width=3, command=lambda: Tomāti.update_amount(-1))
    minus_Tomāti.place(relx=0.04, rely=0.519)

    cart_frame.lift()

    logs.mainloop()

if __name__== '__main__':
    dārzeņi_page()