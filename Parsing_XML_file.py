# -*- coding: utf-8 -*-
"""
Created on Mon May 13 17:53:16 2019

@author: gaura

The task here is to extract data from xml on authors of an article and add it to a list, one item for an author..
The tags for first name, surname and email are mapped directly to the dictionary key.
"""

import xml.etree.ElementTree as ET

article_file = "exampleResearchArticle.xml"

def get_root(fname):
    tree = ET.parse(fname)
    return tree.getroot()