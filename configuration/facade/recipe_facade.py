from configuration.repository.csv.recipe_repository import RecipeRepository


class RecipeFacade:
    def find_all(self):
        return RecipeRepository().find_all()

    def insert(self, recipe):
        return RecipeRepository().insert(recipe)

    def update(self, recipe):
        return RecipeRepository().update(recipe)

    def delete(self, id):
        RecipeRepository().delete(id)