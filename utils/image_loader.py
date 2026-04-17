import os
from cv2 import imread as read_image
from utils.ansi import RED, RESET

class ImageLoader :

    def __init__(self, input_folder = "input_folder"):
        self.input_folder = input_folder
        self.images = []

    def load_images_folder(self):
        self.images.clear()

        if not os.path.exists(self.input_folder):
            raise FileNotFoundError(f"{RED}Input folder '{self.input_folder}' does not exist.{RESET}")
         
        for filename in os.listdir(self.input_folder):
            file_path = os.path.join(self.input_folder, filename)

            if not os.path.isfile(file_path):
                print(f"{RED}Skipping the sub_directory: {file_path}{RESET}")
                continue

            if filename.lower().endswith((".jpg", ".png", ".jpeg")):
                img = read_image(file_path)

                self.images.append((filename, img)) \
                    if img is not None \
                    else print(f"{RED}Failed to load image: {file_path}{RESET}")


        return self.images