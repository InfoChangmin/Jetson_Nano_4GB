from ultralytics import YOLO
import cv2
import nanocamera as nano

cap = nano.Camera(flip=2, width=640, height=480, fps=30)
print('CSI Camera ready? - ', cap.isReady())

model = YOLO('yolov8n.pt')

while cap.isReady():
    try:
        image = cap.read()
        results = model(image, conf=0.5)

        for result in results:
            #print(result.boxes.xyxy.tolist(), result.boxes.conf.tolist())

            result_plotted = results[0].plot()
            cv2.imshow('img', result_plotted)

        if cv2.waitKey(1) == ord('q'):
            break
    except KeyboardInterrupt:
        break
cap.release()

del cap
