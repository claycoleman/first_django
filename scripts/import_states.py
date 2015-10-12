#!/usr/bin/env python

import csv
import sys
import os


sys.path.append('..')
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings")

from main.models import State, StateCapital


dir_name = os.path.dirname(os.path.abspath(__file__))
path_name = "states.csv"
states_csv = os.path.join(dir_name, path_name)
# print '%s/%s' % (os.path.dirname(os.path.abspath(__file__)), "states.csv")
# the following usually for large blocks of text!
# print "{0}/{1}".format(os.path.dirname(os.path.abspath(__file__)),"states.csv")

csv_file = open(states_csv, 'r')

reader = csv.DictReader(csv_file)
print reader

for row in reader:
    new_state, created = State.objects.get_or_create(name=row['state'])
    new_cap, created = StateCapital.objects.get_or_create(name=row['capital'])

    new_state.abbrev = row['abbrev']
    new_cap.population = row['population']
    new_cap.lat = row["latitude"]
    new_cap.lon = row['longitude']
    new_cap.state = new_state

    new_state.save()
    new_cap.save()
