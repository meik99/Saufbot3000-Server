import csv
import os

from pathlib import Path
from typing import List

from configuration.entity.beverage import Beverage
from configuration.entity.recipe import Recipe

PATH = "{}/configuration/files/recipe.csv".format(os.getcwd())


class RecipeRepository:
    def __init__(self):
        file = Path(PATH)

        if file.exists() is False:
            file.touch()

    def find_all(self) -> List[Beverage]:
        result = []

        with open(PATH) as beverages:
            csv_reader = csv.reader(beverages, delimiter=";")

            for row in csv_reader:
                result.append(Beverage(
                    id=int(row[0]), name=row[1]
                ))

        return result

    def insert(self, recipe: Recipe):
        recipes = self.find_all()
        max_id = 0

        for r in recipes:
            if r.id > max_id:
                max_id = r.id

        recipe.id = max_id + 1

        with open(PATH, mode="a") as recipe_file:
            csv_writer = csv.writer(recipe_file, delimiter=";")
            csv_writer.writerow([recipe.id, recipe.name])

        return recipe

    def update(self, recipe):
        recipes = self.find_all()
        rows = []
        result = None

        for r in recipes:
            if r.id == recipe.id:
                r.name = recipe.name
                result = r
            rows.append([r.id, r.name])


        with open(PATH, mode="w") as recipe_file:
            csv_writer = csv.writer(recipe_file, delimiter=";")
            csv_writer.writerows(rows)

        return result

    def delete(self, id):
        recipes = self.find_all()
        rows = []

        for r in recipes:
            if r.id != id:
                rows.append([r.id, r.name])

        with open(PATH, mode="w") as recipe_file:
            csv_writer = csv.writer(recipe_file, delimiter=";")
            csv_writer.writerows(rows)


