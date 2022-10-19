from psycopg2 import Error
import psycopg2
import psycopg2.extras
from pandas import Series, DataFrame
import pandas as pd

# Conectaxion a la base de datos
def conexion():
    try:
        conexionBD = psycopg2.connect(database = 'world', user = 'postgres', host = 'localhost', password = '1327')
        print (conexionBD)
        cursor = conexionBD.cursor(cursor_factory=psycopg2.extras.DictCursor)
        return cursor, conexionBD
    
    except (Exception, psycopg2.DatabaseError) as error :
        print ("Error al conectarse con la base de datos", error)

    # Cerar la conexion al final
    finally:
        # Cerrar la conexion
        if(conexionBD):
            cursor.close()
            conexionBD.close()
            print("Conexion Cerrada")

# Leer CSV y devolver el dataframe
def ObtenerDataframe():
    df = pd.read_csv('top-1m.csv')
    df1 = DataFrame(df, columns=['nroDeOrden', 'dominio', 'entidad', 'tipo_entidad','pais'])
    return df1



# 1. Leer los campos “code2” y “code” de la tabla country y generar un diccionario de la forma: d[code2] = code
def ejercicioUno(cursor, conexionBD):
    # Ejecutar la Query para obtener el code2 y code de la tabla country
    cursor.execute("SELECT code2, code FROM country")
    
    # Diccionario:
    d = {}
    # Obtener todas las filas del resultado de la consulta anterior y devolver una lista de tuplas 
    diccionario = cursor.fetchall()
    for row in diccionario:
        d[row[0].lower()] = row[1]
        
    cursor.close() # Cerrar consulta
    
    # print("Diccionario: ")

def ejdos():
    df1 = ObtenerDataframe()
    # Split dobre el dominio

curs, conex = conexion()
ejercicioUno(curs, conex)
