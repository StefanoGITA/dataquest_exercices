import csv
from datetime import datetime
from pprint import pprint

census = {}
kill_x_date_count = {}
kill_x_sex_count = {}
kill_x_race_count = {}
homicide_race_counts ={}

mapping = {
    'Asian/Pacific Islander' :['Race Alone - Asian', 'Race Alone - Native Hawaiian and Other Pacific Islander'],
    'Black': ['Race Alone - Black or African American'],
    'Hispanic': ['Race Alone - Hispanic'],
    'Native American/Native Alaskan': ['Race Alone - American Indian and Alaska Native'],
    'White': ['Race Alone - White']}

def count_keys(p_dict, p_key, next_value=1):
    try:
        p_dict[p_key] += next_value
    except KeyError:
        p_dict[p_key] = next_value

def elabora_census():
    with open('data\census.csv') as f:
        #census has 1 header and 1 ro data
        csvdata = list(csv.DictReader(f))[0]
        for key in mapping:
            for value in mapping[key]:
                count_keys(census, key, int(csvdata[value]))

def elabora_kills():
    with open('data\guns.csv') as f:
        ldata = list(csv.reader(f))
    headers = ldata[0]
    #print(headers)
    ldata.pop(0)
    for row in ldata:
        ldate = datetime(int(row[1]), int(row[2]), 1)
        count_keys(kill_x_date_count, ldate)
        count_keys(kill_x_sex_count, row[5])
        count_keys(kill_x_race_count, row[7])
        if row[3] == "Homicide":
            count_keys(homicide_race_counts, row[7])

elabora_census()
elabora_kills()

race_per_100k = {}
for key in kill_x_race_count:
    rate_kill = (kill_x_race_count[key] / census[key]) * 100000
    race_per_100k[key] = rate_kill

race_homicide_per_100k = {}
for key in homicide_race_counts:
    rate_kill = (homicide_race_counts[key] / census[key]) * 100000
    race_homicide_per_100k[key] = rate_kill

print("race_homicide_per_100k")
pprint(race_homicide_per_100k, indent=4)

# print("\nConta per data:")
# pprint(kill_x_date_count)
# print("\nConta per sesso:")
# pprint(kill_x_sex_count)
# print("\nConta per razza:")
# pprint(kill_x_race_count)
#
