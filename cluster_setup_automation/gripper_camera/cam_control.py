import cv2
from basket_detection import BasketDetector
from pose_detection import PoseDetector

# |----------------------------------------------------------------------------|
# showImage
# |----------------------------------------------------------------------------|
def showImage(image, name):
    cv2.imshow(name, image)
    cv2.waitKey(0)
# |----------------------End of showImage---------------------------|



def live_detection(device_id, basket_type, station_num, crop_coords):
    cap = cv2.VideoCapture(device_id)
    basket_detection = BasketDetector()
    pose_detection = PoseDetector()
    if not (cap.isOpened()):
        print("could not connect to the camera")

    else:
        cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1920)
        cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 1080)

        cv2.namedWindow("preview", cv2.WINDOW_NORMAL)
        cv2.resizeWindow("preview", 1300, 720)
        while True:
            ret, frame = cap.read()
            cv2.imwrite("input.bmp", frame)
            if basket_type == 0:
                crop_coords = [128, 25, 1656, 952]
                crop_coords_cross_hair = [[132, 0, 50, 99],[375, 0, 50, 99],[620, 0, 50, 99],[865, 0, 50, 99]]
                comparison_values = [[0,100],[250,350],[450,550],[700,800]]
                result_image = basket_detection.basket_detection_pipeline(frame, station_num, basket_type,
                crop_coords,comparison_values, crop_coords_cross_hair)
                cv2.rectangle(result_image, (crop_coords[0], crop_coords[1]), (crop_coords[0]+crop_coords[2],
                crop_coords[1]+crop_coords[3]), (0,0,255), 2)
            elif basket_type == 1:
                crop_coords = [480, 854, 990, 148]
                crop_coords_cross_hair = [[132, 0, 50, 99],[375, 0, 50, 99],[620, 0, 50, 99],[865, 0, 50, 99]]
                comparison_values = [[0,100],[250,350],[450,550],[700,800]]
                result_image = basket_detection.basket_detection_pipeline(frame, station_num, basket_type,
                crop_coords,comparison_values, crop_coords_cross_hair)
                cv2.rectangle(result_image, (665,285), (1255,794), (0,0,255), 2)
            elif basket_type == 2:
                result_image = pose_detection.pose_detection_pipeline(frame)
            # cv2.imshow("preview", result_image)
            elif basket_type == 3:
                roi_arr = [ (333 , 236), (565 , 257),
                (723 , 241), (940 , 264),
                (1086 , 246), (1402 , 271),
                (1498 , 245), (1780 , 267),

                (328 , 333), (584 , 366),
                (703 , 344), (972 , 364),
                (1095 , 344), (1392 , 373),
                (1510 , 366), (1750 , 384),

                (330 , 409), (573 , 442),
                (747 , 427), (967 , 463),
                (1106 , 428), (1356 , 477),
                (1486 , 433), (1767 , 475),

                (336 , 501), (594 , 533),
                (721 , 508), (968 , 538),
                (1098 , 515), (1376 , 562),
                (1506 , 532), (1799 , 569),

                (391 , 579), (571 , 619),
                (775 , 597), (957 , 647),
                (1100 , 593), (1310 , 638),
                (1513 , 611), (1758 , 660)
                ]

                for ctr in range(int(len(roi_arr)/2)):

                    # grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

                    TL = roi_arr[2 * ctr]
                    BR = roi_arr[2 * ctr + 1]
                    slide_roi = frame[TL[1]:BR[1], TL[0]:BR[0]]
                    slide_roi_blue = slide_roi[:,:,0]
                    slide_roi_green = slide_roi[:,:,1]
                    slide_roi_red = slide_roi[:,:,2]

                    mean_blue, std_blue = cv2.meanStdDev(slide_roi_blue)
                    mean_green, std_green = cv2.meanStdDev(slide_roi_green)
                    mean_red, std_red = cv2.meanStdDev(slide_roi_red)
                    mean = max(mean_blue, mean_green, mean_red)
                    std = max(std_blue, std_green, std_red)
                    if std < 30:
                        cv2.putText(frame, f'std:{std}',
                                    roi_arr[2*ctr], cv2.FONT_HERSHEY_SIMPLEX, 
                                    0.8, (0,0,255), 1, cv2.LINE_AA)
                    else:
                        cv2.putText(frame, f'std:{std}',
                                    roi_arr[2*ctr], cv2.FONT_HERSHEY_SIMPLEX, 
                                    0.8, (0,255,0), 1, cv2.LINE_AA)
                    cv2.rectangle(frame, roi_arr[2*ctr], roi_arr[2*ctr+1], (0,255,0), 3)
                    if std < 30:
                        cv2.rectangle(frame, roi_arr[2*ctr], roi_arr[2*ctr+1], (0,0,255), 3)
                    else:
                        cv2.rectangle(frame, roi_arr[2*ctr], roi_arr[2*ctr+1], (0,255,0), 3)

            cv2.imshow("preview", result_image)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        cap.release()
        cv2.destroyAllWindows()

crop_coords = [128, 25, 1656, 952]
live_detection(2, 2, 1, crop_coords) 