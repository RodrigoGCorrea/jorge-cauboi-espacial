from math import exp

owned_strenght = 0
owned_life = 0
owned_heal = 0


def reset():
    global owned_strenght
    global owned_life
    global owned_heal

    owned_strenght = 0
    owned_life = 0
    owned_heal = 0


# STRENGHT
def cost_strength():
    global owned_strenght
    return int(100 * (1.3) ** owned_strenght)


def update_strenght():
    global owned_strenght
    owned_strenght += 1
    return int(50 * exp(0.1255 * owned_strenght))


# LIFE
def cost_life():
    return int(100 * (1.4) ** owned_life)


def update_life():
    global owned_life
    owned_life += 1
    return 10


# HEAL
def cost_heal():
    return int(100 * (1.5) ** owned_heal)


def heal_player(player):
    global owned_heal
    owned_heal += 1
    player.life = player.max_life
