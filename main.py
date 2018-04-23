from PIL import Image
import glob 
import shutil
import os


for img in glob.iglob('*.jpg'):
    try:
        im = Image.open(img)
        print(img + ': good')
    except(OSError):
        print(img + ': error')
        if not os.path.isdir('./deleted'):
            os.mkdir('./deleted')
        shutil.move(img, './deleted')




