from tkinter import Label, Button
from PIL import Image, ImageTk
import tkinter as tk
from Iepirkumu_grozs import CartData

def load_test_ui(logs, screen_width, screen_height, go_to_main_kategorijas, hide_go_to_main=False):
    def resize_image(image_path, width_factor, height_factor):
        img = Image.open(image_path)
        new_width = int(screen_width * width_factor)
        new_height = int(screen_height * height_factor)
        img = img.resize((new_width, new_height), Image.LANCZOS)
        return ImageTk.PhotoImage(img)

    līni = resize_image('Main/4v.png', 0.65, 0.002)
    ATi = resize_image('Main/b.png', 0.14, 0.12)
    maki = resize_image('Main/MAKSĀT.png', 0.24, 0.12)
    sari = resize_image('Main/SAR.png', 0.3, 0.95)
    tīr = resize_image('Main/notīr.png', 0.25, 0.08)

    linl = Label(logs, image=līni)
    linl.place(relx=0, rely=0.8)

    if not hide_go_to_main:
        ATp = Button(logs, image=ATi, borderwidth=0, command=lambda:go_to_main_kategorijas(logs))
        ATp.place(relx=0.1, rely=0.83)

    makp = Button(logs, image=maki, borderwidth=0)
    makp.place(relx=0.35, rely=0.83)

    sarp = Label(logs, image=sari, borderwidth=0)
    sarp.place(relx=0.67, rely=0.01)

    notī = Button(logs, image=tīr, borderwidth=0, bg='#dadada')
    notī.place(relx=0.7, rely=0.86)

    logs.image_refs = [līni, ATi, maki, sari, tīr]

def saraksts(logs, product_count):
    def increase_count(self):
        self.product_count += 1
        self.update_label()

    def decrease_count(self):
        """Neaiziet tālāk par nulli"""
        if self.product_count > 0:
            self.product_count -= 1
        self.update_label()

    def update_label(self):
        """Atjauno daudzuma skaitu"""
        self.label.config(text={self.product_count})
    
    logs.main_info = [increase_count, decrease_count, update_label]

class CartManager:
    def __init__(self, parent):
        self.Iepirkumu_grozs = CartData()
        self.cart_label = tk.Label(parent, font=("Arial", 12), justify="center", bg='#dadada')
        self.cart_label.pack(padx=10, pady=10)
        self.refresh()
    
    def update_product(self, product, qty, price):
        self.Iepirkumu_grozs.update(product, qty, price)
        self.refresh()

    def refresh(self):
        """Atjauno iepirkumu grozu balstoties uz tā esošo saturu."""
        cart = self.Iepirkumu_grozs.get_cart()
        text = "\n"
        total = 0.0
        for product, info in cart.items():
            qty = info["qty"]
            price = info["price"]
            subtotal = qty * price
            total += subtotal
            text += f"{product}: {qty} x €{price:.2f} = €{subtotal:.2f}\n"
        text += f"\nKopā: €{total:.2f}"
        self.cart_label.config(text=text)


class ProductController:
    def __init__(self, amount_label, cart_manager, product_name, price):
        self.amount_label = amount_label
        self.cart_manager = cart_manager
        self.product_name = product_name
        self.price = price
        self.amount = 0  # Starting quantity

    def update_amount(self, delta):
        """Daudzuma maiņa"""
        self.amount = max(0, self.amount + delta)
        self.amount_label.config(text=str(self.amount))
        # Update the shared basket display via the CartManager.
        self.cart_manager.update_product(self.product_name, self.amount, self.price)
