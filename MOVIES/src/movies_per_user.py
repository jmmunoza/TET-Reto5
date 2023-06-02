from mrjob.job import MRJob

class MoviesPerUser(MRJob):

    def mapper(self, _, line):
        user, movie, rating, genre, date = line.split(',')
        yield user, (movie, rating)

    def reducer(self, key, values):
        movies = []
        ratings = []

        for movie, rating in values:
            if movie not in movies:
                movies.append(movie)
            
            ratings.append(float(rating))
                
        yield key, (len(movies), sum(ratings)/len(ratings))

if __name__ == '__main__':
    MoviesPerUser.run()