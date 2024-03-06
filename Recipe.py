from colors import *

known_recipes = dict()              # Known Recipe list
unknown_queue = []                  # Unknown recipes. Allow user to define at a later time

class Recipe:
    def __init__(self, recipe_name: str):
        global known_recipes
        self.name = recipe_name
        
        self.ingredients = dict()       # {RecipeName: count}
        self.fullRaw = dict()           # Stores the total quantity of raw materis reqired.

        # Create a new entry in the known recipe dict and add object to it.
        known_recipes[self.name] = self

        self.isRaw = None
        self.getIngredients()
    

    def getIngredients(self):
        global known_recipes
        """Takes user input for the ingredients recipe. If added ingredient is not known"""
        n = input("Enter number of elements in the recipe, Enter to skip: ")
        
        if not n:
            print(f'Skipped: Setting {YELLOW(self.name)} as a raw resource')
            self.isRaw = True
            return
        
        # Input from the user
        _recipe_list = dict()
        _unknown_ing = []           # Ingredients not previously defined.
        for i in range(n):
            recipe_name, count = input("Element name and count: ")
            _recipe_list[recipe_name] = count
            if not known_recipes.get(recipe_name, None):
                _unknown_ing.append(recipe_name)

        # Verification of recipe from user
        print("Verify list of input ingredients")
        for rname, rcount in _recipe_list.items():
            print(f'\t{CYAN(rname)} -- {PINK(rcount)}')
        
        # Update ingredients list if verified else restart.
        if not input("Continue? Type anything to restart "):
            self.ingredients = _recipe_list.copy()      # Set the ingredients dict for the recipe
            unknown_queue.extend(_unknown_ing)          # Update unkown recipe queue with new additions
        else:
            self.getIngredients()

    def calculateTotalRaw(self):
        """Returns the list of total raw materis required for the main recipe"""
        if self.fullRaw:
            return self.fullRaw
        