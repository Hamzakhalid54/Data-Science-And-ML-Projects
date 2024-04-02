import matplotlib.pyplot as plt

class F1DataVisualization:
    def __init__(self, query_module):
        self.query_module = query_module

    def show_circuits_per_country_pie(self):
        data = self.query_module.get_circuits_per_country()
        plt.figure(figsize=(10, 10))
        plt.pie(data["num_circuits"], labels=data["country"], autopct='%1.1f%%', startangle=90)
        plt.title("Distribution of Circuits per Country")
        plt.show()

    def display_races_per_season_line(self):
        data = self.query_module.get_races_per_season()
        plt.figure(figsize=(12, 6))
        plt.plot(data["year"], data["num_races"], marker='o')
        plt.title("Number of Races per Season (Line Chart)")
        plt.xlabel("Year")
        plt.ylabel("Number of Races")
        plt.grid(True)
        plt.show()

    def present_constructors_per_nationality_horizontal_bar(self):
        data = self.query_module.get_constructors_per_nationality()
        plt.figure(figsize=(10, 8))
        bars = plt.barh(data["nationality"], data["num_constructors"])
        plt.title("Number of Constructors per Nationality (Horizontal Bar Chart)")
        plt.xlabel("Number of Constructors")
        plt.ylabel("Nationality")
        plt.tight_layout()
        plt.show()

    def visualize_constructor_points_boxplot(self):
        data = self.query_module.get_constructor_points()
        plt.figure(figsize=(10, 6))
        plt.boxplot(data["total_points"])
        plt.title("Boxplot of Total Points per Constructor")
        plt.ylabel("Total Points")
        plt.show()

    def plot_constructor_participation_scatter(self):
        data = self.query_module.get_constructor_participation()
        plt.figure(figsize=(10, 6))
        plt.scatter(data["constructorId"], data["num_participations"])
        plt.title("Scatter Plot of Participations per Constructor")
        plt.xlabel("Constructor ID")
        plt.ylabel("Number of Participations")
        plt.grid(True)
        plt.tight_layout()
        plt.show()
