from environment import variables as gvar
from environment.instances import window

from controller.player import player


def run():
    # PRINT WAVE
    from controller.enemy import wave

    window.draw_text(
        "wave: {}".format(wave),
        940,
        770,
        "./src/assets/fonts/pixel.ttf",
        size=20,
        color=(255, 255, 255),
    )

    window.draw_text(
        "score: {}".format(gvar.SCORE),
        710,
        770,
        "./src/assets/fonts/pixel.ttf",
        size=20,
        color=(255, 255, 255),
    )

    # PRINT LIFE
    window.draw_text(
        "life: {}".format(player.life),
        55,
        770,
        "./src/assets/fonts/pixel.ttf",
        size=20,
        color=(255, 255, 255),
    )
