# how to use zipfile to compress files in Python

import zipfile
mi_zip = zipfile.ZipFile('Carpeta_9/archivo_comprimido.zip','w')
mi_zip.write('Carpeta_9/mi_texto_A.txt')
mi_zip.write('Carpeta_9/mi_texto_B.txt')
mi_zip.close()

#%%
# How to use zipfile to decompress files in Python 
import zipfile
mi_zip = zipfile.ZipFile('Carpeta_9/archivo_comprimido.zip','r')
mi_zip.extractall('archivo_comprimido.zip/Carpeta_9')
mi_zip.close()
# %%

