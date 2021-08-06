import numpy as np
import cv2 
import glob
import time

# ==============================================================================
# PoseDetector
# ==============================================================================
class PoseDetector:

# class variables
    start = time.time()
    CAMERA_MATRIX = np.array([[2.37452352e+03, 0.00000000e+00, 1.00468591e+03], 
        [0.00000000e+00, 2.38400589e+03,  5.34980549e+02],
        [0.00000000e+00, 0.00000000e+00, 1.00000000e+00]])

    DISTORTION_ARRAY = np.array([3.36171786e-01, -5.01286869e+00,  3.41931516e-03, 
        -6.76305820e-03, 3.08759257e+01])
    
    CHECKER_BOARD = (4, 3)
    end = time.time()
    print(f"time taken to create class variables {end-start}s")

# |----------------------------------------------------------------------------|
# draw_pose_axis
# |----------------------------------------------------------------------------|
    def draw_pose_axis(self, img, corners, imgpts):
        int_corner_0 = corners[0].astype(int)
        int_imgpts = imgpts.astype(int)
        corner = tuple(int_corner_0.ravel())
        img = cv2.line(img, corner, tuple(int_imgpts[0].ravel()), (255,0,0), 5)
        img = cv2.line(img, corner, tuple(int_imgpts[1].ravel()), (0,255,0), 5)
        img = cv2.line(img, corner, tuple(int_imgpts[2].ravel()), (0,0,255), 5)
        return img
# |---------------------- End of identify_checker_board ---------------------------|

# |----------------------------------------------------------------------------|
# pre_requisites
# |----------------------------------------------------------------------------|
    def pre_requisites(self):
        criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 30, 0.001)
        objp = np.zeros((self.CHECKER_BOARD[0] * self.CHECKER_BOARD[1],3), np.float32)
        objp[:,:2] = np.mgrid[0:self.CHECKER_BOARD[0], 0:self.CHECKER_BOARD[1]].T.reshape(-1,2)

        axis = np.float32([[3,0,0], [0,3,0], [0,0,-3]]).reshape(-1,3) 

        return axis, criteria, objp
# |---------------------- End of pre_requisites ---------------------------|

# |----------------------------------------------------------------------------|
# pre_requisites
# |----------------------------------------------------------------------------|
    def pose_detection_pipeline(self, img):
        start = time.time()
        # img = img[665:1255, 285:794]
        gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        end = time.time()
        print(f"time taken to create convert to gray {end-start}s")
        start = time.time()
        ret, corners = cv2.findChessboardCorners(gray, self.CHECKER_BOARD,None)
        end = time.time()
        print(f"time taken to create find chessboard corners {end-start}s")
        start = time.time()
        axis, criteria, objp = self.pre_requisites()
        end = time.time()
        print(f"time taken for pre requisite to run:{end-start}")
        if ret == True:
            start = time.time()
            corners2 = cv2.cornerSubPix(gray,corners,(11,11),(-1,-1),criteria)
            end = time.time()
            print(f"time taken for corner sub pix:{end-start}")
            # Find the rotation and translation vectors.
            start = time.time()
            ret,rvecs, tvecs = cv2.solvePnP(objp, corners2,
            self.CAMERA_MATRIX, self.DISTORTION_ARRAY)
            end = time.time()
            print(f"time taken for solvepnp:{end-start}")
            # project 3D points to image plane
            start = time.time()
            imgpts, jac = cv2.projectPoints(axis, rvecs, tvecs,
            self.CAMERA_MATRIX, self.DISTORTION_ARRAY)
            end = time.time()
            print(f"time taken for project points:{end-start}")
            
            print(imgpts)
            start = time.time()
            img = self.draw_pose_axis(img,corners2,imgpts)
            end = time.time()
            print(f"time taken for draw pose axis:{end-start}")
        return img

if __name__ == '__main__': 
    image_folder = "/home/adminspin/Desktop/cropped_pose_images/"
    start = time.time()
    pose_detection = PoseDetector()
    end = time.time()
    print(f"time taken for class:{end-start}")
    for fname in glob.glob(image_folder+'*.jpg'):
        print("image name", fname)
        img = cv2.imread(fname)
        cv2.imshow('img',img)
        k = cv2.waitKey(0) & 0xFF
        if k == ord('s'):
            cv2.imwrite(fname[:6]+'.png', final_image)
        start = time.time()
        final_image = pose_detection.pose_detection_pipeline(img)
        end = time.time()
        print(f"time taken for pose pipeline to run:{end-start}")
        cv2.imshow('img',final_image)
        k = cv2.waitKey(0) & 0xFF
        if k == ord('s'):
            cv2.imwrite(fname[:6]+'.png', final_image)
    cv2.destroyAllWindows()



