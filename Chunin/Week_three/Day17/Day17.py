#Day 17 Begins
#Creating a class in python
class User:


    def __init__(self, user_id, username):
        self.id  = user_id
        self.username = username
        self.followers = 0
        self.following = 0

    def follow(self, user):
        user.followers += 1
        self.following += 1
    
user_1 = User("001", "angela")
user_2 = User("002", "Jack")

print(user_1.followers)

user_1.follow(user_2)
print(user_1.followers)
print(user_1.following)
print(user_2.followers)
print(user_2.following)

#Quiz Game
#Creating the Question class
class Question:

    def __init__(self, q_text, q_answer):
       self.text = q_text
       self.answer = q_answer








