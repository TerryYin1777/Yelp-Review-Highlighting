#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  8 14:39:07 2017

@author: enyaning
"""


import pandas as pd

from textblob import TextBlob

csv_path = 'chinese.csv'
data = pd.read_csv(csv_path)

jsons = []

review_number = 0
for index, row in data.iterrows():
    try:
        review = row['review_text']
        restaurantId = row['restaurantId']
        
        blob = TextBlob(review)
        blob.noun_phrases
        
        for i in range(len(blob.sentences)):
            sentence = blob.sentences[i]
            for phrase in sentence.noun_phrases:
                json = {
                    "restaurantId": restaurantId,
                    "review_id": index,
                    "sentence_id": i,
                    "sentence": sentence.raw,
                    "phrase": phrase
                }
                jsons.append(json)
    except TypeError:
        print("TypeError");
    finally:
        if review_number%20 == 0:
            print(review_number)
        review_number += 1

pd.DataFrame(jsons).to_csv('test.csv')
