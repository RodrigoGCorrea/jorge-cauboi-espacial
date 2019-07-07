from library.PPlay.animation import Animation
from library.PPlay.sprite import Sprite

from environment import variables as gvar
from environment.instances import window, mouse, keyboard

from controller.player import player
from controller.atributes import (
    cost_strength,
    cost_heal,
    cost_life,
    heal_player,
    update_life,
    update_strength
)


title = Sprite("./src/assets/menu/powerup_title.png")
title.set_position(gvar.WIDTH / 2 - title.width / 2, 150 - title.height / 2)

power = Animation("./src/assets/menu/power.png", 2)
power.set_position(gvar.WIDTH / 2 - power.width / 2, 350 - power.height / 2)

life = Animation("./src/assets/menu/life.png", 2)
life.set_position(gvar.WIDTH / 2 - life.width / 2, 500 - life.height / 2)

heal = Animation("./src/assets/menu/heal.png", 2)
heal.set_position(gvar.WIDTH / 2 - heal.width / 2, 700 - heal.height / 2)


def run():
    global title
    global power
    global life
    global heal

    if keyboard.key_pressed("esc"):
        gvar.STATE = 1
        window.delay(150)

    # POWER
    if mouse.is_over_object(power):
        power.set_curr_frame(1)
        if mouse.is_button_pressed(1) and gvar.SCORE > cost_strength():
            gvar.SCORE -= cost_strength()
            player.strenght = update_strength()
            window.delay(150)
    else:
        power.set_curr_frame(0)

    # LIFE
    if mouse.is_over_object(life):
        life.set_curr_frame(1)
        if mouse.is_button_pressed(1) and gvar.SCORE > cost_life():
            gvar.SCORE -= cost_life()
            player.max_life += update_life()
            window.delay(150)
    else:
        life.set_curr_frame(0)

    # HEAL
    if mouse.is_over_object(heal):
        heal.set_curr_frame(1)
        if mouse.is_button_pressed(1) and gvar.SCORE > cost_heal():
            gvar.SCORE -= cost_heal()
            heal_player(player)
            window.delay(150)
    else:
        heal.set_curr_frame(0)

    window.set_background_color((0, 0, 0))

    # SCORE
    window.draw_text(
        "score: {}".format(gvar.SCORE),
        title.x + 30,
        title.y + title.height + 30,
        "./src/assets/fonts/pixel.ttf",
        size=24,
        color=(255, 255, 255),
    )

    # PRICE AND OWNED POWER
    window.draw_text(
        "price: {}".format(cost_strength()),
        power.x + power.width + 25,
        power.y + 10,
        "./src/assets/fonts/pixel.ttf",
        size=16,
        color=(255, 255, 255),
    )

    from controller.atributes import owned_strength
    window.draw_text(
        "owned: {}".format(owned_strength),
        power.x + power.width + 25,
        power.y + 50,
        "./src/assets/fonts/pixel.ttf",
        size=16,
        color=(255, 255, 255),
    )

    # PRICE AND OWNED LIFE
    window.draw_text(
        "price: {}".format(cost_life()),
        life.x + life.width + 25,
        life.y + 10,
        "./src/assets/fonts/pixel.ttf",
        size=16,
        color=(255, 255, 255),
    )

    from controller.atributes import owned_life
    window.draw_text(
        "owned: {}".format(owned_life),
        life.x + life.width + 25,
        life.y + 50,
        "./src/assets/fonts/pixel.ttf",
        size=16,
        color=(255, 255, 255),
    )

    # PRICE HEAL
    window.draw_text(
        "price: {}".format(cost_heal()),
        heal.x + heal.width + 25,
        heal.y + 10,
        "./src/assets/fonts/pixel.ttf",
        size=16,
        color=(255, 255, 255),
    )

    title.draw()
    power.draw()
    life.draw()
    heal.draw()
