from library.PPlay.animation import Animation

from environment import variables as gvar
from environment.instances import window, mouse, keyboard


title = Animation("./src/assets/menu/powerup_title.png", 1)
title.set_position(gvar.WIDTH / 2 - title.width / 2, 200 - title.height / 2)

power_button = Animation("./src/assets/menu/power.png", 2)
power_button.set_position(
    gvar.WIDTH / 2 - power_button.width / 2, 350 - power_button.height / 2
)

life_button = Animation("./src/assets/menu/life.png", 2)
life_button.set_position(
    gvar.WIDTH / 2 - life_button.width / 2, 500 - life_button.height / 2
)

def run():
    global title
    global power_button
    global life_button

    if keyboard.key_pressed("esc"):
        gvar.STATE = 1
        window.delay(150)

    if mouse.is_over_object(power_button):
        power_button.set_curr_frame(1)
        if mouse.is_button_pressed(1):
            pass
    else:
        power_button.set_curr_frame(0)

    if mouse.is_over_object(life_button):
        life_button.set_curr_frame(1)
        if mouse.is_button_pressed(1):
            pass
    else:
        life_button.set_curr_frame(0)

    window.set_background_color((0, 0, 0))

    title.draw()
    power_button.draw()
    life_button.draw()
