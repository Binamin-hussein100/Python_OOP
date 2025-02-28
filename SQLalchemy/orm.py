from sqlalchemy import create_engine, Column, Integer,String, ForeignKey
from sqlalchemy.orm import declarative_base, sessionmaker, relationship

DATABASE_URL= 'sqlite:///inventory.db'
engine = create_engine(DATABASE_URL)

# ORM BASE
Base = declarative_base()


# user class
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    email = Column(String(100), unique=True , nullable=False)
    nationality  = Column(String(50))


# creating tables
Base.metadata.create_all(engine)

# session => 
Session = sessionmaker(bind=engine)
session = Session()

# CRUD
# Creating the instance, add to the db table and saving the change
def create_user(name, email):
    user = User(name=name, email = email)
    session.add(user)
    session.commit()
    print(f"Successfully saved {user}")
    return user

def get_all_users():
    users = session.query(User).all()
    for user in users:
        print(f"Username: {user.name}")



if __name__ == "__main__":
    # alice = create_user("Test", "test@mail")
    # bob = create_user("bob", "bob@email")
     
    print("All users")
    get_all_users()
