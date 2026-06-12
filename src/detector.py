from ultralytics import YOLO

model = YOLO("yolov8n.pt")

def detect_objects(image_path):

    results = model(image_path)

    boxes = []

    for r in results:
        for b in r.boxes:

            x1,y1,x2,y2 = map(int,b.xyxy[0])

            boxes.append(
                (x1,y1,x2,y2)
            )

    return boxes