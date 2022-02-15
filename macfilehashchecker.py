import os
import hashlib
import filecmp

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
            except:
                continue



file1 = open('/Volumes/'+ mydrive +'/acquired_hash.txt', 'r')
file2 = open('/Volumes/'+ mydrive +'/names_and_hashes.txt', 'r')
file3 = open('/Volumes/'+ mydrive +'/foundmatches.txt', 'a')



print('SEARCH COMPLETE')
