import pandas as pd
import os

from XMLTemplates.scanner_input import scanner

class sf_Calibration:
    def get_fiducial_coords(self, sf_fiducial):
        point_1 = sf_fiducial.split(",")
        point_1 = list(map(float, point_1))
        return point_1

    def read_csv(self, file_path):
        return pd.read_csv(file_path)
    
    #modify this based on 
    def calculate_sf_values(self, sf_details, folder_path,dest_path, sf_fiducial):
        try:
            sf_fiducial = self.get_fiducial_coords(sf_fiducial)
            print(type(sf_fiducial[1]), type(sf_details["basket_width"]))
            calc_py = sf_fiducial[1] - (gripper_width/2) + (sf_details["basket_width"]/2) - \
                sf_details["wall_thickness"]
            calc_px = sf_fiducial[0] + ((sf_details["basket_depth"] - std_slide_height)/2)
            calc_pz = sf_fiducial[2] -  sf_details["z_offset"]
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
                data_frame_drop1_sx.loc[2:, "RX"] = drop.arm("rx")
                data_frame_drop1_sx.loc[2:, "RY"] = drop.arm("ry")
                data_frame_drop1_sx.loc[2:, "RZ"] = drop.arm("rz")
                data_frame_drop2_sx = [data_frame_drop1_sx.loc[[2]], drop2_sx_data]
                data_frame_drop2_sx = pd.concat(data_frame_drop2_sx, ignore_index=True)
                data_frame_drop2_sx.loc[0, "PZ"] = (sf_fiducial[2] - (sf_details["basket_height"]/2))/1000
                data_frame_drop2_sx.loc[0, "RX"] = drop.arm("rx")
                data_frame_drop2_sx.loc[0, "RY"] = drop.arm("ry")
                data_frame_drop2_sx.loc[0, "RZ"] = drop.arm("rz")
                data_frame_drop1_sx.to_csv(dest_path+f"/drop1_s{basket_num+1}.csv", index=False)
                data_frame_drop2_sx.to_csv(dest_path+f"/drop2_s{basket_num+1}.csv", index=False)
                calc_py = calc_py + sf_details["basket_gap"] + sf_details["basket_width"]
            return True, "Calibration successful"
        except Exception as msg:
            return False, msg