import streamlit as st
import cv2
import numpy as np
from scripts.vegetaive_indices import VegetationIndices
from scripts.classify_region import ClassifierModel
from scripts.metrics import compute_metrics

st.set_page_config(page_title = "Vegetation Analyzer", layout = "wide")
st.title("Vegetation Analysis App ")

show_metrics = st.checkbox("Show Metrics")
show_histogram = st.checkbox("Show NDVI Histogram")

uploaded_files = st.file_uploader(
    "Upload Images",
    type=["jpg" , "png" , "jpeg"],
    accept_multiple_files = True
)

def convert_image_to_bytes(image):
    success, buffer = cv2.imencode(".png", image)
    if not success:
        return None
    return buffer.tobytes()

if uploaded_files:
    model = ClassifierModel()

    for uploaded_file in uploaded_files:

        st.markdown("----")
        st.subheader(f"{uploaded_file.name}")
        file_bytes = np.asarray(bytearray(uploaded_file.read() ), dtype=np.uint8)
        image = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)

        if image is None:
            st.error(f"Failed to read {uploaded_file.name}")
            continue
        ndvi = VegetationIndices.compute_ndvi(image )
        ndvi = np.round(ndvi, 2)
        ndvi_img = VegetationIndices.normalize_index(ndvi)
        model.tune_thresholds(ndvi)
        region = model.classify(ndvi)

        col1, col2, col3 = st.columns(3)

        with col1:
            st.image(cv2.cvtColor(image , cv2.COLOR_BGR2RGB) , caption="Original")
        with col2:
            st.image(ndvi_img , caption="NDVI")
        with col3:
            st.image(cv2.cvtColor(region, cv2.COLOR_BGR2RGB) , caption="Region Map")

        if show_metrics:
            st.markdown("Metrics")
            metrics = compute_metrics(region)
            st.write(metrics)

        if show_histogram:
            st.markdown(" NDVI Histogram")
            hist, _ = np.histogram(ndvi , bins=50 )
            st.line_chart(hist)

        download_toggle = st.checkbox(
            f"Enable Download for {uploaded_file.name}",
            key=f"download_{uploaded_file.name}"
        )

        if download_toggle:
            st.markdown(" Download Options")

            ndvi_bytes = convert_image_to_bytes(ndvi_img)
            region_bytes = convert_image_to_bytes(region)

            col_d1, col_d2, col_d3 = st.columns(3)
            with col_d1:
                if ndvi_bytes:
                    st.download_button(
                        label="Download NDVI",
                        data=ndvi_bytes,
                        file_name=f"ndvi_{uploaded_file.name}.png" ,
                        mime="image/png",
                        key=f"ndvi_{uploaded_file.name}"
                    )

            with col_d2:
                if region_bytes:
                    st.download_button(
                        label="Download Region Map",
                        data=region_bytes,
                        file_name=f"region_{uploaded_file.name}.png" ,
                        mime="image/png",
                        key=f"region_{uploaded_file.name}"
                    )

            if show_metrics:
                metrics_text = "\n".join([f"{k} : {v} %" for k, v in metrics.items()])
                with col_d3:
                    st.download_button(
                        label="Download Metrics",  
                        data=metrics_text,
                        file_name=f"metrics_{uploaded_file.name}.txt",
                        mime="text/plain",
                        key=f"metrics_{uploaded_file.name}"
                    )