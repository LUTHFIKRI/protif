#!/usr/bin/python

from xml.dom import minidom
import time
import urllib
import sys

xmldoc = minidom.parse('detik.xml') 
count = 0
#itemlist = xmldoc.getElementsByTagName('item') 
#print len(itemlist)
#print itemlist[0].attributes['http'].value
#for s in itemlist :
#    print s.attributes['http'].value

print count
