import os

path = r'E:\_Projects\_git\test_fixsequence'
files = []
tmp = os.listdir(path)
for t in tmp:
    if os.path.isfile(os.path.join(path,t)):
        files.append(t)

timeRender = os.path.getctime(files)
sizefile = os.path.getsize(files)
print(timeRender)
print(sizefile)
print(files)