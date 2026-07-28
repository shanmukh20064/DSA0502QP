import pandas as pd
# Read CSV file
df = pd.read_csv("orders.csv")
# Find duplicate Order IDs
duplicates = df[df.duplicated(subset="OrderID", keep=False)]
print("Duplicate Orders:")
print(duplicates)
# Remove duplicate orders and create a copy
df_clean = df.drop_duplicates(subset="OrderID").copy()
print("\nAfter Removing Duplicates:")
print(df_clean)
# Calculate Total Order Amount
df_clean["TotalAmount"] = df_clean["Quantity"] * df_clean["Price"]
print("\nOrders with Total Amount:")
print(df_clean)
print("\nTotal Sales =", df_clean["TotalAmount"].sum())
# Customer with highest purchase value
customer_total = df_clean.groupby("Customer")["TotalAmount"].sum()
highest_customer = customer_total.idxmax()
highest_amount = customer_total.max()
print("\nCustomer with Highest Purchase Value:")
print(highest_customer, "-", highest_amount)
# Save cleaned dataset
df_clean.to_csv("clean_orders.csv", index=False)
print("\nCleaned dataset saved as clean_orders.csv")