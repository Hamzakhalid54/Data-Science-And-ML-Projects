import sqlite3
import pandas as pd
import os

class F1Database:
    def __init__(self, database_path="F1DataStores.db"):
        self.database_path = database_path
        self.connection = sqlite3.connect(database_path)
        self.initialize_tables()

    def initialize_tables(self):
        with self.connection:
            cursor = self.connection.cursor()

        # Circuits Table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS circuits (
                circuitId INTEGER PRIMARY KEY,
                circuitRef TEXT,
                name TEXT,
                location TEXT,
                country TEXT,
                lat REAL,
                lng REAL,
                alt INTEGER,
                url TEXT
            );
        """)

        # Constructor Results Table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS constructor_results (
                constructorResultsId INTEGER PRIMARY KEY,
                raceId INTEGER,
                constructorId INTEGER,
                points REAL,
                status TEXT
                -- Add other columns as needed
            );
        """)

        # Constructor Standings Table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS constructor_standings (
                constructorStandingsId INTEGER PRIMARY KEY,
                raceId INTEGER,
                constructorId INTEGER,
                points REAL,
                position INTEGER,
                positionText TEXT,
                wins INTEGER
                -- Add other columns as needed
            );
        """)

        # Constructors Table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS constructors (
                constructorId INTEGER PRIMARY KEY,
                constructorRef TEXT,
                name TEXT,
                nationality TEXT,
                url TEXT
            );
        """)

        # Driver Standings Table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS driver_standings (
                driverStandingsId INTEGER PRIMARY KEY,
                raceId INTEGER,
                driverId INTEGER,
                points REAL,
                position INTEGER,
                positionText TEXT,
                wins INTEGER
                -- Add other columns as needed
            );
        """)

        # Drivers Table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS drivers (
                driverId INTEGER PRIMARY KEY,
                driverRef TEXT,
                number INTEGER,
                code TEXT,
                forename TEXT,
                surname TEXT,
                dob TEXT,
                nationality TEXT,
                url TEXT
                -- Add other columns as needed
            );
        """)

        # Lap Times Table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS lap_times (
                raceId INTEGER,
                driverId INTEGER,
                lap INTEGER,
                position INTEGER,
                time TEXT,
                milliseconds INTEGER
                -- Add other columns as needed
            );
        """)

        # Pit Stops Table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS pit_stops (
                raceId INTEGER,
                driverId INTEGER,
                stop INTEGER,
                lap INTEGER,
                time TEXT,
                duration TEXT,
                milliseconds INTEGER
                -- Add other columns as needed
            );
        """)

        # Qualifying Table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS qualifying (
                qualifyId INTEGER PRIMARY KEY,
                raceId INTEGER,
                driverId INTEGER,
                constructorId INTEGER,
                number INTEGER,
                position INTEGER,
                q1 TEXT,
                q2 TEXT,
                q3 TEXT
                -- Add other columns as needed
            );
        """)

        # Races Table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS races (
                raceId INTEGER PRIMARY KEY,
                year INTEGER,
                round INTEGER,
                circuitId INTEGER,
                name TEXT,
                date TEXT,
                time TEXT,
                url TEXT,
                fp1_date TEXT,
                fp1_time TEXT,
                fp2_date TEXT,
                fp2_time TEXT,
                fp3_date TEXT,
                fp3_time TEXT,
                quali_date TEXT,
                quali_time TEXT,
                sprint_date TEXT,
                sprint_time TEXT
            );
        """)

        # Results Table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS results (
                resultId INTEGER PRIMARY KEY,
                raceId INTEGER,
                driverId INTEGER,
                constructorId INTEGER,
                number INTEGER,
                grid INTEGER,
                position INTEGER,
                positionText TEXT,
                positionOrder INTEGER,
                points REAL,
                laps INTEGER,
                time TEXT,
                milliseconds INTEGER,
                fastestLap INTEGER,
                fastestLapTime TEXT,
                statusId INTEGER
                -- Add other columns as needed
            );
        """)

        # Seasons Table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS seasons (
                year INTEGER PRIMARY KEY,
                url TEXT
                -- Add other columns as needed
            );
        """)

        # Sprint Results Table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS sprint_results (
                resultId INTEGER PRIMARY KEY,
                raceId INTEGER,
                driverId INTEGER,
                constructorId INTEGER,
                number INTEGER,
                grid INTEGER,
                position INTEGER,
                positionText TEXT,
                positionOrder INTEGER,
                points REAL,
                laps INTEGER,
                time TEXT,
                milliseconds INTEGER,
                fastestLap INTEGER,
                fastestLapTime TEXT,
                statusId INTEGER
                -- Add other columns as needed
            );
        """)

        # Status Table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS status (
                statusId INTEGER PRIMARY KEY,
                status TEXT
                -- Add other columns as needed
            );
        """)
            

    def create_table(self, cursor, table_name, columns):
        columns_str = ", ".join(columns)
        cursor.execute(f"CREATE TABLE IF NOT EXISTS {table_name} ({columns_str});")

    def load_csv(self, csv_file_path, table_name):
        if os.path.exists(csv_file_path):
            df = pd.read_csv(csv_file_path)
            df.to_sql(table_name, self.connection, if_exists="replace", index=False)
        else:
            print(f"File not found: {csv_file_path}")
