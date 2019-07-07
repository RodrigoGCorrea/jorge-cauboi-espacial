from math import exp
from environment.instances import store

owned_strength = 0
owned_life = 0
owned_heal = 0


def reset():
    global owned_strength
    global owned_life
    global owned_heal

    owned_strength = 0
    owned_life = 0
    owned_heal = 0


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


def heal_player(player):
    store.dispatch("owned_heal", lambda heal: heal + 1)
    player.life = player.max_life
