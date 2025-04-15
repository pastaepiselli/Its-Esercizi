special_chars = ['~','!','@','#', '$', '%', '^', '&', '*']
def validate_password(password: str):
    upper: int = 0 
    special: int = 0
    if len(password) > 20:
        
        for chr in password:

            if chr.isupper():

                upper += 1
            
            if chr in special_chars:

                special += 1
        
        if upper >= 3 and special >= 4:

            return True
        else:
            if upper < 3:

                raise ValueError("La password deve contenere 3 o piu caratteri in maiuscolo")
            
            elif special < 4:

                raise ValueError("La password deve contenere 4 o piu caratteri speciali")
    else:

        raise ValueError("La password deve essere lunga piu di 20 caratteri")

       
    
            
validate_password('tdrwdrwd')