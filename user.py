class User:
    def __init__(self, name, email, password, job):
        self.name = name
        self.email = email
        self.password = password
        self.job = job


    def change_password(self, new_password):
        self.password = new_password


    def change_job_title(self, new_job):
        self.job = new_job


    def get_user_info(self):
        print(f"User {self.name} is a {self.job} and can be reached at {self.email}")




