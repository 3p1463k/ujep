#env /python
from tkinter import *
from tkinter import ttk
import os
import shutil

class Root(Tk):
    def __init__(self):
        super(Root, self).__init__()
        self.title("POSUNOVAC 4.0")
        self.geometry("600x200+100+100")
        self.configure(background='#4D4D4D')

        self.initUI()

    def slozka(self):
        self.label1.configure(text = self.namedir.get())

    def makmov(self):
        self.label3.configure(background="red", text = "Premistuji Video.....")
        path = self.namedir.get()
        pat2f = str(path)

        os.chdir(pat2f)
        files = sorted(os.listdir(os.getcwd()), key=os.path.getmtime)
        oldest = files[0]
        newest = files[-1]
        a = oldest[1:4]

        for oldest in files:
            shutil.move(oldest, "/home/evzen/doc/b")
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
                os.system('python /home/evzen/doc/script/feedCSV.py')


            else:
                print("CVS nenalezeno after waiting:", time_limit, " seconds!")


    def initUI(self):

         self.namedir = StringVar()

         self.button1 = ttk.Button(self, text="NOVE VIDEO", command = self.makmov)
         self.button1.place(x=400, y=30)

         self.button2 = ttk.Button(self, text="ULOZIT Novou Cestu", command = self.slozka)
         self.button2.place(x=10, y=80)

         self.button3 = ttk.Button(self, text="NACTI DALSI CHYBU v ADTF")
         self.button3.place(x=400, y=120)





         self.label = ttk.Label(self, background="purple", text="Cesta SLOZKA IMPORT")
         self.label.place(x=10, y=10)

         self.label1 = ttk.Label(self, background="green", text="ZADEJ Cestu SLOZKA IMPORT a ULOZ")
         self.label1.place(x=10, y=50)

         self.label3 = ttk.Label(self, background="green", text="Klik premistit video")
         self.label3.place(x=400, y=60)

         self.textbox1 = ttk.Entry(self, width=50, textvariable = self.namedir)
         self.textbox1.place(x=10, y=30)

root = Root()
root.mainloop()
