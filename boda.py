
# This program models a simple boda boda business using object-oriented programming.
# It shows how a parent class can store common motorcycle data while a child class
# calculates income, expenses, and profit for a daily business operation.


class Motorcycle:
    """Parent class containing information shared by motorcycles."""

    # The __init__ method is called whenever a new Motorcycle object is created.
    # It stores the motorcycle's registration or identification number.
    def __init__(self, motorcycle_number):
        self.__motorcycle_number = motorcycle_number

    # This getter returns the motorcycle number for use elsewhere in the program.
    def get_motorcycle_number(self):
        return self.__motorcycle_number

    # This setter updates the motorcycle number only if the value is not blank.
    # This helps prevent empty or invalid values from being accepted.
    def set_motorcycle_number(self, motorcycle_number):
        if motorcycle_number.strip():
            self.__motorcycle_number = motorcycle_number


class BodaBusiness(Motorcycle):
    """Child class that calculates fares, expenses, and profit."""

    # The constructor receives all the details needed to run the boda business.
    # It calls the parent constructor first so the motorcycle number is inherited.
    def __init__(
        self,
        rider_name,
        motorcycle_number,
        distance,
        passenger_weight,
        road_condition,
        fuel_litres,
        fuel_price_per_litre,
        base_fare,
        other_expenses,
    ):
        super().__init__(motorcycle_number)
        self.__rider_name = rider_name
        self.set_distance(distance)
        self.set_passenger_weight(passenger_weight)
        self.set_road_condition(road_condition)
        self.set_fuel_litres(fuel_litres)
        self.set_fuel_price_per_litre(fuel_price_per_litre)
        self.set_base_fare(base_fare)
        self.set_other_expenses(other_expenses)

    # The following methods are examples of encapsulation.
    # They control how data is accessed and validated before being stored.
    def get_rider_name(self):
        return self.__rider_name

    def set_rider_name(self, rider_name):
        if rider_name.strip():
            self.__rider_name = rider_name

    # This method validates the distance travelled and refuses negative values.
    def set_distance(self, distance):
        if distance >= 0:
            self.__distance = distance
        else:
            raise ValueError("Distance cannot be negative.")

    # This ensures the passenger weight is within a realistic range for the business.
    def set_passenger_weight(self, passenger_weight):
        if 0 <= passenger_weight <= 200:
            self.__passenger_weight = passenger_weight
        else:
            raise ValueError("Passenger weight must be between 0 and 200 kg.")

    # The road condition is standardized to a valid business value.
    # If an invalid road condition is passed, the system defaults to Normal.
    def set_road_condition(self, road_condition):
        conditions = ("normal", "rainy", "dusty", "peak")
        if road_condition.lower() in conditions:
            self.__road_condition = road_condition.title()
        else:
            self.__road_condition = "Normal"

    # Fuel used cannot be negative because a business cannot consume a negative quantity.
    def set_fuel_litres(self, fuel_litres):
        if fuel_litres >= 0:
            self.__fuel_litres = fuel_litres
        else:
            raise ValueError("Fuel litres cannot be negative.")

    # The price per litre must not be below zero to avoid invalid calculations.
    def set_fuel_price_per_litre(self, fuel_price_per_litre):
        if fuel_price_per_litre >= 0:
            self.__fuel_price_per_litre = fuel_price_per_litre
        else:
            raise ValueError("Fuel price cannot be negative.")

    # Base fare is the starting amount charged before extra trip factors are added.
    def set_base_fare(self, base_fare):
        if base_fare >= 0:
            self.__base_fare = base_fare
        else:
            raise ValueError("Base fare cannot be negative.")

    # Other expenses such as maintenance, snacks, or small unexpected costs are stored here.
    def set_other_expenses(self, other_expenses):
        if other_expenses >= 0:
            self.__other_expenses = other_expenses
        else:
            raise ValueError("Other expenses cannot be negative.")

    # The business methods below calculate different parts of the total cost and income.
    # Each method is independent, making the class easier to maintain and understand.
    def calculate_distance_charge(self):
        # The distance charge is calculated as a set value per kilometre.
        return self.__distance * 1000

    def calculate_weight_charge(self):
        # Passenger weight affects the fare in different bands.
        if self.__passenger_weight > 100:
            return 3000
        if self.__passenger_weight > 80:
            return 2000
        if self.__passenger_weight > 60:
            return 1000
        return 0

    def calculate_road_charge(self):
        # Road-related charges vary depending on weather or travel difficulty.
        charges = {"Rainy": 2000, "Dusty": 1000, "Peak": 3000}
        return charges.get(self.__road_condition, 0)

    def calculate_fare(self):
        # The total fare is the combination of the starting fare and all extra charges.
        return (
            self.__base_fare
            + self.calculate_distance_charge()
            + self.calculate_weight_charge()
            + self.calculate_road_charge()
        )

    def calculate_fuel_cost(self):
        # Fuel cost is simply the amount of fuel used multiplied by the price per litre.
        return self.__fuel_litres * self.__fuel_price_per_litre

    def calculate_total_expenses(self):
        # Total expenses combine fuel cost and any additional business costs.
        return self.calculate_fuel_cost() + self.__other_expenses

    def calculate_profit(self):
        # Profit is the difference between the income earned and total business expenses.
        return self.calculate_fare() - self.calculate_total_expenses()

    def display_business_details(self):
        # This method prints a full summary of the business activity in a readable format.
        print("========== BODA BUSINESS ==========")
        print(f"Rider: {self.__rider_name}")
        print(f"Motorcycle: {self.get_motorcycle_number()}")
        print(f"Distance: {self.__distance} KM")
        print(f"Passenger weight: {self.__passenger_weight} KG")
        print(f"Road condition: {self.__road_condition}")
        print(f"Fuel used: {self.__fuel_litres} litres")
        print("-----------------------------------")
        print(f"Base fare: UGX {self.__base_fare:,.0f}")
        print(f"Distance charge: UGX {self.calculate_distance_charge():,.0f}")
        print(f"Weight charge: UGX {self.calculate_weight_charge():,.0f}")
        print(f"Road charge: UGX {self.calculate_road_charge():,.0f}")
        print(f"TOTAL FARE: UGX {self.calculate_fare():,.0f}")
        print(f"Fuel cost: UGX {self.calculate_fuel_cost():,.0f}")
        print(f"Other expenses: UGX {self.__other_expenses:,.0f}")
        print(f"TOTAL EXPENSES: UGX {self.calculate_total_expenses():,.0f}")
        print(f"PROFIT: UGX {self.calculate_profit():,.0f}")
        print("===================================")


# This section runs only when the file is executed directly as a script.
# It creates one example boda business and prints its financial summary.
if __name__ == "__main__":
    boda = BodaBusiness(
        rider_name="Leo",
        motorcycle_number="UAX 123A",
        distance=8,
        passenger_weight=75,
        road_condition="Dusty",
        fuel_litres=2,
        fuel_price_per_litre=5200,
        base_fare=3000,
        other_expenses=2000,
    )
    boda.display_business_details()