from sqlite3 import connect, Error

class Database(object):
    def __init__(self):
        self.con = None
        try:
            self.con = connect('scores.db')
            c = self.con.cursor()
            c.execute("CREATE TABLE IF NOT EXISTS scores (name TEXT, score INT, wave INT);")

            self.con.commit()
        except Error as e:
            print("SQLITE ERRO: {}".format(e))
        
    def save_score(self, name, score, wave):
        try:
            c = self.con.cursor()
            c.execute("INSERT INTO scores VALUES (?, ?, ?);", (name, score, wave))
            self.con.commit()
        except Error as e:
            print("SQLITE ERRO: {}".format(e))
    
    def get_scores(self):
        data = None

        try:
            c = self.con.cursor()
            c.execute("SELECT * FROM scores ORDER BY score DESC LIMIT 10;")

            data = c.fetchall()

        except Error as e:
            print("SQLITE ERRO: {}".format(e))
        
        return data

    def __del__(self):
        self.con.close()
