from library.PPlay.animation import Animation

from environment import variables as gvar
from environment.instances import keyboard, window, mouse


title = Animation("./src/assets/menu/title.png", 10)
title.set_position(gvar.WIDTH / 2 - title.width / 2, 200 - title.height / 2)
title.set_sequence_time(0, 10, 100)
title.play()

play_button = Animation("./src/assets/menu/play.png", 2)
play_button.set_position(
    gvar.WIDTH / 2 - play_button.width / 2, 375 - play_button.height / 2
)

rank_button = Animation("./src/assets/menu/rank.png", 2)
rank_button.set_position(
    gvar.WIDTH / 2 - rank_button.width / 2, 500 - rank_button.height / 2
)


def run():
    if keyboard.key_pressed("esc"):
        gvar.GAME_STARTED = False

    if mouse.is_over_object(play_button):
        play_button.set_curr_frame(1)
        if mouse.is_button_pressed(1):
            gvar.STATE = 1
    else:
        play_button.set_curr_frame(0)

    if mouse.is_over_object(rank_button):
        rank_button.set_curr_frame(1)
        if mouse.is_button_pressed(1):
            gvar.STATE = 4
    else:
        rank_button.set_curr_frame(0)

    window.set_background_color((0, 0, 0))

    title.update()

    title.draw()
    play_button.draw()
    rank_button.draw()
