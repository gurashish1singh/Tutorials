'''
Creating a simple database using SQLAlchemy - J S
'''
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

Base = declarative_base()


class User(Base):
    '''
    Base User class to set up the schema
    '''
    __tablename__ = 'person'

    id = Column('id', Integer, primary_key=True)
    username = Column('username', String, unique=True)


# Creates the engine based on what kind of DB and location
engine = create_engine('sqlite:///users.db', echo=True)

# Setting up the schema
Base.metadata.create_all(bind=engine)

# Creating a session and binding to the existing schema
Session = sessionmaker(bind=engine)

# Creating the object(much like a cursor)
session = Session()

# # Initializing a user
# user = User()
# user.id = 0
# user.username = 'TestUser'

# # Adding the user to the schema
# session.add(user)
# session.commit()

# Querying for users
users = session.query(User).all()

for user in users:
    print(f'User with username: {user.username} and id: {user.id}')

session.close()
