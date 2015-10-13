#!/usr/bin/env python
import urllib
import urllib2
import re, sys, os
from lxml import etree
import StringIO

parser = etree.HTMLParser()

malay_page = urllib.urlopen('http://www.kamus.com/eng-may/speed')
malay_page_html = malay_page.read()
tree = etree.parse(StringIO.StringIO(malay_page_html), parser)

lang_xpath = '//*[@id="trans"]/table/tbody/tr/td[1]/text()'

lang_html = tree.xpath(lang_xpath)
print lang_html