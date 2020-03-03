import csv
import os

from pathlib import Path
from pprint import pprint
from typing import List

from configuration.entity.pump import Pump

PATH = "{}/configuration/files/pump.csv".format(os.getcwd())


class PumpRepository:
    def __init__(self):
        file = Path(PATH)

        if file.exists() is False:
            file.touch()

    def find_all(self) -> List[Pump]:
        result = []

        with open(PATH) as pump_file:
            csv_reader = csv.reader(pump_file, delimiter=";")

            for row in csv_reader:
                result.append(Pump(
                    id=int(row[0]), pin=int(row[1]), colors=(row[2], row[3]), beverageId=int(row[4])
                ))

        return result

    def update(self, pump: Pump) -> Pump:
        pumps = self.find_all()
        rows = []
        result = None

        for p in pumps:
            if p.id == pump.id:
                p.beverageId = pump.beverageId
                result = p
            rows.append([p.id, p.pin, p.colors[0], p.colors[1], p.beverageId])

        with open(PATH, "w") as pump_file:
            csv_writer = csv.writer(pump_file, delimiter=";")
            csv_writer.writerows(rows)

        return result