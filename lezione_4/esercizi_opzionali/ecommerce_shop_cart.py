def product(name: str, price: float, quantity: int) -> dict:

    return {'Name': name, 'Price': price, 'Quantity': quantity}


shopping_cart: list[dict] = []

def add_item(prodotto: dict) -> None:
    
    for elem in shopping_cart:

        if prodotto['Name'] == elem['Name']:

            print('Prodotto gia presente nel carrello')
            scelta = str(input('Aggiungere +1 al carrello? S/n: '))

            if scelta.lower() == 's':

                elem['Quantity'] += 1

            elif scelta.lower() == 'n':

                print('ok')

            else:

                raise ValueError('Inserire S/n!!')
            
            return None
    
    shopping_cart.append(prodotto)


def remove_prodotto(nome_prodotto: str) -> None:

    for elem in shopping_cart:

        if nome_prodotto == elem['Name']:

            if elem['Quantity'] <= 1:

                shopping_cart.remove(elem)

            else:

                elem['Quantity'] -= 1


            return None
    
    print('IL prodotto non e presente ne carrello')

def view_products() -> list[dict]:

    return shopping_cart


def cart_tot(carrello: list[dict],  discount: int = 0) -> float:
    tot: int =  0
    for elem in carrello:

        tot = elem['Price'] * elem['Quantity'] 

    if discount > 0:

        tot = tot - (tot * discount) / 100

    return f'{tot:.t2f}'

p1 = product("Mela", 0.5, 2)
add_item(p1)
p2 = product("Banana", 0.3, 3)
add_item(p2)
print(view_products())
print(cart_tot(shopping_cart, discount=10))  # Applica 10% di sconto







        
            


                
