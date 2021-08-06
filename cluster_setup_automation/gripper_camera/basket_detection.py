import cv2
import math
import numpy as np

# ==============================================================================
# BasketDetector
# ==============================================================================

class BasketDetector():

# |----------------------------------------------------------------------------|
# vertical_ray_profiler
# |----------------------------------------------------------------------------|
    def vertical_ray_profiler(self, image, column, circle_image):
        height, width = image.shape
        basket_bottom_edge = 0
        basket_top_edge = 0
        width = 0
        # self.showImage(image, "image")
        for top in range(0, height-1):
            if image[top][column] > 150:
                # print(column, image[top][column])
                basket_top_edge = top
                break
        for bottom in range(height-1, 0, -1):
            if image[bottom][column] > 150:
                basket_bottom_edge = bottom
                break
        # circle_image = cv2.line(circle_image, (column, 0), (column, height-1),
        #                          255, 2)
        width = basket_bottom_edge - basket_top_edge
        # print("width:", width)
        if width > 600:
            return basket_top_edge, basket_bottom_edge, circle_image, width
        else:
            return None, None, circle_image, width
# |---------------------- End of vertical_ray_profiler ---------------------------|

# |----------------------------------------------------------------------------|
# horizontal_ray_profiler
# |----------------------------------------------------------------------------|
    def horizontal_ray_profiler(self, image, row, circle_image):
        height, width = image.shape
        basket_left_edge = 0
        basket_right_edge = 0
        for left in range(0, width-1):
            if image[row][left] > 150:
                basket_left_edge = left
                break
        for right in range(width-1, 0, -1):
            if image[row][right] > 150:
                basket_right_edge = right
                break
        # print("length:", basket_right_edge-basket_left_edge)
        if (basket_right_edge-basket_left_edge) > 500:
            return basket_left_edge, basket_right_edge, circle_image
        else:
            return None, None, circle_image
# |---------------------- End of horizontal_ray_profiler ---------------------------|

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
# removeNoise
# |----------------------------------------------------------------------------|
    def removeNoise(self, input_mask, minArea):
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
# fit_line_horizontal
# |----------------------------------------------------------------------------|
    def fit_line_horizontal(self, length_top_edge_arr, circle_image,
        top_edge_arr, bottom_edge_arr, column_arr, centre_color, outline_color):
        xy_arr_top = []
        xy_arr_bottom = []
        for index in range(0, length_top_edge_arr):
            xy_arr_top.append([column_arr[index], top_edge_arr[index]])
            circle_image = cv2.circle(circle_image, (column_arr[index],
                                                    top_edge_arr[index]),
                                                    10, (0,255,0), 2)
            
            xy_arr_bottom.append([column_arr[index], bottom_edge_arr[index]])
            circle_image = cv2.circle(circle_image, (column_arr[index],
                                                    bottom_edge_arr[index]),
                                                    10, (0,255,0), 2)
            
        rows, cols, channels = circle_image.shape
        
        xy_arr_top = np.asarray(xy_arr_top, dtype=np.int32)
        [vx,vy,x,y] = cv2.fitLine(xy_arr_top, cv2.DIST_L12, 0, 0.01, 0.01)
        top_line_fit_details = [vx,vy,x,y]
        
        top_mid_point_x = int((column_arr[0]+ column_arr[
            len(column_arr)-1])/2)
        top_mid_point_y = int(((top_mid_point_x-x)*vy/vx)+y)
        lefty = int((-x*vy/vx) + y)
        righty = int(((cols-x)*vy/vx)+y)
        
        circle_image = cv2.circle(circle_image, (top_mid_point_x, top_mid_point_y),
                                25, (0,0,255), 2)
        circle_image = cv2.line(circle_image, (cols-1,righty), (0,lefty), (0,255,0), 2)
        top_line = [[cols-1,righty], [0,lefty]]
        
        
        xy_arr_bottom = np.asarray(xy_arr_bottom, dtype=np.int32)
        [vx,vy,x,y] = cv2.fitLine(xy_arr_bottom, cv2.DIST_L12, 0, 0.01, 0.01)
        bottom_line_fit_details = [vx,vy,x,y]
        
        bottom_mid_point_x = int((column_arr[0]+ column_arr[
            len(column_arr)-1])/2)
        bottom_mid_point_y = int(((top_mid_point_x-x)*vy/vx)+y)
        lefty = int((-x*vy/vx) + y)
        righty = int(((cols-x)*vy/vx)+y)
        
        circle_image = cv2.circle(circle_image, (bottom_mid_point_x, bottom_mid_point_y),
                                25, (0,0,255), 2)
        circle_image = cv2.line(circle_image, (cols-1,righty), (0,lefty), (0,255,0), 2)
        bottom_line = [[cols-1,righty], [0,lefty]]

        centre_point_x = int((top_mid_point_x + bottom_mid_point_x)/2)
        centre_point_y = int((top_mid_point_y + bottom_mid_point_y)/2)

        # cv2.imshow("circle_image", circle_image)
        # cv2.waitKey(0)
        return circle_image, top_line, bottom_line, centre_point_x, top_line_fit_details, bottom_line_fit_details
