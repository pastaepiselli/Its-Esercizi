n = int(input("Soldi disponibli: "))
barrette: int = 0
coupon: int = 0
while n > 0:
    barrette += 1
    coupon += 1
    n -=1
    if coupon % 6 == 0:
        barrette += 1
        coupon -= 6
print(f"Il numero di barrette è {barrette}")
print(f"Il numero di coupon è {coupon}")
