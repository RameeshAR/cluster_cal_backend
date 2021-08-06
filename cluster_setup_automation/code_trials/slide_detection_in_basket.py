import cv2
import numpy as np

# |----------------------------------------------------------------------------|
# removeNoise
# |----------------------------------------------------------------------------|
def removeNoise(input_mask, minArea):
    '''
    Function to remove the noise presnt in the input image 
    @Inputs : 1. Mask image
            2. Minimum area threshold for the blob to called as noise
    @Output : Returms the mask after removing the noise present in the input image 
    '''
    nc, lb, st, cnt = cv2.connectedComponentsWithStats(input_mask)

    return_img = np.zeros(input_mask.shape, np.uint8)

    for j in range(1, nc):

        area = st[j, 4]
        #Check for min area of the blob to remove the noise- Dont check for annotation on them
        if area > minArea : 
            check_SingleBlob = 255*np.uint8((lb == j))
            return_img += check_SingleBlob 
    return return_img
# |---------------------- End of removeNoise ---------------------------|

# |----------------------------------------------------------------------------|
# removeNoise
# |----------------------------------------------------------------------------|
def detect_slide(image, step_x, step_y, crop_coords, row, column, minContourArea):
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    basket_matrix = np.zeros((4,30))
    for i in range(0, row):
        y_pos = crop_coords[1]-((i)*step_y)
        for j in range(0, column):
            x_pos = ((j)*step_x)+crop_coords[0]
            print(y_pos, x_pos)
            image = cv2.rectangle(image, (x_pos, y_pos),
            (x_pos+crop_coords[2], y_pos+crop_coords[3]), (0,255,0), 2)
            # temp_crop = gray_image[y_pos:y_pos+crop_coords[3],
            # x_pos:x_pos+crop_coords[2]]
            # temp_crop = 255 - temp_crop
            # misc, threshOut = cv2.threshold(temp_crop, 165, 255, cv2.THRESH_BINARY)
            # noiseRemovedImage = removeNoise(threshOut, minContourArea)
            for val in range(0, crop_coords[2]):
                print(i, j)
    cv2.imshow("noise", image)
    cv2.waitKey(0)
# |---------------------- End of detect_slide ---------------------------|

image = cv2.imread("/home/adminspin/Downloads/pick_basket_03.jpg")
crop_coords = [144,726,65,247]
detect_slide(image, 68, 238, crop_coords, 4, 30, 5000)