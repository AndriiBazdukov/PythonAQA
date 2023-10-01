class Apple:

    def __init__(self, number_of_employees: int, company_net_worth: float, annual_budget: float, production: list):
        self.number_of_employees = number_of_employees
        self.company_net_worth = company_net_worth
        self.annual_budget = annual_budget
        self.production = production

    def show_company_info(self):
        products = ', '.join(map(str, self.production))
        print(f"{self.__class__.__name__} company with net worth of {self.company_net_worth}$, we are a top sellers"
              f" of {products} on the market, we have {self.number_of_employees} employees and "
              f"{self.annual_budget}$ annual budget")

    @staticmethod
    def create_item(item):
        print(f"Here is your new {item}")


if __name__ == "__main__":
    apple = Apple(10000, 10000000000, 1000000000, ["Smart phone"
                                                   , "Tablet", "Laptop"])
    apple.show_company_info()
