from psycopg2 import Error
import psycopg2
import psycopg2.extras
from pandas import Series, DataFrame
import pandas as pd
import funciones


# Leer CSV y devolver el dataframe
def ObtenerDataframe():
    df = pd.read_csv('./Practica_3/top-1m.csv')
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
    
    print("code2 | code")
    for k,v in diccionario:
        print( str(k), " | ", str(v))
    
# Para cada lınea de la archivo ”top-1m.csv” separar el nro. de orden y el dominio
def ejercicioDos():
    df1 = ObtenerDataframe()
    df1['nroDeOrden'] = df1['nroDeOrden'].str.split('.').str[0]
    df1['dominio'] = df1['dominio'].str.split('.').str[2]
    
    print (df1)
    
def ejercicioCuatro():
    df1 = ObtenerDataframe()
    _, conexionBD = funciones.conexion()
    cursor1 = conexionBD.cursor()
    for _, fila in df1.iterrows():
        if(str(fila['codigo']) != 'nan'):
            postgres_insert_query = "INSERT INTO sitio (id, entidad,tipo_entidad,pais,countrycode) VALUES(%s,%s,%s,%s,%s)"
            record_to_insert = (fila['nroDeOrden'], fila['entidad'], fila['tipo_entidad'], fila['pais'], fila['codigo'])
            cursor1.execute(postgres_insert_query, record_to_insert)
            conexionBD.commit()
    cursor1.close()

    print("¡Datos cargados con exito!")

cursor, conexionBD = funciones.conexion()
ejercicioUno(cursor, conexionBD)
# ejercicioDos()
# ejercicioTres()
ejercicioCuatro()