# |----------------------End of fit_line_horizontal---------------------------|

# |----------------------------------------------------------------------------|
# fit_line_vertical
# |----------------------------------------------------------------------------|
    def fit_line_vertical(self, length_left_edge_arr, circle_image,
        left_side_arr, right_side_arr, row_arr, centre_color, outline_color):
        xy_left_arr = []
        xy_right_arr = []
        for index in range(0, length_left_edge_arr):
            circle_image = cv2.circle(circle_image, (left_side_arr[index],
                                                        row_arr[index]),
                                                        10, outline_color, 2)
            circle_image = cv2.circle(circle_image, (right_side_arr[index],
                                                        row_arr[index]),
                                                        10, outline_color, 2)
        
            xy_left_arr.append([left_side_arr[index], row_arr[index]])
            xy_right_arr.append([right_side_arr[index], row_arr[index]])
            
        xy_left_arr= np.asarray(xy_left_arr, dtype=np.int32)
        [vx,vy,x,y] = cv2.fitLine(xy_left_arr, cv2.DIST_L12,0,0.01,0.01)
        left_line_fit_details = [vx,vy,x,y]
        
        rows,cols,channels = circle_image.shape
        
        left_mid_point_y = int((row_arr[0]+row_arr[len(row_arr)-1])/2)
        left_mid_point_x = int(((left_mid_point_y-y)*vx/vy)+x)

        topx = int((-y*vx/vy) + x)
        bottomx = int(((rows-y)*vx/vy)+x)
        
        circle_image = cv2.circle(circle_image, (left_mid_point_x,
                                                    left_mid_point_y),
                                                    25, outline_color, 2)
        circle_image = cv2.line(circle_image,(topx, 0),(bottomx,
                                                        rows-1),outline_color,2)
        left_line = [[topx, 0],[bottomx,rows-1]]
        
        xy_right_arr= np.asarray(xy_right_arr, dtype=np.int32)
        [vx,vy,x,y] = cv2.fitLine(xy_right_arr, cv2.DIST_L12,
                                    0, 0.01, 0.01)
        right_line_fit_details = [vx,vy,x,y]
        
        right_mid_point_y = int((row_arr[0]+row_arr[len(row_arr)-1])/2)
        right_mid_point_x = int(((right_mid_point_y-y)*vx/vy)+x)
        
        topx = int((-y*vx/vy) + x)
        bottomx = int(((rows-y)*vx/vy)+x)
        
        circle_image = cv2.circle(circle_image, (right_mid_point_x,
                                                    right_mid_point_y),
                                                    25, outline_color, 2)
        circle_image = cv2.line(circle_image,(topx, 0),(bottomx,rows-1),
                                outline_color,2)
        right_line = [[topx, 0],[bottomx,rows-1]]

        centre_point_x = int((right_mid_point_x + left_mid_point_x)/2)
        centre_point_y = int((right_mid_point_y + left_mid_point_y)/2)

        # cv2.imshow("circle_image", circle_image)
        # cv2.waitKey(0)
        # self.show_image(circle_image, "circle")
        # circle_image = cv2.line(circle_image, (centre_point_x, 0), (centre_point_x,crop_h),
        #                      centre_color, 2)
        return  circle_image, left_line, right_line, centre_point_x
# |----------------------End of fit_line_vertical---------------------------|

