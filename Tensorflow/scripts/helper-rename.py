import os

folder_path = 'C:/Users/Barbara/Desktop/fer/6.sem/zavrsni/Tensorflow/data/train/' # desired folder path
prefix = 'znak'
counter = 1

for filename in os.listdir(folder_path):
    if filename.endswith('.jpg') or filename.endswith('.JPG') or filename.endswith('.JPEG'): # change file extensions to your desired image formats
        new_filename = prefix + str(counter).zfill(3) + os.path.splitext(filename)[1]
        os.rename(folder_path + filename, folder_path + new_filename)
        counter += 1
