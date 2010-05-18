# -*- coding: utf-8 -*-

class Ingredient():
    FOOD_STUFF = 0
    ADDITIVE = 1
    
    def __init__(self, name, type, amount):
        self.name = name
        self.type = type
        self.amount = amount
    
    def __repr__(self):
        if self.amount is not None:
            return " ".join([self.amount, self.name])
        else:
            return self.name

class Task():
    def __init__(self, verb, ingredient, with_ingredient, time):
        self.verb = verb
        self.ingredient = ingredient
        self.with_ingredient = with_ingredient
        self.time = time
    
    def __repr__(self):
        if self.with_ingredient is None:
            if self.time is not None:
                return " ".join([self.verb, str(self.ingredient), "for", self.time])
            else:
                return " ".join([self.verb, str(self.ingredient)])
        else:
            if self.time is not None:
                return " ".join([self.verb, str(self.ingredient), "with", self.with_ingredient, "for", self.time])
            else:
                return " ".join([self.verb, str(self.ingredient), "with", self.with_ingredient])

class Recipe():
    def __init__(self, name, tasks = None):
        self.name = name
        self.tasks = tasks
        self.ingredients = {}
        self.tasks = []

    def addTask(self, verb, ingredient_name, other = None, time = None):
        if not ingredient_name in self.ingredients.keys():
            return False
        
        if other is not None and not other in self.ingredients.keys():
            return False
        
        ingredient = self.ingredients[ingredient_name];
        self.tasks.append( Task(verb, ingredient, other, time) )
        
        return True
    
    def addIngredient(self, name, type = Ingredient.FOOD_STUFF, amount = None):
        if name in self.ingredients:
            return False
        
        ingredient = Ingredient(name, type, amount)
        self.ingredients[name] = ingredient
    
    def __repr__(self):
        retval = "Recipe: " + self.name + "\n\n"
        retval += "Ingredients:\n"
        for ingredient in self.ingredients.values():
            if ingredient.type != Ingredient.ADDITIVE:
                retval += "\t" + str(ingredient) + "\n"
        retval += "\n"
        retval += "Instructions:\n"
        for i, task in enumerate(self.tasks):
            retval += "\t" + str(i+1) + ". " + str(task) + "\n"
        return retval
            

if __name__ == "__main__":
    recipe = Recipe("Skillet Chicken Parmesan")
    
    recipe.addIngredient( "parmesan", Ingredient.FOOD_STUFF, "6 tbsp" )
    recipe.addIngredient( "pasta sauce", Ingredient.FOOD_STUFF, "1 1/2 cups" )
    recipe.addIngredient( "cooking spray", Ingredient.ADDITIVE )
    recipe.addIngredient( "chicken", Ingredient.FOOD_STUFF, "6" )
    recipe.addIngredient( "mozzarella", Ingredient.ADDITIVE, "1 1/2 cups" )
    
    recipe.addTask( "stir", "parmesan", "pasta sauce" )
    recipe.addTask( "cook till brown", "chicken" )
    recipe.addTask( "drain", "chicken" )
    recipe.addTask( "pour over", "pasta sauce", "chicken" )
    recipe.addTask( "cook", "chicken", time = "10'" )
    
    print recipe

        