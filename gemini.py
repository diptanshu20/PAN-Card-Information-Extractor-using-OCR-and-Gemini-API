import json
import google.generativeai as genai

genai.configure(api_key="your api key")

def extract_pan_info_with_gemini(text):
    prompt = f"""
    Extract the following PAN card details from the text:
    - Full Name
    - Date of Birth
    - PAN Number

    Text:
    {text}

    Output only raw JSON with keys: Name, DOB, PAN. No explanation or markdown.
    """

    model = genai.GenerativeModel('gemini-2.0-flash')
    response = model.generate_content(prompt)
    raw = response.text.strip()

    # Sanitize if it's wrapped in a code block
    if raw.startswith("```"):
        raw = raw.strip("`")              # Remove all backticks
        raw = raw.split("json\n")[-1]     # Remove leading ```json
        raw = raw.strip()                 # Remove trailing whitespace
        if raw.endswith("```"):
            raw = raw[:-3].strip()

    try:
        return json.loads(raw)
    except json.JSONDecodeError as e:
        return {"error": f"JSON Parse Error: {e}", "raw_output": raw}
