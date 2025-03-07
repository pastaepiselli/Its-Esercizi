tutor: int = 2
attesa: int = 0
status: bool = True
while status:
    studente = str(input("Inserire studente: "))
    if tutor > 0:
        tutor -= 1
        print("Tutor assegnato correttamente!")
    else:
        attesa += 1
        print("Assegnato a lista di attesa")
    if tutor == 0 and attesa == 3:
        status: bool = False
print("Posti esauriti!")