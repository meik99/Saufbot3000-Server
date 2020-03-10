import asyncio
from math import ceil

from gpiozero import LED

from configuration.entity.recipe import Recipe
from configuration.facade.pump_facade import PumpFacade
from configuration.facade.recipe_beverage_facade import RecipeBeverageFacade

from pprint import pprint

ML_PER_SECOND = 2.3


class BrewRepository():
    def brew(self, recipe_id):
        asyncio.run(self._brew(recipe_id))

    async def _brew(self, recipe_id):
        pumps = PumpFacade().find_all()
        ingredients = RecipeBeverageFacade().find_by_recipe(Recipe(id=recipe_id))
        tasks = []

        for ingredient in ingredients:
            _pumps = []
            for p in pumps:
                if p.beverageId == ingredient.beverage_id:
                    _pumps.append(p)
            for p in _pumps:
                tasks.append(asyncio.create_task(self._run_pump(p, ceil(ingredient.milliliters / len(_pumps)))))

        for task in tasks:
            await task

    async def _run_pump(self, pump, milliliters):
        pump_led = LED(pump.pin)

        if pump_led.value == 1:
            return

        pump_led.off()
        await asyncio.sleep(milliliters / ML_PER_SECOND)
        pump_led.on()


