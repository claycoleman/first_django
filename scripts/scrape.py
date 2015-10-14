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

from main.models import State

result = urllib.urlopen('http://www.50states.com/')
html = result.read()

parser = etree.HTMLParser()
tree = etree.parse(StringIO.StringIO(html), parser)

href_xpath = '//*[@id="ar-full-homepage"]/div/ul/li/a/@href'
filtered_html = tree.xpath(href_xpath)

# link_list = []
# for link in filtered_html:
#     if 'htm' in link:
#         link_list.append(link)
# 

links = [html for html in filtered_html if 'htm' in html]

# print links

for link in links:

    state_page = urllib.urlopen("http://50states.com/%s" % link)
    state_page_html = state_page.read()
    tree = etree.parse(StringIO.StringIO(state_page_html), parser)

    state_abbrev_xpath = '//*[@id="content"]/div[1]/div[2]/div/div[1]/h1/text()'
    state_abbrev_string = tree.xpath(state_abbrev_xpath)
    state_abbrev_pattern = "(?<=\().*(?=\))"
    cleaned_abbrev = re.search(state_abbrev_pattern, '%s' % state_abbrev_string)
    state = None
    try:
        state_abbrev = cleaned_abbrev.group()
        state = State.objects.get(abbrev=state_abbrev)
    except Exception, e:
        print e
        continue
    # print state
    if (state is not None): 
# //*[@id="collapseFacts"]/div/ul/li[2]/div/a[1]

        # state_admit_xpath = '//*[@id="collapseQuick-Facts"]/div/ul/li[1]/div/a/text()'

        # state_admit_string = tree.xpath(state_admit_xpath)[0]
        # state.date_admitted = state_admit_string
        # print state.abbrev
        # if state.abbrev in 'CO':
        #     state.nickname = 'Centennial'
        # elif state.abbrev in 'DE':
        #     state.nickname = 'First'
        # else:
        #     state_nickname_xpath = '//*[@id="collapseQuick-Facts"]/div/ul/li[5]/div/a/text()'
        #     state_nickname_string = tree.xpath(state_nickname_xpath)[0]
        #     state_nickname_pattern = '.*(?=\s)'
        #     nickname = re.search(state_nickname_pattern, '%s' % state_nickname_string).group().lstrip('The ')
        #     state.nickname = nickname
        
        # state_rank_xpath = '//*[@id="collapseQuick-Facts"]/div/ul/li[1]/div/text()'
        # state_rank_string = tree.xpath(state_rank_xpath)
        # state_rank_pattern = '(?<=\().*(?=\s)'
        # cleaned_rank = re.search(state_rank_pattern, '%s' % state_rank_string).group()
        # state.rank_admitted = cleaned_rank

        url = 'http://www.50states.com/images/redesign/flags/%s-largeflag.png' % state.abbrev.lower()
        print url

        # state_flag_xpath = '//*[@id="content"]/div[1]/div[3]/div/a[2]/div/div/div[1]/img/@src'
        # state_flag_image = tree.xpath(state_flag_xpath)[0]
        # url = "http://www.50states.com/%s" % state_flag_image

        image_response = urllib2.urlopen(url).read()
        
        temp_image = NamedTemporaryFile(delete=True)
        temp_image.write(image_response)

        state.flag.save('flag_img.png', File(temp_image))


        # state_seal_xpath = '//*[@id="content"]/div[1]/div[3]/div/a[3]/div/div/div[1]/img/@src'
        # state_seal_image = tree.xpath(state_seal_xpath)[0]
        # url = "http://www.50states.com/%s" % state_seal_image

        # image_response = urllib2.urlopen(url).read()
        
        # temp_image = NamedTemporaryFile(delete=True)
        # temp_image.write(image_response)

        # state.seal.save('seal_img.png', File(temp_image))

        # state_population_xpath = '//*[@id="collapseQuick-Facts"]/div/ul/li[6]/div/text()'

        # if (link.startswith('/colorado') or link.startswith('/delaware')):
        #     state_population_xpath = '//*[@id="collapseQuick-Facts"]/div/ul/li[5]/div/text()'
            
        # state_population_string = str(tree.xpath(state_population_xpath)).replace(' ', '').replace(',', '')
        # print state_population_string
        # state_population_pattern = "\d+"

        # cleaned_pop = re.search(state_population_pattern, "%s" % state_population_string)
        # if state is not None:
        #     if len(link) > 8 or not link.startswith('/search'):
        #         try:
        #             state.population = cleaned_pop.group()
        #             state.save()
        #         except Exception, e:
        #             print e



        # state_map_link_xpath = '//*[@id="collapseGovernment"]/div/ul/li[2]/div/a/@href'

        # state_map_link = tree.xpath(state_map_link_xpath)[0]
        # state_map_page = urllib.urlopen(state_map_link)
        # state_map_html = state_map_page.read()
        # tree = etree.parse(StringIO.StringIO(state_map_html), parser)

        # image_link_xpath = '//*[@id="innerPage"]/img/@src'
        # state_map_image = tree.xpath(image_link_xpath)[0]
        # url = "http://quickfacts.census.gov/%s" % state_map_image
        # image_response = urllib2.urlopen(url).read()
        
        # temp_image = NamedTemporaryFile(delete=True)
        # temp_image.write(image_response)

        # state.state_map.save('map_img.gif', File(temp_image))



        # state.save()
# //*[@id="content"]/div[1]/div[2]/div/div[1]/h1
# //*[@id="content"]/div[1]/div[2]/div/div[1]/h1