# |----------------------------------------------------------------------------|
# find_intersection
# |----------------------------------------------------------------------------|
    def find_intersection(self, line_1, line_2):
        D  = line_1[0] * line_2[1] - line_1[1] * line_2[0]
        Dx = line_1[2] * line_2[1] - line_1[1] * line_2[2]
        Dy = line_1[0] * line_2[2] - line_1[2] * line_2[0]
        if D != 0:
            x = int(Dx / D)
            y = int(Dy / D)
            return x,y
        else:
            return False
# |----------------------End of find_intersection---------------------------|

# |----------------------------------------------------------------------------|
# get_line_parameters
# |----------------------------------------------------------------------------|
    def get_line_parameters(self, point_1, point_2):
        A = (point_1[1] - point_2[1])
        B = (point_2[0] - point_1[0])
        C = (point_1[0]*point_2[1] - point_2[0]*point_1[1])
        return A, B, -C
# |----------------------End of get_line_parameters---------------------------|

# |----------------------------------------------------------------------------|
# pick_basket_detection
# |----------------------------------------------------------------------------|
    def drop_basket_detection(self, image, crop_coords, minContourArea, step):
        crop_image = image[crop_coords[1]:crop_coords[1]+crop_coords[3],
        crop_coords[0]:crop_coords[0]+crop_coords[2]]
        gray_image = cv2.cvtColor(crop_image, cv2.COLOR_BGR2GRAY)
        misc, threshOut = cv2.threshold(gray_image, 100, 255, cv2.THRESH_BINARY)
        noiseRemovedImage = self.removeNoise(threshOut, minContourArea)
        # cv2.imshow("noise", noiseRemovedImage)
        # cv2.waitKey(0)
        # cv2.imwrite("/home/adminspin/Desktop/noise.bmp", noiseRemovedImage)
        final_basket_edges = []
        loop_condition = 0
        while loop_condition < crop_coords[2]:
            print("entered loop")
            basket_edges = self.drop_basket_profiler(noiseRemovedImage, 127,
            loop_condition)
            if len(basket_edges) > 0:
                print("drop_gap", basket_edges[1]-basket_edges[0])
                if 150 < (basket_edges[1]-basket_edges[0]) < 250:
                    final_basket_edges.append(basket_edges)
                    print("basket_edge:", basket_edges)
                    loop_condition = basket_edges[1] + 25
                    print("loop_condition:", loop_condition)
                else:
                    break
            else:
                break
        return final_basket_edges
# |---------------------- End of pick_basket_detection ---------------------------|

# |----------------------------------------------------------------------------|
# drop_basket_profiler
# |----------------------------------------------------------------------------|
    def drop_basket_profiler(self, image, row, start_range):
        height, width = image.shape
        marker_arr = []
        for i in range(start_range, width):
            # print("start_range", start_range)
            if image[row][i] > 0:
                marker_arr.append(i)
                print("1st edge:", i)
                break
        if len(marker_arr) > 0:
            start = marker_arr[0]+200+25
            if start > width:
                start = width-1
            for i in range(start, start_range, -1):
                if image[row][i] > 0:
                    marker_arr.append(i)
                    print("2nd edge:", i)
                    break
        return marker_arr
# |---------------------- drop_basket_profiler ---------------------------|

# |----------------------------------------------------------------------------|
# detect_slide_angle
# |----------------------------------------------------------------------------|
    def detect_slide_angle(self, top_line_details):
        diff_x = top_line_details[0]
        diff_y = top_line_details[1]
        dividend = diff_y/diff_x
        
        slide_angle = math.degrees(math.atan(dividend))
        return slide_angle
# |---------------------- detect_slide_angle ---------------------------|

