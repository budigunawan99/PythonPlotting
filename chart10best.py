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
from matplotlib import pyplot as plt

filedir = "/home/bnawan/Documents/BIGDATA/tugas1/cleaned"
files= os.popen('ls '+filedir).read()
listfile=str(files).split('\n')
kamus={}
print("\nLoading...\n",flush=True)

for thefile in listfile:
    if thefile=='':
        continue

    file = filedir+"/"+os.path.basename(thefile)
    textfile=os.popen('cat '+file).read()
    textfile=textfile.lower()
    textfile=re.sub(r'[^a-zA-Z\s]', ' ', textfile)
    tokenizedfile = nltk.word_tokenize(textfile)
        
    for bg, count in FreqDist(ngrams(tokenizedfile, 1)).most_common():
        kata = ' '.join(bg)
        if kata in kamus:
            kamus[kata]= kamus.get(kata, 0) + 1
        else:
            kamus[kata]=count
        #print('\t'.join([' '.join(bg), str(count)]), end='\n', file=fileHandler)

word = []
value = []
sortedword = sorted(kamus.items(), key=lambda kv: kv[1], reverse=True)
sorteddict = collections.OrderedDict(sortedword)

for hashkata in list(sorteddict.keys())[0:10]:
    word.append(hashkata)
    value.append(kamus[hashkata])
    #print(word)  
    #print(value) 

#Top 10 words in histogram

xs = [i + 0.1 for i, _ in enumerate(word)]
# plot bars with left x-coordinates [xs], heights [num_oscars]
plt.bar(xs, value, color='g')
plt.xlabel("word list")
plt.ylabel("frequency of word")
plt.title("Top 10 words in 3000 news")
# label x-axis with movie names at bar centers
plt.xticks([i + 0.1 for i, _ in enumerate(word)], word)
plt.show()

#Top 10 words in pie bar chart

fig1, ax1 = plt.subplots()
patches, texts, autotexts = ax1.pie(value, textprops=dict(color="w"), labels=word, autopct='%1.1f%%', startangle=90)
for text in texts:
    text.set_color('black')
for autotext in autotexts:
    autotext.set_color('black')
# Equal aspect ratio ensures that pie is drawn as a circle
ax1.axis('equal')  
plt.tight_layout()
plt.show()


        
