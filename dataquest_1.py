#!/usr/bin/env python
# -*- coding: utf-8 -*-

import csv
import pandas

class Suspension(object):
    def __init__(self, row):
        assert isinstance(row,list)
        #name,team,games,category,desc.,year,source
        self.name = row[0]
        self.team = row[1]
        self.games = row[2]
        self.year = row[5]


fname = 'nfl_suspensions_data.csv'
# nfl_suspensions = list(csv.reader(open(fname, "r")))[1:]
# third_suspension = Suspension(nfl_suspensions[2])


reader = csv.DictReader(open(fname, "r"))
r1 = next(reader)
r2 = next(reader)


df = pandas.read_csv(fname)
x = df.loc[df['name'] == 'F. Filchock']
print(type(x))
#media anno
pandas.to_numeric(df["year"], errors='coerce').mean()

df = df.set_index('name')
x = df.loc['F. Filchock']
for k in df.keys():
    print(f'{k}: {x[k]}')
