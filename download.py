#!/usr/bin/python3
import wget
import os
import sys

output = "/home/bnawan/Documents/BIGDATA/tugas1/downloadedfile/"
file= sys.argv[1]
# Open file 
with open (file, "r") as fileHandler:
    x = 1
    # Read each line in loop
    for line in fileHandler:
        line=line.rstrip("\n")
        os.system('wget -O '+output+'file-'+str(x)+'.html '+line)
        x+=1