# |----------------------------------------------------------------------------|
# pick_basket_detection
# |----------------------------------------------------------------------------|
    def pick_basket_detection(self, image, crop_coords, minContourArea, step,
    threshold=200):
        basket_angle = -360
        crop_image = image[crop_coords[1]:crop_coords[1]+crop_coords[3],
        crop_coords[0]:crop_coords[0]+crop_coords[2]]
        gray_image = cv2.cvtColor(crop_image, cv2.COLOR_BGR2GRAY)
        gray_image = 255-gray_image
        misc, threshOut = cv2.threshold(gray_image, threshold,
                                            255, cv2.THRESH_BINARY)
        noiseRemovedImage = self.removeNoise(threshOut, minContourArea)
        # cv2.imshow("noise", noiseRemovedImage)
        # cv2.waitKey(0)
        top_edge = []
        bottom_edge = []
        column_arr = []
        left_edge = []
        right_edge = []
        row_arr = []
        fit_line_vertical_status = False
        fit_line_horizontal_status = False
        width_arr = []
        circle_image = crop_image.copy()
        for attempt in range(0, crop_coords[2], step):
            basket_top_edge, basket_bottom_edge, circle_image, width = self.vertical_ray_profiler(
                threshOut, attempt, circle_image)
            if basket_top_edge and basket_bottom_edge:
                top_edge.append(basket_top_edge)
                bottom_edge.append(basket_bottom_edge)
                column_arr.append(attempt)
                width_arr.append(width)
        if len(top_edge) > 10:
            fit_line_horizontal_status = True
            circle_image, top_line, bottom_line, centre_point_x, top_line_details, bottom_line_details = \
                self.fit_line_horizontal(
                    len(top_edge), circle_image, top_edge, bottom_edge, column_arr, (0,0,255), (255,100,100))
            basket_angle = self.detect_slide_angle(top_line_details)
        
        for attempt in range(0, crop_coords[3], step):
            basket_left_edge, basket_right_edge, circle_image = self.horizontal_ray_profiler(
                threshOut, attempt, circle_image)
            if basket_left_edge and basket_right_edge:
                left_edge.append(basket_left_edge)
                right_edge.append(basket_right_edge)
                row_arr.append(attempt)
        if len(left_edge) > 10:
            fit_line_vertical_status = True
            circle_image, left_line, right_line, centre_point_x = self.fit_line_vertical(
                len(left_edge), circle_image, left_edge, right_edge, row_arr, (0,0,255), (255,100,100))
        # self.showImage(circle_image, "image")
        # cv2.waitKey(0)

        if fit_line_horizontal_status and fit_line_vertical_status:
            top_line_coords = self.get_line_parameters(top_line[0], top_line[1])
            bottom_line_coords = self.get_line_parameters(bottom_line[0], bottom_line[1])
            left_line_coords = self.get_line_parameters(left_line[0], left_line[1])
            right_line_coords = self.get_line_parameters(right_line[0], right_line[1])

            left_top = self.find_intersection(left_line_coords, top_line_coords)
            right_top = self.find_intersection(right_line_coords, top_line_coords)
            left_bottom = self.find_intersection(left_line_coords, bottom_line_coords)
            right_bottom = self.find_intersection(right_line_coords, bottom_line_coords)

            left_height = left_bottom[1]-left_top[1]
            right_height = right_bottom[1]-right_top[1]
            top_width = right_top[0] - left_top[0]
            bottom_width = right_bottom[0] - left_bottom[0]

            left_top_x = crop_coords[0] + left_top[0]
            left_top_y = crop_coords[1] + left_top[1]

            left_bottom_x = crop_coords[0] + left_bottom[0]
            left_bottom_y = left_top_y + left_height

            right_top_x = left_top_x + top_width
            right_top_y = crop_coords[1] + right_top[1]

            right_bottom_x = left_bottom_x + bottom_width
            right_bottom_y = right_top_y + right_height

            left_top = (left_top_x, left_top_y)
            left_bottom = (left_bottom_x, left_bottom_y)
            right_top = (right_top_x, right_top_y)
            right_bottom = (right_bottom_x, right_bottom_y)
            return left_top, right_top, left_bottom, right_bottom, basket_angle
        else:
            return None, None, None, None, basket_angle
# |---------------------- End of pick_basket_detection ---------------------------|

# |----------------------------------------------------------------------------|
# cross_hair_profiler
# |----------------------------------------------------------------------------|
    def cross_hair_profiler(self, image, row, width):
        status = False
        count = 0
        for i in range(0, width):
            print("cross", image[row][i], i)
            if image[row][i] < 75:
                status = True
            if status:
                count += 1
            if status and image[row][i] > 75:
                break
        return count
# |---------------------- End of cross_hair_profiler ---------------------------|

