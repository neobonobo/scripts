from mylib import User

username=input("Please enter a username:")
first_name=input("Please enter a first name:")
last_name=input("Please enter a last name:")
user=User(username,first_name,last_name)
user.save()
