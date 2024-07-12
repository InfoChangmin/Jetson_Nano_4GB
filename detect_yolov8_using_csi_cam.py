# 실행하기 전에 반드시 pip3 install ultralytics -> pip uninstall opencv-python
# opencv-python를 삭제하는 이유는 이미 우분투에 opencv 4.8.0가 빌드되어 있음.
# 이를 지키지 않으면 지스트리머 미설치로 CSI 카메라를 활용할 수 없음.


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
