#!/usr/bin/python3
#created by Budi Gunawan

import sys
import mechanicalsoup
import re
import os
from datetime import datetime

browser = mechanicalsoup.StatefulBrowser()
	
# Returns a datetime object containing the local date and time
dateTimeObj = datetime.now()

if len(sys.argv) == 2 :
	file= sys.argv[1]
	print (file)
else:
	print("Invalid argument inserted !\nPlease insert $ filename newfile")
	sys.exit(1)

print("\nloading ...\n")
print("\nMembuat file "+file)
f=open(file,"w")
print ("\nBerhasil membuat file "+file+"\n")
print("\nLoading ...\n")

count=0
urls={}
tgl1=1
tgl2=31 
bln1=7 
bln2=7 
thn1=2019
thn2=2019
forcebreak= False

while thn1<=thn2:
	tahun=thn1
	while bln1<=bln2:
		bulan = bln1
		while tgl1<=tgl2:
			tanggal=tgl1
			halaman=1
			while halaman <=10:
				url=""
				if tanggal<10 :
					if bulan<10 :
						url = "https://news.detik.com/indeks/all/"+str(halaman)+"?date=0"+str(bulan)+"/0"+str(tanggal)+"/"+str(tahun)
						#print(url)
						#f.write(url+"\n")
					else :
						url = "https://news.detik.com/indeks/all/"+str(halaman)+"?date="+str(bulan)+"/0"+str(tanggal)+"/"+str(tahun)
						#print(url)
						#f.write(url+"\n")
				else:
					if bulan<10 :
						url = "https://news.detik.com/indeks/all/"+str(halaman)+"?date=0"+str(bulan)+"/"+str(tanggal)+"/"+str(tahun)
						#print(url)
						#f.write(url+"\n")
					else :
						url = "https://news.detik.com/indeks/all/"+str(halaman)+"?date="+str(bulan)+"/"+str(tanggal)+"/"+str(tahun)
						#print(url)
						#f.write(url+"\n")
				halaman+=1
				browser.open(url)	
				test=browser.links()
				for link in test:
					page=link['href']
					a = re.search("/berita/",page)
					if (a) and page not in urls:
						urls[page]=dateTimeObj
						count+=1
						print("\rTanggal "+str(tanggal)+" bulan "+str(bulan)+" => Total link(s) : "+str(count))
						if count >= 3000:
							forcebreak = True
							break
			if forcebreak: break
			tgl1+=1
		if forcebreak: break
		bln1+=1
	if forcebreak: break
	thn1+=1
	

browser.close()
for link in urls.keys():
	f.write(link+"\n")


f.close()
print("\nBerhasil mendapatkan "+str(count)+" url\n")
print("\nApakah Anda ingin langsung mendownload halaman dari link yang telah didapat ? Y/N")

pilih = sys.stdin.readline()
pilih = pilih.rstrip("\n")

if pilih == 'y' or pilih == 'Y':
	print("\nMenjalankan \'python3 download.py filename\' ... \n")
	os.system('python3 download.py '+sys.argv[1])
else :
	print("\nAnda dapat menjalankan \'python3 download.py filename\' untuk mendownload halaman dari link yang telah didapat ... \n")



			
