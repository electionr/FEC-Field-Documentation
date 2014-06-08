#! /usr/bin/python

from openpyxl import load_workbook
import csv
import codecs
wb = load_workbook(filename = r'e-filing headers all versions.xlsx')

ws = wb.get_sheet_by_name('all versions')

with codecs.open('e-filing headers all versions.csv','w',encoding='utf-8') as f:
    c = csv.writer(f)
    for r in ws.rows:
        n = []
        for cell in r: 
            v = cell.value 
            if v:
                #print v
                n.append(v.encode('ascii','replace'))
            else:
                n.append(v)
        #print n
        c.writerow(n)
