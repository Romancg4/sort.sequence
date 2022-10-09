import os
import shutil
path = r'E:\_Projects\_git\test_fixsequence'
correctname = 'shot_01'
padding = 4
# list of files
tmp = os.listdir(path)
files = []
for t in tmp:
    if os.path.isfile(os.path.join(path,t)):
        files.append(t)
# print(files)
# separate
frames = []
for i in files:
    name, ext = os.path.splitext(i)
    fullName = name
    while name[-1].isdigit():
        name = name[:-1]
    digits = int(fullName.replace(name,''))
    frames.append(digits)
offset = min(frames) - 1

#new name files
outfolder = os.path.join(path,correctname)
if not os.path.exists(outfolder):
    os.mkdir(outfolder)
for i,f in enumerate(files):
    old = os.path.join(path,f)
    name,ext = os.path.splitext(f)
    newname = correctname + '_' + str(frames[i] - offset).zfill(padding) + ext
    new = os.path.join(path, correctname, newname)
    if os.path.exists(new):
        os.remove(new)
    shutil.copy2(old, new)

# search missing files
fullrange = range(min(frames), max(frames) + 1)
missingFiles = []
for i in fullrange:
    if not i in frames:
        missingFiles.append(i)
print('Missing frames:', *missingFiles)

# search empty and black files

# Remove old frames
answed = input('Remove old files? y/n:')
# if answed == 'y' or answed == 'Y':
#     for f in files:
#         os.remove(os.path.join(path,f))
# print('Old files removed!')

# message
print('Ok, frames copy to', outfolder)
if answed == 'n' or answed == 'N':
    print('Old frames saved in', path)