import pandas as pd
import os

class DropBasketCalibration:

    def get_fiducial_coords(self):
        point_1 = []
        point_2 = []

        point_1.append(float(input("Enter Px of point 1: ")))
        point_1.append(float(input("Enter Py of point 1: ")))
        point_1.append(float(input("Enter Pz of point 1: ")))
        point_1.append(float(input("Enter Rx of point 1: ")))
        point_1.append(float(input("Enter Ry of point 1: ")))
        point_1.append(float(input("Enter Rz of point 1: ")))
        
        point_2.append(float(input("Enter Px of point 2: ")))
        point_2.append(float(input("Enter Py of point 2: ")))
        point_2.append(float(input("Enter Pz of point 2: ")))
        point_2.append(float(input("Enter Rx of point 2: ")))
        point_2.append(float(input("Enter Ry of point 2: ")))
        point_2.append(float(input("Enter Rz of point 2: ")))
        return point_1, point_2

    def read_csv(self, file_path):
        return pd.read_csv(file_path)

    def calculate_cal_values(self, drop_basket_details, file_path,
                            gripper_width, gripper_jaw_thickness,
                            std_slide_height, dest_path):
        fiducial_1, fiducial_2 = self.get_fiducial_coords()
        print(type(fiducial_1[1]), type(drop_basket_details["basket_width"]))
        calc_py = fiducial_1[1] + (gripper_width/2) - (drop_basket_details["basket_width"]/2)
        calc_px = fiducial_1[0] + ((drop_basket_details["basket_depth"] - std_slide_height)/2) +\
                  std_slide_height
        calc_pz = fiducial_1[2] -  drop_basket_details["z_offset"]
        for basket_num in range(0, 4):
            mov2_sx_data = self.read_csv(file_path+f"mov2_s{basket_num+1}_out.csv").loc[[0,1]]
            drop1_sx_data = self.read_csv(file_path+f"drop1_s{basket_num+1}.csv").loc[[2]]
            drop2_sx_data = self.read_csv(file_path+f"drop2_s{basket_num+1}.csv").loc[[1,2]]
            data_frame_drop1_sx = [mov2_sx_data, drop1_sx_data, drop1_sx_data]
            data_frame_drop1_sx = pd.concat(data_frame_drop1_sx, ignore_index=True)
            data_frame_drop1_sx.loc[2, "PY"] = calc_py
            data_frame_drop1_sx.loc[3, "PY"] = calc_py
            data_frame_drop1_sx.loc[3, "PX"] = calc_px
            data_frame_drop1_sx.loc[3, "PZ"] = calc_pz
            data_frame_drop2_sx = [data_frame_drop1_sx.loc[[2]], drop2_sx_data]
            data_frame_drop2_sx = pd.concat(data_frame_drop2_sx, ignore_index=True)
            data_frame_drop2_sx.loc[0, "PZ"] = fiducial_1[2] - (drop_basket_details["basket_height"]/2)
            print()
            data_frame_drop1_sx.to_csv(dest_path+f"/drop1_s{basket_num+1}.csv", index=False)
            data_frame_drop2_sx.to_csv(dest_path+f"/drop2_s{basket_num+1}.csv", index=False)


hell = DropBasketCalibration()
drop_basket_details = {}
drop_basket_details["basket_width"] = 48
drop_basket_details["basket_depth"] = 83.5
drop_basket_details["z_offset"] = 10
drop_basket_details["basket_height"] = 225
dest_path = "/home/adminspin/Desktop"
hell.calculate_cal_values(drop_basket_details, "/home/adminspin/Desktop/ur3/UR3e_28_06_21/",7,1.5,75,dest_path)