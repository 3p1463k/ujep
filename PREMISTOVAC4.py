import os
import shutil
import schedule
import time
from time import sleep
from datetime import datetime


timestamp = str(datetime.now())
append4 = open("/home/evzen/doc/kpi/data/Daily_log.txt", "a")
append4.write("Spoustim PREMISTOVAC4: " + timestamp + "\n")
append4.close()
plocha = '/home/evzen/Desktop/'
P4pid = os.getpid()
write_pid = open("/home/evzen/doc/kpi/data/P4pid.txt", "w")
P4pid_str = str(P4pid)
write_pid.write(P4pid_str)
write_pid.close()
print(P4pid)

def job1():

	timestamp = str(datetime.now())
	cesta_1 = open("/home/evzen/doc/kpi/data/folderPATH.txt", "r")
	path1 = cesta_1.read()
	os.chdir(path1)
	x = sum(os.path.isdir(folder) for folder in os.listdir(path1))

	print(x)

	path2 = '/home/evzen/doc/a/'
	os.chdir(path2)
	y = sum(os.path.isdir(folder) for folder in os.listdir(path2))

	print(y)
	#print("From:"  path1, "To:", path2, timestamp[:19])

	if x > 0 and y < 6:

		os.chdir(path1)
		files = sorted(os.listdir(os.getcwd()), key=os.path.getmtime)
		oldest = files[0]
		newest = files[-1]
		for oldest in files:
			shutil.move(oldest, path2)
			sleep(1)
			append1 = open("/home/evzen/doc/kpi/data/ReportPremisteno.txt", "a")
			append1.write("From:" + str(path1) + oldest + ' ' " To:" + str(path2) + oldest + ' ' + str(timestamp[:19]) + "\n")
			append1.close()
			sleep(1)

			break
	elif x == 0:
			append4 = open("/home/evzen/doc/kpi/data/Daily_log.txt", "a")
			append4.write("Zastavuji PREMISTOVAC4: " + timestamp + "\n")
			append4.close()
			print('NO MORE TO MOVE')
			#import ctypes  # An included library with Python install.
			#ctypes.windll.user32.MessageBoxW(0, "Nemam vice videi", "PREMISTOVAC4", 1)
			exit()

def job2():

	timestamp = str(datetime.now())
	append2 = open("/home/evzen/doc/kpi/data/ReportPremisteno.txt", "a")
	append2.write(str(timestamp[:19]) + "\n")
	append2.close()
	sleep(1)


def job3():

	path3 = '/home/evzen/doc/kpi/bakup/'
	os.chdir(path3)
	pocet_bakup = sum(os.path.isdir(folder) for folder in os.listdir(path3))
	print(pocet_bakup)

	if pocet_bakup > 3:

		folders = sorted (os.listdir(os.getcwd()), key=os.path.getmtime)
		oldest = folders[0]
		newest = folders[-1]

		for oldest in folders:
			timestamp = str(datetime.now())
			append3 = open("/home/evzen/doc/kpi/data/ReportVymazano.txt", "a")
			append3.write("Smazano video :" + oldest + str(timestamp[:19]) + "\n")
			append3.close()
			shutil.rmtree(oldest)
			break


#schedule.every().day.at("15:40").do(job2)
#schedule.every().hour.do()
#schedule.every(1).minute.do(job3)
#schedule.every(1).minute.do(job1)
schedule.every(15).seconds.do(job1)


while 1:
	schedule.run_pending()
	sleep(1)

