from library.PPlay.sprite import Sprite

from classes.database import Database

from environment import config
from environment.instances import window, keyboard, store

title = Sprite("./src/assets/menu/rank_title.png")
title.set_position(config.WIDTH / 2 - title.width / 2, 200 - title.height / 2)


def run():
    if keyboard.key_pressed("esc"):
        store.dispatch("state", value=0)
        window.delay(150)

    window.set_background_color((0, 0, 0))

    data = Database().get_scores()
    data.insert(0, ["name:", "score:", "wave:"])
    i = 0
    for d in data:
        draw_name(d[0], 280, 300 + i)
        draw_score(d[1], 540, 300 + i)
        draw_wave(d[2], 810, 300 + i)
        i += 40

    title.draw()


def draw_name(name, x, y):
    window.draw_text(
        "{}".format(name),
        x,
        y,
        "./src/assets/fonts/pixel.ttf",
        size=30,
        color=(255, 255, 255),
    )


def draw_score(score, x, y):
    window.draw_text(
        "{}".format(score),
        x,
        y,
        "./src/assets/fonts/pixel.ttf",
        size=30,
        color=(255, 255, 255),
    )


def draw_wave(wave, x, y):
    window.draw_text(
        "{}".format(wave),
        x,
        y,
        "./src/assets/fonts/pixel.ttf",
        size=30,
        color=(255, 255, 255),
    )
