import os
from PIL import Image
import numpy as np

#def resize_image(image_path):
#    with Image.open(image_path) as img:
#        img = img.resize((70, 70))
#        img.save(image_path)
#
#def squish_images(directory):
#    for foldername, subfolders, filenames in os.walk(directory):
#        for filename in filenames:
#            if filename.endswith('.jpg'):
#                resize_image(os.path.join(foldername, filename))

# Replace 'your_directory' with the path to the directory you want to start in
#squish_images('C:\\Users\\chris\\Downloads\\clothing-dataset-small-master\\test\\train')

def images_to_ndarray(directory):
    label_dict = {}
    images = []
    labels = []
    label_counter = 0

    for foldername, subfolders, filenames in os.walk(directory):
        for filename in filenames:
            if filename.endswith('.jpg'):
                with Image.open(os.path.join(foldername, filename)) as img:
                    img = img.resize((70, 70))
                    img_array = np.array(img)
                    if img_array.shape == (70, 70, 3):  # Ensure the image is in the correct format
                        img_array = np.transpose(img_array, (2, 0, 1))  # Change format to (3, 70, 70)
                        images.append(img_array)
                        if foldername not in label_dict:
                            label_dict[foldername] = label_counter
                            label_counter += 1
                        labels.append(label_dict[foldername])

    return np.array(images), np.array(labels)

images, labels = images_to_ndarray('C:\\Users\\chris\\Downloads\\clothing-dataset-small-master\\test\\train')
print("Done!")

print(images[0])