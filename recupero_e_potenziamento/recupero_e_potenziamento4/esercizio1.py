import math

def calculateCharges(num_ore: float) -> str:
    # costo parte sempre da 2 
    costo: int = 2
    if num_ore <= 3:
        return f'2.00$'

    elif num_ore == 24:
        return f'10.00$'
    # arrotonda sempre per eccesso
    num_ore = math.ceil(num_ore)

    # aggiungo le ore in eccesso pagate 0.5 all'ora
    costo += (num_ore - 3) * 0.5
    return f'{costo}$'

print(calculateCharges(5.1))

# la lunghezza della lista sono le macchine il valori sono le ore di sosta
car: list[float] = [1.5, 4.0, 5.50, 24.0]


def print_tabella(car: list[float]) -> None:

    print(f'{'Car':<10} {'Hours':<10} {'Charge':<10}')

    for i in range(len(car)):
        totale = 0

        a = calculateCharges(car[i])
        print(f'{i + 1:<10} {car[i]:<10} {a:<10}')
        totale += a
    
    print(f'{'TOTAL':<10} {sum(car):<10} {a:<10}')


print_tabella(car)


