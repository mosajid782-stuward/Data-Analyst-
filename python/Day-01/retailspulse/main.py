"""Main script demonstrating RetailPulse Day 2 billing library and OOP models."""

import math
from datetime import datetime
from billing import generate_invoice
from models import Product, Order, PremiumOrder


def main():
    """Run demonstrations for Tasks T1 through T6 and verify self-check values."""
    print("=" * 55)
    print("1. FLEXIBLE INVOICE, LAMBDA SORT & MATH/DATETIME (T1-T3)")
    print("=" * 55)

    invoice = generate_invoice(
        "Aarav Sharma",
        ("Notebook Pack", 3, 150),
        ("Wireless Mouse", 2, 799),
        ("USB-C Cable", 1, 299),
        gst_rate=0.18,
        currency="INR",
    )

    invoice_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    rounded_payable = math.ceil(invoice["grand_total"])

    print(f"Customer     : {invoice['customer']}")
    print(f"Invoice Date : {invoice_date}")
    print("Sorted Items (Descending by line total):")
    for line in invoice["lines"]:
        print(f"  - {line['product']}: {line['qty']} x {line['unit_price']} = {line['line_total']}")
    print(f"Grand Total  : {invoice['grand_total']} {invoice['currency']}")
    print(f"Payable (ceil): {rounded_payable} {invoice['currency']}")

    print("\n" + "=" * 55)
    print("2. OOP CLASSES, INHERITANCE & POLYMORPHISM (T4-T5)")
    print("=" * 55)

    mouse = Product("Wireless Mouse", "Electronics", 799, stock=10)
    print("Product Info :", mouse)

    # Self-check 1 & 2: Order vs PremiumOrder
    std_order = Order(101, mouse, 2)
    prem_order = PremiumOrder(102, mouse, 2)

    print(f"Standard Order Total (Expected 1885.64) : {std_order.total()}")
    print(f"Premium Order Total  (Expected 1829.07) : {prem_order.total()}")

    # Polymorphism demo on a mixed list
    print("\nPolymorphism Demo (Mixed Orders):")
    orders = [std_order, prem_order]
    for o in orders:
        print(f"  Order #{o.order_id} ({type(o).__name__}) -> Total: {o.total()}")

    # Classmethod from_row() demo
    row_data = {"order_id": 1001, "product": mouse, "quantity": 2}
    row_order = Order.from_row(row_data)
    print(f"\nCreated via from_row() -> Order #{row_order.order_id}, Total: {row_order.total()}")

    print("\n" + "=" * 55)
    print("3. ENCAPSULATION & EXCEPTION HANDLING (T6)")
    print("=" * 55)

    print(f"Initial Stock: {mouse.stock}")
    mouse.reduce_stock(4)
    print(f"Stock after reducing 4: {mouse.stock}")

    try:
        print("Attempting to reduce stock by 10 (exceeds available stock)...")
        mouse.reduce_stock(10)
    except ValueError as e:
        print(f"Caught Expected Error -> {e}")

    print(f"Final Stock (must remain unchanged at 6): {mouse.stock}")


if __name__ == "__main__":
    main()