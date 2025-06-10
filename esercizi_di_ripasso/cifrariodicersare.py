from string import ascii_lowercase, ascii_uppercase

def caesar_cypher_encrypt(s: str, key: int) ->  str:

    frase: str = ''
    for letter in s:

        if letter in ascii_lowercase:

            frase += ascii_lowercase[(ascii_lowercase.index(letter) + key) % len(ascii_lowercase)]

        elif letter in ascii_uppercase:

            frase += ascii_uppercase[(ascii_uppercase.index(letter) + key) % len(ascii_uppercase)]

        else:
            frase += letter

    return frase

print(caesar_cypher_encrypt('z5', 2))

