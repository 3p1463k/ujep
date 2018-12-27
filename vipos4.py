#env /python
from tkinter import *
from tkinter import ttk
import os
import shutil

class Root(Tk):
    def __init__(self):
        super(Root, self).__init__()
        self.title("POSUNOVAC 4.0")
        self.geometry("480x550+100+100")
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

        for oldest in files:
            shutil.move(oldest, "/home/evzen/doc/b")
            break



    def initUI(self):

         self.namedir = StringVar()

         self.button1 = ttk.Button(self, text="APC1", command=self.makmov)
         self.button1.place(x=250, y=60)

         self.button2 = ttk.Button(self, text="APC2", command=self.makmov)
         self.button2.place(x=250, y=90)

         self.button3 = ttk.Button(self, text="APC3", command=self.makmov)
         self.button3.place(x=250, y=120)

         self.button4 = ttk.Button(self, text="APC4", command=self.makmov)
         self.button4.place(x=250, y=150)

         self.button5 = ttk.Button(self, text="APC5", command=self.makmov)
         self.button5.place(x=250, y=180)

         self.button6 = ttk.Button(self, text="APC6", command=self.makmov)
         self.button6.place(x=250, y=210)

         self.button7 = ttk.Button(self, text="APC7", command=self.makmov)
         self.button7.place(x=250, y=240)

         self.button8 = ttk.Button(self, text="APC8", command=self.makmov)
         self.button8.place(x=250, y=270)

         self.button9 = ttk.Button(self, text="APC9", command=self.makmov)
         self.button9.place(x=250, y=300)

         self.button10 = ttk.Button(self, text="APC10", command=self.makmov)
         self.button10.place(x=250, y=330)

         self.button11 = ttk.Button(self, text="APC11", command=self.makmov)
         self.button11.place(x=250, y=360)

         self.button12 = ttk.Button(self, text="APC12", command=self.makmov)
         self.button12.place(x=250, y=390)

         self.button13 = ttk.Button(self, text="APC13", command=self.makmov)
         self.button13.place(x=250, y=420)

         self.button14 = ttk.Button(self, text="APC14", command=self.makmov)
         self.button14.place(x=250, y=450)

         self.button15 = ttk.Button(self, text="APC15", command=self.makmov)
         self.button15.place(x=250, y=480)


         self.button16 = ttk.Button(self, text="APC16", command = self.makmov)
         self.button16.place(x=350, y=60)

         self.button17 = ttk.Button(self, text="APC17", command=self.makmov)
         self.button17.place(x=350, y=90)

         self.button18 = ttk.Button(self, text="APC18", command=self.makmov)
         self.button18.place(x=350, y=120)

         self.button19 = ttk.Button(self, text="APC19", command=self.makmov)
         self.button19.place(x=350, y=150)

         self.button20 = ttk.Button(self, text="APC20", command=self.makmov)
         self.button20.place(x=350, y=180)

         self.button21 = ttk.Button(self, text="APC21", command=self.makmov)
         self.button21.place(x=350, y=210)

         self.button22 = ttk.Button(self, text="APC22", command=self.makmov)
         self.button22.place(x=350, y=240)

         self.button23 = ttk.Button(self, text="APC23", command=self.makmov)
         self.button23.place(x=350, y=270)

         self.button24 = ttk.Button(self, text="APC24", command=self.makmov)
         self.button24.place(x=350, y=300)

         self.button25 = ttk.Button(self, text="APC25", command=self.makmov)
         self.button25.place(x=350, y=330)

         self.button26 = ttk.Button(self, text="APC26", command=self.makmov)
         self.button26.place(x=350, y=360)

         self.button27 = ttk.Button(self, text="APC27", command=self.makmov)
         self.button27.place(x=350, y=390)

         self.button28 = ttk.Button(self, text="APC28", command=self.makmov)
         self.button28.place(x=350, y=420)

         self.button29 = ttk.Button(self, text="APC29", command=self.makmov)
         self.button29.place(x=350, y=450)

         self.button30 = ttk.Button(self, text="APC30", command=self.makmov)
         self.button30.place(x=350, y=480)




         self.button32 = ttk.Button(self, text="ULOZIT Novou Cestu", command = self.slozka)
         self.button32.place(x=10, y=80)

         self.label = ttk.Label(self, background="purple", text="Cesta SLOZKA DISTRIBUTION IMPORT")
         self.label.place(x=10, y=10)

         self.label1 = ttk.Label(self, background="green", text="ZADEJ CESTU DISTRIBUTION a ULOZ")
         self.label1.place(x=10, y=55)

         # self.label3 = ttk.Label(self, background="green", text="Klik premistit video")
         # self.label3.place(x=400, y=60)

         self.textbox1 = ttk.Entry(self, width=55, textvariable = self.namedir)
         self.textbox1.place(x=10, y=30)

         self.radbtn1 = ttk.Radiobutton(self, text = 'POSILAT 1 VIDEO', value=1)
         self.radbtn1.place(x=10, y=120)

         self.radbtn2 = ttk.Radiobutton(self, text='POSILAT 5 VIDEI ', value=2)
         self.radbtn2.place(x=10, y=160)

root = Root()
root.mainloop()