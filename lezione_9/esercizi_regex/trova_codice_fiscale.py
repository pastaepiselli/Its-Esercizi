import re
def  find_cf(text: str) -> list[str]:

    pattern = r'[A-Z]{6}[0-9]{2}[A-Z]{1}[0-9]{2}[A-Z]{1}[0-9]{3}[A-Z]{1}'

    match = re.findall(pattern, text)
    return match

print(find_cf('Mario Rossi CF: RSSMRA85M01H501Z, mentre Maria Bianchi ha il CF BNCMRA85T41H501Y."'))
