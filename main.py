from post import Post
from user import User

# from post import Post

user1 = User("jeff ouko", "jeff@nn", "pwd1", "Devops Engineer")
user2 = User("Linus Tovalds", "nn@nn", "pwd2", "Mlops Engineer")

user1.change_job_title("Finops")
user1.get_user_info()
user2.get_user_info()

new_post= Post("on a secret mission today.",user1.name)

new_post.display_message()

filename = input("Enter file to delete: ")
# If user enters: "notes.txt; rm -rf /", it deletes everything!
os.system(f"rm {filename}")
