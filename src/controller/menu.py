from library.PPlay.mouse import Mouse
from library.PPlay.animation import Animation

from environment import variables as gvar
from environment.instances import window, mouse


play_button = Animation("./src/assets/menu/play.png", 2)
play_button.set_position(
    gvar.WIDTH / 2 - play_button.width / 2, gvar.HEIGHT / 2 - play_button.height / 2
)


def run():
    if mouse.is_over_object(play_button):
        play_button.set_curr_frame(1)
        if mouse.is_button_pressed(1):
            gvar.STATE = 1
    else:
        play_button.set_curr_frame(0)

    window.set_background_color((0, 0, 0))

    window.draw_text(
        "Jorge The Space Cowboy",
        gvar.WIDTH / 2,
        gvar.HEIGHT / 2 - 220,
        "./src/assets/fonts/pixel.ttf",
        50,
        (255, 255, 255),
    )

    play_button.draw()
