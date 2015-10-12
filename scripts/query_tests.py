#!/usr/bin/env python

import csv
import sys
import os

sys.path.append('..')
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings")

import django
django.setup()


from main.models import State, StateCapital

# print State.objects.all()
# print State.objects.filter(name__startswith="al")
#print State.objects.get(pk=55)

# states = State.objects.all().order_by('population')
# for state in states:
#     print state.name

# states = State.objects.all().exclude(name__contains="c")
# states = State.objects.all().exclude(name__icontains="c")

# for state in states:
#     print state


# outputs objects as dicts
# states = State.objects.all().values('name','population')
# for state in states:
#     print state

# states = State.objects.all().values_list('name','abbrev','pk')
# for state in states:
#     # print state[2]
#     print "State Name: %s, Abbreviation: %s" % (state[0],state[1])

# states = State.objects.all().values_list('name', 'abbrev','population')

# for name, abb, pop in states:
#     print "Name:{0}, Abbrev:{1}, Pop:{2}".format(name,abb,pop)
    # print name
    # print abb
    # print pop

# states = State.objects.all().exclude(name__istartswith="n").filter(population__gte=100000).order_by('-population')

# for state in states:
#     print "%s %s" %(state.name, state.population)

# try again with .values()
# states = State.objects.all().exclude(name__istartswith="n").filter(population__gte=100000).order_by('-population').values('name','population')
# for state in states:
#     print "%s %s" %(state['name'], state['population'])

# states_list = ['Texas','California', "Nevada", 'Alaska']
# states = State.objects.filter(name__in=states_list)

# print states


# state = State.objects.get(name="Colorado")
# print state
# print state.abbrev
# print state.statecapital_set.all()

# state = State.objects.get(pk=56)
# state1 = State.objects.get(pk=57)
# state2 = State.objects.get(pk=58)
# state3 = State.objects.get(pk=59)
# cap = StateCapital.objects.get(pk=2)

# print state
# print cap

# # state.statecapital_set.remove(cap)
# cap.state.add(state)
# cap.state.add(state1)
# cap.state.add(state2)
# cap.state.add(state3)

states = State.objects.all()
for state in states:
    print "%s's capital is %s" % (state, state.statecapital)
