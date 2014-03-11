from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String, ForeignKey, Date
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship, backref

	

ENGINE = create_engine("sqlite:///ratings.db", echo=False) 
session = scoped_session(sessionmaker(bind=ENGINE,
                                      autocommit = False,
                                      autoflush = False))



Base = declarative_base()
Base.query = session.query_property()



class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    age = Column(Integer, nullable=True)
    #gender=Column(Integer, nullable=True)
    #occupation=Column(String(64), nullable=True)
    email = Column(String(64), nullable=True)
    password = Column(String(64), nullable=True)
    zipcode = Column(String(15), nullable=True)


class Movie(Base):
	__tablename__ = "movies"

	id = Column(Integer, primary_key=True)
	title = Column(String(64), nullable=True)
	release_date = Column(Date, nullable=True)
	imdb = Column(String(64), nullable=True)

class Rating(Base):
	__tablename__ = "ratings"

	id = Column(Integer, primary_key=True)
	movie_id = Column(Integer, nullable=True)
	user_id = Column(Integer, ForeignKey('users.id'))
	rating = Column(Integer, nullable=True)

	user = relationship("User",
            backref=backref("ratings", order_by=id))

### End class declarations

def main():
    """In case we need this for something"""
    pass

if __name__ == "__main__":
    main()