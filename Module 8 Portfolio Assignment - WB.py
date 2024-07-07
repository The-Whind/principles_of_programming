# Define the ItemToPurchase class
class ItemToPurchase:
    # The constructor sets up the item's details
    def __init__(self, item_name="none", item_price=0.0, item_quantity=0, item_description="none"):
        self.item_name = item_name
        self.item_price = item_price
        self.item_quantity = item_quantity
        self.item_description = item_description

    # Method to print the cost of the item
    def print_item_cost(self):
        total_cost = self.item_price * self.item_quantity
        print(self.item_name + " " + str(self.item_quantity) + " @ $" + str(self.item_price) + " = $" + str(total_cost))


# Define the ShoppingCart class
class ShoppingCart:
    # Constructor initializes the shopping cart's attributes
    def __init__(self, customer_name="none", current_date="January 1, 2020"):
        self.customer_name = customer_name
        self.current_date = current_date
        self.cart_items = []

    # Method to add an item to the cart
    def add_item(self, item):
        self.cart_items.append(item)

    # Method to remove an item from the cart by name
    def remove_item(self, item_name):
        item_removed = False
        for item in self.cart_items:
            if item.item_name == item_name:
                self.cart_items.remove(item)
                item_removed = True
                break
        if not item_removed:
            print("Item not found in cart. Nothing removed.")

    # Method to modify an existing item's details
    def modify_item(self, item):
        item_modified = False
        for cart_item in self.cart_items:
            if cart_item.item_name == item.item_name:
                if item.item_description != "none":
                    cart_item.item_description = item.item_description
                if item.item_price != 0.0:
                    cart_item.item_price = item.item_price
                if item.item_quantity != 0:
                    cart_item.item_quantity = item.item_quantity
                item_modified = True
                break
        if not item_modified:
            print("Item not found in cart. Nothing modified.")

    # Method to get the total number of items in the cart
    def get_num_items_in_cart(self):
        total_quantity = 0
        for item in self.cart_items:
            total_quantity += item.item_quantity
        return total_quantity

    # Method to get the total cost of all items in the cart
    def get_cost_of_cart(self):
        total_cost = 0.0
        for item in self.cart_items:
            total_cost += item.item_price * item.item_quantity
        return total_cost

    # Method to print the total cost of the cart
    def print_total(self):
        print("OUTPUT SHOPPING CART")
        print(self.customer_name + "'s Shopping Cart - " + self.current_date)
        if not self.cart_items:
            print("SHOPPING CART IS EMPTY")
        else:
            print("Number of Items: " + str(self.get_num_items_in_cart()))
            for item in self.cart_items:
                item.print_item_cost()
            print("Total: $" + str(self.get_cost_of_cart()))

    # Method to print the descriptions of all items in the cart
    def print_descriptions(self):
        print("OUTPUT ITEMS' DESCRIPTIONS")
        print(self.customer_name + "'s Shopping Cart - " + self.current_date)
        print("Item Descriptions")
        for item in self.cart_items:
            print(item.item_name + ": " + item.item_description)


# Function to display the menu and process user input
def print_menu(shopping_cart):
    while True:
        print("\nMENU")
        print("a - Add item to cart")
        print("r - Remove item from cart")
        print("c - Change item quantity")
        print("i - Output items' descriptions")
        print("o - Output shopping cart")
        print("q - Quit")
        choice = input("Choose an option: ")

        if choice == 'a':
            # Add item to cart
            item_name = input("Enter the item name: ")
            item_price = float(input("Enter the item price: "))
            item_quantity = int(input("Enter the item quantity: "))
            item_description = input("Enter the item description: ")
            item = ItemToPurchase(item_name, item_price, item_quantity, item_description)
            shopping_cart.add_item(item)
        elif choice == 'r':
            # Remove item from cart
            item_name = input("Enter the name of the item to remove: ")
            shopping_cart.remove_item(item_name)
        elif choice == 'c':
            # Change item quantity
            item_name = input("Enter the name of the item to change: ")
            new_quantity = int(input("Enter the new quantity: "))
            item = ItemToPurchase(item_name=item_name, item_quantity=new_quantity)
            shopping_cart.modify_item(item)
        elif choice == 'i':
            # Output items' descriptions
            shopping_cart.print_descriptions()
        elif choice == 'o':
            # Output shopping cart
            shopping_cart.print_total()
        elif choice == 'q':
            # Quit
            break
        else:
            print("Choose a valid option.")


# Main function to start the program
def main():
    # Prompt for customer's name and date
    customer_name = input("Enter customer's name: ")
    current_date = input("Enter today's date: ")
    print("Customer name: " + customer_name)
    print("Today's date: " + current_date)

    # Create a ShoppingCart object with the customer's name and date
    shopping_cart = ShoppingCart(customer_name, current_date)
    # Display the menu and process user input
    print_menu(shopping_cart)


# Run the main function when the script starts
if __name__ == "__main__":
    main()
