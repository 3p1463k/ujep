#!/usr/bin/env python

#Evzen Ptacek

#Navod :
#1 vytvor folder KPI na plose
#2 zkopiruj do ni tento soubor
#3 v tomto souboru na radku path = zkopirujte svuj adresar z ktereho chcete tahat  
#4 ulozte soubor a na plose vytvorte novy shortcut k tomuto souboru
#5 kliknete na novy shortcut a windows se yepta jak to chcete otevrit
#6 navedte windows na C:\WinPython_3_4\python-3.4.3.amd64\pythonw
#7 a je to, ted po kliknuti na tento shortcut se vam presune video na plochu
#8 a v mysi mate vzstrihle cislo vipro audi tool

import os

import shutil

import pyperclip

path = ' U:\\FOR_VALIDATION\\VPC2\\KPI\\LEVEL_1\\Ptáèek Evžen\\ '

os.chdir(path)

files = sorted(os.listdir(os.getcwd()), key=os.path.getmtime)

oldest = files[0]
newest = files[-1]

pyperclip.copy(oldest[11:26]

shutil.move (oldest,"C:\\Users\\anotator\\Desktop\\KPI\\")
               
               
               
               
import os
import shutil
import pyperclip

def makmov():
    path = 'U:\\FOR_VALIDATION\\VPC2\\KPI\\LEVEL_1\\Ptáček Evžen\\'    

    os.chdir(path)
    files = sorted(os.listdir(os.getcwd()), key=os.path.getmtime)

        oldest = files[0]
        newest = files[-1]

        pyperclip.copy(oldest[11:26])

        for oldest in files:
            shutil.move(oldest, "/C:\\Users\\anotator\\Desktop\\KPI\\")
            break
makmov()
               
               
               
               





