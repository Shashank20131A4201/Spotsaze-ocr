# Use a pipeline as a high-level helper
from transformers import pipeline
def OCR1(image):
    pipe = pipeline("image-to-text", model="DunnBC22/trocr-base-printed_license_plates_ocr")
    return pipe(image)
def OCR2(image):
    pipe = pipeline("image-to-text", model="chanelcolgate/trocr-base-printed_captcha_ocr")
    return pipe(image)
def OCR3(image):
    pipe = pipeline("image-to-text", model="DunnBC22/trocr-large-printed-cmc7_tesseract_MICR_ocr")
    return pipe(image)
