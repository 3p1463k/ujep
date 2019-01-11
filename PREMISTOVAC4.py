import os
import shutil
import schedule
import time
from time import sleep
from datetime import datetime

def job1():

	timestamp = str(datetime.now())
	path1 = '/home/evzen/doc/b/'
	os.chdir(path1)
	x = sum(os.path.isdir(folder) for folder in os.listdir(path1))
	print(x)

	path2 = '/home/evzen/doc/a/'
	os.chdir(path2)
	y = sum(os.path.isdir(folder) for folder in os.listdir(path2))
	print(y)
	#print("From:"  path1, "To:", path2, timestamp[:19])
	if y < 6 and x > 0:
		os.chdir(path1)
		files = sorted(os.listdir(os.getcwd()), key=os.path.getmtime)
		oldest = files[0]
		newest = files[-1]
		for oldest in files:
			shutil.move(oldest, path2)
			sleep(1)
			append1 = open("/home/evzen/doc/kpi/PREMISTOVAC4DATA.txt", "a")
			append1.write("From:" + str(path1) + oldest + ' ' " To:" + str(path2) + oldest + ' ' + str(timestamp[:19]) + "\n")
			append1.close()
			sleep(1)

			break
	elif x == 0: 
			print('NO MORE TO MOVE')

def job2():
	append2 = open("/home/evzen/doc/kpi/Report.txt", "a")
	append2.write(str(timestamp[:19]) + "\n")
	append2.close()
	sleep(1)



schedule.every().day.at("15:00")do(job2)
#schedule.every().hour.do()
#schedule.every().minute.do()
schedule.every(15).seconds.do(job1)

while 1:
	schedule.run_pending()
	sleep(1)

