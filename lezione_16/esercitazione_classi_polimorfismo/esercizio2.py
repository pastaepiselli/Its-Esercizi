class RecipeManager:

    def __init__(self) -> None:
        self.ricette: dict[dict[str, list]] = dict()

    def create_recipe(self, name: str, ingredients: list[str]) -> dict:
        
        # se gia esiste
        if name in self.ricette:
            raise ValueError('La ricetta esiste gia')

        # la aggiungo alle ricette
        ricette[name] = ingredients
        
        # Restituisce un nuovo dizionario con la sola ricetta appena creata
        ricetta = {name: ingredients}
        return ricetta    

    def add_ingredient(self, recipe_name: str, ingredient: str) -> dict:

        if recipe_name not in self.ricette:
            raise ValueError('La ricetta non esiste')   

        self.ricette[recipe_name].append(ingredient)

        

    def remove_ingredient(self, recipe_name: str, ingredient: str) -> dict:

        if recipe_name not in self.ricette:
            raise ValueError('La ricetta non esiste')

        self.ricette[recipe_name].remove(ingredient)

    def update_ingrediente(self, recipe_name: str, old_ingredient: str, new_ingredient: str) -> 
