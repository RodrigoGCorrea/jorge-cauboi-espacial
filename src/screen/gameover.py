from library.PPlay.animation import Animation

from environment import variables as gvar
from environment.instances import keyboard, window, mouse


title = Animation("./src/assets/menu/gameover_title.png", 9)
title.set_position(gvar.WIDTH / 2 - title.width / 2, gvar.HEIGHT / 2 - title.height / 2)
title.set_sequence_time(0, 9, 100)
title.play()

def run():
    global title

    if keyboard.key_pressed("esc"):
        gvar.STATE = 0
        window.delay(150)
    
    if title.get_curr_frame() < title.get_final_frame() - 1:  
        title.update()

    window.set_background_color((0, 0, 0))
    title.draw()
