import pandas as pd
import numpy as np

class PickBasketCal:


    def get_input_pose(self, fiducial_1, fiducial_2, fiducial_3, fiducial_4):
        print(fiducial_1, fiducial_2, fiducial_3, fiducial_4)
        point_1 = fiducial_1.split(",")
        point_2 = fiducial_2.split(",")
        point_3 = fiducial_3.split(",")
        point_4 = fiducial_4.split(",")
        return point_1, point_2, point_3, point_4
    
    def calc_cal_outcomes(self, basket_num, folder_path, robot_movement_params, dest_path,
    basket_dimensions, fiducial_1, fiducial_2, fiducial_3, fiducial_4):
        print("entered")
        try:
            fiducial_1, fiducial_2, fiducial_3, fiducial_4 = self.get_input_pose(
                fiducial_1, fiducial_2, fiducial_3, fiducial_4)
            dataframe_basket_set = self.read_csv(folder_path+"/BasketSett.csv")
            
            #bref calculations
            dataframe_basket_ref = self.read_csv(folder_path+"/bref.csv")
            print(dataframe_basket_ref)
            dataframe_basket_ref.loc[basket_num-1, "PX"] = ((fiducial_1[0] - \
                (robot_movement_params["gripper_width"]/2)) +\
                    (basket_dimensions["row_distance"]/2))/1000
            dataframe_basket_ref.loc[basket_num-1, "PY"] = ((fiducial_1[1] + \
                robot_movement_params["gripper_jaw_thickness"]) - \
                    basket_dimensions["column_distance"])/1000
            dataframe_basket_ref.loc[basket_num-1, "PZ"] = (fiducial_1[2] + \
                robot_movement_params["z_offset_distance"])/1000
            dataframe_basket_ref.loc[basket_num-1, "RX"] = robot_movement_params["rx"]
            dataframe_basket_ref.loc[basket_num-1, "RY"] = robot_movement_params["ry"]
            dataframe_basket_ref.loc[basket_num-1, "RZ"] = robot_movement_params["rz"]
            dataframe_basket_ref.loc[basket_num-1, "V"] = robot_movement_params["velocity"]
            dataframe_basket_ref.loc[basket_num-1, "TO"] = robot_movement_params["time_out"]
            dataframe_basket_ref.loc[basket_num-1, "MOVELJ"] = robot_movement_params["movement_type"]
            dataframe_basket_ref.loc[basket_num-1, "FORCE"] = robot_movement_params["force"]
            dataframe_basket_ref.to_csv(dest_path+f"bref.csv", index=False)

            # basketsett calculations
            px1 = (fiducial_1[0] - (robot_movement_params["gripper_width"] / 2))
            py1 = (fiducial_1[1] + robot_movement_params["gripper_jaw_thickness"])
            pz1 = fiducial_1[2]

            px2 = (fiducial_2[0] + (robot_movement_params["gripper_width"] / 2))
            py2 = (fiducial_2[1] + robot_movement_params["gripper_jaw_thickness"])
            pz2 = fiducial_2[2]

            px3 = (fiducial_3[0] + (robot_movement_params["gripper_width"] / 2))
            py3 = (fiducial_3[1] - robot_movement_params["gripper_jaw_thickness"])
            pz3 = fiducial_3[2]

            px4 = (fiducial_4[0] - (robot_movement_params["gripper_width"] / 2))
            py4 = (fiducial_4[1] - robot_movement_params["gripper_jaw_thickness"])
            pz4 = fiducial_4[2]

            dataframe_basket_set = self.read_csv(folder_path+"/BasketSett.csv")
            dataframe_basket_set.loc[basket_num-1, "Max Rows"] = basket_dimensions["max_row_count"]
            dataframe_basket_set.loc[basket_num-1, "Max Cols"] = basket_dimensions["max_column_count"]
            dataframe_basket_set.loc[basket_num-1, "Row Dist"] = basket_dimensions["row_distance"]/1000
            dataframe_basket_set.loc[basket_num-1, "Col Dist"] = basket_dimensions["column_distance"]/1000
            dataframe_basket_set.loc[basket_num-1, "Z Pick Speed"] = robot_movement_params["z_pick_speed"]
            dataframe_basket_set.loc[basket_num-1, "Z Place Speed"] = robot_movement_params["z_place_speed"]
            dataframe_basket_set.loc[basket_num-1, "Z Pick Pos"] = -robot_movement_params["z_offset_distance"]
            dataframe_basket_set.loc[basket_num-1, "Z Place Pos"] = robot_movement_params["z_place_pos"]
            dataframe_basket_set.loc[basket_num-1, "Row Dir"] = robot_movement_params["row_direction"]
            dataframe_basket_set.loc[basket_num-1, "Col Dir"] = robot_movement_params["column_direction"]
            dataframe_basket_set.loc[basket_num-1, "Row Offset"] = (((py2 - py1) / basket_dimensions["width"])\
                * basket_dimensions["row_distance"])/1000
            dataframe_basket_set.loc[basket_num-1, "Col Offset"] = (((px4 - px1) / basket_dimensions["length"])\
                * basket_dimensions["column_distance"])/1000
            dataframe_basket_set.loc[basket_num-1, "Z Pick Offset Col"] = (((pz4-pz1) / basket_dimensions["length"])\
                * basket_dimensions["column_distance"])/1000
            dataframe_basket_set.loc[basket_num-1, "Z Place Offset Col"] = 0/1000
            dataframe_basket_set.loc[basket_num-1, "Z Pick Offset Row"] = (((pz2 - pz1) / basket_dimensions["width"])\
                * basket_dimensions["row_distance"])/1000
            dataframe_basket_set.loc[basket_num-1, "Z Place Offset Row"] = 0/1000

            dataframe_basket_ref.to_csv(dest_path+"bref.csv", index=False)
            dataframe_basket_set.to_csv(dest_path+"BasketSett.csv", index=False)
            return True, "Calibration successful"
        except Exception as msg:
            print(msg)
            return False, msg
    def read_csv(self, file_path):
        return pd.read_csv(file_path)

#test case

if __name__ == '__main__':
    basket_cal = PickBasketCal()
    basket_num = 1
    folder_path = "/home/adminspin/Desktop/ur3/UR3e_28_06_21"

    robot_movement_params = {}
    robot_movement_params["rx"] = 3.148
    robot_movement_params["ry"] = 0
    robot_movement_params["rz"] = 0
    robot_movement_params["velocity"] = 1
    robot_movement_params["time_out"] = 15
    robot_movement_params["movement_type"] = 1
    robot_movement_params["force"] = 1
    robot_movement_params["gripper_width"] = 7
    robot_movement_params["gripper_jaw_thickness"] = 1.5
    robot_movement_params["z_pick_speed"] = 0.5
    robot_movement_params["z_place_speed"] = 0.5
    robot_movement_params["z_offset_distance"] = 103
    robot_movement_params["z_place_pos"] = 0
    robot_movement_params["row_direction"] = 1
    robot_movement_params["column_direction"]= 0

    dest_path = "/home/adminspin/Desktop/ur3/semi_automatic_calibration/"

    basket_dimensions = {}
    basket_dimensions["max_row_count"] = 3
    basket_dimensions["max_column_count"] = 29
    basket_dimensions["row_distance"] = 30
    basket_dimensions["column_distance"] = 7
    basket_dimensions["length"] = 222
    basket_dimensions["width"] = 124
    basket_dimensions["height"] = 72.64

    basket_cal.calc_cal_outcomes(basket_num, folder_path, robot_movement_params, dest_path, basket_dimensions)