# |----------------------------------------------------------------------------|
# drop_basket_slide_detection
# |----------------------------------------------------------------------------|
    def drop_basket_slide_detection(self, image, crop_coords, cross_hair_crop, step):
        crop_image = image[crop_coords[1]:crop_coords[1]+crop_coords[3],
        crop_coords[0]:crop_coords[0]+crop_coords[2]]
        crop_image = crop_image[cross_hair_crop[1]:cross_hair_crop[1]+cross_hair_crop[3],
        cross_hair_crop[0]:cross_hair_crop[0]+cross_hair_crop[2]]
        gray_image = cv2.cvtColor(crop_image, cv2.COLOR_BGR2GRAY)
        # self.showImage(gray_image, "cross")
        count = []
        for i in range(cross_hair_crop[3]-1, 0, -step):
            # circle_image = cv2.line(gray_image, (0, i), (cross_hair_crop[2],i),
            #                                     (0,255,0), 1)
            result_count = self.cross_hair_profiler(gray_image,
            i, cross_hair_crop[2])
            print("result: ", result_count)
            if 5 < result_count < 15:
                count.append(result_count)
        print(count)
        if len(count) < 4:
            return False
        else:
            return True
# |------------------End of drop_basket_slide_detection ----------------------|

# |----------------------------------------------------------------------------|
# pick_basket_detection
# |----------------------------------------------------------------------------|
    def basket_detection_pipeline(self, image, station_num, basket_type, crop_coords,
    comparison_values, cross_hair_coords, min_area=2500,step=25):
        # Basket1
        try:
            if basket_type == 0:
                # crop_coords = [278, 1188, 1164, 694]
                left_top, right_top, left_bottom, right_bottom, basket_angle = self.pick_basket_detection(image, crop_coords, min_area, step,)
                circle_image = image.copy()
                if left_top and right_bottom and left_bottom and right_bottom:
                    left_width = left_bottom[1] - left_top[1]
                    right_width = right_bottom[1] - right_top[1]
                    print(left_width, right_width, "width")
                    print("entered")
                    circle_image = cv2.line(circle_image, left_top, right_top,
                                            (0,255,0), 5)
                    circle_image = cv2.line(circle_image, right_top, right_bottom,
                                            (0,255,0), 5)
                    circle_image = cv2.line(circle_image, right_bottom, left_bottom,
                                            (0,255,0), 5)
                    circle_image = cv2.line(circle_image, left_bottom, left_top,
                                            (0,255,0), 5)
                    cv2.putText(circle_image, f"Basket:{station_num} present",
                                    (crop_coords[0]+int(crop_coords[2]/3),int(crop_coords[3]/2)),
                                    cv2.FONT_HERSHEY_SIMPLEX, 
                                    3, (0,0,0), 5, cv2.LINE_AA)
                    cv2.putText(circle_image, f"Basket Angle:{round(basket_angle, 3)}deg",
                                    (crop_coords[0]+int(crop_coords[2]/3),int(crop_coords[3]/2)+200),
                                    cv2.FONT_HERSHEY_SIMPLEX, 
                                    2, (0,0,0), 3, cv2.LINE_AA)
                    cv2.putText(circle_image, f"(x: {left_top[0]}, y:{left_top[1]})",
                                    left_top, cv2.FONT_HERSHEY_SIMPLEX, 
                                0.6, (255, 0, 0), 1, cv2.LINE_AA)
                    cv2.putText(circle_image, f"(x: {right_top[0]}, y:{right_top[1]})",
                                    right_top, cv2.FONT_HERSHEY_SIMPLEX, 
                                0.6, (255, 0, 0), 1, cv2.LINE_AA)
                    cv2.putText(circle_image, f"(x: {left_bottom[0]}, y:{left_bottom[1]})",
                                    left_bottom, cv2.FONT_HERSHEY_SIMPLEX, 
                                0.6, (255, 0, 0), 1, cv2.LINE_AA)
                    cv2.putText(circle_image, f"(x: {right_bottom[0]}, y:{right_bottom[1]})",
                                    right_bottom, cv2.FONT_HERSHEY_SIMPLEX, 
                                0.6, (255, 0, 0), 1, cv2.LINE_AA)
                    if abs(right_width-left_width) > 20:
                        if left_width > right_width:
                            msg = "Left side not placed properly"
                            circle_image = cv2.line(circle_image, left_bottom, left_top,
                                            (0,0,255), 5)
                        else:
                            msg = "right side not placed properly"
                            circle_image = cv2.line(circle_image, right_bottom, right_top,
                                            (0,0,255), 5)
                        cv2.putText(circle_image, f"{msg}",
                                    (crop_coords[0]+int(crop_coords[2]/3),int(crop_coords[3]/2)+400),
                                    cv2.FONT_HERSHEY_SIMPLEX, 
                                    1.5, (0, 0, 255), 2, cv2.LINE_AA)
                                    
                else:
                    print("entered")
                    cv2.putText(circle_image, f"Basket not placed properly",
                                    (crop_coords[0]+int(crop_coords[2]/3),int(crop_coords[3]/2)),
                                    cv2.FONT_HERSHEY_SIMPLEX, 
                                    2, (0,0,255), 5, cv2.LINE_AA)
            # drop basket
            if basket_type == 1:
                height, width, channels = image.shape
                circle_image = image.copy()
                # crop_coords = [636, 102, 1526, 248]
                final_basket_coords = self.drop_basket_detection(image, crop_coords, min_area, step)
                length = len(final_basket_coords)
                print("final_basket_coords", final_basket_coords)
                drop_bask_status = [False, False, False, False]
                if length == 4:
                    pos_x = int((final_basket_coords[0][0]+ final_basket_coords[length-1][0])/2)
                    circle_image = cv2.putText(circle_image, "All drop baskets are proper",
                                    (pos_x,crop_coords[3]), cv2.FONT_HERSHEY_SIMPLEX, 
                                0.6, (0,255,0), 2, cv2.LINE_AA)
                elif length == 0:
                    circle_image = cv2.putText(circle_image, "None of the baskets are present",
                    (crop_coords[0]+comparison_values[0][1], crop_coords[3]),
                    cv2.FONT_HERSHEY_SIMPLEX, 1.5, (0,0,255), 2, cv2.LINE_AA)
                else:
                    for i in range(0, length):
                        for j in range(0,4):
                            if comparison_values[j][0] < final_basket_coords[i][0] < comparison_values[j][1]:
                                drop_bask_status[j] = True
                    print(drop_bask_status)
                    for num, status in enumerate(drop_bask_status):
                        if status:
                            slide_status = self.drop_basket_slide_detection(
                                image, crop_coords, cross_hair_coords[num], step=10)
                            circle_image = cv2.putText(circle_image, f"basket {num+1} Present",
                                        (crop_coords[0]+comparison_values[num][1], crop_coords[3]),
                                        cv2.FONT_HERSHEY_SIMPLEX,
                                        0.6, (0,255,0), 2, cv2.LINE_AA)
                            if not slide_status:
                                circle_image = cv2.putText(circle_image, f"basket not empty",
                                        (crop_coords[0]+comparison_values[num][1], height-200),
                                        cv2.FONT_HERSHEY_SIMPLEX,
                                        0.6, (0,0,255), 2, cv2.LINE_AA)
                        else:
                            circle_image = cv2.putText(circle_image, f"basket {num+1} not present",
                                        (crop_coords[0]+comparison_values[num][1], crop_coords[3]),
                                        cv2.FONT_HERSHEY_SIMPLEX,
                                        0.6, (0,0,255), 2, cv2.LINE_AA)
            return circle_image
        except Exception as msg:
            print("exception occurred:", msg)
            return image

if __name__ == '__main__':
    image = cv2.imread("/home/adminspin/Music/revolutionary_ideas/cluster_setup_automation/gripper_camera/drop_basket_input_images/drop_basket_set10.jpg")
    detect_basket = BasketDetector()
    # pick basket detection params
    # crop_coords = [128, 70, 1656, 952]
    # drop basket detection params
    crop_coords = [480, 854, 990, 148]
    crop_coords_cross_hair = [[132, 0, 50, 99],[375, 0, 50, 99],[620, 0, 50, 99],[865, 0, 50, 99]]
    comparison_values = [[0,100],[250,350],[450,550],[700,800]]
    basket_type=1
    station_num=1
    step = 10
    circle_image = detect_basket.basket_detection_pipeline(image, station_num, basket_type, crop_coords,
    comparison_values, crop_coords_cross_hair)
    # detect_basket.drop_basket_slide_detection(image, crop_coords, crop_coords_cross_hair, step)
    print("he")
    cv2.namedWindow("circle_image", cv2.WINDOW_NORMAL)
    cv2.resizeWindow("circle_image", 600, 600)
    cv2.imshow("circle_image", circle_image)
    cv2.waitKey(0)