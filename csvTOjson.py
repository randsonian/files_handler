# -*- coding: utf-8 -*-
"""
Created on Sun Sep  2 21:14:11 2018

@author: juan
"""

import os

input_files_location = r'C:\Users\juan\Documents\dev\benefits_input'
output_location = r'C:\Users\juan\Documents\dev\benefits_input'

def parse_record(record):
    parse_r = []
    element = ''
    for c in record:
        if c != '|':
            element += c
        elif c == '|':
            parse_r.append(element)
            element = ''
    return(parse_r)


## Read input files in input_list
input_list = []
os.chdir(input_files_location)
with open('bi_001.txt') as input_file:
    #Read Header
    header_txt = input_file.readline()
    header = parse_record(header_txt)
    while True:
        record = input_file.readline()
        if record == '':
            break
        else:
            record_p = parse_record(record)
            print(header)
            print(record_p)
            ##inter = [(header[i], record_p[i]) for i in range(len(header))]
        
    

## Prepare output file
## os.chdir(output_location)
## if os.path.isfile('output.json'): os.remove('output.json')
## con_file = open('conFile.txt', 'w+')




print(header)


