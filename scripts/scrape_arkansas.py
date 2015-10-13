#!/usr/bin/env python
import urllib
import urllib2
import re, sys, os
from lxml import etree
import StringIO

sys.path.append("..")  
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings")

from django.core.files import File
from django.core.files.temp import NamedTemporaryFile

from main.models import State, StateCapital

# state_page = urllib.urlopen("http://50states.com/%s" % link)
# state_page_html = state_page.read()
# tree = etree.parse(StringIO.StringIO(state_page_html), parser)

# state_abbrev_xpath = '//*[@id="content"]/div[1]/div[2]/div/div[1]/h1/text()'
# state_abbrev_string = tree.xpath(state_abbrev_xpath)
# state_abbrev_pattern = "(?<=\().*(?=\))"
# cleaned_abbrev = re.search(state_abbrev_pattern, '%s' % state_abbrev_string)

result = urllib.urlopen('http://www.50states.com/arkansas.htm')
html = result.read()

parser = etree.HTMLParser()
tree = etree.parse(StringIO.StringIO(html), parser)


state_xpath = '//*[@id="content"]/div[1]/div[2]/div/div[1]/h1/text()'
state_string = tree.xpath(state_xpath)[0]

abbrev_pattern = "(?<=\().*(?=\))"
name_pattern = "(?=\w\w).*(?=\W\()"
cleaned_abbrev = re.search(abbrev_pattern, '%s' % state_string).group()
cleaned_name = re.search(name_pattern, '%s' % state_string).group()
print cleaned_name + " :" + cleaned_abbrev

state_population_xpath = '//*[@id="collapseQuick-Facts"]/div/ul/li[6]/div/text()'
state_population_string = str(tree.xpath(state_population_xpath)).replace(' ', '').replace(',', '')
state_population_pattern = "\d+"
cleaned_pop = re.search(state_population_pattern, "%s" % state_population_string).group()
print cleaned_pop

state_capital_xpath = '//*[@id="collapseQuick-Facts"]/div/ul/li[4]/div/a/text()'
state_capital_string = tree.xpath(state_capital_xpath)[0]
print state_capital_string

state_map_link_xpath = '//*[@id="collapseGovernment"]/div/ul/li[2]/div/a/@href'

state_map_link = tree.xpath(state_map_link_xpath)[0]
state_map_page = urllib.urlopen(state_map_link)
state_map_html = state_map_page.read()
tree = etree.parse(StringIO.StringIO(state_map_html), parser)

image_link_xpath = '//*[@id="innerPage"]/img/@src'
state_map_image = tree.xpath(image_link_xpath)[0]
url = "http://quickfacts.census.gov/%s" % state_map_image
image_response = urllib2.urlopen(url).read()
temp_image = NamedTemporaryFile(delete=True)
temp_image.write(image_response)

littlerock, created = StateCapital.objects.get_or_create(name=state_capital_string)
littlerock.population = "197706"
littlerock.lat = "34.736009"
littlerock.lon = "-92.331122"


state, created = State.objects.get_or_create(name=cleaned_name)
state.abbrev = cleaned_abbrev
state.population = cleaned_pop
littlerock.state = state
state.state_map.save('map_img.gif', File(temp_image))

littlerock.save()
state.save()


