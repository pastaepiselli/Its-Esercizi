from string import ascii_lowercase
from string import punctuation

def seach_words(s: str) -> dict[str, int]:
    new_dict: dict[str, int] = {}
    search = s.lower().strip('.')
    parole: str= ''
    punteggiatura = ''

    for letter in search:

        if letter == " ":
            if parole in new_dict:
                new_dict[parole] += 1
                parole = ''

            else:
                new_dict[parole] = 1
                parole = ''
        if letter in ascii_lowercase:
            parole += letter
    return new_dict

text = "Hello, world! Hello... PYTHON? world."

print(seach_words(text))


# correzione esercizio


def words(text: str) -> dict[str, int]:
    # trasformo la frase in minuscolo
    text = text.lower()
    # lista di "token" spazi vuoti nella frase
    tokens: list[str] = text.split(" ")
    # 
    d: dict[str, int] = {}
    # itero sulla lista di parole che restituisce .split(" ")
    for token in tokens:
        # rimuovo tutta la punteggiatura 
        token = token.strip(punctuation)
        # non ce la chiave quindi la creo
        if token not in d:
            d[token] = 1
        # ce la chiave quindi la aggiungo
        else:
            d[token] += 1

    return d

print(words(text))

