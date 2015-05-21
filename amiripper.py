#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2015 Gabriel Fornaeus <gf@hax0r.se>
#
# Distributed under terms of the GPLv3 license.

"""A small program which downloads all songs from http://amigaremix.com

Very simple, but very complex at the same time :)
"""

__author__ = 'Gabriel Fornaeus'
__version__ = '0.1'

from bs4 import BeautifulSoup
import requests
import sys

class amiripper:
    baseUrl = 'http://amigaremix.com/'
    outputFolder = ''
    pageUrls = []
    songUrls = []
    numberOfPages = 0

    def __init__(self, outputFolder):
        """
        Initializes all the variables
        """
        amiripper.getNumberOfPages
        amiripper.outputFolder = outputFolder
        amiripper.populatePageUrls(self)

    def getNumberOfPages(self):
        """
        Figures out how many pages there are to download from
        """
        r = requests.get(amiripper.baseUrl)
        soup = BeautifulSoup(r.text)
        selects = soup.find('select', attrs={'name': 'page'})
        amiripper.numberOfPages = len(selects.find_all('option')))

    def populatePageUrls(self):
        """
        Populates the url-list
        """
        for page in range(1, pages):
            amiripper.pageUrls.append(amiripper.baseUrl + str(page))

    def getSongUrls(self):
        """
        Gets all the URLs for the songs
        """
        #for page in amiripper.pageUrls:
        r = requests.get(amiripper.pageUrls[0])
        htmlSource = r.text
        soup = BeautifulSoup(htmlSource)
        hrefs = [td.find('a',class_='remix') for td in soup.findAll('td',class_='c1')]

        for tag in hrefs:
            print(amiripper.baseUrl + str(tag["href"]))



def main(argv):
    ripper = amiripper(sys.argv[1])
    ripper.getNumberOfPages()

if __name__ == '__main__':
    if (len(sys.argv)) is not 2:
        sys.exit("Usage %s <destination-folder>" % sys.argv[0])
    main(sys.argv[1])
