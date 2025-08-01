import streamlit as st
from PIL import Image
import io

from geminiwoocr import extract_pan_info_from_image  

st.title("PAN Card Info Extractor (via Gemini)")

uploaded_file = st.file_uploader("Upload PAN Card Image", type=["png", "jpg", "jpeg"])

if uploaded_file:
    st.image(uploaded_file, caption="Uploaded Image", use_column_width=True)
    
    image_bytes = uploaded_file.read()
    image = Image.open(io.BytesIO(image_bytes))

    with st.spinner("Extracting with Gemini..."):
        result = extract_pan_info_from_image(image)
        st.subheader("Extracted PAN Details")
        st.text(result)
