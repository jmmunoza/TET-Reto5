from mrjob.job import MRJob


class BlackDay(MRJob):

    def mapper(self, _, line):
        company, price, date = line.split(',')
        yield None, (company, date, price)

    def reducer(self, key, values):
        companies = {}
        
        for company, date, price in values:
            if not company in companies:
                companies[company] = []
                
            companies[company].append((date, price))
            
        for company in companies:
            lowest = companies[company][0]
            for date, price in companies[company]:
                if price < lowest[1]:
                    lowest = (date, price)
            
            companies[company] = lowest          
             
        dates = {}
        
        for company in companies:
            if not companies[company][0] in dates:
                dates[companies[company][0]] = 1
            else:
                dates[companies[company][0]] += 1
                
        dates = sorted(dates.items(), key=lambda x: x[1], reverse=True)
            
        yield dates[0][0], dates[0][1]
         

if __name__ == '__main__':
    BlackDay.run()