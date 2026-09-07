


class Motorcycle:
    """Parent class containing information shared by motorcycles."""

    def __init__(self, motorcycle_number):
        self.__motorcycle_number = motorcycle_number

    def get_motorcycle_number(self):
        return self.__motorcycle_number

    def set_motorcycle_number(self, motorcycle_number):
        if motorcycle_number.strip():
            self.__motorcycle_number = motorcycle_number


class BodaBusiness(Motorcycle):
    """Child class that calculates fares, expenses, and profit."""

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

    # Getters and setters demonstrate encapsulation.
    def get_rider_name(self):
        return self.__rider_name

    def set_rider_name(self, rider_name):
        if rider_name.strip():
            self.__rider_name = rider_name

    def set_distance(self, distance):
        if distance >= 0:
            self.__distance = distance
        else:
            raise ValueError("Distance cannot be negative.")

    def set_passenger_weight(self, passenger_weight):
        if 0 <= passenger_weight <= 200:
            self.__passenger_weight = passenger_weight
        else:
            raise ValueError("Passenger weight must be between 0 and 200 kg.")

    def set_road_condition(self, road_condition):
        conditions = ("normal", "rainy", "dusty", "peak")
        if road_condition.lower() in conditions:
            self.__road_condition = road_condition.title()
        else:
            self.__road_condition = "Normal"

    def set_fuel_litres(self, fuel_litres):
        if fuel_litres >= 0:
            self.__fuel_litres = fuel_litres
        else:
            raise ValueError("Fuel litres cannot be negative.")

    def set_fuel_price_per_litre(self, fuel_price_per_litre):
        if fuel_price_per_litre >= 0:
            self.__fuel_price_per_litre = fuel_price_per_litre
        else:
            raise ValueError("Fuel price cannot be negative.")

    def set_base_fare(self, base_fare):
        if base_fare >= 0:
            self.__base_fare = base_fare
        else:
            raise ValueError("Base fare cannot be negative.")

    def set_other_expenses(self, other_expenses):
        if other_expenses >= 0:
            self.__other_expenses = other_expenses
        else:
            raise ValueError("Other expenses cannot be negative.")

    # Business methods.
    def calculate_distance_charge(self):
        return self.__distance * 1000

    def calculate_weight_charge(self):
        if self.__passenger_weight > 100:
            return 3000
        if self.__passenger_weight > 80:
            return 2000
        if self.__passenger_weight > 60:
            return 1000
        return 0

    def calculate_road_charge(self):
        charges = {"Rainy": 2000, "Dusty": 1000, "Peak": 3000}
        return charges.get(self.__road_condition, 0)

    def calculate_fare(self):
        return (
            self.__base_fare
            + self.calculate_distance_charge()
            + self.calculate_weight_charge()
            + self.calculate_road_charge()
        )

    def calculate_fuel_cost(self):
        return self.__fuel_litres * self.__fuel_price_per_litre

    def calculate_total_expenses(self):
        return self.calculate_fuel_cost() + self.__other_expenses

    def calculate_profit(self):
        return self.calculate_fare() - self.calculate_total_expenses()

    def display_business_details(self):
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