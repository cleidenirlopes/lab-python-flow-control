# Exercise: Managing Customer Orders

# Step 1: Define the list of products
products = ["t-shirt", "mug", "hat", "book", "keychain"]

# Step 2: Create an empty dictionary for inventory
dict_inventory = {}

# Loop through each product to ask for quantities
for product in products:
    while True:
        try:
            # Ask the user to input the quantity of each product
            quantity = int(input(f"What is the quantity of {product}: "))
            # Store the quantity of a product inside the inventory dictionary
            dict_inventory[product] = quantity
            break  # Exit the loop if a valid quantity is entered
        except ValueError:
            print("Please enter a valid number.")

# Create an empty set for customer orders
customer_orders = set()

# Loop to allow customers to add products to the order
while True:
    order = input("What is the product that customer wants to order? ").lower()
    if order in products:
        customer_orders.add(order)  # Add valid orders to the set
        another = input("Do you want to add another product? (yes/no): ").strip().lower()
        if another != 'yes':
            break  # Exit the loop if the user does not want to add more products
    else:
        print("Invalid product, please choose from the list.")

# Print the customer orders
print("\nCustomer orders:", customer_orders)

# Calculate order statistics
total_products_ordered = len(customer_orders)  # Calculate total unique products ordered
percentage_ordered = (total_products_ordered / len(products)) * 100  # Calculate percentage
order_status = (total_products_ordered, percentage_ordered)  # Create a tuple for order status

# Print the order statistics
print("Order Statistics:")
print(f"Total Products Ordered: {total_products_ordered}")  # Total ordered products
print(f"Percentage of Products Ordered: {percentage_ordered:.2f}%")  # Formatted percentage to 2 decimal places

# Update the inventory by subtracting 1 from the quantity of each product in customer orders
for product in customer_orders:
    if product in dict_inventory and dict_inventory[product] > 0:  # Check if the product exists in inventory
        dict_inventory[product] -= 1  # Subtract 1 from the inventory
    else:
        print(f"{product} not found in inventory or out of stock.")  # Handle case if product is not found or out of stock

# Print the updated inventory
print("\nUpdated Inventory:")
for product, quantity in dict_inventory.items():
    print(f"{product}: {quantity} units available")  # Display each product and its quantity