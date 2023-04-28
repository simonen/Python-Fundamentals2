class Vehicle:

    def __init__(self, vtype, model, price):
        self.type = vtype
        self.model = model
        self.price = price
        self.owner = None

    def buy(self, money: int, owner: str):
        if self.owner is not None:
            return "Car already sold"
        elif money >= self.price:
            diff = money - self.price
            self.owner = owner
            return f"Successfully bought a {self.type}. Change: {diff:.2f}"
        else:
            return "Sorry, not enough money"

    def sell(self):
        if self.owner is not None:
            self.owner = None
        else:
            return "Vehicle has no owner"

    def __repr__(self):
        if self.owner is not None:
            return f"{self.model} {self.type} is owned by: {self.owner}"
        else:
            return f"{self.model} {self.type} is on sale: {self.price}"


v_type = "car"
v_model = "BMW"
v_price = 30000

vehicle = Vehicle(v_type, v_model, v_price)
truck = Vehicle('truck', 'camaro', 10)
print(truck)
print(vehicle)
print(vehicle.sell())
