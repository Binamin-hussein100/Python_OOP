from sqlalchemy import create_engine, Column, Integer,String,Table, ForeignKey
from sqlalchemy.orm import declarative_base, sessionmaker, relationship

DATABASE_URL= 'sqlite:///inventory.db'
engine = create_engine(DATABASE_URL)

# ORM BASE
Base = declarative_base()


order_products = Table(
    "order_products", Base.metadata,
    Column('order_id', Integer, ForeignKey("orders.id")),
    Column('product_id', Integer, ForeignKey("products.id"))
)

class Profile(Base):
    __tablename__ = "profiles"

    id = Column(Integer, primary_key=True)
    address = Column(String(50))
    phone = Column(String(20))

    # relationship
    user_id = Column(Integer, ForeignKey('users.id'), unique=True)    
    user = relationship("User", back_populates="profile")



# user class
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    email = Column(String(100), unique=True , nullable=False)
    nationality  = Column(String(50))
    # relationships
    profile = relationship("Profile", back_populates="user", uselist=False)
    orders = relationship("Order", back_populates="user")


class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    user = relationship("User", back_populates="orders")
    products = relationship("Product", secondary=order_products, back_populates="orders")

class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True)
    name  = Column(String(50), nullable=False)
    price = Column(Integer, nullable=False)
    orders = relationship("Order", secondary=order_products, back_populates="products")

class Cashout(Base):
    __tablename__ = "cashouts"

    id = Column(Integer, primary_key=True)
    amount  = Column(String(50), nullable=False)
    mode  = Column(String(50))

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
