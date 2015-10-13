#!/usr/bin/env python

import csv
import sys
import os

sys.path.append('..')
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings")

import django
django.setup()

from main.models import State, Area


dir_name = os.path.dirname(os.path.abspath(__file__))
path_name = "zip_codes_states.csv"
states_csv = os.path.join(dir_name, path_name)
# print '%s/%s' % (os.path.dirname(os.path.abspath(__file__)), "states.csv")
# the following usually for large blocks of text!
# print "{0}/{1}".format(os.path.dirname(os.path.abspath(__file__)),"states.csv")

csv_file = open(states_csv, 'r')

reader = csv.DictReader(csv_file)
print reader
# Area.objects.all().delete()
for row in reader:
    new_area, created = Area.objects.get_or_create(zip_code=row['zip_code'])

    print new_area.zip_code
    new_area.lat = row['latitude']
    new_area.lon = row['longitude']
    new_area.city = row["city"]
    new_area.county = row['county']
    new_area.state_abbrev = row['state']
    try:
        state = State.objects.get(abbrev=row['state'])
        new_area.state = state
    except Exception, e:
        new_area.state = None
    new_area.save()

