# QueryF1DB.py
import sqlite3
import pandas as pd

class QueryF1DB:
    def __init__(self, db_path="F1Results.db"):
        self.conn = sqlite3.connect(db_path)

    def query_circuits_per_country(self):
        query = """
            SELECT country, COUNT(DISTINCT circuitId) AS num_circuits
            FROM circuits
            GROUP BY country;
        """
        return pd.read_sql_query(query, self.conn)

    def query_races_per_season(self):
        query = """
            SELECT year, COUNT(DISTINCT raceId) AS num_races
            FROM races
            GROUP BY year;
        """
        return pd.read_sql_query(query, self.conn)

    def query_constructors_per_nationality(self):
        query = """
            SELECT nationality, COUNT(DISTINCT constructorId) AS num_constructors
            FROM constructors
            GROUP BY nationality;
        """
        return pd.read_sql_query(query, self.conn)

    def query_constructor_points(self):
        query = """
            SELECT constructorId, SUM(points) AS total_points
            FROM constructor_results
            GROUP BY constructorId;
        """
        return pd.read_sql_query(query, self.conn)

    def query_constructor_participation(self):
        query = """
            SELECT constructorId, COUNT(DISTINCT raceId) AS num_participations
            FROM constructor_results
            GROUP BY constructorId;
        """
        return pd.read_sql_query(query, self.conn)
