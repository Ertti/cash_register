class CartData:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(CartData, cls).__new__(cls)
            cls._instance.cart = {}  # Initialize the cart dictionary.
        return cls._instance

    def update(self, product, qty, price):
        """Update or add a product in the cart."""
        self.cart[product] = {"qty": qty, "price": price}

    def get_cart(self):
        """Return the current cart data."""
        return self.cart