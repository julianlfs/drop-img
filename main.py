from PIL import Image
import glob 
import shutil
import os

folder = './deleted'

for img in glob.iglob('*.jpg'):
    try:
        im = Image.open(img)
        print(img + ': good')
        im.close()
    except IOError as err:
        print('error: ' + str(err))
        if not os.path.isdir(folder):
            os.mkdir(folder)
        shutil.move(img, folder)
