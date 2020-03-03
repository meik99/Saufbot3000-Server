from configuration.entity.pump import Pump
from configuration.repository.csv.pump_repository import PumpRepository


class PumpFacade:
    def find_all(self):
        return PumpRepository().find_all()

    def update(self, pump: Pump):
        return PumpRepository().update(pump)