import mysql.connector

class Connection:
    def __init__(self):
        try:
            self.connection = mysql.connector.connect(
                host = "localhost",
                user = "root",
                password = "1234",
                database = "dannafox"
            )
        except mysql.connector.Error as e:
            print(f"Error al conectar con la base de datos: {e}")
            self.connection = None

    def __enter__(self):
        return self.connection.cursor() if self.connection else None

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.connection:
            self.connection.commit()
            self.connection.close()
