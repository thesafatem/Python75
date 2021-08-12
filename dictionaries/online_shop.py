shop = {}

while True:
    role = input("Please, enter your role\n")
    if role == 'admin':
        while True:
            option = int(input("1 to add items\n2 to change role\n"))
            if option == 1:
                name = input("Please, enter item name\n")
                price = int(input("Please, enter item price\n"))
                amount = int(input("Please, enter item amount\n"))
                shop[name] = {
                    'price': price,
                    'amount': amount
                }
                print(shop)
            elif option == 2:
                break
    elif role == 'customer':
        cart = {}
        while True:
            print("Name\tPrice\tAmount")
            for name in shop:
                print(f'{name}\t{shop[name]["price"]}\t{shop[name]["amount"]}')
            option = int(input("1 to add item\n2 to buy\n3 to change role\n"))
            if option == 1:
                name = input("Please, enter item name\n")
                amount = int(input("Please, enter item amount\n"))
                if cart.get(name) is None:
                    if amount > shop[name]['amount']:
                        print("Amount exceeded")
                    else:
                        cart[name] = {
                            'price': shop[name]['price'],
                            'amount': amount
                        }
                else:
                    if amount + cart[name]['amount'] > shop[name]['amount']:
                        print("Amount exceeded")
                    else:
                        cart[name]['amount'] += amount
            elif option == 2:
                total = 0
                for name in cart:
                    total += cart[name]['price'] * cart[name]['amount']
                    shop[name]['amount'] -= cart[name]['amount']
                    if shop[name]['amount'] == 0:
                        del shop[name]
                print(f"Total: {total}")
                cart.clear()
            elif option == 3:
                break