import csv
import os
from pathlib import Path
from typing import List

from configuration.entity.recipe import Recipe
from configuration.entity.recipe_beverage import RecipeBeverage

PATH = "{}/configuration/files/recipe_beverage.csv".format(os.getcwd())


class RecipeBeverageRepository:
    def __init__(self):
        file = Path(PATH)

        if file.exists() is False:
            file.touch()

    def find_by_recipe(self, recipe: Recipe) -> List[RecipeBeverage]:
        result = []

        with open(PATH) as file:
            csv_reader = csv.reader(file, delimiter=";")

            for row in csv_reader:
                try:
                    milliliters = int(row[3])
                except (ValueError, TypeError):
                    milliliters = 0

                entity = RecipeBeverage(
                    id=int(row[0]),
                    recipe_id=int(row[1]),
                    beverage_id=int(row[2]),
                    milliliters=milliliters
                )
                if entity.recipe_id == recipe.id:
                    result.append(entity)

        return result

    def find_all(self) -> List[RecipeBeverage]:
        result = []

        with open(PATH) as file:
            csv_reader = csv.reader(file, delimiter=";")

            for row in csv_reader:
                try:
                    milliliters = int(row[3])
                except (ValueError, TypeError):
                    milliliters = 0

                entity = RecipeBeverage(
                    id=int(row[0]),
                    recipe_id=int(row[1]),
                    beverage_id=int(row[2]),
                    milliliters=milliliters
                )
                result.append(entity)

        return result

    def update(self, recipe_beverage: RecipeBeverage) -> RecipeBeverage:
        entities = self.find_all()
        result = None
        rows = []

        for e in entities:
            if e.id == recipe_beverage.id:
                e.recipe_id = recipe_beverage.recipe_id
                e.beverage_id = recipe_beverage.beverage_id
                e.milliliters = recipe_beverage.milliliters
                result = e
            rows.append([e.id, e.recipe_id, e.beverage_id, e.milliliters])

        with open(PATH, "w") as file:
            csv_writer = csv.writer(file, delimiter=";")
            csv_writer.writerows(rows)

        return result

    def insert(self, recipe_beverage: RecipeBeverage):
        entities = self.find_all()
        rows = []
        max_id = 0

        for e in entities:
            if e.id > max_id:
                max_id = e.id
            rows.append([e.id, e.recipe_id, e.beverage_id, e.milliliters])

        recipe_beverage.id = max_id + 1
        rows.append([recipe_beverage.id, recipe_beverage.recipe_id, recipe_beverage.beverage_id, recipe_beverage.milliliters])

        with open(PATH, "w") as file:
            csv_writer = csv.writer(file, delimiter=";")
            csv_writer.writerows(rows)

        return recipe_beverage

    def delete(self, id):
        entities = self.find_all()
        rows = []

        for e in entities:
            if e.id != id:
                rows.append([e.id, e.recipe_id, e.beverage_id, e.milliliters])

        with open(PATH, "w") as file:
            csv_writer = csv.writer(file, delimiter=";")
            csv_writer.writerows(rows)