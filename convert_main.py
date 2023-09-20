from change_names import change_data_of_dir, change_data_of_file
from convert_image import change_image, change_images_of_directory
import os
from PIL import Image
import re

def convert_main():
    current_dir = os.getcwd()
    # convert images
    change_images_of_directory(current_dir)
    # change data
    change_data_of_dir(current_dir)

if __name__ == "__main__":
    convert_main()