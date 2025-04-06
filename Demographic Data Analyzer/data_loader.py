import pandas as pd

class DataLoader:
    """
    Clase encargada de cargar y preparar los datos demográficos.
    """
    def __init__(self, file_path="data/adult.data.csv"):
        self.file_path = file_path
        self.df = None

    def load_data(self):
        """
        Cargar los datos desde el archivo CSV y asignar nombres de columnas.
        """
        self.df = pd.read_csv(self.file_path, header=None, names=[
            'age', 'workclass', 'fnlwgt', 'education', 'education-num',
            'marital-status', 'occupation', 'relationship', 'race', 'sex',
            'capital-gain', 'capital-loss', 'hours-per-week', 'native-country',
            'salary'
        ])
        
        self.df = self.df.apply(lambda col: col.str.strip() if col.dtype == 'object' else col)
        self.df['sex'] = self.df['sex'].replace({'male': 'Male', 'female': 'Female'})
        self.df['salary'] = self.df['salary'].replace({'<50K': '<=50K', '>50K': '>50K'})
        self.df = self.df.dropna()  # Eliminar filas con valores faltantes

    def get_data(self):
        """
        Obtener el DataFrame cargado.
        """
        if self.df is None:
            raise ValueError("Data has not been loaded. Call load_data() first.")
        return self.df
