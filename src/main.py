from PPlay.window import Window
import globals

def main():
    window = Window(globals.WIDTH, globals.HEIGHT)
    window.set_title("JSC")

    while globals.GAME_STARTED:
        window.update()

if __name__ == "__main__":
    main()