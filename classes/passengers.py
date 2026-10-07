class Passengers:
    # Class attribute declarations (explicit mapping to SQL column types)
    passenger_id: int
    title: str
    number: int

    def __init__(self, passenger_id: int, title: str, number: int):
        self.passenger_id = passenger_id
        self.title = title
        self.number = number
