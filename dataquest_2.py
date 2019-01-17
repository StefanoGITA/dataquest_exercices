#!/usr/bin/env python
# -*- coding: utf-8 -*-
import csv
from pprint import pprint

class Dataset(object):
    def __init__(self, fname, type="csv"):
        self.header = None
        self.data = None
        self.type = type.lower()
        if self.type == 'csv':
            self.data = list(csv.reader(open(fname, "r")))
            self.header = self.data[0]
            self.data = self.data[1:]
        else:
            raise BaseException ("{0} è un tipo file non gestito!".format(type))

    def __str__(self):
        nrows=10
        return str(self.data[:nrows])

    def print_firstRows(self, nrows=10):
        print('\n'.join([str(row) for row in self.data][:nrows]))

    def extract_header(self):
        return self.header

    def column(self, label):
        column_data = []
        try:
            index = self.header.index(label)
            for row in self.data:
                column_data.append(row[index])
        except ValueError:
            column_data = None
        return column_data

    def count_unique(self, label):
        unique_values = set(self.column(label))
        return len(unique_values)

class NflSuspensions(Dataset):
    def __init__(self):
        fname = 'nfl_suspensions_data.csv'
        super(NflSuspensions, self).__init__(fname)
        self.years = {}
        self.unique_teams = set(())
        self.unique_games = set(())

    def suspension_by_year(self):
        if not self.years:
            for line in self.data:
                year = line[5]
                try:
                    self.years[year] += 1
                except KeyError:
                    self.years.update({year: 1})
        return self.years

    def get_teams(self):
        if len(self.unique_teams) == 0:
            for line in self.data:
                team = line[1]
                if team not in self.unique_teams:
                    self.unique_teams.add(team)
        return self.unique_teams

    def get_games(self):
        if len(self.unique_games) == 0:
            for line in self.data:
                game = line[2]
                if game not in self.unique_games:
                    self.unique_games.add(game)
        return self.unique_games


wrk = NflSuspensions()
print(wrk.extract_header())
pprint(wrk.suspension_by_year())
print(wrk.get_games())
print(wrk.get_teams())

'''
Create the Suspension class.
Define the __init__() method with the following criteria:
The sole required parameter is a list representing a row from the dataset.
To create a Suspension instance, we want to be able to pass in a list from nfl_suspensions.
Currently, we're only interested in storing the name, team, games and year columns. Upon instantiation:
Set the name value for that row to the name property.
Set the team value for that row to the team property.
Set the games value for that row to the games property.
Set the year value for that row to the year property.
Create a Suspension instance using the third row in nfl_suspensions, and assign it to the variable third_suspension.
'''