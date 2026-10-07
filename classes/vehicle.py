class Vehicle:
    vehicle_id: int
    registration: str
    make: str
    model: str
    colour: str

    def __init__(self, vehicle_id: int, registration: str, make: str, model: str, colour: str):
        self.vehicle_id = vehicle_id
        self.registration = registration
        self.make = make
        self.model = model
        self.colour = colour