import pandas as pd

datos = pd.read_csv("cardata.csv",sep=",")

print(datos.columns) # ha cogido el primer registro como nombres de columnas

# creo los nombres de columnas
datos.columns = ["PRECIO","COSTE MANTENIMIENTO","PUERTAS","CAPACIDAD","TAMAÑO","SEGURIDAD","DECISION"]

print(datos.columns)
# PRECIO y PUERTAS de los ultimos 10 coches utilizando tail()
print(datos[["PRECIO" , "PUERTAS"]].tail(10))

# PRECIO y PUERTAS de los ultimos 10 coches sin utilizar tail()
print(datos[["PRECIO" , "PUERTAS"]][len(datos)-10:len(datos)])

# PRECIO y PUERTAS de los ultimos 10 coches sin utilizar tail() v2
print(datos[["PRECIO" , "PUERTAS"]][len(datos)-10:])

lista = [1, 2, 3]
print(dir(lista))

# que tengan 3 o 4 PUERTAS, SEGURIDAD alta, y DECISION acceptable
df_filtrado = datos[((datos["PUERTAS"] == "3") | (datos["PUERTAS"] == "4"))
                    & (datos["SEGURIDAD"] == "high") & (datos["DECISION"]=="acc")]
print(df_filtrado.head(10))  # muestra los primeros 10 registros

# sustituir PUERTAS 3 o PUERTAS 4 por el valor "entre 3 y 4"
datos["PUERTAS"].replace(("3","4"),("entre 3 y 4"),inplace=True)
print(datos["PUERTAS"].unique())  # ['2' 'entre 3 y 4' '5more']