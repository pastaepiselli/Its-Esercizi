from string import ascii_lowercase

def caesar_cypher_encrypt(s: str, key: int) ->  str:

    frase: str = ''
    for letter in s:

        if letter in ascii_lowercase:

            frase += ascii_lowercase[ascii_lowercase.index(letter) + key]

        else:
            frase += letter

    return frase

print(caesar_cypher_encrypt('a5', 2))

