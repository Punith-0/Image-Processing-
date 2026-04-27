import os
import cv2
import numpy as np

INPUT_FOLDER = "data/input_folder_tiff"
OUTPUT_FOLDER = "output/output_folder_png"

os.makedirs(OUTPUT_FOLDER, exist_ok=True)

def stretch_contrast(channel):
    p2, p98 = np.percentile(channel, (2, 98))
    stretched = np.clip((channel - p2) / (p98 - p2), 0, 1)
    return (stretched * 255).astype(np.uint8)

for filename in os.listdir(INPUT_FOLDER):

    if not filename.lower().endswith((".tif", ".tiff")):
        continue

    path = os.path.join(INPUT_FOLDER, filename)
    img = cv2.imread(path, cv2.IMREAD_UNCHANGED)

    if img is None:
        continue

    if len(img.shape) == 3 and img.shape[2] >= 3:
        b, g, r = img[:, :, 0], img[:, :, 1], img[:, :, 2]

        r = stretch_contrast(r)
        g = stretch_contrast(g)
        b = stretch_contrast(b)

        rgb = cv2.merge([r, g, b])

    else:
        rgb = stretch_contrast(img)

    name = os.path.splitext(filename)[0]
    out_path = os.path.join(OUTPUT_FOLDER, f"{name}.png")

    cv2.imwrite(out_path, rgb)

print("Done.")