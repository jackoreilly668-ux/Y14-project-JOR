class Trip:

    trip_id: int
    pickup: str
    destination: str
    date: str
    time: str
    fare: float

    def __init__(self, trip_id: int, pickup: str, destination: str, date: str, time: str, fare: float):
        self.trip_id = trip_id
        self.pickup = pickup
        self.destination = destination
        self.date = date
        self.time = time
        self.fare = fare