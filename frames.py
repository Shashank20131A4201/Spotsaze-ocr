from transformers import YolosFeatureExtractor, YolosForObjectDetection
from PIL import Image
import requests
def crop_img(image):
    image = Image.open(requests.get(url, stream=True).raw)
    feature_extractor = YolosFeatureExtractor.from_pretrained('nickmuchi/yolos-small-finetuned-license-plate-detection')
    model = YolosForObjectDetection.from_pretrained('nickmuchi/yolos-small-finetuned-license-plate-detection')
    inputs = feature_extractor(images=image, return_tensors="pt")
    outputs = model(**inputs)
    logits = outputs.logits
    boxes = outputs.pred_boxes
    return boxes

def video(video):
    cap = cv2.VideoCapture(video_path)
    
    # Check if the video file is opened successfully
    if not cap.isOpened():
        print("Error: Could not open video.")
        return
    while True:
        ret, frame = cap.read()
        if not ret:
            break
  
        
        frame_count += 1
    


