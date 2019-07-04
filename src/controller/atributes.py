from math import exp

owned_strenght = 0
owned_velocity = 0
owned_life = 0
owned_heal = 0


def reset():
    global owned_strenght
    global owned_velocity
    global owned_life
    global owned_heal

    owned_strenght = 0
    owned_velocity = 0
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


# VELOCITY
def cost_velocity(current):
    return int(100 * (1.07) ** current)


def update_velocity(current):
    current += 1
    return int(50 * exp(0.1255 * current))


# LIFE
def cost_life(current):
    return int(100 * (1.07) ** current)


def update_life(current):
    current += 1
    return int(50 * exp(0.1255 * current))


# HEAL
def cost_heal(current):
    current += 1
    return int(100 * (1.07) ** current)


def heal(current):
    return int(50 * exp(0.1255 * current))
