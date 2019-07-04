from library.PPlay.window import Window
from library.PPlay.keyboard import Keyboard
from library.PPlay.mouse import Mouse

from . import variables as gvar

window = Window(gvar.WIDTH, gvar.HEIGHT)
window.set_title("JSC 1.0.0")

keyboard = Keyboard()

mouse = Mouse()
