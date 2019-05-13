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

def get_authors(root):
    authors = []
    for author in root.findall('./fm/bibl/aug/au'):
        data = {
                "fnm": None,
                "snm": None,
                "email": None,
                "insr": []

        }

        data["fnm"] = author.find('./fnm').text
        data["snm"] = author.find('./snm').text
        data["email"] = author.find('./email').text
        insr = author.findall('./insr')
        for i in insr:
            data["insr"].append(i.attrib["iid"])
        authors.append(data)

    return authors

def test():
    solution = [{'fnm': 'Omer', 'snm': 'Mei-Dan', 'email': 'omer@extremegate.com'}, {'fnm': 'Mike', 'snm': 'Carmont', 'email': 'mcarmont@hotmail.com'}, {'fnm': 'Lior', 'snm': 'Laver', 'email': 'laver17@gmail.com'}, {'fnm': 'Meir', 'snm': 'Nyska', 'email': 'nyska@internet-zahav.net'}, {'fnm': 'Hagay', 'snm': 'Kammar', 'email': 'kammarh@gmail.com'}, {'fnm': 'Gideon', 'snm': 'Mann', 'email': 'gideon.mann.md@gmail.com'}, {'fnm': 'Barnaby', 'snm': 'Clarck', 'email': 'barns.nz@gmail.com'}, {'fnm': 'Eugene', 'snm': 'Kots', 'email': 'eukots@gmail.com'}]
    
    root = get_root(article_file)
    data = get_authors(root)

    assert data[0] == solution[0]
    assert data[1]["fnm"] == solution[1]["fnm"]
    

test()