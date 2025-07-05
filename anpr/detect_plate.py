### 🔹 anpr/detect_plate.py
```python
# YOLOv8 ANPR detection logic
from ultralytics import YOLO
import cv2

def detect_plate(image_path='sample.jpg'):
    model = YOLO("anpr/model/yolov8n-license-plate.pt")  # Replace with actual model path
    results = model(image_path)
    try:
        for result in results:
            boxes = result.boxes
            for i, box in enumerate(boxes):
                x1, y1, x2, y2 = map(int, box.xyxy[0])
                plate_img = cv2.imread(image_path)[y1:y2, x1:x2]
                cv2.imwrite(f"anpr/model/detected_plate_{i}.jpg", plate_img)
                return f"PLATE_{i}"  # Simulated text extraction
    except Exception as e:
        print("❌ ANPR detection failed:", e)
        return "UNKNOWN"
