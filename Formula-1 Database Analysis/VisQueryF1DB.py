# VisQueryF1DB.py
import matplotlib.pyplot as plt

class VisQueryF1DB:
    def __init__(self, query_module):
        self.query_module = query_module

    def plot_circuits_per_country(self):
        data = self.query_module.query_circuits_per_country()
        data.plot(kind="bar", x="country", y="num_circuits", legend=False)
        plt.title("Number of Circuits per Country")
        plt.xlabel("Country")
        plt.ylabel("Number of Circuits")
        plt.show()

    def plot_races_per_season(self):
        data = self.query_module.query_races_per_season()
        plt.figure(figsize=(20, 6))  # Increase the figure size
        bars = plt.bar(data["year"], data["num_races"], width=1.2)  # Adjust bar width
        plt.title("Number of Races per Season")
        plt.xlabel("Year")
        plt.ylabel("Number of Races")

        # Set a custom rotation for x-axis labels
        plt.xticks(data["year"], rotation=45, ha="right")

        plt.tight_layout()  # Adjust layout to prevent overlapping labels
        plt.show()

    def plot_constructors_per_nationality(self):
        data = self.query_module.query_constructors_per_nationality()
        plt.figure(figsize=(14, 6))  # Increase the figure size
        bars = plt.bar(data["nationality"], data["num_constructors"], width=0.8)  # Adjust bar width
        plt.title("Number of Constructors per Nationality")
        plt.xlabel("Nationality")
        plt.ylabel("Number of Constructors")

        # Set a custom rotation for x-axis labels
        plt.xticks(data["nationality"], rotation=45, ha="right")

        plt.tight_layout()
        plt.show()

    def plot_constructor_points(self):
        data = self.query_module.query_constructor_points()
        plt.figure(figsize=(20, 6))  # Increase the figure size
        bars = plt.bar(data["constructorId"], data["total_points"], width=0.8)  # Adjust bar width
        plt.title("Total Points per Constructor")
        plt.xlabel("Constructor ID")
        plt.ylabel("Total Points")

        # Set a custom rotation for x-axis labels
        plt.xticks(data["constructorId"], rotation=45, ha="right")

        plt.grid(True)
        plt.tight_layout()
        plt.show()

    def plot_constructor_participation(self):
        data = self.query_module.query_constructor_participation()
        plt.figure(figsize=(20, 6))  # Increase the figure size
        bars = plt.bar(data["constructorId"], data["num_participations"], width=0.8)  # Adjust bar width
        plt.title("Number of Participations per Constructor")
        plt.xlabel("Constructor ID")
        plt.ylabel("Number of Participations")

        # Set a custom rotation for x-axis labels
        plt.xticks(data["constructorId"], rotation=45, ha="right")

        plt.grid(True)
        plt.tight_layout()
        plt.show()
