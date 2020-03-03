import csv
import os

from pathlib import Path
from typing import List

from configuration.entity.beverage import Beverage

PATH = "{}/configuration/files/beverage.csv".format(os.getcwd())


class BeverageRepository:
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

    def insert(self, beverage):
        beverages = self.find_all()
        max_id = 0

        for b in beverages:
            if b.id > max_id:
                max_id = b.id

        beverage.id = max_id + 1

        with open(PATH, mode="a") as beverage_file:
            csv_writer = csv.writer(beverage_file, delimiter=";")
            csv_writer.writerow([beverage.id, beverage.name])

        return beverage

    def update(self, beverage):
        beverages = self.find_all()
        rows = []
        result = None

        for b in beverages:
            if b.id == beverage.id:
                b.name = beverage.name
                result = b
            rows.append([b.id, b.name])


        with open(PATH, mode="w") as beverage_file:
            csv_writer = csv.writer(beverage_file, delimiter=";")
            csv_writer.writerows(rows)

        return result

    def delete(self, id):
        beverages = self.find_all()
        rows = []

        for b in beverages:
            if b.id != id:
                rows.append([b.id, b.name])

        with open(PATH, mode="w") as beverage_file:
            csv_writer = csv.writer(beverage_file, delimiter=";")
            csv_writer.writerows(rows)


