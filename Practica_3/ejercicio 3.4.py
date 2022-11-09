from psycopg2 import Error
import psycopg2
import psycopg2.extras
from pandas import Series, DataFrame
import pandas as pd
import funciones
import json, os, boto3

# Leer CSV y devolver el dataframe
def ObtenerDataframe(dic):
    df = pd.read_csv('./Practica_3/top-1m.csv',header=None, sep=',', names=['nroDeOrden', 'dominio', 'entidad', 'tipo_entidad','pais'])
    df1 = DataFrame(df, columns=['nroDeOrden', 'dominio', 'entidad', 'tipo_entidad','pais'])
    ActualizarCSV(dic, df1)
    return df1

def ActualizarCSV(diccionario, df1):
    df1.loc[df1['tipo_entidad'].isnull(), 'codigo'] = 'USA'
    df1.loc[df1['tipo_entidad'] == 'uk', 'codigo'] = 'GBR'

    # Dataframe listo para ser cargado en la tabla sitio
    for key in diccionario:
        df1.loc[df1['tipo_entidad'] == key, 'codigo'] = diccionario.get(key)
  
    # CSV actualizado
    df1.to_csv(r'./Practica_3/top-1m-actualizado.csv', index = False, header=False)

# Leer los campos “code2” y “code” de la tabla country y generar un diccionario de la forma: d[code2] = code
def lecturaDeCampos(cursor, conexionBD):
    # Ejecutar la Query para obtener el code2 y code de la tabla country
    cursor.execute("SELECT code2, code FROM country")
    
    # Diccionario:
    dic = {}
    # Obtener todas las filas del resultado de la consulta anterior y devolver una lista de tuplas 
    diccionario = cursor.fetchall()
    for row in diccionario:
        dic[row[0].lower()] = row[1]
        
    cursor.close() # Cerrar consulta
    
    print("code2 | code")
    for k,v in diccionario:
        print( str(k), " | ", str(v))
        
    return dic
    
# Para cada lınea de la archivo ”top-1m.csv” separar el nro. de orden y el dominio
# Carga de los registros en la tabla Sitio de PostgreSQL
def cargarRegistros(dic):
    df1 = ObtenerDataframe(dic)
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
dic = lecturaDeCampos(cursor, conexionBD)
cargarRegistros(dic)



# QUERYS:
# SELECT count(*) FROM sitio

# SELECT * FROM sitio where countrycode != 'USA';

# delete from sitio