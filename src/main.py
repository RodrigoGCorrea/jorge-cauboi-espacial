from PPlay.window import Window

WIDTH = 800
HEIGHT = 600

window = Window(WIDTH, HEIGHT)
window.set_title("JSC")

while True:
    window.update()