
class Booking: 
# Class attribute declarations (explicit mapping to SQL column types) 
 booking_id: int 
 title: str 
 number: int
def __init__(self, booking_id: int, title: str, number: int): 
# Assign incoming values to self instance attributes 
    self.booking_id = booking_id 
    self.title = title 
    self.number = number 
