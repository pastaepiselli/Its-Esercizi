spazio: int = 0
n = str(input("Inserire frase: "))
for i in range(0, len(n)):
    if n[i]  == " ":
        spazio += 1
if spazio == 0:
    print("Non ci sono spazi")
else:
    print(f"Ci sono {spazio} spazi nella frase")
