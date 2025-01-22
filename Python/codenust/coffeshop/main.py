class CoffeeShop:
    def __init__(self):
        self.menu = {
            "Espresso": 3.00,
            "Americano":3.50,
            "Latte": 4.00,
            "Cappucino": 4.50,
            "Mocha": 4.75
        }

        self.order = {}

    def display_menu(self):
        print("\n--- Coffee Menu ---")

        for coffee, price in self.menu.items():
            print(f"{coffee}: ${price}")

    def take_order(self):
        print("\nEnter the coffe you'd like to order (or type 'done to finish): ")
        while True:
            coffee = input("Coffe Name: ").capitalize()
            if coffee == "Done":
                break
            elif coffee in self.menu:
                quantity = int(input(f"How many {coffee}s would you like"))
                if coffee in self.order:
                    self.order[coffee] += quantity
                else:
                    self.order[coffee] = quantity
else:
            print("Sorry, we dont have that coffe, Please choose from the menu")

    def calculate_total(self):
        total = 0
        for coffee, quantity in self.order.items():
            total += self.menu[coffee] * quantity
        return total

    def print_receipt(self):
        print("\n --- Receipt ---")
        for coffee, quantity in self.order.items():
            print(f"{coffee} x{quantity} = ${self.menu[coffee] * quantity:.2f}")
    print(f"\nTotal: %{self.calculate_total():2f}")

    def main():
        coffee_shop = CoffeeShop()

        while True:

            print("\n Welcome to the Coffe Shop!")
            coffee_shop.display_menu()
            coffee_shop.take_order()
            coffee_shop.print_receipt()
            another_order = input("\nWould you like to order something else? (yes/no): ").lower()

            if another_order != "yes":
                print ("\nThank you for visiting our Coffee Shop!")
                break

    if __name__ == "__main__":
        main()
