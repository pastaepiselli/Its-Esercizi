class RecipeManager:

    def __init__(self) -> None:
        self.manuale_cucina = {}
    
    def create_recipe(self, name: str, ingredients: list[str]) -> None:
        # creo un dizionario con la ricetta per ritornarla
        ricetta: dict[str, list[str]] = {}

        # aggiungo la ricetta nel dizionario
        ricetta[name] = ingredients

        # aggiungo la ricetta al manuale
        self.manuale_cucina[name] = ingredients

        # ritorno il dizionario appena creato
        return ricetta
    
    def add_ingredient(self, recipe_name: str, ingredient: str) -> None | dict:

        if recipe_name not in self.manuale_cucina:
            print('La ricetta non e nel manuale')
            return

        self.manuale_cucina[recipe_name].append(ingredient)

        return self.manuale_cucina[recipe_name]

    def remove_ingredient(self, recipe_name: str, ingredient: str) -> None | dict:

        if recipe_name not in self.manuale_cucina:
            print('La ricetta non e nel manuale')
            return None
        
        

