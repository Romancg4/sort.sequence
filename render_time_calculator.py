import os

path = r'L:\VantageScenes\Interior_test2\_render\2022-09-29\150'
tmp = os.listdir(path)
files = []
for t in tmp:
    if os.path.isfile(os.path.join(path,t)):
        files.append(t)
# size = os.path.getsize(files)
alltime = [] 
for s in files:
    edittime = os.path.getmtime(os.path.join(path, s))
    alltime.append(edittime)
sec = alltime[-1] - alltime[0]
minutes = 0
hours = 0

print('Render time sequence:', round(sec), 'seconds')
