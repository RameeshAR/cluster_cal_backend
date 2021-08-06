import cv2
import numpy as np


class SlideDetector:

# |----------------------------------------------------------------------------|
# find_the_roi_markers
# |----------------------------------------------------------------------------|
    def find_the_roi_markers(self, image, crop_coords):
        image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        image_gray_crop = image_gray[crop_coords[1]:crop_coords[1]+crop_coords[3],
                        crop_coords[0]:crop_coords[0]+crop_coords[2]]
        image_gray_crop = 255 - image_gray_crop
        noise_removed_image, x_arr_start, x_arr_end = self.preprocessing(
            image_gray_crop, 225, 255, 20)
        x_arr_start.sort()
        x_arr_end.sort()
        print(x_arr_start)
        print(x_arr_end)
        return x_arr_start, x_arr_end, image_gray
# |----------------------End of find_the_roi_markers---------------------------|

# |----------------------------------------------------------------------------|
# removeNoise
# |----------------------------------------------------------------------------|
    def removeNoise(self, input_mask, minArea):
        '''
        Function to remove the noise presnt in the input image 
        @Inputs : 1. Mask image
                2. Minimum area threshold for the blob to called as noise
        @Output : Returms the mask after removing the noise present in the input image 
        '''
        num, label, stats, cnt = cv2.connectedComponentsWithStats(input_mask)

        return_img = np.zeros(input_mask.shape, np.uint8)
        x_arr_start = []
        x_arr_end = []
        for j in range(1, num):

            area = stats[j, 4]
            # Check for min area of the blob to remove the noise- Dont check for annotation on them
            if area > minArea : 
                check_SingleBlob = 255 * np.uint8((label == j))
                return_img += check_SingleBlob 
            if 10 < area < 150:
                x = stats[j, cv2.CC_STAT_LEFT]
                y = stats[j, cv2.CC_STAT_TOP]
                w = stats[j, cv2.CC_STAT_WIDTH]
                h = stats[j, cv2.CC_STAT_HEIGHT]
                x_arr_end.append(x+w)
                x_arr_start.append(x)
                print(x, y, w, h)
        print(len(x_arr_end))
        # contours, hierarchy = cv2.findContours(return_img, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
        return return_img, x_arr_start, x_arr_end
# |---------------------- End of removeNoise ---------------------------|

# |----------------------------------------------------------------------------|
# preprocessing
# |----------------------------------------------------------------------------|
    def preprocessing(self, image, edgeMinThreshold, edgeMaxThreshold,
                      minContourArea):
        misc, threshOut = cv2.threshold(image, edgeMinThreshold,
                                        edgeMaxThreshold, cv2.THRESH_BINARY)
#         self.showImage(threshOut, "threshout")
        noiseRemovedImage, x_arr_start, x_arr_end = self.removeNoise(threshOut, minContourArea)
        self.showImage(noiseRemovedImage, "noiseRemovedImage")
        return noiseRemovedImage, x_arr_start, x_arr_end
# |----------------------End of preprocessing---------------------------|

# |----------------------------------------------------------------------------|
# showImage
# |----------------------------------------------------------------------------|
    def showImage(self, image, name):
        cv2.namedWindow(name, cv2.WINDOW_NORMAL)
        cv2.resizeWindow(name, 600, 600)
        cv2.imshow(name, image)
        cv2.waitKey(0)
# |----------------------End of showImage---------------------------|

# |----------------------------------------------------------------------------|
# slide_detection_pipeline
# |----------------------------------------------------------------------------|
    def slide_detection_pipeline(self, image, init_crop_coords,
    dot_crop_coords, y_arr):
        image = image[init_crop_coords[1]:init_crop_coords[1]+init_crop_coords[3],
                        init_crop_coords[0]:init_crop_coords[0]+init_crop_coords[2]]
        x_arr_start, x_arr_end, image_gray = slide_detector.find_the_roi_markers(
            image, dot_crop_coords)
        
        for row in range(0, 4):
            for i in range(0, 30):
                print("crop_coords",  x_arr_start[i], x_arr_end[i+1], y_arr[row][0], y_arr[row][1])
                temp_image_gray = image_gray[y_arr[row][0]+50:y_arr[row][1]-100, x_arr_start[i]:x_arr_end[i+1]]
                image_rect = cv2.rectangle(image, (x_arr_start[i], y_arr[row][0]),
                                           (x_arr_end[i+1], y_arr[row][1]), 255, 1)
                tight = cv2.Canny(255-temp_image_gray, 170, 170)
                # self.showImage(tight, f"crop_pattern{row}{i}")
                # cv2.destroyWindow(f"crop_pattern{row}{i}")
        self.showImage(image_rect, f"crop_pattern{row}{i}")




slide_detector = SlideDetector()
image =  cv2.imread("/home/adminspin/Music/revolutionary_ideas/cluster_setup_automation/image_data_set/set1_pick_basket3.jpg")
init_crop_coords = [370, 196, 1388, 784]
dot_crop_coords = [0,557,1354,56]
y_arr = [(560, 740), (390, 570), (220, 400), (40, 220)]
slide_detector.slide_detection_pipeline(image, init_crop_coords, dot_crop_coords, y_arr)
