"""Models module defining Product, Order, and PremiumOrder classes."""

from billing import calculate_subtotal, apply_discount, calculate_gst


class Product:
    """Represents a retail product with encapsulated stock management."""

    def __init__(self, name, category, unit_price, stock=0):
        """Initialize a Product instance."""
        self.name = name
        self.category = category
        self.unit_price = unit_price
        self.__stock = stock  # Private attribute (Encapsulation)

    @property
    def stock(self):
        """Read-only property to access current stock."""
        return self.__stock

    def reduce_stock(self, qty):
        """Reduce stock by qty; raise ValueError if stock is insufficient."""
        if qty > self.__stock:
            raise ValueError(
                f"Insufficient stock for '{self.name}'. Available: {self.__stock}, Requested: {qty}"
            )
        self.__stock -= qty

    def __str__(self):
        """Return a readable string representation of the product."""
        return f"{self.name} ({self.category}) - ₹{self.unit_price:.2f} [Stock: {self.__stock}]"


class Order:
    """Represents a standard customer order."""

    def __init__(self, order_id, product, quantity):
        """Initialize an Order instance."""
        self.order_id = order_id
        self.product = product
        self.quantity = quantity

    def total(self):
        """Calculate the final payable total (after slab discount + 18% GST)."""
        subtotal = calculate_subtotal(self.quantity, self.product.unit_price)
        discount = apply_discount(subtotal)
        taxable_amount = subtotal - discount
        gst = calculate_gst(taxable_amount)
        return round(taxable_amount + gst, 2)

    @classmethod
    def from_row(cls, row):
        """Create an Order instance from a dictionary row."""
        return cls(
            order_id=row["order_id"],
            product=row["product"],
            quantity=row["quantity"],
        )


class PremiumOrder(Order):
    """Represents a premium customer order with an extra 3% discount before GST."""

    def total(self):
        """Override total() to apply an extra 3% discount on subtotal before GST."""
        subtotal = calculate_subtotal(self.quantity, self.product.unit_price)
        base_discount = apply_discount(subtotal)
        extra_discount = subtotal * 0.03  # Extra 3% discount before GST
        taxable_amount = subtotal - (base_discount + extra_discount)
        gst = calculate_gst(taxable_amount)
        return round(taxable_amount + gst, 2)