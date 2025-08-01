# PAN-Card-Information-Extractor-using-OCR-and-Gemini-API
Developed a Streamlit web app that extracts PAN card details (Name, DOB, PAN) from images using two AI models: one combining Tesseract OCR with Gemini API, and another using Gemini API alone. Used OpenCV and Pytesseract for preprocessing and deployed for real-time JSON output extraction.


This project is an AI-powered PAN card information extractor. It takes an image of an Indian PAN card as input and returns a structured JSON object containing:
- Full Name  
- Date of Birth (DOB)  
- PAN Number  

🔍 Models Used

This project showcases two different pipelines for data extraction:

 1. OCR + Gemini API (Hybrid Model)
- Uses **Tesseract OCR** to extract raw text from the image.
- The text is then cleaned and passed to **Google Gemini API** to identify and structure PAN details.
![ocr1](https://github.com/user-attachments/assets/4698b111-5c78-464b-b182-1aeb2537b658)
![ocr2](https://github.com/user-attachments/assets/545e1e1f-a7a7-41fe-96b8-817ae7dc3d31)




 2. Gemini API Only
- Skips OCR completely.
- Directly feeds the image into **Gemini's multimodal model** to extract structured data.
![ss](https://github.com/user-attachments/assets/d73f7800-67cc-4b20-8f5b-ae85f523cc3a)



📦 Output Example (JSON)
```json
{
  "Name": "DIPTANSHU SINGH CHANDEL",
  "DOB": "20/05/2003",
  "PAN": "BTXXXXXX"
}
