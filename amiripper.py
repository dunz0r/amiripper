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

import requests
import sys

class amiripper(url):
    urls = []
    def __init__(self, urls):
        populateUrls(url)

    def populateUrls(self, url):
        """
        Populates the url-list
        Keyword arguments:
        url -- the base url to use
        """
        for page in range(1, 64):
            amiripper.urls[page] = "http://amigaremix.com/remixes/%s" % page

def main(argv):
    outputFolder = argv

if __name__ == '__main__':
    if (len(sys.argv)) is not 2:
        sys.exit("Usage %s <destination-folder>" % sys.argv[0])
    main(sys.argv[1])
