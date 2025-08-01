import google.generativeai as genai
import base64

genai.configure(api_key="yyour api key")

model = genai.GenerativeModel(model_name="gemini-2.0-flash")

def extract_pan_info_from_image(image_bytes):
    prompt = """
    This is an Indian PAN card. Please extract the following details:
    - Full Name
    - Date of Birth
    - PAN Number

    Return the output in raw JSON format with keys: Name, DOB, PAn
    """

    response = model.generate_content(
        contents=[prompt, image_bytes],
        stream=False
    )

    text = response.text.strip()

    # Clean up markdown if present
    if text.startswith("```"):
        text = text.strip("`").split("json\n")[-1]
        if text.endswith("```"):
            text = text[:-3].strip()

    return text
