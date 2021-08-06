import cv2
import numpy as np
import os
import glob

# base_path = "C:\\Users\\Manish Shiralkar\\Documents\\01_work\\Projects\\"
# project_path = "cluster calibration\\data\\gripper_camera_leopard_imaging\\at_known_robot_pose\\"
image_name_list = glob.glob("/home/adminspin/Music/revolutionary_ideas/cluster_setup_automation/gripper_camera/label_detection_input_images/set_3/*jpg")
cv2.namedWindow('img', 0)
count = 0
for image_path in image_name_list:

    img = cv2.imread(image_path)

    roi_arr = [ (312,221), (532,247),
                (701,226), (953,258),
                (1078,221), (1367,242),
                (1487,227), (1767,262),

                (305,310), (526,337),
                (703,310), (945,334),
                (1080,303), (1349,350),
                (1481,314), (1777,350),

                (315,385), (540,427),
                (700,396), (957,432),
                (1083,390), (1351,441),
                (1478,401), (1780,450),

                (329,470), (543,513),
                (716,484), (950,516),
                (1089,482), (1352,535),
                (1487,495), (1768,540),

                (336,552), (556,603),
                (713, 566), (962, 612),
                (1074,561), (1361,612),
                (1484,569), (1768,630)
                ]

    for ctr in range(int(len(roi_arr)/2)):

        # grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        TL = roi_arr[2 * ctr]
        BR = roi_arr[2 * ctr + 1]
        slide_roi = img[TL[1]:BR[1], TL[0]:BR[0]]
        slide_roi_blue = slide_roi[:,:,0]
        slide_roi_green = slide_roi[:,:,1]
        slide_roi_red = slide_roi[:,:,2]

        mean_blue, std_blue = cv2.meanStdDev(slide_roi_blue)
        mean_green, std_green = cv2.meanStdDev(slide_roi_green)
        mean_red, std_red = cv2.meanStdDev(slide_roi_red)
        mean = max(mean_blue, mean_green, mean_red)
        std = max(std_blue, std_green, std_red)
        if std < 30:
            cv2.putText(img, f'std:{std}',
                        roi_arr[2*ctr], cv2.FONT_HERSHEY_SIMPLEX, 
                        0.8, (0,0,255), 1, cv2.LINE_AA)
        else:
            cv2.putText(img, f'std:{std}',
                        roi_arr[2*ctr], cv2.FONT_HERSHEY_SIMPLEX, 
                        0.8, (0,255,0), 1, cv2.LINE_AA)

        cv2.rectangle(img, roi_arr[2*ctr], roi_arr[2*ctr+1], (0,255,0), 3)
        if std < 15:
            cv2.rectangle(img, roi_arr[2*ctr], roi_arr[2*ctr+1], (0,0,255), 3)
        else:
            cv2.rectangle(img, roi_arr[2*ctr], roi_arr[2*ctr+1], (0,255,0), 3)
        print(mean, std)

    cv2.imshow('img', img)
    cv2.waitKey(0)
    cv2.imwrite(f"/home/adminspin/Desktop/th_30/op_{count}.png", img)
    count += 1

cv2.destroyAllWindows()

