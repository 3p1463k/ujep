import os
import shutil
import pyperclip

def makmov():
    path = 'U:\\FOR_VALIDATION\\VPC2\\KPI\\LEVEL_1\\Ptáček Evžen'

    os.chdir(path)
    files = sorted(os.listdir(os.getcwd()), key=os.path.getmtime)
    oldest = files[0]
    newest = files[-1]
    pyperclip.copy(oldest[11:26])

    for oldest in files:
        shutil.move(oldest, "C:\\Users\\anotator\\Desktop\\KPI")
        break
makmov()
