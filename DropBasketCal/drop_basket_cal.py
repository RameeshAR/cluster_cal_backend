import pandas as pd
import os

class DropBasketCalibration:

    def get_fiducial_coords(self, fiducial_1, fiducial_2):
        point_1 = fiducial_1.split(",")
        point_2 = fiducial_2.split(",")
        point_1 = list(map(float, point_1))
        point_2 = list(map(float, point_2))
        return point_1, point_2

    def read_csv(self, file_path):
        return pd.read_csv(file_path)

    def calculate_cal_values(self, drop_basket_details, file_path,
                            gripper_width, gripper_jaw_thickness,
                            std_slide_height, dest_path, fiducial_1,
                            fiducial_2):
        try:
            fiducial_1, fiducial_2 = self.get_fiducial_coords(fiducial_1, fiducial_2)
            print(type(fiducial_1[1]), type(drop_basket_details["basket_width"]))
            calc_py = fiducial_1[1] - (gripper_width/2) + (drop_basket_details["basket_width"]/2) - \
                drop_basket_details["wall_thickness"]
            calc_px = fiducial_1[0] + ((drop_basket_details["basket_depth"] - std_slide_height)/2)
            calc_pz = fiducial_1[2] -  drop_basket_details["z_offset"]
            for basket_num in range(0, 4):
                mov2_sx_data = self.read_csv(file_path+f"/mov2_s{basket_num+1}_out.csv").loc[[0,1]]
                drop1_sx_data = self.read_csv(file_path+f"/drop1_s{basket_num+1}.csv").loc[[2]]
                drop2_sx_data = self.read_csv(file_path+f"/drop2_s{basket_num+1}.csv").loc[[1,2]]
                data_frame_drop1_sx = [mov2_sx_data, drop1_sx_data, drop1_sx_data]
                data_frame_drop1_sx = pd.concat(data_frame_drop1_sx, ignore_index=True)
                data_frame_drop1_sx.loc[2, "PY"] = calc_py/1000
                data_frame_drop1_sx.loc[3, "PY"] = calc_py/1000
                data_frame_drop1_sx.loc[3, "PX"] = calc_px/1000
                data_frame_drop1_sx.loc[2, "PZ"] = calc_pz/1000
                data_frame_drop1_sx.loc[3, "PZ"] = calc_pz/1000
                data_frame_drop2_sx = [data_frame_drop1_sx.loc[[2]], drop2_sx_data]
                data_frame_drop2_sx = pd.concat(data_frame_drop2_sx, ignore_index=True)
                data_frame_drop2_sx.loc[0, "PZ"] = (fiducial_1[2] - (drop_basket_details["basket_height"]/2))/1000
                data_frame_drop1_sx.to_csv(dest_path+f"/drop1_s{basket_num+1}.csv", index=False)
                data_frame_drop2_sx.to_csv(dest_path+f"/drop2_s{basket_num+1}.csv", index=False)
                calc_py = calc_py + drop_basket_details["basket_gap"] + drop_basket_details["basket_width"]
            return True, "Calibration successful"
        except Exception as msg:
            return False, msg
# test case

if __name__ == '__main__':
    hell = DropBasketCalibration()
    drop_basket_details = {}
    drop_basket_details["basket_width"] = 48
    drop_basket_details["basket_depth"] = 83.5
    drop_basket_details["z_offset"] = 10
    drop_basket_details["basket_height"] = 225
    drop_basket_details["basket_gap"] = 14
    drop_basket_details["wall_thickness"] = 4
    dest_path = "C:/Users/Robotic Arm/Documents/"
    hell.calculate_cal_values(drop_basket_details, "C:/UR3e/",7,1.5,75,dest_path)