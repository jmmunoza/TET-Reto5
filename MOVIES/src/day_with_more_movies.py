from mrjob.job import MRJob

class DayWithMoreMovies(MRJob):

    def mapper(self, _, line):
        user, movie, rating, genre, date = line.split(',')
        yield None, date

    def reducer(self, key, values):
        dates = {}
        
        for date in values:
            if date in dates:
                dates[date] += 1
            else:
                dates[date] = 1
                
        dates = sorted(dates.items(), key=lambda x: x[1])
            
        yield dates[-1][0], dates[-1][1]

if __name__ == '__main__':
    DayWithMoreMovies.run()