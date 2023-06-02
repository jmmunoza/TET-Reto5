from mrjob.job import MRJob

class AverageSectorSalary(MRJob):

    def mapper(self, _, line):
        idemp, sector, salary, year = line.split(',')
        yield sector, salary

    def reducer(self, key, values):
        total = 0 
        count = 0 
        for salary in values:
            total += int(salary)
            count += 1
            
        yield key, total / count

if __name__ == '__main__':
    AverageSectorSalary.run()