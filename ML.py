import fitz  # PyMuPDF
import pytesseract
import cv2
from pytesseract import Output
import openai

openai.api_key = 'sk-proj-QSOh1YmVzphYFK6kspyaT3BlbkFJuTfwKQrNICtncWxAIkDI'

def extract_text_from_image(image_path):
    try:
        image = cv2.imread(image_path)
        gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        _, thresh_image = cv2.threshold(gray_image, 150, 255, cv2.THRESH_BINARY)
        custom_config = r'--oem 3 --psm 6'
        details = pytesseract.image_to_data(thresh_image, output_type=Output.DICT, config=custom_config)
        extracted_text = ""
        n_boxes = len(details['text'])
        for i in range(n_boxes):
            if int(details['conf'][i]) > 50:
                extracted_text += details['text'][i] + " "
        return extracted_text
    except Exception as e:
        return str(e)

def extract_text_from_pdf(pdf_path):
    try:
        document = fitz.open(pdf_path)
        text = ""
        for page_num in range(document.page_count):
            page = document.load_page(page_num)
            text += page.get_text()
        return text
    except Exception as e:
        return str(e)

def extract_health_info(text):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant that extracts key health information from text and give the medicine advice, diet plan and fitness plan"},
            {"role": "user", "content": f"Extract key health information from the following text: {text} and give the medicine advice, diet plan and fitness plan"}
        ]
    )
    return response.choices[0].message['content'].strip()



