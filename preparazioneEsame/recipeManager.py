class RecipeManager:
    def __init__(self):
        self.ricette = {}
    
    def create_recipe(self, name, ingredients):
        if name in self.ricette:
            return "Errore, ricetta esiste gia"
        self.ricette[name] = ingredients
        return {name: self.ricette[name]}
    
    def add_ingredient(self, recipe_name, ingredient):
        if recipe_name not in self.ricette:
            return "Errore, ricetta non esiste"
        elif ingredient in self.ricette[recipe_name]:
            return "Errore, ingrediente gia presente"
        self.ricette[recipe_name].append(ingredient)
        return {recipe_name : self.ricette[recipe_name]}
    
    def remove_ingredient(self, recipe_name, ingredient):
        if recipe_name not in self.ricette:
            return "Errore, ricetta non esiste"
        elif ingredient not in self.ricette[recipe_name]:
            return "Errore, ingrediente non presente"
        self.ricette[recipe_name].remove(ingredient)
        return {recipe_name: self.ricette[recipe_name]}
    
    def update_ingredient(self, recipe_name, old_ingredient, new_ingredient):
        if recipe_name not in self.ricette:
            return "Errore, ricetta non esiste"
        elif old_ingredient not in self.ricette[recipe_name]:
            return "Errore, ingrediente non presente"
        index = self.ricette[recipe_name].index(old_ingredient)
        self.ricette[recipe_name][index] = new_ingredient
        return {recipe_name: self.ricette[recipe_name]}
    
    def list_recipes(self):
        return list(self.ricette.keys())
    
    def list_ingredients(self, recipe_name):
        if recipe_name not in self.ricette:
            return "Errore, ricetta non esiste"
        return self.ricette[recipe_name]
    
    def search_recipe_by_ingredient(self, ingredient):
        d = {}
        for k, v in self.ricette.items():
            if ingredient in v:
                d[k] = v
        if not d:
            return "Nessuna ricetta trovata"
        return d