# class User:
#     pass

# class User:
#
#     def __init__(self):
#         print("a new user is being created")

class User:

    def __init__(self, user_id):
        self.id = user_id
        self.followers = 0
        self.following = 0

    def follow(self, user):
        user.followers += 1
        self.following += 1

user_1 = User("001")

user_1.name = "Rafael"

print(user_1.name)
print(user_1.id)

user_2 = User("002")

user_2.name = "Gabriel"

user_1.follow(user_2)
print(user_1.followers)
print(user_1.following)
print(user_2.followers)
print(user_2.following)

#
# user_1.id = "002"
# user_1.name = "Gabriel"