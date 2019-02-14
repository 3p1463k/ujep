#!/usr/bin/env python
from tkinter import *
from tkinter import ttk
from tkinter import messagebox as msg
from tkinter import filedialog
import os
import shutil
import psutil
import time
import subprocess
from sys import executable
from subprocess import Popen
from time import sleep
from datetime import datetime
from selenium import webdriver
import keyboard
from keyboard import press
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import glob
from pathlib import Path
from selenium.webdriver.chrome.options import Options
from multiprocessing import Process
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk


kill_file = ("/home/evzen/doc/kpi/data/kill.txt")
if os.path.exists(kill_file) == True:
    os.unlink(kill_file)
else:
    print("NO KILL FILE")
    pass

# file_to_overwrite = ('/home/evzen/Desktop/WEBOupdate.txt')
# my_file = ('/home/evzen/doc/kpi/data/WEBOupdate.txt')
#
# if os.path.exists(my_file) == True
#     shutil.copy2(my_file, file_to_overwrite)
#     print(my_file)
#     sleep(0.5)
#
#     exit()

# else:
#     pass


class Root(Tk):

    def __init__(self):
        super(Root, self).__init__()
        self.title("WEB-O-MAT 4.0")
        self.geometry("660x550+100+100")
        self.configure(background='#222222')
        img = PhotoImage(file='/home/evzen/doc/kpi/data/icons/WEBOMAT.gif')
        self.tk.call('wm', 'iconphoto', self._w, img)

        self.matplotCanvas()

        self.initUI()


    def matplotCanvas(self):
        f = Figure(figsize=(3, 2), dpi=100)
        a = f.add_subplot(111)
        a.plot([1, 2, 3, 4, 5, 6, 7, 8], [5, 6, 1, 3, 8, 3, 3, 5], color="brown")

        canvas = FigureCanvasTkAgg(f, self)
        canvas.get_tk_widget().place(x=10, y=180)
        toolbar = NavigationToolbar2Tk(canvas, self)
        canvas._tkcanvas.place(x=10, y=200)





    def find_info(self):

        if not self.namedir5.get():
            msg.showwarning("WEB-O-MAT4", "ZADEJTE CISLO VIDEA")
            return
        else:
            filehandle1 = open("/home/evzen/doc/kpi/data/ReportPremisteno.txt", "r")
            filehandle2 = open("/home/evzen/doc/kpi/data/ReportVymazano.txt", "r")

            text = self.namedir5.get()
            for i, line in enumerate(filehandle1, 1):
                if text in line:
                    self.label7.configure(text=line, background="#666666")
                    print(line)
                else:
                    #msg.showinfo("WEB-)-MAT4", "NENALEZENO")
                    pass
            for j, line in enumerate(filehandle2, 1):
                if text in line:
                    self.label8.configure(text=line, background="#666666")
                    print(line)
                else:
                     pass

    def ukoncit_program(self):
        exit()
    def otevri_file(self):
        return filedialog.askopenfilename()

    def slozka1(self):
        entry_path = self.namedir1.get()
        if not entry_path:
            msg.showwarning("WEB-O-MAT4 ERROR", "NEMATE VYPLNENY UDAJ O SLOZCE PRO PREMISTOVAC")
            return
        else:
            slozka1_cesta1 = str(entry_path)
            slozka1_zaznam = open("/home/evzen/doc/kpi/data/folderPATH.txt", "w+")
            slozka1_zaznam.write(slozka1_cesta1)
            slozka1_zaznam.close()
            self.label1.configure(text=self.namedir1.get())

    def import_cesta(self):
        self.label2.configure(text=self.namedir2.get())

    def user_name(self):
        self.label3.configure(text=self.namedir3.get())

    def premistovac_on(self):

        entry_path = self.namedir1.get()
        if not entry_path:
            msg.showwarning("WEB-O-MAT4 ERROR", "NEMATE VYPLNENY UDAJ O SLOZCE PRO PREMISTOVAC")
            return
        else:
            pass

        pidP4 = open("/home/evzen/doc/kpi/data/P4pid.txt", "r")
        pidn = pidP4.read()
        # print(pidn)
        pidf = int(pidn)
        # print(pidf)

        if psutil.pid_exists(pidf):
            msg.showinfo("PREMISTOVAC4.0", "PREMISTOVAC JE ZAPNUTY", )
            print("a process with pid %d exists" % pidf)
            self.label2.configure(text='ZAPNUTO', background="#65B87A")

        else:
            proc = subprocess.Popen(['python', '/home/evzen/doc/proj/valeujep/PREMISTOVAC4.py'], shell=False,
                                    stdin=None, stdout=subprocess.PIPE,
                                    stderr=open('/home/evzen/doc/kpi/data/P4errlogfile.log', 'a'))
            proc1 = subprocess.Popen(['python', '/home/evzen/doc/proj/script/guardian.py'], shell=False,
                                    stdin=None, stdout=subprocess.PIPE,
                                    stderr=open('/home/evzen/doc/kpi/data/guardian.log', 'a'))

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
                self.label2.configure(text='VYPNUTO', background="#CC0000")


                #pass

            cesta_1 = open("/home/evzen/doc/kpi/data/folderPATH.txt", "r")
            path1 = cesta_1.read()
            os.chdir(path1)
            x = sum(os.path.isdir(folder) for folder in os.listdir(path1))
            pocet = str(x)
            self.label6.configure(text=pocet)
            msg.showinfo("PREMISTOVAC4.0", "Startuji, pocet ve slozce k premisteni: " + pocet)



    def nacist_video(self):

        bakup_folder = '/home/evzen/doc/kpi/bakup/'
        path1 = '/home/evzen/doc/kpi/kpi'
        os.chdir(path1)
        try:
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
            if not feedhslo:
                msg.showerror("HOUSTON WE GOT PROBLEM", "ZADEJTE HESLO DO AUDI TOOL A ZNOVU ZMACKNETE NACIST VIDEO")
                return
            audijmeno = self.namedir3.get()
            audiuser = str(audijmeno)
            print('Vystrih: ', vystrih_videa)
            driver = webdriver.Chrome()
            #driver.service.process
            driver.maximize_window()
            driver.get('http://www.google.com/xhtml')
            #driver_pid = psutil.Process(driver.service.process.pid)
            #print(driver_pid.children(recursive=True))
            search_box = driver.find_element_by_name('q')
            search_box.send_keys(feedhslo)
            search_box.submit()
            sleep(0.05)
            driver.quit()
            if os.path.isdir(os.path.join(bakup_folder, oldest)):
                msg.showerror("WEBOMAT4.0", "CHYBA, SOUBOR UZ EXISTUJE")
                return
            else:
                shutil.move(os.path.join(path1, oldest), os.path.join(bakup_folder, oldest))

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

            # total = 0
            # with open("/home/evzen/doc/kpi/data/dayreport.txt", "r") as my_file:
            #     file_lines = my_file.readlines()
            #     first_line = file_lines[0].strip()
            #     z = len(first_line)
            #     print(z)
            #     self.z = StringVar
            #     print(z)
            #     self.label6.configure(textvariable=self.z)

                cesta_1 = open("/home/evzen/doc/kpi/data/folderPATH.txt", "r")
                path1 = cesta_1.read()
                os.chdir(path1)
                x = sum(os.path.isdir(folder) for folder in os.listdir(path1))
                pocet = str(x)
                self.label6.configure(text=pocet)




        except IndexError:
            files = None
            msg.showwarning("WEB-O-MAT", "VE SLOZCE UZ NEJSOU VIDEA")


    def uklizec_plochy(self):

        try:
            self.label2.configure(text='VYPNUTO', background="#CC0000")
            timestamp = str(datetime.now())
            datum = timestamp[0:19]
            pid_of_process_to_kill = open("/home/evzen/doc/kpi/data/kill.txt", "w")
            pid_of_process_to_kill.close()
            path1 = ("/home/evzen/doc/kpi/kpi")
            path2 = open("/home/evzen/doc/kpi/data/folderPATH.txt")
            cesta_2 = path2.read()
            path2move_files = str(cesta_2)
            print(path2move_files)
            os.chdir(path1)
            pocet_kpi = sum(os.path.isdir(folder) for folder in os.listdir(path1))
            print("Přesunu " + str(pocet_kpi) + ' ' + datum)
            pocet_videi = str(pocet_kpi)
            sleep(1)
            msg.showinfo("Zastavuji PŘEMÍSŤOVAČ4.0", "Uklidím plochu a přemístím zpet: " + pocet_videi)
            sleep(1)

            if pocet_kpi > 0:
                x = os.path.isdir(path1)
                if x:
                    y = os.listdir(path1)
                    for x in y:
                        if os.path.isdir(os.path.join(path2move_files, x)):
                            msg.showerror("WEBOMAT4.0", "CHYBA, SOUBOR PRO PREMISTENI UZ EXISTUJE")
                            return
                        else:
                            shutil.move(os.path.join(path1, x), os.path.join(path2move_files, x))
            else:
                msg.showinfo("Zastavuji PŘEMÍSŤOVAČ4.0", "MAM UKLIZENO")
                exit()
            exit()
        except (IndexError):
            files = None
            msg.showinfo("UKLIZEC4", "VE SLOZCE UZ NEJSOU VIDEA, UKONCUJI PREMISTOVAC, EXITING")
            exit()




    def initUI(self):




         self.namedir1 = StringVar()
         self.namedir3 = StringVar()
         self.namedir4 = StringVar()
         self.namedir5 = StringVar()

         self.button1 = ttk.Button(self, text="NACTI DALSI VIDEO", command=self.nacist_video)
         self.button1.place(x=350, y=10)
         self.button2 = ttk.Button(self, text="ZAPNI PREMISTOVACE", command=self.premistovac_on)
         self.button2.place(x=350, y=90)

         self.button3 = ttk.Button(self, text="ULOZIT Novou Cestu", command=self.slozka1)
         self.button3.place(x=10, y=45)
         self.button4 = ttk.Button(self, text="JDU DOMU, UKLIĎ PLOCHU ", command=self.uklizec_plochy)
         self.button4.place(x=350, y=150)

         self.button5 = ttk.Button(self, text="ULOZIT Username", command=self.user_name)
         self.button5.place(x=120, y=110)
         self.button7 = ttk.Button(self, text="FILE EXPLORER", command=self.otevri_file)
         self.button7.place(x=350, y=190)

         self.button8 = ttk.Button(self, text="VIDEO INFO", command=self.find_info)
         self.button8.place(x=300, y=480)
         self.button9 = ttk.Button(self, text="UKONCIT", command=self.ukoncit_program)
         self.button9.place(x=490, y=480)

         self.label1 = ttk.Label(self, background="#65B87A", foreground="black", text="SLOZKA NA UCKU")
         self.label1.place(x=10, y=25)
         self.label2 = ttk.Label(self, background="#CC0000", foreground="black", text="VYPNUTO")
         self.label2.place(x=350, y=116)

         self.label3 = ttk.Label(self, background="#FFCC00", foreground="black", text="Username AudiTool")
         self.label3.place(x=120, y=90)
         self.label4 = ttk.Label(self, background="#CC0000", foreground="black", text="Napis heslo do AudiTool")
         self.label4.place(x=120, y=160)

         self.label5 = ttk.Label(self, background="#336699", foreground="black", text="VYSTRIH  CISLA VIDEA")
         self.label5.place(x=350, y=40)
         self.label6 = ttk.Label(self, background="#666666", foreground="black", text="0")
         self.label6.place(x=350, y=60)

         self.label7 = ttk.Label(self, background="#222222", foreground="black")
         self.label7.place(x=10, y=420)
         self.label8 = ttk.Label(self, background="#222222", foreground="black")
         self.label8.place(x=10, y=440)


         unameAudi = open("/home/evzen/doc/kpi/data/unameAudi.txt", "r")
         fpatr = open("/home/evzen/doc/kpi/data/folderPATH.txt", "r")
         pidP4 = open("/home/evzen/doc/kpi/data/P4pid.txt", "r")
         pidn = pidP4.read()
         print(pidn)
         pidf = int(pidn)
         # print(pidf)
         if psutil.pid_exists(pidf):
             print("a process with pid %d exists" % pidf)
             self.label2.configure(text='ZAPNUTO', background="#65B87A")
         else:
             pass

         self.textbox1 = ttk.Entry(self, width=30, textvariable=self.namedir1)
         self.textbox1.insert(END, fpatr.read())
         self.textbox1.place(x=10, y=5)

         self.textbox3 = ttk.Entry(self, width=12, textvariable=self.namedir3)
         self.textbox3.place(x=10, y=90)
         self.textbox3.insert(END, unameAudi.read())

         self.textbox4 = ttk.Entry(self, width=12, textvariable=self.namedir4, show='*')
         self.textbox4.place(x=10, y=160)
         self.textbox5 = ttk.Entry(self, width=40, textvariable=self.namedir5)
         self.textbox5.place(x=10, y=480)



root = Root()
root.mainloop()
