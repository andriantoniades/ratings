import model
import csv
import datetime

def load_users(session):
    with open('seed_data/u.user', 'rb') as csvfile:
    #create a variable that establishes the parsed line
        user_file = csv.reader(csvfile, delimiter='|')
        #iterate over the list
        for row in user_file:
            #establish what the output should look like
            # user = model.User(id=row[0], email=row[1], password=row[2], age=row[1], zipcode=row[4])
            user = model.User(id=row[0], age=row[1], zipcode=row[2])
            #add that output to the database
            session.add(user)
    #commit it        
    session.commit()
    

def load_movies(session):
    with open('seed_data/u.item', 'rb') as csvfile:
        #establish a variable that creates a parsed line
        movie_file = csv.reader(csvfile, delimiter = '|')
        #iterate over the list
        for row in movie_file:
            #use strptime on release_date
            if not row[2]:
                continue
            release_date = datetime.datetime.strptime(row[2], "%d-%b-%Y")
            #establish what the output should look like
            movie = model.Movie(id=row[0], 
                                title=unicode(row[1], errors='replace'), 
                                release_date=release_date, 
                                imdb=unicode(row[3], errors='replace'))
            #add that output to the database
            session.add(movie)

    session.commit()


def load_ratings(session):
    # use u.data
    with open('seed_data/u.data', 'rb') as csvfile:
    #establish a variable that creates a parsed line
        ratings_file = csv.reader(csvfile, delimiter = ' ')
    #iterate over the list
        for row in ratings_file:
        #establish what the output should look like
            row = model.Rating(id=row[0], movie_id=row[1], rating=[2])
    

def main(session):
    #load_users(session)
    #load_movies(session)
    load_ratings(session)
    # You'll call each of the load_* functions with the session as an argument
   

if __name__ == "__main__":
    s= model.connect()
    main(s)