import os
from cv2 import imread as read_image
from cv2 import imwrite as save_image
from .ansi import RED, RESET , GREEN , BOLD

class ImageLoader :

    def __init__(self, input_folder = "input_folder"):
        self.input_folder = input_folder
        self.images = []

    def load_images_from_folder(self):
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

                """self.images.append((filename, img)) \
                    if img is not None \
                    else print(f"{RED}Failed to load image: {file_path}{RESET}")"""
                if img is None :
                    print(f"{RED}Failed to load image: {file_path}{RESET}")
                    continue
                self.images.append((filename , img))


        return self.images

class ImageSaver :
    def __init__(self , output_folder = "output_folder"):
        self.output_folder = output_folder
    
    def save_images_into_folder(self, images  , prefix = ""):
        os.makedirs(self.output_folder , exist_ok = True)

        for filename , image in images :
            name , extension = os.path.splitext(filename)
            if extension == "" :
                extension = ".jpg"
            save_path = os.path.join(self.output_folder , f"{prefix}{name}{extension}")

            save_done = save_image(save_path , image)

            print(f"{GREEN}Saved {save_path}{RESET}" \
            if save_done else \
            f"{RED}Cannot save {save_path}{RESET}")

if __name__ == "__main__" :
    print(f"{BOLD}{GREEN}The objects are working fine{RESET}")