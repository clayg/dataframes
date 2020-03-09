import pandas as pd


data = pd.read_csv("nba.csv", index_col="Name")
third = data.query('Age > 25 & Salary > 10000000')


def print_dataseries(dataseries):
    d = dataseries.to_dict()
    print(d['Age'])
    print(d['Salary'])
    print(d.keys())


print_dataseries(third)
