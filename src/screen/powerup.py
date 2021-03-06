from library.PPlay.animation import Animation
from library.PPlay.sprite import Sprite

from environment import config
from environment.instances import window, mouse, keyboard, store

from controller.atributes import (
    cost_strength,
    cost_heal,
    cost_life,
    update_heal,
    update_life,
    update_strength,
)


title = Sprite("./src/assets/menu/powerup_title.png")
title.set_position(config.WIDTH / 2 - title.width / 2, 150 - title.height / 2)

power = Animation("./src/assets/menu/power.png", 2)
power.set_position(config.WIDTH / 2 - power.width / 2, 350 - power.height / 2)

life = Animation("./src/assets/menu/life.png", 2)
life.set_position(config.WIDTH / 2 - life.width / 2, 500 - life.height / 2)

heal = Animation("./src/assets/menu/heal.png", 2)
heal.set_position(config.WIDTH / 2 - heal.width / 2, 700 - heal.height / 2)


def run():
    if keyboard.key_pressed("esc"):
        store.dispatch("state", value=1)
        window.delay(150)

    # POWER
    if mouse.is_over_object(power):
        power.set_curr_frame(1)
        if mouse.is_button_pressed(1) and store.get("score") > cost_strength():
            aux_str = cost_strength()
            store.dispatch("score", lambda score: score - aux_str)

            store.get("player").strenght = update_strength()

            window.delay(150)
    else:
        power.set_curr_frame(0)

    # LIFE
    if mouse.is_over_object(life):
        life.set_curr_frame(1)
        if mouse.is_button_pressed(1) and store.get("score") > cost_life():
            aux_life = cost_life()
            store.dispatch("score", lambda score: score - aux_life)

            store.get("player").max_life += update_life()

            window.delay(150)
    else:
        life.set_curr_frame(0)

    # HEAL
    if mouse.is_over_object(heal):
        heal.set_curr_frame(1)
        if mouse.is_button_pressed(1) and store.get("score") > cost_heal():
            aux_heal = cost_heal()
            store.dispatch("score", lambda score: score - aux_heal)

            update_heal()
            store.get("player").life = store.get("player").max_life

            window.delay(150)
    else:
        heal.set_curr_frame(0)

    window.set_background_color((0, 0, 0))

    # SCORE
    window.draw_text(
        "score: {}".format(store.get("score")),
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

    window.draw_text(
        "owned: {}".format(store.get("owned_strength")),
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

    window.draw_text(
        "owned: {}".format(store.get("owned_life")),
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
