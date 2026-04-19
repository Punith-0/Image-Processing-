from utils.ansi import RED , GREEN , BOLD , YELLOW , HIGHLIGHT , RESET  , BLUE , CYAN
from utils.file_operations import ImageLoader  , ImageSaver
from classify_region import ClassifierModel
from vegetaive_indices import VegetationIndices
import os 

def main() :
    print(f"{BOLD}{BLUE}----VEGETATION ANALYZER----{RESET}")
    input_path = "input_folder"
    output_path = "output_folder"
    os.makedirs(input_path, exist_ok=True)
    os.makedirs(output_path, exist_ok=True)
    loader = ImageLoader(input_path)
    images = loader.load_images_from_folder()
    
    if not images :
        print(f"{YELLOW}No images found in '{input_path}'. Please add some images and try again.{RESET}")
        return
    model = ClassifierModel()
    saver = ImageSaver(output_path)
    ndvi_outputs = []
    region_outputs = []

    for filename , image in images :
        print(f"{CYAN}Processing {filename}...{RESET}")
        try :
            ndvi = VegetationIndices.compute_ndvi(image)
            ndvi[ndvi <= -0.2] = -1
            ndvi_img = VegetationIndices.normalize_index(ndvi)
            model.tune_thresholds(ndvi)
            region = model.classify(ndvi)
            ndvi_outputs.append((filename , ndvi_img))
            region_outputs.append((filename , region))
        except Exception as e :
            print(f"{RED}Error processing {filename}: {e}{RESET}")
            continue
    
    print(f"{GREEN}Processing Finished{RESET}")
    saver.save_images_into_folder(ndvi_outputs , prefix = "ndvi_")
    saver.save_images_into_folder(region_outputs , prefix = "region_")
    
    print(f"{BOLD}{GREEN}Processing complete. Check the '{output_path}' folder for results.{RESET}")

if __name__ == "__main__" :
    main()