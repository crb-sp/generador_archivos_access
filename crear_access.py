import pyodbc
from dbConexion import Connection

def obtener_num (localidad):
    with Connection() as cursor:
        if cursor:
            cursor.execute ("SELECT numero FROM numeros JOIN localidades ON numeros.localidad_id = localidades.localidad_id WHERE localidades.ciudad = %s", (localidad,))
            return [row[0] for row in cursor.fetchall()]
        
def crear_arch (nom_arch, numeros):
    conn_access = pyodbc.connect(r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=' + nom_arch + '.accdb;')
    cursor_access = conn_access.cursor()
    
    cursor_access.execute ("CREATE TABLE campania (numero VARCHAR(15))")   
    
    for i in range (0, len(numeros), 7000):
        batch = numeros [i : i + 7000]
        for numero in batch:
            cursor_access.execute ("INSERT INTO campania (numero) VALUES (?)", (str(numero),))                 

    conn_access.commit()
    cursor_access.close()
    conn_access.close()
    
def main ():
    localidad = 'LocalidadEjemplo'
    nom_arch = 'Campania'    
    
    numeros = obtener_num (localidad)
    
    crear_arch (nom_arch, numeros)
    
if __name__ == "__main__":
    main()    

