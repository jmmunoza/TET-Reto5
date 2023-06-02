from mrjob.step import MRStep
from mrjob.job import MRJob


class AverageSectorSalary(MRJob):
    def steps(self):
        return [
            MRStep(mapper=self.mapper,
                   reducer=self.reducer),
        ]

    def mapper(self, _, line): 
        print(line)
        columns = ['id_emp', 'sec_econ', 'salary', 'year']
        data_row = dict(zip(columns, line.split(',')))
        yield (data_row['id_emp'], float(data_row['salary']))

    def reducer(self, id_emp, salaries):
        print(id_emp)
        list_salaries = list(salaries)
        yield (id_emp, sum(list_salaries) / len(list_salaries)) if len(list_salaries) > 0 else 0

if __name__ == '__main__':
    AverageSectorSalary.run()