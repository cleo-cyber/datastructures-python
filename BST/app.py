# : As a senior backend engineer at Jovian, you are tasked with developing a fast in-memory data structure to manage profile information (username, name and email) for 100 million users. It should allow the following operations to be performed efficiently:

# To manage user information we'll use a class.
# Operations:
# 1. Insert User profile
# 2. Find User profile by username
# 3. Update User profile by username
# 4 List all users sorted by username


# Edge cases:
# 1. What if the username is not found?
# 2. Insert in an empty list
# 3. Insert at the beginning of the list
# 4. Insert at the end of the list
# 5. Insert in the middle of the list
# 6. List is empty
# 7. User is not found

# Algorithm:
# 1. Insert User profile
#     1.1. If the list is empty, insert at the beginning
#     1.2. If the list is not empty, find the correct position to insert the user profile
# 2. Find User profile by username
#     2.1. If the list is empty, return None
#     2.2. If the list is not empty, find the user profile by username
# 3. Update User profile by username
#     3.1. If the list is empty, return None
#     3.2. If the list is not empty, find the user profile by username and update it
# 4. List all users sorted by username
#     4.1. If the list is empty, return None
#     4.2. If the list is not empty, return all the users sorted by username

# Insert Implementation Logic
# 1. Insert User profile
#     1.1. Loop through the list, check if username is greater than the current user profile's username if not insert at the current position
#     1.2. If the username is greater than all the user profiles in the list, insert at the end of the list



class User:
    def __init__(self, username, name, email):
        self.username = username
        self.name = name
        self.email = email



    def __repr__(self):
        return f'@{self.username} ({self.name}): {self.email}'
class userProfile:
    def __init__(self):
        self.users = []
    def insert(self, user):
            i=0
            while i<len(self.users):
                if self.users[i].username>user.username:
                    break
                i+=1
            self.users.insert(i,user)
    def find(self,username):
            for user in self.users:
                if user.username==username:
                    return user
            return None
    def update(self,user):
            target=self.find(user.username)
            if target:
                target.name=user.name
                target.email=user.email
    def list(self):
            return self.users

    
# Sample Input:
aakash = User('aakash', 'Aakash Rai', 'aakash@example.com')
biraj = User('biraj', 'Biraj Das', 'biraj@example.com')
hemanth = User('hemanth', 'Hemanth Jain', 'hemanth@example.com')
jadhesh = User('jadhesh', 'Jadhesh Verma', 'jadhesh@example.com')
siddhant = User('siddhant', 'Siddhant Sinha', 'siddhant@example.com')
sonaksh = User('sonaksh', 'Sonaksh Kumar', 'sonaksh@example.com')
vishal = User('vishal', 'Vishal Goel', 'vishal@example.com')


database = userProfile()
database.insert(aakash)
database.insert(biraj)
database.insert(hemanth)
database.insert(jadhesh)


# Sample Output:
ff=database.list() # Should return a User object with username 'aakash'
print(ff)