import cv2
#from nanocamera.NanoCam import Camera
import nanocamera as nano

if __name__ == '__main__':
    # Create the Camera instance
    camera = nano.Camera(flip=2, width=640, height=480, fps=30)
    print('CSI Camera ready? - ', camera.isReady())
    while camera.isReady():
        try:
            # read the camera image
            frame = camera.read()
            # display the frame
            cv2.imshow("Video Frame", frame)
            if cv2.waitKey(25) & 0xFF == ord('q'):
                break
        except KeyboardInterrupt:
            break

    # close the camera instance
    camera.release()

    # remove camera object
    del camera
