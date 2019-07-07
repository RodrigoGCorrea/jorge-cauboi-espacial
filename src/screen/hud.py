from environment import config 
from environment.instances import window, store

def run():
    # PRINT WAVE
    window.draw_text(
        "wave: {}".format(store.get("wave")),
        940,
        770,
        "./src/assets/fonts/pixel.ttf",
        size=20,
        color=(255, 255, 255),
    )

    window.draw_text(
        "score: {}".format(store.get("score")),
        710,
        770,
        "./src/assets/fonts/pixel.ttf",
        size=20,
        color=(255, 255, 255),
    )

    # PRINT LIFE
    window.draw_text(
        "life: {}".format(store.get("player").life),
        55,
        770,
        "./src/assets/fonts/pixel.ttf",
        size=20,
        color=(255, 255, 255),
    )
