import os
import hashlib
import filecmp
import time

rootmac = '/'
print(os.listdir('/Volumes'))
mydrive = input('Please type the exact name of your USB drive as listed above in quotes: ')

for rootmac,dirs,files in os.walk(rootmac):
    for file in files:
        file_name = os.path.join(rootmac,file)
        file_ext = os.path.splitext(file_name)[1]
        if file_ext == '.avi' or \
            file_ext == '.mp4' or \
            file_ext == '.mov' or \
            file_ext == '.jpg' or \
            file_ext == '.png':
            print(file)
            hashermd5 = hashlib.md5()
            try:
                with open(file_name, 'rb') as inFile:
                    buffmd5 = inFile.read()
                    hashermd5.update(buffmd5)
                    with open('/Volumes/'+ mydrive +'/acquired_hash.txt', 'a') as myFile:
                        myFile.write(file + '\n' + hashermd5.hexdigest() + '\n')
                    print(hashermd5.hexdigest())
            except:
                continue
myFile.close()

print('\n' + '\n' + '\n' + 'RESULTS')

file1 = open('/Volumes/'+ mydrive +'/acquired_hash.txt')
file2 = open('/Volumes/'+ mydrive +'/names_and_hashes.txt')
file3 = open('/Volumes/'+ mydrive +'/found.txt', 'a')

mytargets = [lines.strip() for lines in file2]
myacquired = [lines.strip() for lines in file1]
for line in myacquired:
    if line in mytargets:
        found = line
        file3.write(found + '\n')
        print(found + '\n')


print('\n' + '\n' + '\n' + 'SEARCH COMPLETE! CHECK FOUND.TXT FOR RESULTS!')
