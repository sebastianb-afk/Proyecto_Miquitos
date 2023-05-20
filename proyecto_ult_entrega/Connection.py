import psycopg2

class Connection:
    def __init__(self):
        self.connection = None

    def openConnection(self):
        try:
            self.connection = psycopg2.connect(user = "postgres", password = "1", database = "miquitos", host = "localhost", port = "5433")

        except Exception as e:
            print(e)

    def CloseConnection (self):
        self.connection.close()
