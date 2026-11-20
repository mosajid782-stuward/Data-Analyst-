import csv
import json
from datetime import datetime

# ==========================================
# T1: Load and clean the CSV
# ==========================================
records = []
skipped = []

with open("sales_raw.csv", mode="r", newline="", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        # Check for missing quantity
        if row["quantity"].strip() == "":
            skipped.append(row["order_id"].strip())
            continue
        
        # Clean and type-cast fields
        row["order_id"] = row["order_id"].strip()
        row["store"] = row["store"].strip().title()
        row["product"] = row["product"].strip()
        row["payment_mode"] = row["payment_mode"].strip()
        row["quantity"] = int(row["quantity"].strip())
        row["unit_price"] = float(row["unit_price"].strip())
        
        records.append(row)

print("--- T1: Data Loading ---")
print(f"Rows loaded: {len(records)}")
print(f"Rows skipped: {len(skipped)} (Order IDs: {', '.join(skipped)})\n")


# ==========================================
# T2: Collections (Dicts, Sets, Sorted Tuples)
# ==========================================
# (a) Dictionary of revenue per store
store_revenue = {}
for r in records:
    store = r["store"]
    rev = r["quantity"] * r["unit_price"]
    store_revenue[store] = store_revenue.get(store, 0.0) + rev

# (b) Sets of unique products and stores
unique_products = {r["product"] for r in records}
unique_stores = {r["store"] for r in records}

# (c) List of (store, revenue) tuples sorted descending by revenue
sorted_store_revenue = sorted(store_revenue.items(), key=lambda x: x[1], reverse=True)

print("--- T2: Collections ---")
print(f"Unique stores ({len(unique_stores)}): {sorted(unique_stores)}")
print(f"Unique products ({len(unique_products)}): {sorted(unique_products)}")
print("Store Revenue (Descending):", sorted_store_revenue, "\n")


# ==========================================
# T3: List & Dictionary Comprehensions
# ==========================================
# List comprehension: order_ids paid by UPI
upi_orders = [r["order_id"] for r in records if r["payment_mode"].upper() == "UPI"]

# Dictionary comprehension: product -> total quantity
product_quantities = {
    prod: sum(r["quantity"] for r in records if r["product"] == prod)
    for prod in unique_products
}

print("--- T3: Comprehensions ---")
print(f"UPI Orders ({len(upi_orders)}): {', '.join(upi_orders)}")
print("Product Quantities:", product_quantities, "\n")


# ==========================================
# T4: Write Report & Append Run Log
# ==========================================
total_revenue = sum(store_revenue.values())

# Write store_report.txt (mode 'w')
with open("store_report.txt", mode="w", encoding="utf-8") as f:
    f.write("RetailPulse Store-Wise Revenue Report\n")
    f.write("=" * 40 + "\n")
    for store, rev in sorted_store_revenue:
        f.write(f"{store:<15}: Rs. {rev:,.2f}\n")
    f.write("-" * 40 + "\n")
    f.write(f"{'Total Revenue':<15}: Rs. {total_revenue:,.2f}\n")

# Append timestamped line to run_log.txt (mode 'a')
timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
with open("run_log.txt", mode="a", encoding="utf-8") as f:
    f.write(f"[{timestamp}] Processed {len(records)} records, skipped {len(skipped)}. Total Revenue: Rs. {total_revenue:,.2f}\n")

print("--- T4: Report Files ---")
print("Saved 'store_report.txt' and appended to 'run_log.txt'.\n")


# ==========================================
# T5: JSON Serialization & Exception Handling
# ==========================================
summary_data = {
    "rows_loaded": len(records),
    "rows_skipped": skipped,
    "unique_stores_count": len(unique_stores),
    "unique_products_count": len(unique_products),
    "total_revenue": total_revenue,
    "revenue_by_store": dict(sorted_store_revenue),
    "product_quantities": product_quantities,
    "upi_orders": upi_orders
}

# Save to summary.json
with open("summary.json", mode="w", encoding="utf-8") as f:
    json.dump(summary_data, f, indent=4)

# Read back from summary.json
with open("summary.json", mode="r", encoding="utf-8") as f:
    loaded_summary = json.load(f)

print("--- T5: JSON & Error Handling ---")
print(f"Successfully verified summary.json (Loaded Total Revenue: Rs. {loaded_summary['total_revenue']:,.2f})")

# Attempt to open a missing file with try / except / finally
try:
    with open("sales_missing.csv", mode="r", encoding="utf-8") as f:
        data = f.read()
except FileNotFoundError as e:
    print(f"Handled Expected Error: Could not find 'sales_missing.csv' ({e})")
finally:
    print("File check routine completed.")