#!/usr/bin/python3
#created by Budi Gunawan

import os
import sys
import re
from bs4 import BeautifulSoup

count=1
print("Loading...\n")

rawdir = "/home/bnawan/Documents/BIGDATA/tugas1/downloadedfile"
#rawdir = "/home/bnawan/Documents/BIGDATA/tugas1/test"
ls = os.popen('ls '+rawdir).read()
files = str(ls).split('\n')
print(files)
for thefile in files:
    if thefile=='':
        continue
    print("\nProcessing file-"+str(count)+"\n",flush=True)
    fileout=os.path.basename(thefile)+'.bersih.dat'
    print("fileout : "+fileout+"\n")
    
    pathclean = "/home/bnawan/Documents/BIGDATA/tugas1/cleaned"
    fileout=pathclean+"/"+fileout
    print(fileout+"\n")

    try:
        with open (fileout, "w") as fileHandler:
            html=os.popen('cat '+rawdir+'/'+thefile).read()
            ekstraktor=BeautifulSoup(html, 'html.parser')
            title=ekstraktor.title.string
            print(title)
            htmltime=ekstraktor.find(attrs={"name":"publishdate"})
            time=htmltime['content']
            print(time)
            # kill all script and style elements
            
            content=str(ekstraktor.find_all(id='detikdetailtext'))
            contentext=BeautifulSoup(content, 'html.parser')

            for script in contentext(["script", "style"]):
                script.extract()    # rip it out
            
            detailtag=contentext.find("div", {'class':'detail_tag'})
            if detailtag:
                detailtag.decompose()

            text=contentext.get_text()
            # break into lines and remove leading and trailing space on each
            lines = (line.strip() for line in text.splitlines())
            # break multi-headlines into a line each
            chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
            # drop blank lines
            text = '\n'.join(chunk for chunk in chunks if chunk)

            text=re.sub(r'[\[!@#$\]]', '', text)
            text=re.sub('\n', '', text)
            print(text)
            fileHandler.write(title+"\n"+time+"\n"+text)
    except OSError as exc:
        print("Cannot open file !")
        sys.exit(1)

    count+=1



