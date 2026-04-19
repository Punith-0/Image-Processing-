from utils.ansi import RED , GREEN , BOLD , RESET
import cv2
import numpy as np

class VegetationIndices :

    @staticmethod
    def nir(image) :
        return len(image.shape) == 3 and image.shape[2] >= 4

    @staticmethod
    def compute_ndvi(image) :
        
        image = image.astype(float)

        if len(image.shape) != 3 :
            raise ValueError(f"{RED}Input image must be a color image (3 channels){RESET}")
        if VegetationIndices.nir(image) :
            print(f"{GREEN}NIR channel detected. Using the 4th channel for NIR NDVI.{RESET}")
            b , g , r , nir = cv2.split(image)
            up = nir - r
            down = nir + r + 1e-5
        else :
            print(f"{RED}Using RGB for NDVI approximation{RESET}")
            b , g , r = cv2.split(image)
            up = g -r
            down = g +r +1e-5
        return (up/down)
    
    @staticmethod
    def compute_gndvi(image):
        
        image = image.astype(float)

        if len(image.shape) != 3 :
            raise ValueError(f"{RED}Input image must be a color image (3 channels){RESET}")
        if VegetationIndices.nir(image) :
            print(f"{GREEN}NIR channel detected. Using the 4th channel for NIR GNDVI.{RESET}")
            b , g , r , nir = cv2.split(image)
            up = nir - g
            down = nir + g + 1e-5
        else :
            print(f"{RED}Using RGB for GNDVI approximation{RESET}")
            b , g , r = cv2.split(image)
            up = g - r
            down = g + r +1e-5
        return (up/down)
    
    @staticmethod
    def normalize_index(index) :
        normalize = cv2.normalize(index , None , 0 , 255 , cv2.NORM_MINMAX)
        return normalize.astype(np.uint8)
    
    @staticmethod
    def enhance_index(index):
        normalized = VegetationIndices.normalize_index(index)
        enhanced = cv2.equalizeHist(normalized)
        return enhanced


    @staticmethod
    def get_statistics(index):
        return {"min": float(np.min(index))  ,
            "max": float(np.max(index )),
            "mean": float(np.mean(index) ) ,
            "std": float(np.std(index))}