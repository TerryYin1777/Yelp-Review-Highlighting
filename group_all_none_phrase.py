#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  8 14:39:07 2017

@author: enyaning
"""


import pandas as pd
import json

csv_path = 'test.csv'
data = pd.read_csv(csv_path)

reduce1 = {}
print('reducing 1')

for index, row in data.iterrows():
    key = str(row['restaurantId']) + "|" + row['phrase'] + "|" + str(row['review_id']) # + "|" + str(row['sentence_id'])
    if key not in reduce1:
        reduce1[key] = []
    reduce1[key].append(row['sentence'])
    
reduce2 = {}
print('reducing 2')

for k, v in reduce1.items():
    parts = k.split("|")
    key = parts[0] + "|" + parts[1] # restaurantId | phrase
    if key not in reduce2:
        reduce2[key] = []
    reduce2[key].append({'review_id': parts[2], 'sentences': v})

reduce3 = {}
print('reducing 3')

for k, v in reduce2.items():
    parts = k.split("|")
    key = parts[0] # restaurantId
    if key not in reduce3:
        reduce3[key] = []
    reduce3[key].append({'phrase': parts[1], 'reviews': v})
        
def sort_top_100(arr):
    return sorted(arr, key = lambda k: len(k['reviews']), reverse=True)[:100]

print('finally')

res = []
for k, v in reduce3.items():
    res.append({'restaurantId': k, 'top-none-phrases': sort_top_100(v)})
    
with open('json.json', 'w') as f:
    json.dump(res, f, indent=4, sort_keys=True)

