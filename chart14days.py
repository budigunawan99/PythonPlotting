#!/usr/bin/python3
#created by Budi Gunawan

import nltk
#nltk.download('punkt')
import numpy as np
from nltk import word_tokenize
from nltk.util import ngrams
from nltk import FreqDist
import os
import re
import operator
import collections
import datetime
from matplotlib import pyplot as plt

dates = ["2019-07-01", "2019-07-02", "2019-07-03", "2019-07-04", "2019-07-05", "2019-07-06", "2019-07-07",
        "2019-07-08", "2019-07-09", "2019-07-10", "2019-07-11", "2019-07-12", "2019-07-13", "2019-07-14"]            
filedir = "/home/bnawan/Documents/BIGDATA/tugas1/cleaned"

files= os.popen('ls '+filedir).read()
listfile=str(files).split('\n')
kamus={}
day={}
datecounter=0
print("\nLoading...\n",flush=True)

for date in dates:
    day[datecounter] = {}
    for thefile in listfile:
        if thefile=='':
            continue

        file = filedir+"/"+os.path.basename(thefile)
        textfile=os.popen('cat '+file).read()
        line = str(textfile).split('\n')
        #print(line[1])
        alldatetime = line[1]
        dateobj = datetime.datetime.strptime(alldatetime, '%Y/%m/%d %H:%M:%S')
        checkdate = str(dateobj.date())
        if date==checkdate:
            print("date matched "+date)
            textfile=textfile.lower()
            textfile=re.sub(r'[^a-zA-Z\s]', ' ', textfile)
            tokenizedfile = nltk.word_tokenize(textfile)
            
            for bg, count in FreqDist(ngrams(tokenizedfile, 1)).most_common():
                kata = ' '.join(bg)
                if kata in kamus:
                    kamus[kata]= kamus.get(kata, 0) + 1
                    day[datecounter][kata]= kamus.get(kata, 0) + 1
                else:
                    kamus[kata]=count
                    day[datecounter][kata]= count
            #print(checkdate,flush=True)
    datecounter+=1    

top10=[]
word = {}
freq=[]
sortedword = sorted(kamus.items(), key=lambda kv: kv[1], reverse=True)
sorteddict = collections.OrderedDict(sortedword)

for hashkata in list(sorteddict.keys())[0:10]:
    top10.append(hashkata)
print("\nTop 10 list :\n")
for katas in top10:
    for tgl in range(0,14):
         freq.append(day[tgl][katas]) 
    word[katas]=[]
    word[katas].extend(freq)
    freq.clear()
    print(katas+"\t"+str(word[katas]))

for x in word:
    plt.plot(dates, word[x], label=x)

plt.xticks(rotation=45)
plt.title("Grafik Top 10 Kata pada 14 Hari Pertama Juli 2019")    
plt.xlabel('Days')
plt.ylabel('Frequency')
plt.legend(loc=1)
plt.show()
