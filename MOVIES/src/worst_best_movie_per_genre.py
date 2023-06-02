from mrjob.job import MRJob

class WorstBestMoviePerGenre(MRJob):

    def mapper(self, _, line):
        user, movie, rating, genre, date = line.split(',')
        yield genre, (movie, rating)

    def reducer(self, key, values):
        movies = {}
        
        for movie, rating in values:
            if movie not in movies:
                movies[movie] = []
                
            movies[movie].append(float(rating))
        
        for movie in movies:
            movies[movie] = sum(movies[movie])/len(movies[movie])
            
        movies = sorted(movies.items(), key=lambda x: x[1], reverse=True)
        
        yield key, (movies[0], movies[-1])

if __name__ == '__main__':
    WorstBestMoviePerGenre.run()