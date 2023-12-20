import os
import re
from PIL import Image


def change_images_of_directory(directory):
    for filename in os.listdir(directory):
        # if filename is directory, then call this function recursively
        if os.path.isdir(filename):
            change_images_of_directory(os.path.join(directory, filename))
        else:
            # if filename is image, then change it
            if filename.endswith(".jpg") or filename.endswith(".png") or filename.endswith(".jpeg"):
                change_image(os.path.join(directory, filename))

    delete_files_of_directory(directory)


def delete_files_of_directory(directory):
    for filename in os.listdir(directory):
        # if filename is directory, then call this function recursively
        if os.path.isdir(filename):
            delete_files_of_directory(os.path.join(directory, filename))
        else:
            # if filename is image, then delete it
            if filename.endswith(".jpg") or filename.endswith(".png") or filename.endswith(".jpeg"):
                os.remove(filename)


def change_image(filename):
    img = Image.open(filename)
    # change to webp
    if filename.endswith(".jpg") or filename.endswith(".png"):
        filename = filename[:-4] + ".webp"
    elif filename.endswith(".jpeg"):
        filename = filename[:-5] + ".webp"
    img.save(filename, "webp")


def change_data_of_file(file_path):
    # read file
    file = open(file_path, 'r')
    data = file.read()
    file.close()

    # change data
    data = re.sub(r'\.png', '.webp', data)
    data = re.sub(r'\.jpeg', '.webp', data)
    data = re.sub(r'\.jpg', '.webp', data)

    # write file
    file = open(file_path, 'w')
    file.write(data)
    file.close()


def change_data_of_dir(dir_path):
    # crawl through all files and folders of dir_path
    for root, dirs, files in os.walk(dir_path):
        for file in files:
            if os.path.isdir(file):
                change_data_of_dir(os.path.join(root, file))
            else:
                change_data_of_file(os.path.join(root, file))


def convert_main():
    current_dir = os.getcwd()
    # convert images
    change_images_of_directory(current_dir)
    # change data
    change_data_of_dir(current_dir)


if __name__ == "__main__":
    convert_main()
