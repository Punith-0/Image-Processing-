import numpy as np
from utils.ansi import RED , GREEN , BOLD , RESET

class ClassifierModel :
    def __init__(self ):
        self.thresholds = {
            'water' : 0.0,
            'soil' : 0.2,
            'grass' : 0.5
        }

    def tune_thresholds(self , ndvi):
        if len(ndvi.shape) != 2 :
            raise ValueError(f"{RED}NDVI input must be a single channel image{RESET}")
        mean = float(np.mean(ndvi))
        std = float(np.std(ndvi))
        water = mean -std
        soil = mean
        grass = mean + std
        water = max(-1.0  , water)
        grass = min(1.0 , grass)
        self.thresholds['water'] = water
        self.thresholds['soil'] = soil
        self.thresholds['grass'] = grass
    
    def threshold(self  , water = 0.0 , soil = 0.2 , grass = 0.5) :
        self.thresholds['water'] = water
        self.thresholds['soil'] = soil
        self.threshhlds['grass'] = grass

    def classify(self , ndvi ):
        if len(ndvi.shape) != 2:
            raise ValueError(f"{RED}NDVI must be an 2D array {RESET}")
        h , w = ndvi.shape
        output = np.zeros((h , w , 3) , dtype=np.uint8) #bug fix (h , w) -> (h , w , 3) for color output
        t = self.thresholds
        output[ndvi < t["water"]] = [255 , 0 ,  0]
        output[(ndvi >= t["water"]) & (ndvi < t["soil"])] = [42 , 42 , 165]
        output[(ndvi >= t['soil']) & (ndvi < t['grass'])] = [144 , 238 , 144]
        output[ndvi >= t['grass']] = [0 , 100 ,  0]
        return output
    
    def show_thresholds(self) :
        return self.thresholds
    
if __name__ == "__main__" :
    model = ClassifierModel()
    print(f"{GREEN}Default Thresholds:{BOLD}\n{model.show_thresholds()}{RESET}")
    