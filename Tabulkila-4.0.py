import os
import glob
import pandas as pd

""" Udaje anotatoru """
video = "nejaktvideo.dat"#glob.iglob(C:/APC/*/*.dat)
APC = "APC22"#glob.iglob(C:/APC*/)
jmeno = "Evzen Ptacek"#glob.iglob(C:/GE/)
date = "21.06.2019"#"datetime.now"
hour_start = "06:52"
pauza = 0
hour_finish = "07:52"
status1 = "Anotable"
status2 = "Send for validation"
# """ Udaje validatoru"""
# validator_folder = "U:/"
# 1st_validation_time = "00:30"
# 2nd_validation_time = 
# 3rd_validation_time =
# status_v = 
# pauza_v= 

""" Create dataframe """
df = pd.DataFrame({"video":[video], "status1":[status1], "name":[jmeno],"date":[date],
	                "start":[hour_start], "break":[pauza], "finish":[hour_finish],
	                "status2":[status2] })

report = df.to_excel("/home/evzen/doc/misc/report.xlsx")
df
report

def job1():
	

#schedule.every().day.at("15:40").do(job2)
schedule.every(5).minutes.do(job4)
schedule.every(10).seconds.do(job3)
schedule.every(5).seconds.do(job2)
schedule.every(12).seconds.do(job1)

while 1:
	schedule.run_pending()
	sleep(1)