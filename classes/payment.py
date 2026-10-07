class Payment:
    payment_id: int
    amount: float
    payment_method: str

    def __init__(self, payment_id: int, amount: float, payment_method: str):
        self.payment_id = payment_id
        self.amount = amount
        self.payment_method = payment_method