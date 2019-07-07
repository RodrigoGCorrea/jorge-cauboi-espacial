class Store(object):
    def __init__(self, initial_store=None):
        if initial_store != None and type(initial_store) is dict:
            self.store = initial_store
        else:
            self.store = {
                "game_started": True,
                "state": 0,
                "score": 0,
                "enemy_mtx": [],
                "wave": 1,
                "player": None,
                "owned_strength": 0,
                "owned_life": 0,
                "owned_heal": 0
            }

    def dispatch(self, name, value=0, callback=None):
        if callback != None and callable(callback):
            self.store[name] = callback(self.store[name])
        else:
            self.store[name] = value

    def get(self, name):
        return self.store[name]
