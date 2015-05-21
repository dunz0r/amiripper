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

class amiripper:
    baseUrl = 'http://amigaremix.com/'
    outputFolder = ''
    pageUrls = []
    def __init__(self, outputFolder):
        """
        Initializes all the variables
        """
        amiripper.outputFolder = outputFolder
        amiripper.populatePageUrls(self)

    def populatePageUrls(self):
        """
        Populates the url-list
        Keyword arguments:
        url -- the base url to use
        """
        for page in range(1, 64):
            amiripper.pageUrls.insert(page, amiripper.baseUrl + str(page))
        print(amiripper.pageUrls)

def main(argv):
    ripper = amiripper(sys.argv[1])

if __name__ == '__main__':
    if (len(sys.argv)) is not 2:
        sys.exit("Usage %s <destination-folder>" % sys.argv[0])
    main(sys.argv[1])
