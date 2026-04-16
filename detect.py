import cv2
from ultralytics import YOLO

model = YOLO("yolov5s.pt")

def detect_people(frame):
    results = model(frame)
    count = 0

    for r in results:
        for box in r.boxes:
            if int(box.cls[0]) == 0:  # person class
                count += 1

    return count
