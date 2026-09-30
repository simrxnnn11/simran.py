import pandas as pd

# We put the client data directly inside the code to make it easy!
raw_data = """
ITEM: Premium Leather Wallet | COST: 45.00 USD | AVAILABILITY: In Stock
ITEM: Ergonomic Office Chair | COST: 189.99 USD | AVAILABILITY: Out of Stock
ITEM: Stainless Steel Water Bottle | COST: 24.50 USD | AVAILABILITY: In Stock
ITEM: Bluetooth Pocket Speaker | COST: 35.00 USD | AVAILABILITY: In Stock
ITEM: Minimalist Desk Desk Mat | COST: 15.99 USD | AVAILABILITY: Out of Stock
"""

products = []
prices = []
statuses = []

# Split text by lines
lines = raw_data.strip().split("\n")

for line in lines:
    parts = line.split("|")
    
    # Extract and clean each part using indexes [0], [1], [2]
    product = parts[0].replace("ITEM:", "").strip()
    price = parts[1].replace("COST:", "").replace("USD", "").strip()
    status = parts[2].replace("AVAILABILITY:", "").strip()
    
    products.append(product)
    prices.append(price)
    statuses.append(status)

# Create the layout
final_data = {
    "Product": products,
    "Price": prices,
    "Status": statuses
}

# Save as Excel file
df = pd.DataFrame(final_data)
df.to_excel("client_delivery.xlsx", index=False)

print("🎉 Success! 'client_delivery.xlsx' has been created. Ready for delivery.")

