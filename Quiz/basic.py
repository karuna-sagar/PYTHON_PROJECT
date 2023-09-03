class User:\
    # pass
    def __init__(self,id,name):
        self.id = id
        self.name = name
        self.follower = 0
        self.following = 0
    def follow(self,user):
        user.follower+=1
        self.following +=1 
        

user_1 = User("001","karuna")
user_2 = User("002","Sagar")
print(user_1.follower)
print(user_1.id)
user_1.id = "001"
user_1.name = "karuna"
print(user_1.id)
print(user_1.name)

user_1.follow(user_2)
print(user_1.following)
print(user_2.following)
print(user_2.follower)
print(user_1.follower) 

# user_2.id = "002"
# user_2.name = "2aruna"
# print(user_2.id)
# print(user_2.name)