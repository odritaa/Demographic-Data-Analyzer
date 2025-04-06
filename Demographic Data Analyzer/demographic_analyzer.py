class DemographicAnalyzer:
    """
    Clase encargada de realizar los análisis demográficos.
    """
    def __init__(self, df):
        self.df = df

    def get_race_count(self):
        """
        Número de personas por raza.
        """
        return self.df['race'].value_counts()

    def get_average_age_men(self):
        """
        Edad promedio de los hombres.
        """
        men = self.df[self.df['sex'] == 'Male']
        return round(men['age'].mean(), 1) if not men.empty else 0

    def get_percentage_bachelors(self):
        """
        Porcentaje de personas con licenciatura (Bachelors).
        """
        bachelors_count = (self.df['education'] == 'Bachelors').sum()
        return round((bachelors_count / len(self.df)) * 100, 1)

    def get_higher_education_rich(self):
        """
        Porcentaje de personas con educación avanzada que ganan >50K.
        """
        higher_education = self.df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])
        return round(
            (self.df[higher_education & (self.df['salary'] == '>50K')].shape[0] /
             self.df[higher_education].shape[0]) * 100,
            1
        )

    def get_lower_education_rich(self):
        """
        Porcentaje de personas sin educación avanzada que ganan >50K.
        """
        higher_education = self.df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])
        lower_education = ~higher_education
        return round(
            (self.df[lower_education & (self.df['salary'] == '>50K')].shape[0] /
             self.df[lower_education].shape[0]) * 100,
            1
        )

    def get_min_work_hours(self):
        """
        Mínimo de horas trabajadas por semana.
        """
        return self.df['hours-per-week'].min()

    def get_rich_percentage_min_hours(self):
        """
        Porcentaje de personas que trabajan las horas mínimas y ganan >50K.
        """
        min_work_hours = self.get_min_work_hours()
        num_min_workers = self.df[self.df['hours-per-week'] == min_work_hours]
        return round(
            (num_min_workers[num_min_workers['salary'] == '>50K'].shape[0] / num_min_workers.shape[0]) * 100,
            1
        )

    def get_highest_earning_country(self):
        """
        País con mayor porcentaje de personas que ganan >50K.
        """
        country_percentage = (
            self.df[self.df['salary'] == '>50K']['native-country'].value_counts() /
            self.df['native-country'].value_counts() * 100
        ).fillna(0).sort_values(ascending=False)
        return country_percentage.idxmax(), round(country_percentage.max(), 1)

    def get_most_common_occupation_india(self):
        """
        Ocupación más común entre personas que ganan >50K en India.
        """
        india_rich = self.df[
            (self.df['native-country'] == 'India') & (self.df['salary'] == '>50K')
        ]
        return india_rich['occupation'].value_counts().idxmax() if not india_rich.empty else "No data available"
