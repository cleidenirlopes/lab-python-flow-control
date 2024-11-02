# lab-python-functions.ipynb
def initialize_inventory(products):
    inventory = {}
    for product in products:
        quantity = int(input(f"Enter quantity for {product}: "))
        price = float(input(f"Enter price for {product}: "))
        inventory[product] = {"quantity": quantity, "price": price}
    return inventory

# 2. Function to get customer orders and store them in a set
def get_customer_orders():
    customer_orders = set()
    print("\nEnter the products the customer wants to order (type 'done' to finish):")
    while True:
        product = input("Enter product name: ").strip()
        if product.lower() == 'done':
            break
        elif product:
            customer_orders.add(product)
        else:
            print("Please enter a valid product name.")
    return customer_orders

# Main function to initialize inventory and get customer orders
def main():
    # List of products available in the store
    products = ["Laptop", "Phone", "Headphones", "Charger", "Keyboard"]
    
    # Initialize inventory with user input
    inventory = initialize_inventory(products)
    
    # Print the initialized inventory to confirm it works
    print("\nInitialized Inventory:")
    for product, details in inventory.items():
        print(f"{product}: Quantity = {details['quantity']}, Price = ${details['price']:.2f}")

    # Get customer orders
    customer_orders = get_customer_orders()
    
    # Print the customer orders to verify
    print("\nCustomer Orders:")
    for order in customer_orders:
        print(order)
        
# 3. Function to update the inventory based on customer orders
def update_inventory(customer_orders, inventory):
    for product in customer_orders:
        if product in inventory:
            while True:
                try:
                    quantity = int(input(f"Enter quantity for {product} in order: "))
                    if quantity <= 0:
                        print("Order quantity should be positive. Please enter a valid quantity.")
                    elif inventory[product]["quantity"] >= quantity:
                        inventory[product]["quantity"] -= quantity
                        print(f"{quantity} of {product} sold, new inventory: {inventory[product]['quantity']}")
                        break
                    else:
                        print(f"Not enough {product} in inventory. Only {inventory[product]['quantity']} available.")
                        break
                except ValueError:
                    print("Please enter a valid integer for quantity.")
        else:
            print(f"{product} is not in inventory.")
    return inventory

# 4. Function to calculate order statistics
def calculate_order_statistics(customer_orders, products):
    total_products_ordered = len(customer_orders)
    unique_percentage = (total_products_ordered / len(products)) * 100
    return total_products_ordered, unique_percentage

# 5. Function to print order statistics
def print_order_statistics(order_statistics):
    total_products_ordered, unique_percentage = order_statistics
    print("\nOrder Statistics:")
    print(f"Total Products Ordered: {total_products_ordered}")
    print(f"Percentage of Unique Products Ordered: {unique_percentage:.2f}%")

# 6. Function to print the updated inventory
def print_updated_inventory(inventory):
    print("\nUpdated Inventory:")
    for product, details in inventory.items():
        print(f"{product}: Quantity = {details['quantity']}, Price = ${details['price']:.2f}")

# 7. Main code to call functions in the appropriate sequence
def main():
    # List of products available in the store
    products = ["Laptop", "Phone", "Headphones", "Charger", "Keyboard"]
    
    # Initialize inventory with user input
    inventory = initialize_inventory(products)
    
    # Get customer orders
    customer_orders = get_customer_orders()
    
    # Update inventory based on customer orders
    inventory = update_inventory(customer_orders, inventory)
    
    # Calculate order statistics
    order_statistics = calculate_order_statistics(customer_orders, products)
    
    # Print order statistics
    print_order_statistics(order_statistics)
    
    # Print the updated inventory
    print_updated_inventory(inventory)

# Run the main function to execute the program
main()

