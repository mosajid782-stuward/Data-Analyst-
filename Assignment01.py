# Day 1 - Billing Engine for RetailPulse
# Name: ________   Roll No: ________
 
import math
 
# ---------- T1: Variables and types ----------
order_id = 101
product = "Wireless Mouse"
quantity = 2
unit_price = 799.0
is_cancelled = False
 
print("----- T1 -----")
print(f"order_id = {order_id}, type = {type(order_id)}")
print(f"product = {product}, type = {type(product)}")
print(f"quantity = {quantity}, type = {type(quantity)}")
print(f"unit_price = {unit_price}, type = {type(unit_price)}")
print(f"is_cancelled = {is_cancelled}, type = {type(is_cancelled)}")

 
# ---------- T2: Operators ----------
print("\n----- T2 -----")
subtotal = quantity * unit_price
gst = subtotal * 18 / 100
final = round(subtotal + gst, 2)
print("Subtotal =", subtotal)
print("GST =", gst)
print("Final amount =", final)
 
# 100 notebooks in cartons of 12
cartons = 100 // 12
loose = 100 % 12
print(f"100 notebooks = {cartons} cartons + {loose} loose units")
 
# float problem
print(0.1 + 0.2 == 0.3)                      # False
print(round(0.1 + 0.2, 2) == 0.3)            # True after round()
print(math.isclose(0.1 + 0.2, 0.3))          # True using isclose()