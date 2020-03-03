from configuration.entity.recipe import Recipe
from configuration.entity.recipe_beverage import RecipeBeverage
from configuration.repository.csv.recipe_beverage_repository import RecipeBeverageRepository


class RecipeBeverageFacade:
    def find_all(self):
        return RecipeBeverageRepository().find_all()

    def find_by_recipe(self, recipe: Recipe):
        return RecipeBeverageRepository().find_by_recipe(recipe)

    def insert(self, recipe_beverage: RecipeBeverage):
        return RecipeBeverageRepository().insert(recipe_beverage)

    def update(self, recipe_beverage: RecipeBeverage):
        return RecipeBeverageRepository().update(recipe_beverage)

    def delete(self, id):
        RecipeBeverageRepository().delete(id)