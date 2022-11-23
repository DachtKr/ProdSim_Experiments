import random

# ---- sources ------------------------


def shaft_source(env, factory):
    yield env.timeout(1)
    yield 1

# ---- sinks ---------------------------

# ---- process functions --------------


def drilling(env, item, machine, factory):

    comp_random = random.random()
    res_random = random.normalvariate(2.5, 0.1)

    # print(comp_random)

    if comp_random < machine.drill_breakage:
        item.surface += res_random
        # print("norm:", res_random, item.surface)

    yield env.timeout(2)


def turning(env, item, machine, factory):

    if machine.wear >= 1:
        machine.wear = 0
        yield env.timeout(10)

    item.surface += machine.wear**2 * 1.5 - 2
    # it's possible to use the machine 50 times, before it has to be maintained
    machine.wear += 0.006
    yield env.timeout(1)


def polishing(env, item, machine, factory):

    item.surface -= 8 - factory.temperature * 0.3

    yield env.timeout(1)

# ---- global functions ---------------


# temp_dict = {0: 19, 240: 18, 480: 20, 720: 23, 960: 22, 1200: 20}
temp_dict = {0:17, 60:17, 120:17, 180:17, 240:18, 300:18, 360:18, 420:19, 480:19, 540:20,
             600:20, 660:21, 720:21, 780:22, 840:21, 900:22, 960:22, 1020:21, 1080:21,
             1140:20, 1200:19, 1260:18, 1320:18, 1380:17, 1440:17}


def temperature_func(env, factory):

    # determine the current time of day in minutes
    day_time: int = env.now % 1440 # 1440
    # print(env.now)
    # print(day_time)

    # Set the temperature in the factory based on the time of day
    factory.temperature = temp_dict[day_time]

    # print(factory.temperature)

    yield env.timeout(60) # 240

# ---- distributions ------------------
