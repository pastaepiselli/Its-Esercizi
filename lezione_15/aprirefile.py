PATH : str = 'lezione_15/example.txt' # lettere tutte in maiuscolo = variabile constante
mode: str= 'r'
# possono essere lette in modalita diverse : 'r'= read, 'w'= write = nel caso del write sovrasrive, 'a' = append = aggiunge senza sovrascivere      
encoding: str = 'utf-8'
# attenzione alla codifica che si usa 

file: open = open(PATH) # passo la stringa con la path, la mode per default e 'r'

print(file)

output: str = file.read() # se non gli diamo in input niente leg
print(output)
file.close()
# <_io.TextIOWrapper name='lezione_15/example.txt' mode='r' encoding='UTF-8'>
# wrap = circondare, mettere uno strato sopra, un wrapper ha un cosa e la incapsula in un'altra

# path assoluti = percorso dalla root fino al file /home/lorenzo-rossi/Its-Esercizi/lezione_15/example.txt
# si riferisce alla macchina a cui si riferisce in quel momento, se aperto in un altra macchina il path non funziona

# path relativo = path rispetto alla cartella che contiene il proogetto

