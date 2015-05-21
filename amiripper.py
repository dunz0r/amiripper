#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2015 Gabriel Fornaeus <gf@hax0r.se>
#
# Distributed under terms of the GPLv3 license.

"""
A small program which downloads all songs from http://amigaremix.com
"""

import sys

def main(argv):
    outputFolder = argv

if __name__ == '__main__':
    if (len(sys.argv)) is not 2:
        sys.exit("Usage %s <destination-folder>" % sys.argv[0])
    main(sys.argv[1])
