# -*- coding: utf-8 -*-
"""
Created on Wed Nov  1 15:00:40 2017

@author: Y. Zhao
"""

import time
import requests
import os, shutil

def getReviews(urlBase, url, filepath, maxReviews = 300):
    for p in range(0, int(maxReviews / 20)):
        pageLink=urlBase + url + '?start=' + str(p * 20) + '&sort_by=date_desc'# make the page url
        for i in range(5): # try 5 times
            try:
                #use the browser to access the url
                response=requests.get(pageLink,headers = { 'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36', })
                html=response.content # get the html
                break # we got the file, break the loops
            except Exception as e:# browser.open() threw an exception, the attempt to get the response failed
                print ('failed attempt',i)
                time.sleep(2) # wait 2 secs


        if not html:
            raise Exception()
            continue # couldnt get the page, ignore
        else:
            with open(filepath + '/' + str(p) + '.html', 'w') as f:
                f.write(html.decode('ascii', 'ignore'))


#reviews('https://www.yelp.com', '/biz/lao-sze-chuan-glendale-5')

def getGene(name, maxReviews = 300):
    with open(name + '.txt', 'r') as f:
        ls = f.readlines()
        print(int(len(ls) / 3))
        for i in range(0, len(ls), 3):
            id = ls[i].strip()
            path = ls[i + 2].strip().split('\t')[0]
            print(id + " " + ls[i + 2].strip().split('\t')[1])
            if os.path.exists(os.path.join(os.getcwd(), name + "_" + id)) == False:
                try:
                    os.mkdir(os.path.join(os.getcwd(), 'temp'))
                except FileExistsError as e:
                    shutil.rmtree(os.path.join(os.getcwd(), 'temp/'))
                    os.mkdir(os.path.join(os.getcwd(), 'temp'))
                try:
                    getReviews('https://www.yelp.com', path, os.path.join(os.getcwd(), 'temp'), maxReviews = 300)
                    with open(os.path.join(os.getcwd(), 'temp') + '/metadata', 'w') as f:
                        f.write(ls[i] + ls[i + 1] + ls[i + 2] + str(int(maxReviews / 20)) + '\n')
                    os.rename(os.path.join(os.getcwd(), 'temp'), os.path.join(os.getcwd(), name + "_" + id))
                except Exception as e:
                    print ('failed attempt', name + "_" + id)
                    continue
            
if __name__ == '__main__':
    getGene('chinese', maxReviews = 300)
