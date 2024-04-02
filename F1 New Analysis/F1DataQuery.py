import sqlite3
import pandas as pd

class F1DataQuery:
    def __init__(self, database_path="F1DataStore.db"):
        self.connection = sqlite3.connect(database_path)

    def get_circuits_per_country(self):
        query = """
            SELECT country, COUNT(DISTINCT circuitId) AS num_circuits
            FROM circuits
            GROUP BY country;
        """
        return pd.read_sql_query(query, self.connection)

    def get_races_per_season(self):
        query = """
            SELECT year, COUNT(DISTINCT raceId) AS num_races
            FROM races
            GROUP BY year;
        """
        return pd.read_sql_query(query, self.connection)

    def get_constructors_per_nationality(self):
        query = """
            SELECT nationality, COUNT(DISTINCT constructorId) AS num_constructors
            FROM constructors
            GROUP BY nationality;
        """
        return pd.read_sql_query(query, self.connection)

    def get_constructor_points(self):
        query = """
            SELECT constructorId, SUM(points) AS total_points
            FROM constructor_results
            GROUP BY constructorId;
        """
        return pd.read_sql_query(query, self.connection)

    def get_constructor_participation(self):
        query = """
            SELECT constructorId, COUNT(DISTINCT raceId) AS num_participations
            FROM constructor_results
            GROUP BY constructorId;
        """
        return pd.read_sql_query(query, self.connection)