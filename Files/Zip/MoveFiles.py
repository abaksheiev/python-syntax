from zipfile import *

zipFileName = 'images.zip'

# Create Zip file with 2 files from files
f =ZipFile(zipFileName,'w', ZIP_DEFLATED)

f.write('files/js.png')
f.write('files/letter.png')

f.close()

# UnZip into destination folder

f = ZipFile(zipFileName,'r')
f.extractall('Destination/{zipFileName}')
f.close()