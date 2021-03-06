from library.PPlay.animation import Animation

from classes.database import Database

from environment import config
from environment.instances import keyboard, window, mouse, store

title = Animation("./src/assets/menu/gameover_title.png", 9)
title.set_position(
    config.WIDTH / 2 - title.width / 2, config.HEIGHT / 2 - title.height / 2
)
title.set_sequence_time(0, 9, 100)
title.play()


def run():
    global title

    animation_completed = False

    if title.get_curr_frame() < title.get_final_frame() - 1:
        title.update()
    else:
        animation_completed = True
        title.set_curr_frame(0)

    window.set_background_color((0, 0, 0))
    title.draw()

    if animation_completed:
        aux_name = input("Qual seu nome? \n")

        while len(aux_name) > 9 or len(aux_name) < 3:
            print("Por favor, insira um nome entre 3 e 9 caracteres.\n")
            aux_name = input("Qual seu nome? \n")

        Database().save_score(aux_name.lower(), store.get("score"), store.get("wave"))

        return True

    else:
        return False
