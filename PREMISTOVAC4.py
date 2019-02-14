import os
import shutil
import schedule
import time
from time import sleep
from datetime import datetime
from pathlib import Path


timestamp = str(datetime.now())
append4 = open("/home/evzen/doc/kpi/data/Daily_log.txt", "a")
append4.write("Spoustim PREMISTOVAC4: " + timestamp + "\n")
append4.close()
P4pid = os.getpid()
write_pid = open("/home/evzen/doc/kpi/data/P4pid.txt", "w")
P4pid_str = str(P4pid)
write_pid.write(P4pid_str)
write_pid.close()
print("PID: " + P4pid_str)
kill_file = ("/home/evzen/doc/kpi/data/kill.txt")

if os.path.exists(kill_file) == True:
    os.unlink(kill_file)
else:
    print("NO KILL FILE")
    pass


def job1():
	timestamp = str(datetime.now())
	cesta_1 = open("/home/evzen/doc/kpi/data/folderPATH.txt", "r")
	path1 = cesta_1.read()
	os.chdir(path1)
	x = sum(os.path.isdir(folder) for folder in os.listdir(path1))

	print(x)

	path2 = '/home/evzen/doc/kpi/kpi'
	os.chdir(path2)
	y = sum(os.path.isdir(folder) for folder in os.listdir(path2))

	print(y)

	if x > 0 and y < 3:

		os.chdir(path1)
		files = sorted(os.listdir(os.getcwd()), key=os.path.getmtime)
		oldest = files[0]
		newest = files[-1]

		#os.path.join(x)
		#velikost_dat =
		for oldest in files:
			print(x)
			shutil.move(os.path.join(path1, oldest), os.path.join(path2, oldest))
			#shutil.move(oldest, path2)
			append1 = open("/home/evzen/doc/kpi/data/ReportPremisteno.txt", "a")
			append1.write(str(path1) + " " + oldest + "  " + str(path2) + " " + str(timestamp[:19]) + "\n")
			append1.close()

			print("Premisteno: " + oldest)
			break
	elif x == 0:
			# append4 = open("/home/evzen/doc/kpi/data/Daily_log.txt", "a")
			# append4.write("Zastavuji PREMISTOVAC4 " + timestamp + "\n")
			# append4.close()
			# import tkinter as tk
			# from tkinter import messagebox as msg
			# root = tk.Tk()
			# root.withdraw()
			# msg.showwarning("PREMISTOVAC4.0", "VE SLOZCE DOSLI VIDEA, ZASTUVUJI PREMISTOVANI")
			# print('NO MORE TO MOVE, EXITING')
			# exit()
			pass

def job2():
	kill_file = ("/home/evzen/doc/kpi/data/kill.txt")
	if os.path.exists(kill_file) == True:
		exit()
	else:
		print("NO KILL FILE")
		pass


def job3():

	path3 = '/home/evzen/doc/kpi/bakup/'
	os.chdir(path3)
	pocet_bakup = sum(os.path.isdir(folder) for folder in os.listdir(path3))
	pocet_bak = str(pocet_bakup)
	print("Pocet bakup:" + pocet_bak)
	count = 0

	if pocet_bakup > 3:

		folders = sorted (os.listdir(os.getcwd()), key=os.path.getmtime)
		oldest = folders[0]
		newest = folders[-1]
		for oldest in folders:
			timestamp = str(datetime.now())
			append3 = open("/home/evzen/doc/kpi/data/ReportVymazano.txt", "a")
			append3.write("Smazano " + oldest + " " + str(timestamp[:19]) + "\n")
			append3.close()
			print("Vymazano: " + " " + oldest)
			shutil.rmtree(oldest)
			count += 1
			print(count)
			append5 = open("/home/evzen/doc/kpi/data/dayreport.txt", "a")
			video_smazano = str(count)
			append5.write(video_smazano)
			append5.close()

			break

def job4():
	report_file = open("/home/evzen/doc/kpi/data/dayreport.txt", "r")
	report = report_file.read()
	pocet_pro_graf = len(report)






#schedule.every().day.at("15:40").do(job2)
schedule.every(5).minutes.do(job4)
schedule.every(10).seconds.do(job3)
schedule.every(5).seconds.do(job2)
schedule.every(12).seconds.do(job1)

while 1:
	schedule.run_pending()
	sleep(1)

