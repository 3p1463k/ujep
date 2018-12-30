#env /python 
from tkinter import *
from tkinter import ttk
import os
import shutil

class Root(Tk):
    def __init__(self):
        super(Root, self).__init__()
        self.title("POSUNOVAC 4.0")
        self.geometry("600x350+100+100")
        self.configure(background='#222222')

        self.initUI()

    def slozka1(self):
        self.label1.configure(text = self.namedir1.get())

    def slozka2(self):
        self.label2.configure(text = self.namedir2.get())


    def slozka3(self):
        self.label3.configure(text = self.namedir3.get())

    def slozka4(self):

        pass
        #self.label4.configure(text = self.namedir4.get())

    def makmov(self):

        path1 = self.namedir1.get()
        path2 = self.namedir2.get()
        pat2fol1 = str(path1)
        pat2fol2 = str(path2)
        heslO = self.namedir4.get()
        feedhslo = str(heslO)
        audijmeno = self.namedir3.get()
        audiuser = str(audijmeno)

        def webomat():

            from selenium import webdriver
            from time import sleep

            driver = webdriver.Chrome()
            driver.maximize_window()
            driver.get('http://www.google.com/xhtml')
            sleep(2)
            search_box = driver.find_element_by_name('q')
            search_box.send_keys(feedhslo)
            search_box.submit()
            sleep(2)
            driver.quit()
            # jmeno = driver.find_element_by_name('                ')
            # jmeno.send_keys(audiuser)
            # heslo = driver.element_by_id('          ')
            # heslo.send_keys('feedhslo')
            # cudlik1 = driver.find_element_by_name('          ').click()
            # cudlik2 = driver.find_element_by_name('          ').click()
            #sleep(2)
            #cislovidea = driver.find_element_by_id('        ')
            #cislovidea.send_keys(vystrih_videa)
            #cudlik3 = driver.find_element_by_id('         ')
            #cudlik3.click()
            #sleep(2)
            #cudlik4 = driver.find_element_by_id('        ')
            #cudlik4.click()

        fpatw = open("/home/evzen/doc/kpi/folderPATH.txt", "w+")
        fpatw.write(pat2fol1)
        fpatw.close()
        filewritetxt2 = open("/home/evzen/doc/kpi/dataimport2.txt", "w+")
        filewritetxt2.write(pat2fol2)
        filewritetxt2.close()

        os.chdir(path1)
        files = sorted(os.listdir(os.getcwd()), key=os.path.getmtime)
        oldest = files[0]
        newest = files[-1]
        vystrih_videa = oldest[11:26]

        for oldest in files:
            shutil.move(oldest, pat2fol2)
            break

        def watch_file(filename, time_limit=10, check_interval=2):

            import time

            now = time.time()
            last_time = now + time_limit

            while time.time() <= last_time:

                if os.path.exists(filename):
                    return True
                    break
                else:
                    # Wait for check interval seconds, then check again.
                    time.sleep(check_interval)

            return False

        if __name__ == '__main__':
            filename = '/home/evzen/doc/kpi/adt.csv'
            time_limit = 15  # one hour from now.
            check_interval = 5  # seconds between checking for the file.

            if watch_file(filename, time_limit, check_interval):
                print("CVS File present!")
                os.system('python /home/evzen/doc/proj/script/adtfcsv.py')
                webomat()


            else:
                print("CVS nenalezeno after waiting:", time_limit, " seconds!")


    def initUI(self):

         self.namedir1 = StringVar()
         self.namedir2 = StringVar()
         self.namedir3 = StringVar()
         self.namedir4 = StringVar()

         self.button1 = ttk.Button(self, text="PRESUN NOVE VIDEO", command = self.makmov)
         self.button1.place(x=450, y=10)
         self.button2 = ttk.Button(self, text="ULOZIT Novou Cestu", command = self.slozka1)
         self.button2.place(x=10, y=50)
         self.button3 = ttk.Button(self, text="POSUN NA DALSI CHYBU v ADTF")
         self.button3.place(x=350, y=140)
         self.button4 = ttk.Button(self, text="ULOZIT Novou Cestu", command = self.slozka2)
         self.button4.place(x=10, y=145)
         self.button5 = ttk.Button(self, text="ULOZIT Username", command = self.slozka3)
         self.button5.place(x=120, y=240)
         self.button6 = ttk.Button(self, text="ULOZIT Password", command = self.slozka4)
         self.button6.place(x=120, y=310)

         self.label1 = ttk.Label(self, background="#E5CB21", foreground="black", text="ZADEJ Cestu SLOZKA EXPORT a ULOZ")
         self.label1.place(x=10, y=30)
         self.label2 = ttk.Label(self, background="#E5CB21", foreground="black", text="ZADEJ Cestu SLOZKA IMPORT a ULOZ")
         self.label2.place(x=10, y=125)
         self.label3 = ttk.Label(self, background="#E5CB21", foreground="black", text="Username AudiTool")
         self.label3.place(x=120, y=220)
         self.label4 = ttk.Label(self, background="#E5CB21", foreground="black", text="Password AudiTool")
         self.label4.place(x=120, y=290)

         fpatr = open("/home/evzen/doc/kpi/folderPATH.txt", "r")
         unameAudi = open("/home/evzen/doc/kpi/unameAudi.txt", "r")
         cesta2 = open("/home/evzen/doc/kpi/dataimport2.txt", "r")


         self.textbox1 = ttk.Entry(self, width=30, textvariable = self.namedir1)
         self.textbox1.insert(END, fpatr.read())
         self.textbox1.place(x=10, y=5)

         self.textbox2 = ttk.Entry(self, width=30, textvariable=self.namedir2)
         self.textbox2.place(x=10, y=100)
         self.textbox2.insert(END, cesta2.read())

         self.textbox3 = ttk.Entry(self, width=12, textvariable=self.namedir3)
         self.textbox3.place(x=10, y=220)
         self.textbox3.insert(END, unameAudi.read())

         self.textbox4 = ttk.Entry(self, width=12, textvariable=self.namedir4, show = '*')
         self.textbox4.place(x=10, y=290)





root = Root()
root.mainloop()
