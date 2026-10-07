class fare:
    fare_id: int
    price: float

    def __init__(self, fare_id: int, price: float):
        self.fare_id = fare_id
        self.price = price