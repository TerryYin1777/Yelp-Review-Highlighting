#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  8 14:39:07 2017

@author: enyaning
"""


import pandas as pd
import re
import operator
from nltk.corpus import stopwords

import nltk
from nltk.util import ngrams
from nltk.tokenize import sent_tokenize
from nltk import load

from textblob import TextBlob


csv_path = 'chinese.csv'
data = pd.read_csv(csv_path)

wordcount = {}
stop_words =  set(stopwords.words('english'))
costumer_stop_words = ['chinese', 'italian', 'good', 'great', 'food', 'place']
for word in costumer_stop_words: stop_words.add(word)
costumer_not_stop_words = []
for word in costumer_not_stop_words: stop_words.discard(word)

#make a new tagger
_POS_TAGGER = 'taggers/maxent_treebank_pos_tagger/english.pickle'
tagger = load(_POS_TAGGER)


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

            terms = nltk.word_tokenize(sentence.raw.lower())
            tagged_terms=tagger.tag(terms)
            
            for tg in ngrams(tagged_terms,2):
                if tg[0][1].startswith('NN') and tg[1][1].startswith('NN'):
                    key = tg[0][0] + " " + tg[1][0]
                    json = {
                        "restaurantId": restaurantId,
                        "review_id": index,
                        "sentence_id": i,
                        "sentence": sentence.raw,
                        "phrase": key
                    }
                    jsons.append(json)
                    
    except TypeError:
        print("TypeError");
    finally:
        if review_number%20 == 0:
            print(review_number)
        review_number += 1

pd.DataFrame(jsons).to_csv('test.csv')
