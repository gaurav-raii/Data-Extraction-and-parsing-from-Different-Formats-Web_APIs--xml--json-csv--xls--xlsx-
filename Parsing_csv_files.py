# -*- coding: utf-8 -*-
"""
Created on Sat Apr 27 16:36:16 2019

@author: gaura
"""

DATADIR = ""
DATAFILE = "beatles-diskography.csv"


def parse_file(datafile):
    data = []
    keys = []
    row = []
    data_point = {}
    i = 0
    
    with open(datafile, "r") as f:
        for line in f:
            j = 0
            data_point = {}
            line = line.strip()
            if i == 0:
                keys = line.split(",")
            if i > 10:
                continue
            if i >= 1:
                row = line.split(",")
                for key in keys:
                    data_point[key] = row[j]
                    j += 1
                data.insert(len(data),data_point)
            
            
            i += 1
    print (data)
    return (data)


def test():
    # a simple test of your implemetation
    datafile = os.path.join(DATADIR, DATAFILE)
    d = parse_file(datafile)
    firstline = {'Title': 'Please Please Me', 'UK Chart Position': '1', 'Label': 'Parlophone(UK)', 'Released': '22 March 1963', 'US Chart Position': '-', 'RIAA Certification': 'Platinum', 'BPI Certification': 'Gold'}
    tenthline = {'Title': '', 'UK Chart Position': '1', 'Label': 'Parlophone(UK)', 'Released': '10 July 1964', 'US Chart Position': '-', 'RIAA Certification': '', 'BPI Certification': 'Gold'}

    assert d[0] == firstline
    assert d[9] == tenthline

    
test()