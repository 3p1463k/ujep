#!/usr/bin/env python
from tkinter import *
from tkinter import ttk
from tkinter import messagebox as msg
import os
import shutil
import psutil
import time
import subprocess
from time import sleep
from selenium import webdriver
import keyboard
from keyboard import press
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import glob
from pathlib import Path

file_to_overwrite = '/home/evzen/Desktop/WEBOupdate.txt'
my_file = Path("/home/evzen/doc/kpi/data/WEBOupdate.txt")

if my_file.is_file():
    shutil.copy2(my_file, file_to_overwrite)
    print(my_file)
      

    sleep(0.5)

    exit()


else:
    pass


class Root(Tk):

    def __init__(self):
        super(Root, self).__init__()
        self.title("WEB-O-MAT 4.0")
        self.geometry("500x250+100+100")
        self.configure(background='#222222')
        img = PhotoImage(file='/home/evzen/doc/kpi/data/icons/WEBOMAT.gif')
        self.tk.call('wm', 'iconphoto', self._w, img)

        self.initUI()

    def slozka1(self):
        self.label1.configure(text = self.namedir1.get())

    def import_cesta(self):
        self.label2.configure(text = self.namedir2.get())

    def user_name(self):
        self.label3.configure(text = self.namedir3.get())

    def premistovac_on(self):
        proc = subprocess.Popen(['python', '/home/evzen/doc/proj/valeujep/PREMISTOVAC4.py'], shell=False, stdin=None,
                         stdout=subprocess.PIPE, stderr=open('/home/evzen/doc/kpi/data/P4errlogfile.log', 'a'))
        pid = proc.pid
        pids = str(pid)
        print(pid)
        zije = proc.poll()
        pidwr = open("/home/evzen/doc/kpi/data/P4pid.txt", "w")
        pidwr.write(pids)
        pidwr.close()
        print(zije)
        if zije is None:
            self.label2.configure(text='ZAPNUTO', background="#65B87A")
        else:
            pass

        cesta_1 = open("/home/evzen/doc/kpi/data/folderPATH.txt", "r")
        path1 = cesta_1.read()
        os.chdir(path1)
        x = sum(os.path.isdir(folder) for folder in os.listdir(path1))
        pocet = str(x)
        msg.showinfo("PREMISTOVAC4.0", "Startuji, ve slozce je " + pocet + " Videi k premisteni")


    def nacist_video(self):

        bakup_folder = '/home/evzen/doc/kpi/bakup/'
        plocha = '/home/evzen/Desktop/'
        file_to_move = open("/home/evzen/doc/kpi/data/vystrih_videa.txt", "r")
        x = file_to_move.read()
        print(x)
        list_of_directory = glob.iglob('/home/evzen/Desktop/*')

        for i in list_of_directory:
            if x in i:
                print(i)
                shutil.move(i, bakup_folder)
        else:
            pass
        sleep(1)

        path1 = '/home/evzen/Downloads/'
        os.chdir(path1)
        files = sorted(os.listdir(os.getcwd()), key=os.path.getmtime)
        oldest = files[0]
        newest = files[-1]
        vystrih_videa = oldest[11:26]
        filewrtxt5 = open("/home/evzen/doc/kpi/data/vystrih_videa.txt", "w")
        filewrtxt5.write(vystrih_videa)
        filewrtxt5.close()
        self.label5.configure(text=vystrih_videa, background='#336699')
        heslO = self.namedir4.get()
        feedhslo = str(heslO)
        audijmeno = self.namedir3.get()
        audiuser = str(audijmeno)
        print('Vystrih: ', vystrih_videa)
        driver = webdriver.Chrome()
        #driver.service.process
        driver.maximize_window()
        driver.get('http://www.google.com/xhtml')
        driver_pid = psutil.Process(driver.service.process.pid)
        #print(driver_pid.children(recursive=True))
        search_box = driver.find_element_by_name('q')
        search_box.send_keys(feedhslo)
        search_box.submit()
        sleep(0.05)
        driver.quit()
        shutil.move(oldest, plocha)
        filewrtxt3 = open("/home/evzen/doc/kpi/data/unameAudi.txt", "w+")
        filewrtxt3.write(audiuser)
        filewrtxt3.close()
        pidP4 = open("/home/evzen/doc/kpi/data/P4pid.txt", "r")
        pidn = pidP4.read()
        #print(pidn)
        pidf = int(pidn)
        #print(pidf)
        if psutil.pid_exists(pidf):
            print("a process with pid %d exists" % pidf)
        else:
            self.label2.configure(text='VYPNUTO', background="#CC0000")


    def initUI(self):

         self.namedir1 = StringVar()
         self.namedir3 = StringVar()
         self.namedir4 = StringVar()

         self.button1 = ttk.Button(self, text="NACTI DALSI VIDEO", command = self.nacist_video)
         self.button1.place(x=350, y=10)
         self.button2 = ttk.Button(self, text="ZAPNI PREMISTOVACE", command=self.premistovac_on)
         self.button2.place(x=350, y=110)
         self.button3 = ttk.Button(self, text="ULOZIT Novou Cestu", command=self.slozka1)
         self.button3.place(x=10, y=45)
         self.button5 = ttk.Button(self, text="ULOZIT Username", command=self.user_name)
         self.button5.place(x=120, y=130)

         self.label1 = ttk.Label(self, background="#65B87A", foreground="black",text="SLOZKA NA UCKU")
         self.label1.place(x=10, y=25)
         self.label2 = ttk.Label(self, background="#CC0000", foreground="black", text="VYPNUTO")
         self.label2.place(x=350, y=150)
         self.label3 = ttk.Label(self, background="#FFCC00", foreground="black", text="Username AudiTool")
         self.label3.place(x=120, y=110)
         self.label4 = ttk.Label(self, background="#CC0000", foreground="black", text="Napis heslo do AudiTool")
         self.label4.place(x=120, y=180)
         self.label5 = ttk.Label(self, background="#336699", foreground="black", text="VYSTRIH  CISLA VIDEA")
         self.label5.place(x=350, y=40)




         unameAudi = open("/home/evzen/doc/kpi/data/unameAudi.txt", "r")
         fpatr = open("/home/evzen/doc/kpi/data/folderPATH.txt", "r")

         self.textbox1 = ttk.Entry(self, width=30, textvariable=self.namedir1)
         self.textbox1.insert(END, fpatr.read())
         self.textbox1.place(x=10, y=5)

         self.textbox3 = ttk.Entry(self, width=12, textvariable=self.namedir3)
         self.textbox3.place(x=10, y=110)
         self.textbox3.insert(END, unameAudi.read())

         self.textbox4 = ttk.Entry(self, width=12, textvariable=self.namedir4, show = '*')
         self.textbox4.place(x=10, y=180)


root = Root()
root.mainloop()
