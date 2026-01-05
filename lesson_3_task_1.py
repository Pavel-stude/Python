from user import User

first_name = str(input())
last_name = str(input())

user1 = User(first_name)
user1.sayLastname(last_name)
user1.sayName()