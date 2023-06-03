from mrjob.job import MRJob

class StableStocks(MRJob):

    def mapper(self, _, line):
        company, price, date = line.split(',')
        yield company, (date, price)

    def reducer(self, key, values):
        dates = sorted(values, key=lambda x: x[0])
        stable = True
        for index, (date, price) in enumerate(dates):
            if index == 0:
                continue
            
            if float(price) < float(dates[index - 1][1]):
                stable = False
        
        if stable:
            yield key, dates


if __name__ == '__main__':
    StableStocks.run()