from psycopg2 import Error
import psycopg2
import psycopg2.extras
from pandas import Series, DataFrame
import pandas as pd

def cargaCodigo(diccionario):
	df1.loc[df1['pais'].isnull(), 'codigo'] = 'USA'
	df1.loc[df1['pais'] == 'uk', 'codigo'] = 'GBR'
		
	for key in diccionario:
		df1.loc[df1['pais'] == key, 'codigo'] = diccionario.get(key)
	
def fun(h):
	print(len(h))
	return (len(h) == 2)

# 2. Para cada lınea de la archivo ”top-1m.csv”separar el nro. de orden y el dominio
df = pd.read_csv('top-1m.csv')

df1 = DataFrame(df, columns=['nroDeOrden', 'dominio', 'entidad', 'tipo_entidad','pais'])

df1['entidad'] = df1['dominio'].str.split('.').str[0]
df1['pais'] = df1['dominio'].str.split('.').str[2]


# 3. Separar el dominio en los tres (o dos) campos que lo componen
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

try:
	conexionBD = psycopg2.connect(database = 'world', user = 'postgres', host = 'localhost', password = '1327')
	
	cursor = conexionBD.cursor(cursor_factory=psycopg2.extras.DictCursor)
 
    # Ejecutar la Query
	cursor.execute("SELECT code2, code FROM country")
	d = {}
	diccionario = cursor.fetchall()
	
    # 1. Leer los campos “code2” y “code” de la tabla country y generar un diccionario de la forma: d[code2] = code
	for row in diccionario:
		d[row[0].lower()] = row[1]
		
	cursor.close()
	
	cargaCodigo(d)
	
	cursor1 = conexionBD.cursor()

    # 4. Hacer la insercion del registro correspondiente en la tabla “sitio” haciendo la traduccion correspondiente del paıs
	for indice_fila, fila in df1.iterrows():
		if(str(fila['codigo']) != 'nan'):
			postgres_insert_query = "INSERT INTO sitio (id, entidad,tipo_entidad,pais,countrycode) VALUES(%s,%s,%s,%s,%s)"
			record_to_insert = (fila['nroDeOrden'], fila['entidad'], fila['tipo_entidad'], fila['pais'], fila['codigo'])
			cursor1.execute(postgres_insert_query, record_to_insert)
		
			conexionBD.commit()
	cursor1.close()

	print("¡Datos cargados con exito!")

except (Exception, psycopg2.DatabaseError) as error :
    print ("Error al cargar los datos", error)

finally:
    #closing database connection.
	if(conexionBD):
		cursor.close()
		conexionBD.close()
		print("Conexion Cerrada")
