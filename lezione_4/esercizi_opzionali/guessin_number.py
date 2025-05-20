import random
def random_number(n1: int, n2: int) -> int:

    return random.randint(n1, n2)


x: int = random_number(1, 20)
counter: int = 0
print(x)
while counter <= 5:

    guess= int(input('Inserire numero: '))

    if guess == x:

        print('Numero corretto!')
        break
    
    counter += 1
    

