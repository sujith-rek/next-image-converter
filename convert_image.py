import os
from PIL import Image

def change_images_of_directory(directory):
    for filename in os.listdir(directory):
        # if filename is directory, then call this function recursively
        if os.path.isdir(filename):
            change_images_of_directory(filename)
        else:
            # if filename is image, then change it
            if filename.endswith(".jpg") or filename.endswith(".png") or filename.endswith(".jpeg"):
                change_image(filename)

def change_image(filename):
    img = Image.open(filename)
    # change to webp
    if filename.endswith(".jpg") or filename.endswith(".png"):
        filename = filename[:-4] + ".webp"
    elif filename.endswith(".jpeg"):
        filename = filename[:-5] + ".webp"
    img.save(filename, "webp")
    # delete old image
    os.remove(filename)


