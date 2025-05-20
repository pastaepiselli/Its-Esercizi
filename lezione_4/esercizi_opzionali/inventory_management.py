inventory: list[dict] = []



def item(code: int, name: str, quantity: int, price: float) -> dict:

    return {'Code': code, 'Name': name, 'Quantity': quantity, 'Price': price}

def add_item(item: dict) -> None:
    aggiunto: bool = False
    for elem in inventory:

        if elem['Code'] == item['Code']:
            aggiunto = True
            print('Oggetto gia presente, aggiungo scorte? S/n')

            scelta = str(input(''))

            if scelta.lower() == 's':

                elem['Quantity'] += item['Quantity']
                print(f'Aggiunti {item['Quantity']} oggetti, per un totale di {elem["Quantity"]}')

            elif scelta.lower() == 'no':

                print('ok')

            else:

                raise ValueError('Inserire un valore valido! S/n')
        
    if not aggiunto:
        inventory.append(item)
        print('Oggetto aggiunto correttamente!')
            
def remove_item(item: dict) -> None:
    rimosso: bool = False
    for elem in inventory:

        if elem['Code'] == item['Code']:
            rimosso = True
            inventory.remove(elem)
            print('Oggetto rimosso correttamente')


    if not rimosso:

        print('Oggetto non presente, aggiungerlo? S/n')

        scelta = str(input(''))

        if scelta.lower() == 's':

                add_item(item)

        elif scelta.lower() == 'n':

            print('ok')

        else:

            raise ValueError('Inserire un valore valido tra S/n')
            
def search(item: dict) -> None:
    trovato : bool =  False
    for elem in inventory:

        if elem['Code'] == item['Code']:

            print(f'Oggetto troavato: {elem}')
            trovato = True
            break

    if not trovato:

        print('Oggetto non trovatol, Aggiungerlo?: S/n')

        scelta = str(input(''))
        if scelta.lower() == 's':

                add_item(item)

        elif scelta.lower() == 'n':

            print('ok')

        else:

            raise ValueError('Inserire un valore valido tra S/n')
        

def update_items():


    for elem in inventory:

        print(elem)

    print('Quale elemento vuoi aggiornare? (inserire codice)')
    aggiornamentoh: bool = False
    elemento = int(input(''))

    for elem in inventory:

        if elemento == elem['Code']:
            aggiornamentoh = True

            print('Cosa vuoi aggiornare?')

            agg = str(input('Code, Name, Quantity, Price'))


            match agg.lower():

                case 'code':

                    new_code = int(input('Inserire nuovo codice: '))

                    elem['Code'] = new_code

                case 'name':

                    new_name = str(input('Inserire nuovo nome: '))

                    elem['Name'] = new_name

                case 'quantity':

                    new_quantity = int(input('Inserire nuova quantita: '))

                    elem['Quantity'] = new_quantity

                case 'price':

                    new_price = float(input('Inserire nuovo prezzo: '))

                    elem['Price'] = new_price

                case _:

                    print('Opzione non valida       ')
    if not aggiornamentoh:

        print('L\'oggetto che stai cercando non e nella lista')








        

            





            


        
    






        