from PIL import Image, ImageTk
import tkinter as tk
import main
from main import CartManager, ProductController

from navigation import go_to_main_kategorijas

def saldējumi_page():
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

    k1 = resize_image('Saldējumi produkti/Zemeņu.png',  0.19, 0.12)
    k2 = resize_image('Saldējumi produkti/Šokolādes.png',  0.19, 0.12)
    k3 = resize_image('Saldējumi produkti/Vaniļas.png',  0.19, 0.12)
    k4 = resize_image('Saldējumi produkti/Karameļu.png',  0.19, 0.12)
    k5 = resize_image('Saldējumi produkti/Riekstiem un sīrupu (kastē).png',  0.19, 0.12)
    k6 = resize_image('Saldējumi produkti/Šokolādi un vaniļu (kastē).png',  0.19, 0.12)

    # frame for cart
    cart_frame = tk.Frame(logs, relief=tk.RIDGE, bg='#dadada')
    cart_frame.place(relx=0.7, rely=0.111)

    cart_manager = CartManager(cart_frame)

    # PRODUKTS 1

    image_label = tk.Label(logs, image=k1)
    image_label.place(relx=0.02, rely=0.01)
    Zemeņu = k1

    cena_Zemeņu = 0.70
    cena_text_Zemeņu = tk.Label(text=f"Cena: €{cena_Zemeņu:.2f}", font=("Arial", 12))
    cena_text_Zemeņu.place(relx=0.135, rely=0.141)
    daudzums_Zemeņu = tk.Label(text="0", font=("Arial", 12))
    daudzums_Zemeņu.place(relx=0.068, rely=0.14)
    Zemeņu = ProductController(daudzums_Zemeņu, cart_manager, "Zemeņu saldējums", cena_Zemeņu)

    plus_Zemeņu = tk.Button(text="+", width=3, command=lambda: Zemeņu.update_amount(1))
    plus_Zemeņu.place(relx=0.09, rely=0.14)
    minus_Zemeņu = tk.Button(text="-", width=3, command=lambda: Zemeņu.update_amount(-1))
    minus_Zemeņu.place(relx=0.04, rely=0.14)

    # PRODUKTS 2

    image_label = tk.Label(logs, image=k2)
    image_label.place(relx=0.23, rely=0.01)
    Šokolādes = k2

    cena_Šokolādes = 0.70
    cena_text_Šokolādes = tk.Label(text=f"Cena: €{cena_Šokolādes:.2f}", font=("Arial", 12))
    cena_text_Šokolādes.place(relx=0.345, rely=0.141)
    daudzums_Šokolādes = tk.Label(text="0", font=("Arial", 12))
    daudzums_Šokolādes.place(relx=0.268, rely=0.14)
    Šokolādes = ProductController(daudzums_Šokolādes, cart_manager, "Šokolādes saldējums", cena_Šokolādes)

    plus_Šokolādes = tk.Button(text="+", width=3, command=lambda: Šokolādes.update_amount(1))
    plus_Šokolādes.place(relx=0.29, rely=0.14)
    minus_Šokolādes = tk.Button(text="-", width=3, command=lambda: Šokolādes.update_amount(-1))
    minus_Šokolādes.place(relx=0.24, rely=0.14)

    # PRODUKTS 3

    image_label = tk.Label(logs, image=k3)
    image_label.place(relx=0.44, rely=0.01)
    Vaniļas = k3

    cena_Vaniļas = 0.70
    cena_text_Vaniļas = tk.Label(text=f"Cena: €{cena_Vaniļas:.2f}", font=("Arial", 12))
    cena_text_Vaniļas.place(relx=0.55, rely=0.141)
    daudzums_Vaniļas = tk.Label(text="0", font=("Arial", 12))
    daudzums_Vaniļas.place(relx=0.477, rely=0.14)
    Vaniļas = ProductController(daudzums_Vaniļas, cart_manager, "Vaniļas saldējums", cena_Vaniļas)

    plus_Vaniļas = tk.Button(text="+", width=3, command=lambda: Vaniļas.update_amount(1))
    plus_Vaniļas.place(relx=0.5, rely=0.14)
    minus_Vaniļas = tk.Button(text="-", width=3, command=lambda: Vaniļas.update_amount(-1))
    minus_Vaniļas.place(relx=0.45, rely=0.14)

    # PRODUKTS 4

    image_label = tk.Label(logs, image=k4)
    image_label.place(relx=0.02, rely=0.20)
    Karameļu = k4

    cena_Karameļu = 0.70
    cena_text_Karameļu = tk.Label(text=f"Cena: €{cena_Karameļu:.2f}", font=("Arial", 12))
    cena_text_Karameļu.place(relx=0.135, rely=0.33)
    daudzums_Karameļu = tk.Label(text="0", font=("Arial", 12))
    daudzums_Karameļu.place(relx=0.068, rely=0.329)
    Karameļu = ProductController(daudzums_Karameļu, cart_manager, "Karameļu saldējums", cena_Karameļu)

    plus_Karameļu = tk.Button(text="+", width=3, command=lambda: Karameļu.update_amount(1))
    plus_Karameļu.place(relx=0.09, rely=0.329)
    minus_Karameļu = tk.Button(text="-", width=3, command=lambda: Karameļu.update_amount(-1))
    minus_Karameļu.place(relx=0.04, rely=0.329)

    # PRODUKTS 5

    image_label = tk.Label(logs, image=k5)
    image_label.place(relx=0.23, rely=0.20)
    Riekstiem_un_sīrupu_kastē = k5

    cena_Riekstiem_un_sīrupu_kastē = 2.25
    cena_text_RSkastē = tk.Label(text=f"Cena: €{cena_Riekstiem_un_sīrupu_kastē:.2f}", font=("Arial", 12))
    cena_text_RSkastē.place(relx=0.345, rely=0.33)
    daudzums_RSkastē = tk.Label(text="0", font=("Arial", 12))
    daudzums_RSkastē.place(relx=0.268, rely=0.329)
    Riekstiem_un_sīrupu_kastē = ProductController(daudzums_RSkastē, cart_manager, "Saldē. ar riekstiem un sīrupu (kastē)", cena_Riekstiem_un_sīrupu_kastē)

    plus_RSkastē = tk.Button(text="+", width=3, command=lambda: Riekstiem_un_sīrupu_kastē.update_amount(1))
    plus_RSkastē.place(relx=0.29, rely=0.329)
    minus_RSkastē = tk.Button(text="-", width=3, command=lambda: Riekstiem_un_sīrupu_kastē.update_amount(-1))
    minus_RSkastē.place(relx=0.24, rely=0.329)

    # PRODUKTS 6

    image_label = tk.Label(logs, image=k6)
    image_label.place(relx=0.44, rely=0.20)
    Šokolādi_un_vaniļu_kastē = k6

    cena_Šokolādi_un_vaniļu_kastē = 2.25
    cena_text_ŠVkastē = tk.Label(text=f"Cena: €{cena_Šokolādi_un_vaniļu_kastē:.2f}", font=("Arial", 12))
    cena_text_ŠVkastē.place(relx=0.555, rely=0.33)
    daudzums_ŠVkastē = tk.Label(text="0", font=("Arial", 12))
    daudzums_ŠVkastē.place(relx=0.477, rely=0.329)
    Šokolādi_un_vaniļu_kastē = ProductController(daudzums_ŠVkastē, cart_manager, "Saldē. ar šokolādi un vaniļu (kastē)", cena_Šokolādi_un_vaniļu_kastē)

    plus_ŠVkastē = tk.Button(text="+", width=3, command=lambda: Šokolādi_un_vaniļu_kastē.update_amount(1))
    plus_ŠVkastē.place(relx=0.5, rely=0.329)
    minus_ŠVkastē = tk.Button(text="-", width=3, command=lambda: Šokolādi_un_vaniļu_kastē.update_amount(-1))
    minus_ŠVkastē.place(relx=0.45, rely=0.329)

    cart_frame.lift()

    logs.mainloop()

if __name__== '__main__':
    saldējumi_page()