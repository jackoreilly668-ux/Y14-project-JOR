class Review:
    review_id: int
    rating: int
    comment: str
    date: str

    def __init__(self, review_id: int, rating: int, comment: str, date: str):
        self.review_id = review_id
        self.rating = rating
        self.comment = comment
        self.date = date