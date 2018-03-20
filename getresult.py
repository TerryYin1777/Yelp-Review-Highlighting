# -*- coding: utf-8 -*-
"""
Created on Sat Dec  2 14:32:59 2017

@author: hasee
"""
from textblob import TextBlob
import json
d = {}
with open('groupby_resuaurant_phrase2Grams_review.json') as json_data:
    d=json.load(json_data)
    
for restaurant in d[0:5]:
    print()
    print(restaurant['restaurantId'])
    likes=[]
    dislikes=[]
    for topword in restaurant['top-none-phrases'][0:10]:
        
        scoreword=0
#        print(topword['phrase'])
        for reviews in topword['reviews']:
            countse=0
            scorese=0;
            for sentence in reviews['sentences']:
                sentence=sentence.replace('chicken','beef')
                blob = TextBlob(sentence)
                blob.tags
                blob.noun_phrases
                ns=blob.sentences[0].sentiment.polarity
                scorese+=ns
#                print(sentence)
#                print(ns)
                countse+=1;
            scoreword+=scorese/countse
        result_word_score_avg=scoreword/len(topword['reviews'])
        if result_word_score_avg>0:
            likes.append(topword['phrase'])
        else:
            dislikes.append(topword['phrase'])
#        print(result_word_score_avg)
    print('What the Guests loved Most: ')
    for like in likes:
        print(like)
    print()
    print('What nedd to be improved: ')
    for dislike in dislikes:
        print(dislike)
    print()
    print()
    
