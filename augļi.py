import tkinter as tk
from PIL import Image, ImageTk
import main
from main import CartManager, ProductController

from navigation import go_to_main_kategorijas

def Augļi_page():
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

    k1 = resize_image('Augļu produkti/āboli.png', 0.19, 0.12)
    k2 = resize_image('Augļu produkti/banāni.png', 0.19, 0.12)
    k3 = resize_image('Augļu produkti/bumbier.png', 0.19, 0.12)
    k4 = resize_image('Augļu produkti/Tplūmes.png', 0.19, 0.12)
    k5 = resize_image('Augļu produkti/Ķirši.png', 0.19, 0.12)
    k6 = resize_image('Augļu produkti/Apelsīn.png', 0.19, 0.12)
    k7 = resize_image('Augļu produkti/Zemenes.png', 0.19, 0.12)
    k8 = resize_image('Augļu produkti/Mellenes.png', 0.19, 0.12)

    # frame for cart
    cart_frame = tk.Frame(logs, relief=tk.RIDGE, bg='#dadada')
    cart_frame.place(relx=0.7, rely=0.111)

    cart_manager = CartManager(cart_frame)

    # PRODUKTS 1

    image_label = tk.Label(logs, image=k1)
    image_label.place(relx=0.02, rely=0.01)
    āboli = k1

    cena_āboli = 0.25
    cena_text_āboli = tk.Label(text=f"Cena: €{cena_āboli:.2f}", font=("Arial", 12))
    cena_text_āboli.place(relx=0.135, rely=0.141)
    daudzums_āboli = tk.Label(text="0", font=("Arial", 12))
    daudzums_āboli.place(relx=0.068, rely=0.14)
    āboli = ProductController(daudzums_āboli, cart_manager, "Āboli", cena_āboli)

    plus_āboli = tk.Button(text="+", width=3, command=lambda: āboli.update_amount(1))
    plus_āboli.place(relx=0.09, rely=0.14)
    minus_āboli = tk.Button(text="-", width=3, command=lambda: āboli.update_amount(-1))
    minus_āboli.place(relx=0.04, rely=0.14)

    # PRODUKTS 2

    image_label = tk.Label(logs, image=k2)
    image_label.place(relx=0.23, rely=0.01)
    bana = k2

    cena_bana = 1.19
    cena_text_bana = tk.Label(text=f"Cena: €{cena_bana:.2f}", font=("Arial", 12))
    cena_text_bana.place(relx=0.345, rely=0.141)
    daudzums_bana = tk.Label(text="0", font=("Arial", 12))
    daudzums_bana.place(relx=0.268, rely=0.14)
    bana = ProductController(daudzums_bana, cart_manager, "Banāni", cena_bana)

    plus_bana = tk.Button(text="+", width=3, command=lambda: bana.update_amount(1))
    plus_bana.place(relx=0.29, rely=0.14)
    minus_bana = tk.Button(text="-", width=3, command=lambda: bana.update_amount(-1))
    minus_bana.place(relx=0.24, rely=0.14)

    # PRODUKTS 3

    image_label = tk.Label(logs, image=k3)
    image_label.place(relx=0.44, rely=0.01)
    bumb = k3

    cena_bumb = 0.55
    cena_text_bumb = tk.Label(text=f"Cena: €{cena_bumb:.2f}", font=("Arial", 12))
    cena_text_bumb.place(relx=0.555, rely=0.141)
    daudzums_bumb = tk.Label(text="0", font=("Arial", 12))
    daudzums_bumb.place(relx=0.477, rely=0.14)
    bumb = ProductController(daudzums_bumb, cart_manager, "Bumbieri", cena_bumb)

    plus_bumb = tk.Button(text="+", width=3, command=lambda: bumb.update_amount(1))
    plus_bumb.place(relx=0.5, rely=0.14)
    minus_bumb = tk.Button(text="-", width=3, command=lambda: bumb.update_amount(-1))
    minus_bumb.place(relx=0.45, rely=0.14)

    #PRODUKTS 4

    image_label = tk.Label(logs, image=k4)
    image_label.place(relx=0.02, rely=0.20)
    Tplūm = k4

    cena_Tplūm = 1.50
    cena_text_Tplūm = tk.Label(text=f"Cena: €{cena_Tplūm:.2f}", font=("Arial", 12))
    cena_text_Tplūm.place(relx=0.135, rely=0.33)
    daudzums_Tplūm = tk.Label(text="0", font=("Arial", 12))
    daudzums_Tplūm.place(relx=0.068, rely=0.329)
    Tplūm = ProductController(daudzums_Tplūm, cart_manager, "Tumsās plūmes", cena_Tplūm)

    plus_Tplūm = tk.Button(text="+", width=3, command=lambda: Tplūm.update_amount(1))
    plus_Tplūm.place(relx=0.09, rely=0.329)
    minus_Tplūm = tk.Button(text="-", width=3, command=lambda: Tplūm.update_amount(-1))
    minus_Tplūm.place(relx=0.04, rely=0.329)
    
    #PRODUKTS 5

    image_label = tk.Label(logs, image=k5)
    image_label.place(relx=0.23, rely=0.20)
    Ķirš = k5

    cena_Ķirš = 0.75
    cena_text_Ķirš = tk.Label(text=f"Cena: €{cena_Ķirš:.2f}", font=("Arial", 12))
    cena_text_Ķirš.place(relx=0.345, rely=0.33)
    daudzums_Ķirš = tk.Label(text="0", font=("Arial", 12))
    daudzums_Ķirš.place(relx=0.268, rely=0.329)
    Ķirš = ProductController(daudzums_Ķirš, cart_manager, "Ķirši", cena_Ķirš)

    plus_Ķirš = tk.Button(text="+", width=3, command=lambda: Ķirš.update_amount(1))
    plus_Ķirš.place(relx=0.29, rely=0.329)
    minus_Ķirš = tk.Button(text="-", width=3, command=lambda: Ķirš.update_amount(-1))
    minus_Ķirš.place(relx=0.24, rely=0.329)

    #PRODUKTS 6

    image_label = tk.Label(logs, image=k6)
    image_label.place(relx=0.44, rely=0.20)
    Apel = k6

    cena_Apel = 1.60
    cena_text_Apel = tk.Label(text=f"Cena: €{cena_Apel:.2f}", font=("Arial", 12))
    cena_text_Apel.place(relx=0.555, rely=0.33)
    daudzums_Apel = tk.Label(text="0", font=("Arial", 12))
    daudzums_Apel.place(relx=0.477, rely=0.329)
    Apel = ProductController(daudzums_Apel, cart_manager, "Apelsīni", cena_Apel)

    plus_Apel = tk.Button(text="+", width=3, command=lambda: Apel.update_amount(1))
    plus_Apel.place(relx=0.5, rely=0.329)
    minus_Apel = tk.Button(text="-", width=3, command=lambda: Apel.update_amount(-1))
    minus_Apel.place(relx=0.45, rely=0.329)

    #PRODUKTS 7

    image_label = tk.Label(logs, image=k7)
    image_label.place(relx=0.02, rely=0.39)
    Zemen = k7

    cena_Zemen = 1.20
    cena_text_Zemen = tk.Label(text=f"Cena: €{cena_Zemen:.2f}", font=("Arial", 12))
    cena_text_Zemen.place(relx=0.135, rely=0.52)
    daudzums_Zemen = tk.Label(text="0", font=("Arial", 12))
    daudzums_Zemen.place(relx=0.068, rely=0.519)
    Zemen = ProductController(daudzums_Zemen, cart_manager, "Zemene", cena_Zemen)

    plus_Zemen = tk.Button(text="+", width=3, command=lambda: Zemen.update_amount(1))
    plus_Zemen.place(relx=0.09, rely=0.519)
    minus_Zemen = tk.Button(text="-", width=3, command=lambda: Zemen.update_amount(-1))
    minus_Zemen.place(relx=0.04, rely=0.519)

    #PRODUKTS 8

    image_label = tk.Label(logs, image=k8)
    image_label.place(relx=0.23, rely=0.39)
    Melle = k8

    cena_Melle = 1.25
    cena_text_Melle = tk.Label(text=f"Cena: €{cena_Melle:.2f}", font=("Arial", 12))
    cena_text_Melle.place(relx=0.345, rely=0.52)
    daudzums_Melle = tk.Label(text="0", font=("Arial", 12))
    daudzums_Melle.place(relx=0.268, rely=0.519)
    Melle = ProductController(daudzums_Melle, cart_manager, "Mellenes", cena_Melle)

    plus_Melle = tk.Button(text="+", width=3, command=lambda: Melle.update_amount(1))
    plus_Melle.place(relx=0.29, rely=0.519)
    minus_Melle = tk.Button(text="-", width=3, command=lambda: Melle.update_amount(-1))
    minus_Melle.place(relx=0.24, rely=0.519)

    cart_frame.lift()

    logs.mainloop()

if __name__== '__main__':
    Augļi_page()