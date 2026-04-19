import cv2
import numpy as np
import os

OUTPUT_FOLDER = "output_folder"
REPORT_FILE = os.path.join(OUTPUT_FOLDER, "metrics_report.txt")


def match_color(image, target, tol=10):
    return np.all(np.abs(image - target) <= tol, axis=2)

def compute_metrics(image):

    total = image.shape[0] * image.shape[1]
    water = np.sum(match_color(image, [255, 0, 0]))
    soil = np.sum(match_color(image, [42, 42, 165]))
    grass = np.sum(match_color(image, [144, 238, 144]))
    dense = np.sum(match_color(image, [0, 100, 0]))
    return {
        "water_%": round((water / total) * 100, 2),
        "soil_%": round((soil / total) * 100, 2),
        "grass_%": round((grass / total) * 100, 2),
        "dense_veg_%": round((dense / total) * 100, 2)
    }

def main():
    report_lines = []
    report_lines.append("VEGETATION METRICS REPORT")
    report_lines.append("=" * 40)
    for file in os.listdir(OUTPUT_FOLDER):
        if file.startswith("region_"):
            path = os.path.join(OUTPUT_FOLDER, file)
            img = cv2.imread(path)

            if img is None:
                continue

            metrics = compute_metrics(img)
            print(f"\nImage: {file}")
            print(metrics)
            report_lines.append(f"\nImage: {file}")

            for key, value in metrics.items():
                report_lines.append(f"{key}: {value}%")
    with open(REPORT_FILE, "w") as f:
        for line in report_lines:
            f.write(line + "\n")
    print(f"\n Report saved at:{REPORT_FILE}")

if __name__ == "__main__":
    main()