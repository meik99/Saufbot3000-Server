from configuration.repository.csv.beverage_repository import BeverageRepository


class BeverageFacade:
    def find_all(self):
        return BeverageRepository().find_all()

    def insert(self, beverage):
        return BeverageRepository().insert(beverage)

    def update(self, beverage):
        return BeverageRepository().update(beverage)

    def delete(self, id):
        BeverageRepository().delete(id)