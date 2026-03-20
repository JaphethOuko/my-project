class Post:
    def __init__(self, message, author):
        self.message = message
        self.author = author

    def display_message(self):
        print(f"{self.message} written by {self.author}")
