# -*- coding: utf-8 -*-
"""
Created on Sat Apr 22 16:51:56 2019

@author: gaura
"""
"""
Your task is as follows:
- read the provided Excel file
- find and return the min, max and average values for the COAST region
- find and return the time value for the min and max entries
- the time values should be returned as Python tuples

Please see the test function for the expected return format

"""


import xlrd
from zipfile import ZipFile
datafile = "2013_ERCOT_Hourly_Load_Data.xls"


def open_zip(datafile):
    with ZipFile('{0}.zip'.format(datafile), 'r') as myzip:
        myzip.extractall()


def parse_file(datafile):
    workbook = xlrd.open_workbook(datafile)
    sheet = workbook.sheet_by_index(0)

    
maxval = 0
minval = 999999
maxrow = 1
minrow = 1
total = 0
    
for r in range(1, sheet.nrows):
    if sheet.cell_value(r, 1) > maxval:
            maxval = sheet.cell_value (r, 1)
            maxrow = r 
                
for r in range(1, sheet.nrows):            
    if sheet.cell_value(r, 1) < minval:
            minval = sheet.cell_value(r, 1)
            minrow = r
                
for r in range(1, sheet.nrows):                       
    total += float(sheet.cell_value(r, 1))
    
data = {
        'maxtime': (0, 0, 0, 0, 0, 0),
        'maxvalue': 0,
        'mintime': (0, 0, 0, 0, 0, 0),
        'minvalue': 0,
        'avgcoast': 0
}
data['maxtime'] = xlrd.xldate_as_tuple(sheet.cell_value(maxrow, 0), 0)
data['maxvalue'] = maxval
data['mintime'] = xlrd.xldate_as_tuple(sheet.cell_value(minrow, 0), 0)
data['minvalue'] = minval
data['avgcoast'] = total/(sheet.nrows -1)
    
print (data)
return (data)


def test():
    open_zip(datafile)
    data = parse_file(datafile)

    assert data['maxtime'] == (2013, 8, 13, 17, 0, 0)
    assert round(data['maxvalue'], 10) == round(18779.02551, 10)


test()
