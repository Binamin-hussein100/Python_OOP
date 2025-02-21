class Base_class:  # parent
    def __init__(self,id):
        self.id = id
    
    def save(self):
        print("The new class has been saved.")



# one-to-many relationship with post
class User(Base_class): #proposed child class
    def __init__(self, username, email, id):
        super().__init__(id)
        self.username = username
        self._email = email
        self.posts = []

    @property
    def email(self):
        return self._email
    
    @email.setter
    def email(self, new_email):
        if "@" in new_email:
            self._email = new_email
        else:
            print("Invalid email")
    
    def create_post(self, post):
        self.posts.append(post)
        print(f"Post {post.title} added by {self.username}")


class Post(Base_class):
    total_post = 0
    post_list = []

    def __init__(self, id,  title, content, user):
        super().__init__(id)
        self.user = user
        self.title = title
        self.content = content
        self.comments = []
        self.tags = []
        Post.total_post += 1
        Post.post_list.append(self)

    @classmethod
    def show_post_list(cls):
        return [post.title for post in cls.post_list]

user1 = User("John", "john@gmail.com", 1)
post1 = Post(1,"12derre22", "test", "test", user1)

post2 = user1.create_post(post1)