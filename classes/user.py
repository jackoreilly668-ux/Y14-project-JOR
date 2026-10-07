class User:
    user_id: int
    name: str
    email: str
    phone: str
    password: str

    def __init__(self, user_id: int, name: str, email: str, phone: str, password: str):
        self.user_id = user_id
        self.name = name
        self.email = email
        self.phone = phone
        self.password = password