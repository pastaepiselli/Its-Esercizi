def atm() -> None:

    bilancio: float = 1000.00

    scelta: str = ''
    while scelta.lower() != 'exit':

        scelta = str(input('Input a command (deposit, withdraw or check balance): '))


        if scelta.lower() == 'deposit':

            ammount = float(input('Insert a number for the deposit: '))

            bilancio += ammount
            print(f'Sono stati depositati correttamente {ammount}$, il bilancio totale sale a {bilancio}$')

        elif scelta.lower() == 'withdraw':

            ritiro = float(input('Insert a number for the withdraw: '))

            if bilancio - ritiro > 0:

                bilancio -= ritiro
                print(f'Sono stati ritirati correttamente {ritiro}$, bilancio corrente {bilancio}$')

            else:

                print(f'Non si possono ritirare {ritiro}$, bilancio corrente {bilancio}$')

            
        elif scelta.lower() == 'view':

            print(f'Il bilancio attuale e di {bilancio}$')

        else:

            print('Insert a valid option')


atm()
