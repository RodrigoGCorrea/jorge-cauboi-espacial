from environment import variables as gvar
from environment.instances import window

from controller.enemy import wave
from controller.player import player


def run():
    # PRINT WAVE
    window.draw_text(
        "wave: {}".format(wave),
        960,
        780,
        "./src/assets/fonts/pixel.ttf",
        size=20,
        color=(255, 255, 255),
    )

    # PRINT LIFE
    window.draw_text(
        "life: {}".format(player.life),
        75,
        780,
        "./src/assets/fonts/pixel.ttf",
        size=20,
        color=(255, 255, 255),
    )
