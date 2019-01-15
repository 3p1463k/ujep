#!/usr/bin/env python
from tkinter import *
from tkinter import ttk
import os
import shutil
import time
from time import sleep
from selenium import webdriver


class Root(Tk):

    def __init__(self):
        super(Root, self).__init__()
        self.title("POSUNOVAC 4.0")
        self.geometry("500x250+100+100")
        self.configure(background='#222222')

        self.initUI()


    def user_name(self):
        self.label3.configure(text = self.namedir3.get())

    def pass_word(self):

        pass
        #self.label4.configure(text = self.namedir4.get())

    def nalozit_kotel(self):

        path1 = '/home/evzen/Downloads/'
        heslO = self.namedir4.get()
        feedhslo = str(heslO)
        audijmeno = self.namedir3.get()
        audiuser = str(audijmeno)
        filewrtxt3 = open("/home/evzen/doc/kpi/data/unameAudi.txt", "w+")
        filewrtxt3.write(audiuser)
        filewrtxt3.close()

        os.chdir(path1)
        files = sorted(os.listdir(os.getcwd()), key=os.path.getmtime)
        oldest = files[0]
        newest = files[-1]
        bakup_folder = '/home/evzen/doc/kpi/bakup/'
        vystrih_videa = oldest[11:26]
        print('Vystrih: ', vystrih_videa)
        os.system("pkill -f chrome")

        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get('http://www.google.com/xhtml')
        search_box = driver.find_element_by_name('q')
        search_box.send_keys(audijmeno)
        search_box.submit()
        sleep(0.05)
        #driver.quit()


    def vymaz_video(self):

        shutil.move(oldest, bakup_folder)

    def initUI(self):

         self.namedir3 = StringVar()
         self.namedir4 = StringVar()

         self.button1 = ttk.Button(self, text="NACTI DALSI VIDEO", command = self.nalozit_kotel)
         self.button1.place(x=300, y=10)

         self.button3 = ttk.Button(self, text="VYMAZ ZPRACOVANE VIDEO", command = self.vymaz_video)
         self.button3.place(x=300, y=80)

         self.button5 = ttk.Button(self, text="ULOZIT Username", command = self.user_name)
         self.button5.place(x=120, y=30)
         self.button6 = ttk.Button(self, text="ULOZIT Password", command = self.pass_word)
         self.button6.place(x=120, y=100)


         self.label3 = ttk.Label(self, background="#FFCC00", foreground="black", text="Username AudiTool")
         self.label3.place(x=120, y=10)
         self.label4 = ttk.Label(self, background="#CC0000", foreground="black", text="Password AudiTool")
         self.label4.place(x=120, y=80)

         unameAudi = open("/home/evzen/doc/kpi/data/unameAudi.txt", "r")

         self.textbox3 = ttk.Entry(self, width=12, textvariable=self.namedir3)
         self.textbox3.place(x=10, y=10)
         self.textbox3.insert(END, unameAudi.read())

         self.textbox4 = ttk.Entry(self, width=12, textvariable=self.namedir4, show = '*')
         self.textbox4.place(x=10, y=80)


root = Root()
root.mainloop()
