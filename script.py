import random,sys,os
import mysql.connector
import sqlite3

mysql = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "1234",
    database = "dannafox"
)

def obtener_num (localidad, cantidad = 7000):
    conexion = sqlite3.connect("dannafox.db")
    cursor = conexion.cursor()
    
    cursor.execute("""
        SELECT numero FROM numeros JOIN localidades ON numeros.localidad_id = localidades.localidad_id WHERE localidades.ciudad = ?           
                   """, (localidad,))
    numeros = [row[0] for row in cursor.fetchall()]
    conexion.close()
    
    if len(numeros) < cantidad:
        print (f"No hay suficientes números en la localidad {localidad}, solo contiene {len(numeros)} números.")
        sys.exit(1)
        
        return random.sample(numeros, cantidad)
    
def crear_archivo (numeros, cantidad):
    if not os.path.exists("campanias"):
        os.makedirs("campanias")
    
    for i in range (1, cantidad + 1):
        numeros = obtener_num(localidad)
        
        nom_archivo = f"campanias/Campania_{localidad}_{i}.db"
        
        conexion = sqlite3.connect(nom_archivo)
        cursor = conexion.cursor()
        
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS numeros (numero_id INTEGER PRIMARY KEY AUTOINCREMENT, numero TEXT NOT NULL)           
                       """)
    
        cursor.executemany("INSERT INTO numeros (numero) VALUES (?)", [(str(num),) for num in numeros])
        
        conexion.commit()
        conexion.close()
        
        print (f"Archivo '{nom_archivo}' creado. Contiene {len(numeros)} números telefónicos.")
        
if __name__=="__main__":
    if len(sys.argv) < 2:
        print ("") 
        sys.exit(1)       
        
        localidad = sys.argv[1]
        archivos = int(sys.argv [2]) if len(sys.argv) > 2 else 10
        
        crear_archivo (localidad, cantidad = 10)