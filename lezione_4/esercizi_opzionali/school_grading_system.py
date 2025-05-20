def grading(student: str, voti: dict[str:int]):
    counter: int = 0
    sum: int = 0
    for key, value in voti.items():

        sum+= value
        counter += 1

    media: int = sum / counter
    if sum >= 60:
        
        print(f'Lo studente {student} ha una media di {sum}, ha passato l\'esame') 

    else:

        print(f'Lo studente {student} ha una media di {sum}, non ha passato l\'esame')

