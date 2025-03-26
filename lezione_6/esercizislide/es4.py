class Food:
    def __init__(self, name, price, description):
        self.name = name
        self.price = price
        self.description = description


baguette = Food('Baguette', 5, 'a long slice of bread')
pure = Food("Pure", 7, 'smashed potaes with milk')
fiorentina = Food("Fiorentina", 15, 'big ass piece of meat')

cibi = []
class Menu:
    

    def __init__(self, Foods):
        self.foods: list[Food] = []

    def addFood(self, cibo):
        self.foods.append(cibo)
    
    def removeFood(self, cibo):
        self.foods.remove(cibo)

    def printPrices(self):
        for items in self.foods:
            print(items.name, items.price)

    def getAveragePrice(self):
        for items in self.foods:
            sum += items.price
        media = sum / len(self.foods)
        return media
    
    


cartamenu = Menu(cibi)

cartamenu.addFood(baguette)
cartamenu.addFood(pure)
cartamenu.addFood(fiorentina)



        

        
        