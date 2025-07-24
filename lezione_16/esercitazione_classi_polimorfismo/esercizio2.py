class RecipeManager:

    def __init__(self) -> None:
        self.manuale_cucina = {}
    
    def create_recipe(self, name: str, ingredients: list[str]) -> dict[str, list[str]]:
        # aggiungo la ricetta al manuale
        self.manuale_cucina[name] = ingredients

        # ritorno un dizionario con la ricetta appena aggiunta
        return {name: ingredients}
    
    def add_ingredient(self, recipe_name: str, ingredient: str) -> None | dict:

        if recipe_name not in self.manuale_cucina:
            print('La ricetta non e nel manuale')
            return

        self.manuale_cucina[recipe_name].append(ingredient)

        return {recipe_name: self.manuale_cucina[recipe_name]}

    def remove_ingredient(self, recipe_name: str, ingredient: str) -> None | dict:

        if recipe_name not in self.manuale_cucina:
            print('La ricetta non e nel manuale')
            return None

        self.manuale_cucina[recipe_name].remove(ingredient)

        return {recipe_name: self.manuale_cucina[recipe_name]}

    def update_ingredient(self, recipe_name: str, old_ingredient: str, new_ingredient: str) -> None | dict:

        if recipe_name not in self.manuale_cucina:
            print('La ricetta non e nel manuale')
            return

        if old_ingredient not in self.manuale_cucina[recipe_name]:
            print('L\'ingrediente da rimuovere non e presente nella ricetta')
            return

        if new_ingredient in self.manuale_cucina:
            print('L\'ingrediente da aggiungere e gia nella ricetta')
            return
        
        a = self.manuale_cucina[recipe_name].index(old_ingredient)
        self.manuale_cucina[recipe_name][a] = new_ingredient

        return {recipe_name: self.manuale_cucina[recipe_name]}


    def list_recipes(self) -> None:
        return [*self.manuale_cucina.keys()]

    def list_ingredients(self, recipe_name: str) -> None:

        if recipe_name not in self.manuale_cucina:
            print('La ricetta non e nel manuale')
            return
        
        return self.manuale_cucina[recipe_name]

       
    def search_recipe_by_ingredient(self, ingredient: str) -> list:
        ricette_con_ingrediente = {}

        for key, values in self.manuale_cucina.items():      
            if ingredient in values:
                ricette_con_ingrediente[key] = values
                

        return ricette_con_ingrediente



        
        

