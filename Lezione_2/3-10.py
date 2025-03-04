rivers: list = ["Nilo", "Rio", "Mississipi"]

rivers.pop(0)
print(rivers)

rivers.insert(0, "Enisej")
print(rivers)

rivers.append("Mekong")
print(rivers)

del rivers(2)
print(rivers)

rivers.sorted() # non modifica la lista orig
print(rivers)

rivers.reverse()
print(rivers)

rivers.sort(reverse=True) # vuene modificata la lista 
print(rivers)

