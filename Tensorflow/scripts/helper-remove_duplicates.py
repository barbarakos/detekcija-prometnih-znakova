import os
from PIL import Image
import hashlib

folder_path = 'C:/Users/Barbara/Desktop/fer/6.sem/zavrsni/Tensorflow/data/train/' # desired folder path
hashes = {} # dictionary to store image hashes and their filenames

for filename in os.listdir(folder_path):
    if filename.endswith('.jpg') or filename.endswith('.JPG') or filename.endswith('.JPEG'): # desired image formats
        with open(os.path.join(folder_path, filename), 'rb') as f:
            img_hash = hashlib.md5(f.read()).hexdigest()
            if img_hash in hashes:
                f.close()
                os.remove(os.path.join(folder_path, filename))
                print(f'Removing duplicate file: {filename}')
            else:
                hashes[img_hash] = filename
                print(f'Keeping file: {filename}')
                f.close()
