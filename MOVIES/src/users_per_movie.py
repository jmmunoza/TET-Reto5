from mrjob.job import MRJob

class UsersPerMovie(MRJob):

    def mapper(self, _, line):
        user, movie, rating, genre, date = line.split(',')
        yield movie, (user, rating)

    def reducer(self, key, values):
        users = []
        ratings = []

        for user, rating in values:
            if user not in users:
                users.append(user)
            
            ratings.append(float(rating))
                
        yield key, (len(users), sum(ratings)/len(ratings))

if __name__ == '__main__':
    UsersPerMovie.run()