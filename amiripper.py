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
from time import sleep
import requests
import sys


def shellEscape(s):
    return s.replace("(","\\(").replace(")","\\)").replace(" ","\\ ")

class amiripper:
    baseUrl = 'http://amigaremix.com/'
    pageUrls = []
    songUrls = []
    numberOfPages = 0

    def __init__(self):
        """
        Initializes all the variables
        """
        amiripper.getNumberOfPages()
        amiripper.populatePageUrls()
        amiripper.getSongUrls()
        amiripper.downloadSongs()

    def getNumberOfPages():
        """
        Figures out how many pages there are to download from
        """
        r = requests.get(amiripper.baseUrl)
        soup = BeautifulSoup(r.text)
        selects = soup.find('select', attrs={'name': 'page'})
        amiripper.numberOfPages = len(selects.find_all('option'))

    def populatePageUrls():
        """
        Populates the url-list
        """
        for page in range(amiripper.numberOfPages):
            # Since range starts at 0, add 1
            amiripper.pageUrls.append(amiripper.baseUrl + str(page+1))

    def downloadSongs():
        """
        Downloads a song and saves it with the correct filename
        """
        for index,song in enumerate(amiripper.songUrls):
            r = requests.get(song, stream=True)
            localFilename = song.split('/')[-1].replace("%20", " ")
            with open(localFilename, 'wb') as f:
                for chunk in r.iter_content(chunk_size=1024):
                    if chunk: # filter out keep-alive new chunks
                        f.write(chunk)
                        f.flush()
            print("%d of %d: %s" % (index+1, len(amiripper.songUrls), localFilename))


    def getSongUrls():
        """
        Gets all the URLs for the songs
        """
        for page in amiripper.pageUrls:
            r = requests.get(page)
            htmlSource = r.text
            soup = BeautifulSoup(htmlSource)
            hrefs = [td.find('a',class_='remix') for td in soup.findAll('td',class_='c1')]
            for tag in hrefs:
                amiripper.songUrls.append(amiripper.baseUrl + str(tag["href"]))



def main():
    ripper = amiripper()

if __name__ == '__main__':
    if (len(sys.argv)) is not 1:
        sys.exit("Usage %s" % sys.argv[0])
    main()
