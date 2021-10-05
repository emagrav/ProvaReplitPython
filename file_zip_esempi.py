print("************FILE ZIP ESEMPI ****************")

#import os
import zipfile

'''
archivio = zipfile.ZipFile("Files/archivio_prova.zip","w") #apro il file zip in scrittura

# in caso di windows esempio: "C://Users/chicco/Desktop/archivio_prova.zip"

archivio.write("Files/pippo.txt", compress_type=zipfile.ZIP_DEFLATED) #scrivo il file nell'archivio zip

archivio.close() #chiudo lo zip

archivio = zipfile.ZipFile("Files/archivio_prova.zip","a") #apro ora il file zip in append

archivio.write("Files/trapano.wav", compress_type=zipfile.ZIP_DEFLATED) #ci inserisco dentro un nuovo file

archivio.close() #chiudo lo zip
'''

archivio = zipfile.ZipFile("Files/archivio_prova.zip")

print(archivio.namelist()) #namelist fornisce la lista dei file contenuti nello zip

'''
archivio.extractall("Files/ZipEstratto") #estraggo il file zip
'''

archivio.close()