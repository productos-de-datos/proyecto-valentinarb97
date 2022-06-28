def train_daily_model():
    """Entrena el modelo de pronóstico de precios diarios.

    Con las features entrene el modelo de proóstico de precios diarios y
    salvelo en models/precios-diarios.pkl


    """
    import pandas as pd
    from sklearn.linear_model import LinearRegression
    from sklearn.model_selection import train_test_split

    def load_data():
        import pandas as pd

        input = 'data_lake/business/features/precios_diarios.csv'
        data = pd.read_csv(input, sep=",")
        return data

    y = load_data()['precio']
    x = load_data()
    x.pop('precio')

    x = x['fecha'].str.split("-", expand=True)
    x.columns = ['year', 'month', 'day']
    x['fecha'] = x['year'] + x['month'] + x['day']
    x = x[['fecha']]

    x_train, x_test, y_train, y_test = train_test_split(
        x,
        y,
        test_size=0.25,
        random_state=123456,
    )

    Modelo_rl = LinearRegression()

    Modelo_rl.fit(x_train, y_train)

    def save_model_train():
        import pickle
        filename = 'src/models/precios-diarios.pikle'
        pickle.dump(Modelo_rl, open(filename, 'wb'))
    save_model_train()
    #raise NotImplementedError("Implementar esta función")


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    train_daily_model()

