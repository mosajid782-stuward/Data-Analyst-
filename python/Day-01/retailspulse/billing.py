"""Billing module containing core calculation and invoice generation functions."""


def calculate_subtotal(quantity, unit_price):
    """Calculate the subtotal before discount and tax."""
    return quantity * unit_price


def apply_discount(subtotal):
    """Return the discount amount based on subtotal slabs.
    
    Slabs:
    - Above 5000: 10%
    - Above 2000: 5%
    - Otherwise: 0%
    """
    if subtotal > 5000:
        return subtotal * 0.10
    elif subtotal > 2000:
        return subtotal * 0.05
    return 0.0


def calculate_gst(amount, rate=0.18):
    """Calculate GST on the given amount with a default rate of 18%."""
    return amount * rate


def generate_invoice(customer, *items, **options):
    """Generate a structured invoice dictionary from variable items and options.

    Args:
        customer (str): Name of the customer.
        *items: Tuples of (product_name, quantity, unit_price).
        **options: Optional keyword arguments like 'gst_rate' and 'currency'.

    Returns:
        dict: Invoice details including sorted lines, subtotal, discount, GST, and grand total.
    """
    gst_rate = options.get("gst_rate", 0.18)
    currency = options.get("currency", "INR")

    invoice_lines = []
    raw_subtotal = 0.0

    for product, qty, price in items:
        line_total = calculate_subtotal(qty, price)
        raw_subtotal += line_total
        invoice_lines.append({
            "product": product,
            "qty": qty,
            "unit_price": price,
            "line_total": round(line_total, 2),
        })

    # T3 requirement: Sort invoice lines by line_total in descending order using lambda
    invoice_lines = sorted(invoice_lines, key=lambda x: x["line_total"], reverse=True)

    discount = apply_discount(raw_subtotal)
    discounted_amount = raw_subtotal - discount
    gst_amount = calculate_gst(discounted_amount, rate=gst_rate)
    grand_total = discounted_amount + gst_amount

    return {
        "customer": customer,
        "currency": currency,
        "lines": invoice_lines,
        "subtotal": round(raw_subtotal, 2),
        "discount": round(discount, 2),
        "gst": round(gst_amount, 2),
        "grand_total": round(grand_total, 2),
    }