import Dependencies.MMCorePy as MMCore
import numpy
import cv2
from basket_detection import BasketDetector
# ==============================================================================
# MatrixVisionCameraController
# ==============================================================================
class MatrixVisionCameraController():
    
    def __init__(self):
        self._mmcore = MMCore.CMMCore()
        self.initialise_camera()

# |----------------------------------------------------------------------------|
# initialize_device
# |----------------------------------------------------------------------------|
    def initialize_device(self, devName, libName, propList=None):
        # First load the device.
        self._mmcore.loadDevice(devName, libName, devName)

        # Set the properties if any.
        if propList is not None:
            for propInfo in propList:
                propName = propInfo[0]
                propVal = propInfo[1]

                # Doing try catch because some properties might not be
                # modifiable.
                try:
                    self._mmcore.setProperty(devName, propName, propVal)
                except Exception:
                    pass

        # Initialize device.
        try:
            self._mmcore.initializeDevice(devName)
            if "TOFRA" in devName or "ZStage" in devName:
                self._mmcore.setFocusDevice(devName)
            return True, ""
        except Exception as msg:
            return False, msg
# |----------------------End of initialize_device---------------------------|


# |----------------------------------------------------------------------------|
# initialise_camera
# |----------------------------------------------------------------------------|
    def initialise_camera(self):
        print("entered")
        retVal = False
        adapterName = "MatrixVision"
        devNameList = self._mmcore.getAvailableDevices(adapterName)
        for devName in devNameList:
            if "29" in devName:
                print("Loading device: ", devName)
                try:
                    self.initialize_device(devName, adapterName)
                    self._mmcore.setCameraDevice(devName)
                    propName = "ImageProcessing/WhiteBalanceCalibration"
                    self._mmcore.setProperty(devName, propName, "Calibrate Next Frame")
                    # self._mmcore.setExposure(10)
                    self._cameraName = devName
                    retVal = True
                    break
                except Exception as msg:
                    retVal = False
                    print("Exception occurred in "
                          "AutoConfigureLabEndScope::initStage: ", msg)
        return retVal

# |----------------------------------------------------------------------------|
    def _setExposure(self, exp):
        self._mmcore.setExposure(exp)

# |----------------------End of _setExposure---------------------------|

# |----------------------------------------------------------------------------|
# _snapImage
# |----------------------------------------------------------------------------|
    def _snapImage(self):
        self._mmcore.snapImage()
        img = self._mmcore.getImage()

        imgWidth = self._mmcore.getImageWidth()
        imgHeight = self._mmcore.getImageHeight()

        img2 = img.view(dtype=numpy.uint8)
        imageArr = numpy.zeros((imgHeight, imgWidth, 3),
                               dtype=numpy.uint8)

        row_sampling = 1
        col_sampling = 4

        # Flipped BGR to RGB because display need in RGB format.
        imageArr[:, :, 2] = img2[::row_sampling, ::col_sampling]
        imageArr[:, :, 1] = img2[::row_sampling, 1::col_sampling]
        imageArr[:, :, 0] = img2[::row_sampling, 2::col_sampling]

        return imageArr


# |---------------------------End of _snapImage-------------------------------|

if __name__ == '__main__':
    detect_basket = BasketDetector()
    matrix_camera = MatrixVisionCameraController()
    break_status = True
    matrix_camera._setExposure(80)
    while break_status:
        image = matrix_camera._snapImage()
        circle_image = detect_basket.basket_detection_pipeline(image)
        cv2.namedWindow("image", cv2.WINDOW_NORMAL)
        cv2.resizeWindow("image", 600, 600)
        cv2.imshow("image", circle_image)
        k = cv2.waitKey(10)
        if k == 27:
            break
