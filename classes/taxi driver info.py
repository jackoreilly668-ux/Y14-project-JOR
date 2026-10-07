class TaxiDriver:
    driver_id: int
    name: str
    phone: str
    licence_number: str
    taxi_number: str

    def __init__(self, driver_id: int, name: str, phone: str, licence_number: str, taxi_number: str):
        self.driver_id = driver_id
        self.name = name
        self.phone = phone
        self.licence_number = licence_number
        self.taxi_number = taxi_number