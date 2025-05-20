import random  
import string
def password_gen(length: int,  uppercase: bool, numbers: bool, symbols: bool) -> str:
    password: str = ''
    password_chr: str = ''
    uppercase_letters: list[str] = list(string.ascii_uppercase)
    numbers_list: list[int] = list(range(0, 10))
    symbols_list: list[str] = ['\\', '/' ,':' ,'*', '?', '"', '<', '>', '|']

    if uppercase:

        upp = random.choice(uppercase_letters)
        password_chr += upp

    if numbers:

        num = str(random.choice(numbers_list))
        password_chr += num

    if symbols:

        sim = random.choice(symbols_list)
        password_chr += sim

    for elem in range(length):

        password += random.choice(password_chr)

    return password
 
        
print(password_gen(12, uppercase= True, numbers= True, symbols= True))


        


