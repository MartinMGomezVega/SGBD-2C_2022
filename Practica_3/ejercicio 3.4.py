from psycopg2 import Error
import psycopg2
import psycopg2.extras
from pandas import Series, DataFrame
import pandas as pd

# Conectaxion a la base de datos
def conexion():
    try:
        conexionBD = psycopg2.connect(database = 'world', user = 'postgres', host = 'localhost', password = '1327')
        cursor = conexionBD.cursor(cursor_factory=psycopg2.extras.DictCursor)
        return cursor, conexionBD
    
    except (Exception, psycopg2.DatabaseError) as error :
        print ("Error al conectarse con la base de datos", error)

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

def cargarCodigo(diccionario):
    df1 = ObtenerDataframe()
    df1.loc[df1['pais'].isnull(), 'codigo'] = 'USA'
    df1.loc[df1['pais'] == 'uk', 'codigo'] = 'GBR'
    for key in diccionario:
        df1.loc[df1['pais'] == key, 'codigo'] = diccionario.get(key)

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
    cargarCodigo(d)
    
    print("Diccionario: ")
 
# 2. Para cada lınea de la archivo ”top-1m.csv”separar el nro. de orden y el dominio
def ejercicioDos():
    df1 = ObtenerDataframe()
    df1['entidad'] = df1['dominio'].str.split('.').str[0]
    df1['pais'] = df1['dominio'].str.split('.').str[2]

# 3. Separar el dominio en los tres (o dos) campos que lo componen
def ejercicioTres():
    df1 = ObtenerDataframe()
    for i, row in df1.iterrows():
        txt = str(row['dominio']).split('.')[1]
        print(i)
        if((len(txt) == 2) & (txt != 'co')):
            if(str(row['pais']) == 'nan'):
                df1.loc[i,'pais'] = txt
            else:
                df1.loc[i,'tipo_entidad'] = txt
        else:
            df1.loc[i,'tipo_entidad'] = txt
            
    print (df1)

# 4. Hacer la insercion del registro correspondiente en la tabla “sitio” haciendo la traduccion correspondiente del paıs
def ejercicioCuatro():
    df1 = ObtenerDataframe()
    _, conexionBD = conexion()
    cursor1 = conexionBD.cursor()
    for _, fila in df1.iterrows():
        if(str(fila['codigo']) != 'nan'):
            postgres_insert_query = "INSERT INTO sitio (id, entidad,tipo_entidad,pais,countrycode) VALUES(%s,%s,%s,%s,%s)"
            record_to_insert = (fila['nroDeOrden'], fila['entidad'], fila['tipo_entidad'], fila['pais'], fila['codigo'])
            cursor1.execute(postgres_insert_query, record_to_insert)
            conexionBD.commit()
    cursor1.close()

    print("¡Datos cargados con exito!")

curs, conex = conexion()
ejercicioUno(curs, conex)
ejercicioDos()
ejercicioTres()
ejercicioCuatro()