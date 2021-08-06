import numpy as np
import cv2 
import glob
import time
import math

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
    
    CHECKER_BOARD = (6, 5)
    end = time.time()
    # print(f"time taken to create class variables {end-start}s")

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
# |-------------------------------q---------------------------------------------|
    def pre_requisites(self):
        criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 30, 0.001)
        objp = np.zeros((self.CHECKER_BOARD[0] * self.CHECKER_BOARD[1],3), np.float32)
        objp[:,:2] = np.mgrid[0:self.CHECKER_BOARD[0], 0:self.CHECKER_BOARD[1]].T.reshape(-1,2)
        objp =  4.09 * objp
        print("object_points:", objp)
        axis = np.float32([[3,0,0], [0,3,0], [0,0,-3]]).reshape(-1,3) 
        axis = 4.09 * axis
        return axis, criteria, objp
# |---------------------- End of pre_requisites ---------------------------|

# |----------------------------------------------------------------------------|
# is_rotation_matrix
# |----------------------------------------------------------------------------|
    def is_rotation_matrix(self, R) :
        Rt = np.transpose(R)
        shouldBeIdentity = np.dot(Rt, R)
        I = np.identity(3, dtype = R.dtype)
        n = np.linalg.norm(I - shouldBeIdentity)
        return n < 1e-6
# |---------------------- End of is_rotation_matrix ---------------------------|

# |----------------------------------------------------------------------------|
# rotation_matrix_to_euler_angles
# |----------------------------------------------------------------------------|
    def rotation_matrix_to_euler_angles(self, R) :
        assert(self.is_rotation_matrix(R))
        sy = math.sqrt(R[0,0] * R[0,0] +  R[1,0] * R[1,0])
        singular = sy < 1e-6
        if  not singular :
            x = math.atan2(R[2,1] , R[2,2])
            y = math.atan2(-R[2,0], sy)
            z = math.atan2(R[1,0], R[0,0])
        else :
            x = math.atan2(-R[1,2], R[1,1])
            y = math.atan2(-R[2,0], sy)
            z = 0
        return np.array([x, y, z])
# |---------------------- End of is_rotation_matrix ---------------------------|

# |----------------------------------------------------------------------------|
# pre_requisites
# |----------------------------------------------------------------------------|
    def pose_detection_pipeline(self, img):
        start = time.time()
        # img = img[665:1255, 285:794]
        # img = img[515:1065, 950:1475]
        # img = img[442:1050, 800:1510]
        gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        end = time.time()
        # print(f"time taken to create convert to gray {end-start}s")
        start = time.time()
        ret, corners = cv2.findChessboardCorners(gray, self.CHECKER_BOARD,None)
        end = time.time()
        # print(f"time taken to create find chessboard corners {end-start}s")
        start = time.time()
        axis, criteria, objp = self.pre_requisites()
        end = time.time()
        # print(f"time taken for pre requisite to run:{end-start}")
        if ret == True:
            start = time.time()
            corners2 = cv2.cornerSubPix(gray,corners,(11,11),(-1,-1),criteria)
            end = time.time()
            # print(f"time taken for corner sub pix:{end-start}")
            # Find the rotation and translation vectors.
            start = time.time()
            ret, rvecs, tvecs = cv2.solvePnP(objp, corners2,
            self.CAMERA_MATRIX, self.DISTORTION_ARRAY)
            print("translation:", tvecs)
            end = time.time()
            # print(f"time taken for solvepnp:{end-start}")
            rot_mtx, _ = cv2.Rodrigues(rvecs)
            euler_angle = self.rotation_matrix_to_euler_angles(rot_mtx)
            print("Rx: ", euler_angle[0], "Ry: ", euler_angle[1], "Rz: ", euler_angle[2])
            print("Rx deg: ", math.degrees(euler_angle[0]), "Ry deg: ", math.degrees(euler_angle[1]), "Rz deg: ", math.degrees(euler_angle[2]))
            # project 3D points to image plane
            start = time.time()
            imgpts, jac = cv2.projectPoints(axis, rvecs, tvecs,
            self.CAMERA_MATRIX, self.DISTORTION_ARRAY)
            end = time.time()
            # print(f"time taken for project points:{end-start}")
            start = time.time()
            img = self.draw_pose_axis(img,corners2,imgpts)
            end = time.time()
            # print(f"time taken for draw pose axis:{end-start}")
            cv2.putText(img, f"Rx deg: {math.degrees(euler_angle[0])}",
            (100,400),
            cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,0), 1, cv2.LINE_AA)
            cv2.putText(img, f"Ry deg: {math.degrees(euler_angle[1])}",
            (100,450),
            cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,0), 1, cv2.LINE_AA)
            cv2.putText(img, f"Rz deg: {math.degrees(euler_angle[2])}",
            (100,500),
            cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,0), 1, cv2.LINE_AA)
        return img

if __name__ == '__main__': 
    image_folder = "/home/adminspin/Music/revolutionary_ideas/cluster_setup_automation/gripper_camera/Z_pillar_checker_board/"
    start = time.time()
    pose_detection = PoseDetector()
    end = time.time()
    print(f"time taken for class:{end-start}")
    for fname in glob.glob(image_folder+'*.jpg'):
        # print("image name", fname)
        img = cv2.imread(fname)
        start = time.time()
        final_image = pose_detection.pose_detection_pipeline(img)
        end = time.time()
        # print(f"time taken for pose pipeline to run:{end-start}")
        cv2.imshow('img',img)
        k = cv2.waitKey(0) & 0xFF
        if k == ord('s'):
            cv2.imwrite(fname[:6]+'.png', final_image)
    cv2.destroyAllWindows()



