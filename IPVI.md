# 🌿 Vegetation Analysis using Image Processing

## 📌 Overview
This project implements a complete image processing pipeline to analyze vegetation using digital images. It computes vegetation indices (NDVI approximation), classifies regions, and generates analytical metrics.

---

## 🚀 Features

- 📷 Batch image processing (input folder → output folder)
- 🌱 NDVI computation (supports RGB + NIR if available)
- 🎯 Rule-based region classification
- 🎨 Color-coded output maps
- 📊 Metrics generation (coverage, vegetation score)
- 📄 Automated report generation
- ⚡ Modular and scalable design

---

## 🧠 Concepts Used

- Image Processing (OpenCV)
- Vegetation Indices (NDVI, GNDVI approximation)
- Threshold-based Classification
- NumPy Vectorization
- Color Mapping
- Statistical Analysis

---

## 📂 Project Structure


IP Vegetative Indices/
│
├── input_folder/ # Input images
├── output_folder/ # Output results
│
├── utils/
│ ├── ansi.py # Colored terminal output
│ └── file_operations.py # Image loader & saver
│
├── vegetaive_indices.py # NDVI computation
├── classify_region.py # Rule-based classifier
├── metrics.py # Metrics computation (separate module)
├── main.py # Main pipeline
│
└── README.md


---

## ⚙️ How It Works

1. Load images from input folder
2. Compute NDVI:
   - Uses NIR if available
   - Otherwise uses RGB approximation
3. Smooth and normalize NDVI
4. Automatically tune thresholds
5. Classify pixels into:
   - Water
   - Soil
   - Grass
   - Dense Vegetation
6. Save processed images
7. Compute metrics (separate script)

---

## 🎨 Output

For each image:

- 🖤 NDVI Map (grayscale)
- 🌈 Region Map (color-coded)
- 📄 Metrics Report

---

## 📊 Metrics Computed

- Region Coverage (%)
- Mean NDVI
- Standard Deviation
- Vegetation Score

---

## ▶️ How to Run

### Step 1: Add Images
Place images in:

input_folder/


---

### Step 2: Run Pipeline

python main.py


---

### Step 3: Generate Metrics

python metrics.py


---

## 📁 Output Example


output_folder/

├── region_image1.jpg
├── region_image2.jpg
│
└── metrics_report.txt


---

## ⚠️ Limitations

- RGB-based NDVI is an approximation
- Accuracy improves with NIR images
- JPEG compression may slightly alter colors (handled using tolerance)

---

## 🧠 Key Design Decisions

- Modular architecture
- Rule-based model (interpretable & fast)
- Separate metrics module (no core modification)
- Vectorized operations for efficiency

---

## 🔥 Future Improvements

- Streamlit Web App (UI)
- Machine Learning classification
- NDVI heatmap visualization
- Histogram analysis
- Satellite dataset integration

---

## 🎯 Conclusion

This project demonstrates a complete pipeline from raw images to meaningful vegetation analysis, combining image processing, classification, and statistical reporting.

---

## 👨‍💻 Author

Developed as a hands-on image processing project to understand real-world vegetation analysis systems.

---