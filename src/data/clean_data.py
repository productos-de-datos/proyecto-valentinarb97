def load_data():
    import pandas as pd
    import glob

    path_file = glob.glob(r'data_lake/raw/*.csv')
    li = []

    for filename in path_file:
        df = pd.read_csv(filename, index_col=None, header=0)
        li.append(df)
    return li


def read_data(li):
    import pandas as pd
    read_file = pd.concat(li, axis=0, ignore_index=True)
    read_file = read_file[read_file["Fecha"].notnull()]
    return read_file


def transfort_data(read_file):
    import pandas as pd
    fechas_data = read_file.iloc[:, 0]  # fecha

    lista_datos = []
    precio = 0
    contador_filas = 0

    for fecha in fechas_data:
        for hora in range(0, 24):
            precio = (read_file.iloc[contador_filas, (hora+1)])
            lista_datos.append([fecha, hora, precio])
        contador_filas += 1

    return lista_datos


def create_dataframe(lista_datos):
    import pandas as pd
    data_ordenada = pd.DataFrame(
        lista_datos, columns=["fecha", "hora", "precio"])
    data_ordenada = data_ordenada[data_ordenada["precio"].notnull()]
    return data_ordenada


def save_data(data_ordenada):
    data_ordenada.to_csv("data_lake/cleansed/precios-horarios.csv",
                         index=None, header=True)


def clean_data():
    """Realice la limpieza y transformación de los archivos CSV.

    Usando los archivos data_lake/raw/*.csv, cree el archivo data_lake/cleansed/precios-horarios.csv.
    Las columnas de este archivo son:

    * fecha: fecha en formato YYYY-MM-DD
    * hora: hora en formato HH
    * precio: precio de la electricidad en la bolsa nacional

    Este archivo contiene toda la información del 1997 a 2021.


    """
    li = load_data()
    read_file = read_data(li)
    lista_datos = transfort_data(read_file)
    data_ordenada = create_dataframe(lista_datos)
    save_data(data_ordenada)

    #raise NotImplementedError("Implementar esta función")


def test_columns_dataframe():
    li = load_data()
    read_file = read_data(li)
    lista_datos = transfort_data(read_file)
    assert list(create_dataframe(lista_datos).columns.values) == [
        'fecha', 'hora', 'precio']


if __name__ == "__main__":

    import doctest

    doctest.testmod()
    clean_data()
