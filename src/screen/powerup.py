from library.PPlay.animation import Animation
from library.PPlay.sprite import Sprite

from environment import variables as gvar
from environment.instances import window, mouse, keyboard

from controller.player import player
from controller.atributes import *


title = Sprite("./src/assets/menu/powerup_title.png")
title.set_position(gvar.WIDTH / 2 - title.width / 2, 200 - title.height / 2)

power = Sprite("./src/assets/menu/power.png")
power.set_position(gvar.WIDTH / 2 - power.width / 2, 350 - power.height / 2)
power_plus = Animation("./src/assets/menu/plus.png", 2)
power_plus.set_position(power.x + power.width + 30, power.y)

power_minus = Animation("./src/assets/menu/minus.png", 2)
power_minus.set_position(power.x - power_minus.width - 30, power.y)


life = Sprite("./src/assets/menu/life.png")
life.set_position(gvar.WIDTH / 2 - life.width / 2, 500 - life.height / 2)
life_plus = Animation("./src/assets/menu/plus.png", 2)
life_plus.set_position(life.x + life.width + 30, life.y)

life_minus = Animation("./src/assets/menu/minus.png", 2)
life_minus.set_position(life.x - life_minus.width - 30, life.y)


heal = Animation("./src/assets/menu/heal.png", 2)
heal.set_position(gvar.WIDTH / 2 - heal.width / 2, 700 - heal.height / 2)


def run():
    global title
    global power
    global power_plus
    global power_minus
    global life
    global life_plus
    global life_minus
    global heal

    if keyboard.key_pressed("esc"):
        gvar.STATE = 1
        window.delay(150)

    # POWER PLUS
    if mouse.is_over_object(power_plus):
        power_plus.set_curr_frame(1)
        if mouse.is_button_pressed(1) and gvar.SCORE > cost_strength():
            gvar.SCORE -= cost_strength()
            player.strenght = update_strenght()
            print("dale", gvar.SCORE, player.strenght)
            window.delay(150)
    else:
        power_plus.set_curr_frame(0)

    # POWER MINUS
    if mouse.is_over_object(power_minus):
        power_minus.set_curr_frame(1)
        if mouse.is_button_pressed(1):
            pass
    else:
        power_minus.set_curr_frame(0)

    # LIFE PLUS
    if mouse.is_over_object(life_plus):
        life_plus.set_curr_frame(1)
        if mouse.is_button_pressed(1):
            pass
    else:
        life_plus.set_curr_frame(0)

    # LIFE MINUS
    if mouse.is_over_object(life_minus):
        life_minus.set_curr_frame(1)
        if mouse.is_button_pressed(1):
            pass
    else:
        life_minus.set_curr_frame(0)

    # HEAL
    if mouse.is_over_object(heal):
        heal.set_curr_frame(1)
        if mouse.is_button_pressed(1):
            pass
    else:
        heal.set_curr_frame(0)

    window.set_background_color((0, 0, 0))

    window.draw_text(
        "price:",
        power_plus.x + power_plus.width + 30,
        power_plus.y,
        "./src/assets/fonts/pixel.ttf",
        size=16,
        color=(255, 255, 255),
    )

    window.draw_text(
        "owned:",
        power_plus.x + power_plus.width + 30,
        power_plus.y + 30,
        "./src/assets/fonts/pixel.ttf",
        size=16,
        color=(255, 255, 255),
    )

    title.draw()
    power.draw()
    power_minus.draw()
    power_plus.draw()
    life.draw()
    life_plus.draw()
    life_minus.draw()
    heal.draw()
