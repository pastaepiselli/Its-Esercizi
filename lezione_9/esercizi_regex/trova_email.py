import re
def extract_email(s: str) -> list[str]:
   
    pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
    # findall ritorna una lista 
    match = re.findall(pattern, s)

    return match
    
    
print(extract_email('Scrivi a info@azienda.com oppure a support123@help.it'))