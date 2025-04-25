import re
def find_dates(text: str) -> list[str]:

    date = r'\d{2}/\d{2}/\d{4}'

    match = re.findall(date, text)

    return match

print(find_dates('Le date importanti sono 09/04/2025 e 15/08/2023.'))
    