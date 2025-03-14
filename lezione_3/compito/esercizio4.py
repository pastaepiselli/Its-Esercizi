numeri: list = []
while True: 
    num = int(input("Inserire numero: "))
    if num < 0:
        break
    if num.is_integer:
        numeri.append(num)
print(f"La somma dei numeri è {sum(numeri)}")
print(f"Il massimo è {max(numeri)}")
print(f"Il minio è {min(numeri)}")