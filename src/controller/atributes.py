from math import exp
from environment.instances import store


def reset():
    store.dispatch("owned_strength", value=0)
    store.dispatch("owned_life", value=0)
    store.dispatch("owned_heal", value=0)


# STRENGHT
def cost_strength():
    return int(100 * (1.3) ** store.get("owned_strength"))


def update_strength():
    store.dispatch("owned_strength", lambda strength: strength + 1)
    return int(50 * exp(0.1255 * store.get("owned_strength")))


# LIFE
def cost_life():
    return int(100 * (1.4) ** store.get("owned_life"))


def update_life():
    store.dispatch("owned_life", lambda life: life + 1)
    return 10


# HEAL
def cost_heal():
    return int(100 * (1.5) ** store.get("owned_heal"))


def update_heal():
    store.dispatch("owned_heal", lambda heal: heal + 1)
