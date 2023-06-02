from mrjob.job import MRJob

class EmployeeSectorHistory(MRJob):

    def mapper(self, _, line):
        idemp, sector, salary, year = line.split(',')
        yield idemp, sector

    def reducer(self, key, values):
        sectors = []
        for sector in values:
            if sector not in sectors:
                sectors.append(sector)
            
        yield key, len(sectors)

if __name__ == '__main__':
    EmployeeSectorHistory.run()