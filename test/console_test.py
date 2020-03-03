from gpiozero import LED
from time import sleep
import asyncio

SECS = 10


PUMPS = [
    4
    # , 17, 27, 22, 5, 6, 13, 26
]

#2,3 ml/s

TASKS = []

async def run_pump(pump):
    p = LED(pump)
    p.off()
    await asyncio.sleep(SECS)
    p.on()

async def main():
    for pump in PUMPS:
        TASKS.append(asyncio.create_task(run_pump(pump=pump)))

    for task in TASKS:
        await task


asyncio.run(main())

# for pump in PUMPS:
#     pump1 = LED(pump)
#     pump1.off()
#     sleep(5)
#     pump1.on()

# 4 done
# 17 done
# 27 done
# 22 done
# 5 done
# 6 done
# 13 done

# pump = LED(26)
# pump.off()
# sleep(SECS)
# pump.on()

#
# pump = LED(4)
# pump.off()
# sleep(SECS)
# pump.on()
# sleep(SECS)
# pump.off()
# sleep(SECS)
# pump.on()
# sleep(SECS)
# pump.off()
