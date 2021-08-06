import cv2
import numpy as np
import os
import glob
import time

# ==============================================================================
# CameraCalibration
# ==============================================================================
class CameraCalibration():

# |----------------------------------------------------------------------------|
# identify_checker_board
# |----------------------------------------------------------------------------|
    def identify_checker_board(self, data_path):
        # Defining the dimensions of checkerboard
        CHECKERBOARD = (7, 9)
        criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 30, 0.001)

        # Creating vector to store vectors of 3D points for each checkerboard image
        objpoints = []
        # Creating vector to store vectors of 2D points for each checkerboard image
        imgpoints = []

        # Defining the world coordinates for 3D points
        objp = np.zeros((1, CHECKERBOARD[0] * CHECKERBOARD[1], 3), np.float32)
        objp[0, :, :2] = np.mgrid[0:CHECKERBOARD[0], 0:CHECKERBOARD[1]].T.reshape(-1, 2)
        prev_img_shape = None

        # Extracting path of individual image stored in a given directory
        #images = glob.glob('./images/*.jpg')
        
        images = glob.glob(data_path+'*.bmp')
        cv2.namedWindow('img', 0)

        for fname in images:
            img = cv2.imread(fname)
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            # Find the chess board corners
            # If desired number of corners are found in the image then ret = true
            ret, corners = cv2.findChessboardCorners(
                gray, CHECKERBOARD, cv2.CALIB_CB_ADAPTIVE_THRESH + cv2.CALIB_CB_FAST_CHECK + cv2.CALIB_CB_NORMALIZE_IMAGE)

            """
            If desired number of corner are detected,
            we refine the pixel coordinates and display 
            them on the images of checker board
            """
            if ret == True:
                objpoints.append(objp)
                # refining pixel coordinates for given 2d points.
                corners2 = cv2.cornerSubPix(gray, corners, (11, 11), (-1, -1), criteria)

                imgpoints.append(corners2)

                # Draw and display the corners
                img = cv2.drawChessboardCorners(img, CHECKERBOARD, corners2, ret)

            cv2.imshow('img', img)
            cv2.waitKey(0)
            

        h,w = img.shape[:2]
        return objpoints, imgpoints, gray.shape[::-1]
# |---------------------- End of identify_checker_board ----------------------|
    
# |----------------------------------------------------------------------------|
# get_camera_cal_params
# |----------------------------------------------------------------------------|
    def get_camera_cal_params(self, objpoints, imgpoints, shape):
        """
        Performing camera calibration by 
        passing the value of known 3D points (objpoints)
        and corresponding pixel coordinates of the 
        detected corners (imgpoints)
        """
        ret, mtx, dist, rvecs, tvecs = cv2.calibrateCamera(objpoints,
        imgpoints, shape, None, None)

        print("Camera matrix : \n")
        print(mtx)
        print("dist : \n")
        print(dist)
        print("rvecs : \n")
        print(rvecs)
        print("tvecs : \n")
        print(tvecs)
        return ret, mtx, dist, rvecs, tvecs
# |---------------------- End of get_camera_cal_params -----------------------|

# |----------------------------------------------------------------------------|
# undistort
# |----------------------------------------------------------------------------|
    def undistort(self, image, mtx, dist):
        h,  w = image.shape[:2]
        newcameramtx, roi = cv2.getOptimalNewCameraMatrix(mtx, dist, (w,h), 1, (w,h))

        # undistort
        dst = cv2.undistort(image, mtx, dist, None, newcameramtx)
        # crop the image
        x, y, w, h = roi
        dst = dst[y:y+h, x:x+w]
        # cv2.imwrite('calibresult.png', dst)
        return dst
# |---------------------- End of undistort ---------------------------|

if __name__ == '__main__':
    data_path = "/home/adminspin/Music/revolutionary_ideas/cluster_setup_automation/gripper_camera/checkerboard_images/"
    test_image = cv2.imread("/home/adminspin/Music/revolutionary_ideas/cluster_setup_automation/code_trials/data_images/input_images/set_1.bmp")
    
    calibrate_camera = CameraCalibration()
    objpoints, imgpoints, shape = calibrate_camera.identify_checker_board(data_path)
    ret, mtx, dist, rvecs, tvecs = calibrate_camera.get_camera_cal_params(objpoints, imgpoints, shape)
    undistorted_image = calibrate_camera.undistort(test_image, mtx, dist)

    cv2.imshow('img', undistorted_image)
    cv2.waitKey(0)

    cv2.destroyAllWindows()
