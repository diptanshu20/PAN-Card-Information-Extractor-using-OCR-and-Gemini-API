import streamlit as st
from ocr import extract_text_from_image
from gemini import extract_pan_info_with_gemini

st.title("PAN Card OCR Extractor")

uploaded_file = st.file_uploader("Upload PAN card image", type=["png", "jpg", "jpeg"])
if uploaded_file:
    image_path = "temp.jpg"
    with open(image_path, "wb") as f:
        f.write(uploaded_file.read())

    st.image(image_path, caption="Uploaded Image", use_column_width=True)

    text = extract_text_from_image(image_path)
    st.text_area("Extracted Text", text, height=200)

    with st.spinner("Analyzing with Gemini..."):
        result = extract_pan_info_with_gemini(text)
        st.subheader("Extracted PAN Details:")
        st.json(result)