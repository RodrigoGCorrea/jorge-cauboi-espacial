from library.PPlay.window import Window
from library.PPlay.keyboard import Keyboard

from . import variables as gvar

window = Window(gvar.WIDTH, gvar.HEIGHT)
window.set_title("JSC 0.1.0 alpha")

keyboard = Keyboard()
