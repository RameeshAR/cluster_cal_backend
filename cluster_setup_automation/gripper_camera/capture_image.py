import cv2
from pose_detection import PoseDetector

path = "/home/adminspin/Music/"

cap = cv2.VideoCapture(2)
if not (cap.isOpened()):
        print("could not connect to the camera")

else:
    count = 0
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1920)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 1080)

    cv2.namedWindow("preview", cv2.WINDOW_NORMAL)
    cv2.resizeWindow("preview", 1300, 720)
    while True:
        ret, frame = cap.read()
        cv2.imshow("preview", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            cv2.imwrite(f"{path}/{count}.jpg", frame)
            count += 1
            # break
        # elif cv2.waitKey(1) & 0xFF == ord('c'):
        #     print("saved")

    cap.release()
    cv2.destroyAllWindows()
