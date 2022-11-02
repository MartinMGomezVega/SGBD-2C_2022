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
    # finally:
    #     # Cerrar la conexion
    #     if(conexionBD):
    #         cursor.close()
    #         conexionBD.close()
    #         print("Conexion Cerrada")