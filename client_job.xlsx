import pandas as pd

# 1. Open and read the client's raw text file (using "r" for read mode)
with open("raw_data.txt", "r", encoding="utf-8") as file:
    lines = file.readlines()

products = []
prices = []
statuses = []

# 2. Loop through each line and clean up the text
for line in lines:
    if line.strip():  # Skip empty lines
        # Split the text by the pipeline symbol "|"
        parts = line.split("|")
        
        # Clean up each individual piece of data using index numbers [0], [1], [2]
        product = parts[0].replace("ITEM:", "").strip()
        price = parts[1].replace("COST:", "").replace("USD", "").strip()
        status = parts[2].replace("AVAILABILITY:", "").strip()
        
        # Add the cleaned data to our lists
        products.append(product)
        prices.append(price)
        statuses.append(status)

# 3. Structure the data using the exact headers the client requested
final_data = {
    "Product": products,
    "Price": prices,
    "Status": statuses
}

# 4. Save it as an Excel file
df = pd.DataFrame(final_data)
df.to_excel("client_delivery.xlsx", index=False)

print("✅ Success! 'client_delivery.xlsx' has been created. Ready for delivery.")
