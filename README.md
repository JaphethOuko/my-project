My Project
A clean, modular Python application for managing user profiles and social posts. This project demonstrates Object-Oriented Programming (OOP) principles and includes a CI/CD pipeline via GitHub Actions.

🚀 Features
User Management: Create and manage user profiles with built-in validation.

Post System: Link messages to specific authors.

CI/CD Integrated: Automated workflows to ensure code quality on every push.

🛠️ Installation
Clone the repository:

Bash
git clone https://github.com/JaphethOuko/my-project.git
cd my-project
Set up a virtual environment (Optional but recommended):

Bash
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
💻 Usage
The core logic is handled by main.py. You can run the application using:

Bash
python main.py
Example Code
Python
from user import User
from post import Post

# Create a user
me = User(name="Japheth")

# Create a post
new_post = Post(message="Hello World!", author=me)
print(new_post.message)
🧪 Testing & CI/CD
This project uses GitHub Actions to automate workflows.

The configuration is located in .github/workflows/main.yml.

It currently forces Node 24 for internal actions to ensure compatibility with the latest environments.

📂 Project Structure
user.py: Defines the User class.

post.py: Defines the Post class.

main.py: The entry point for the applicatio
