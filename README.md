젯슨 나노를 활용해 CUDA 가속 환경을 이용하고 싶고.. 파이썬 3.8도 사용해 Yolov8도 구동하고 싶으신 분들이라면 이 코드와 설명이 도움될 것입니다.
버전업 관련 내용은 지속적으로 남기겠습니다.
문제가 발생할 경우 이슈로 달아주시면 함께 토론하면 좋겠습니다.

이 파일은 NVIDIA JETSON NANO 4GB 모델을 활용하며 Ubuntu 20.04 버전을 기준으로 작성되었습니다.

우분투 20.04 버전은 Qengineering님께서 제작해주신 ISO 이미지 파일로 구성되었습니다.
파일이 조각나 있으니 필요한 분들께서는 아래 링크에서 깃허브 링크로 이동하여 부팅 디스크를 제작하시기 바랍니다.
https://qengineering.eu/install-ubuntu-20.04-on-jetson-nano.html

#부팅디스크 ISO링크: https://github.com/Qengineering/Jetson-Nano-Ubuntu-20-image
#부팅디스크 만들기 프로그램 링크: https://rufus.ie/ko/

1. CSI CAMERA: USB 카메라를 활용하지 않고 CSI 카메라를 이용해 화면을 켤 수 있습니다.
   본 코드를 실행하기 전에 반드시 pip3 install nanocamera 가 필요합니다.

2. Yolov8 + CSI 카메라: Yolov8을 Jetson nano에서 구동하고 싶은 분들을 위한 코드입니다.
   유의사항!!!
     가. pip3 install ultralytics 를 진행하세요!
     나. 이후에 opencv-python 4.10이 설치되는데 이는 지스트리머가 없는 버전으로 반드시 pip uninstall opencv-python을 진행하세요.
     다. python3를 실행하여 import cv2를 입력하고 cv2.__version__에서 CV2 버전이 4.8.0인지 꼭 확인하세요.
<img width="1114" alt="image" src="https://github.com/user-attachments/assets/799745f0-f3db-4f70-83f7-dc58d55a3ce8">
