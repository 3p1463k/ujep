import os
import csv
import shutil
import glob

list_of_directories = glob.glob('/home/evzen/doc/proj/*/*/*/*.csv')

for x in list_of_directories:

	if 'ADTF' in x:
		nazev = x[40:55]
		with open(x, 'r') as csv_file:
			y = sum(1 for row in csv_file)
			if y < 18:
				print(nazev + "\t" + str(y))



for z in os.listdir(path1):
	path1 = '/home/evzen/doc/'


