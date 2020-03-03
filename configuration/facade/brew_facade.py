from configuration.repository.gpio.brew_repository import BrewRepository


class BrewFacade():
    def brew(self, recipe_id):
        return BrewRepository().brew(recipe_id)