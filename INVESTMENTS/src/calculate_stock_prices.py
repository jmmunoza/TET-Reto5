from mrjob.job import MRJob

class CalculateStockPrices(MRJob):

    def mapper(self, _, line):
        company, price, date = line.split(',')
        yield company, (date, price)

    def reducer(self, key, values):
        date_lowest_price = (None, 0)
        date_highest_price = (None, 0)
        
    
        for date, price in values:
            if date_lowest_price[1] == 0 or float(price) < date_lowest_price[1]:
                date_lowest_price = (date, float(price))
                
            if date_highest_price[1] == 0 or float(price) > date_highest_price[1]:
                date_highest_price = (date, float(price))

        yield key, (date_lowest_price, date_highest_price)

if __name__ == '__main__':
    CalculateStockPrices.run()