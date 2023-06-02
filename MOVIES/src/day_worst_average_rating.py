from mrjob.job import MRJob

class DayWorstAverageRating(MRJob):

    def mapper(self, _, line):
        user, movie, rating, genre, date = line.split(',')
        yield None, (date, rating)

    def reducer(self, key, values):
        ratings = {}
        
        for date, rating in values:
            if date not in ratings:
                ratings[date] = []
                
            ratings[date].append(float(rating))
        
        for date in ratings:
            ratings[date] = sum(ratings[date])/len(ratings[date])   
            
        ratings = sorted(ratings.items(), key=lambda x: x[1], reverse=True) 
        
        yield ratings[-1][0], ratings[-1][1]

if __name__ == '__main__':
    DayWorstAverageRating.run()