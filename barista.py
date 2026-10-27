class MenuItem:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class Order:
    def __init__(self):
        self.receipt = []

    def add_item(self, item):
        self.receipt.append(item)

    def calculate_total(self):
        return sum(item.price for item in self.receipt)

    def calculate_taxes(self, tax_rate=0.07):
        return self.calculate_total() * tax_rate

    def print_reciept(self):
        print("\nCROSSROADS CAFE")
        print("------------------")
        for item in self.receipt:
            print(f"{item.name:<10} ${item.price:.2f}")
        
        subtotal = self.calculate_total()
        taxes = self.calculate_taxes()
        grand_total = subtotal + taxes
        
        print("------------------")
        print(f"tax:       ${taxes:.2f}")
        print("------------------")
        print(f"the total due is ${grand_total:.2f}\n")

def main():
    menu = [
        MenuItem("bagel", 3.00),
        MenuItem("burrito", 5.00),
        MenuItem("ramen", 1.50),
        MenuItem("gum", 0.50)
    ]
        
    order1 = Order()
    order1.add_item(menu[1]) #burrito
    order1.add_item(menu[1]) #burrito
    order1.add_item(menu[3]) #gum
        
    subtotal = order1.calculate_total()
    taxes = order1.calculate_taxes()
    total = subtotal + taxes
    
        
    order1.print_reciept()

if __name__ == '__main__':
    main()


