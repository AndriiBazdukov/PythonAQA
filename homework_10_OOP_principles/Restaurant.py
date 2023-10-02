class Restaurant:
    def __init__(self, restaurant_cuisine: str, number_of_tables):
        self.number_of_tables = number_of_tables
        self.restaurant_cuisine = restaurant_cuisine

    def show_restaurant_cuisine(self):
        print(f"Restaurant of {self.restaurant_cuisine} food")

    def show_number_of_tables(self):
        print(f"Number of tables: {self.number_of_tables}")