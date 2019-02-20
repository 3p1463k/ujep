import os
from time import sleep
import pandas as pd
from selenium import webdriver


path_to_disk = '/home/evzen'

driver = webdriver.Chrome()
#Load the site
driver.get("htpp://")
# count number of videos
number_of_videos = sum(os.path.isdir(path_to_disk))
print("We gonna process: " + number_of_videos)
print("Starting up, Vypoustim Krakena")

for i in path_to_disk:

	#locate search box
	search_box = driver.find_element(By.XPATH, )
	#Clear the search box
	search_box.clear()
	#insert data
	search_box.send_keys(i)
	#press ENTER
	search_box.submit()
	sleep(1)
	#find out status of video

	#print video and status to screen
	print(i + status + "\t" + "OK")
	#append to a file if not approved
	not_approved = open("/home/evzen/notapproved.txt", "a")
	not_approved.write(i + status + "NOT APPROVED")
	#open actual file


	sleep(1)






