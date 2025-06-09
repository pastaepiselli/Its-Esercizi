from string import ascii_lowercase
def seach_words(s: str) -> dict[str, int]:
    new_dict: dict[str, int] = {}
    search = s.lower().strip('.')
    parole: str= ''

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


