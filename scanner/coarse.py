import pandas as pd
import os

from XMLTemplates.scanner_input import scanner

class sc_Calibration:
    def get_fiducial_coords(self, sc_fiducial):
        point_1 = sc_fiducial.split(",")
        point_1 = list(map(float, point_1))
        return point_1

    def read_csv(self, file_path):
        return pd.read_csv(file_path)
    
    #modify this based on 
    def calculate_sc_values(self, sc_details, file_path,dest_path, sc_fiducial):
        try:
            sc_fiducial = self.get_fiducial_coords(sc_fiducial )
            print(type(sc_fiducial[1]))
            calc_px = sc_fiducial[0]
            calc_py = sc_fiducial[1]
            calc_pz = sc_fiducial[2]
            calc_rx = sc_fiducial[3]
            calc_ry = sc_fiducial[4]
            calc_rz = sc_fiducial[5]
            for basket_num in range(0, 4):
                mov1_sx_data = self.read_csv(file_path+f"/mov1_s{basket_num+1}.csv")
                mov2_sx_data = self.read_csv(file_path+f"/mov2_s{basket_num+1}.csv")
                mov2_sx_home = self.read_csv(file_path+f"/mov2_s{basket_num+1}_home.csv")
                mov2_sx_out = self.read_csv(file_path+f"/mov2_s{basket_num+1}_out.csv")
                drop1_sx_data = self.read_csv(file_path+f"/drop1_s{basket_num+1}.csv")
                #test_mov = pd.DataFrame(columns=['PX','PY','PZ','RX','RY','RZ','V','TO','MOVELJ','FORCE'])
                mov1_sx_data.loc[3, "PX"] = calc_px/1000
                mov1_sx_data.loc[3, "PY"] = calc_py/1000
                mov1_sx_data.loc[3, "PZ"] = calc_pz/1000
                mov1_sx_data.loc[3:, "RX"] = calc_rx
                mov1_sx_data.loc[3:, "RY"] = calc_ry
                mov1_sx_data.loc[3:, "RZ"] = calc_rz
                mov1_sx_data.loc[3:, "V"] = scanner.coarse_input("velocity")
                mov1_sx_data.loc[3:, "TO"] = scanner.coarse_input("time_out")
                mov1_sx_data.loc[3:, "MOVELJ"] = scanner.coarse_input("movement_type")
                mov1_sx_data.loc[3:, "FORCE"] = scanner.coarse_input("force")
                mov1_sx_data.loc[2, "PX"] = calc_px/1000
                mov1_sx_data.loc[2, "PY"] = calc_py/1000
                mov1_sx_data.loc[2:, "RX"] = calc_rx
                mov1_sx_data.loc[2:, "RY"] = calc_ry
                mov1_sx_data.loc[2:, "RZ"] = calc_rz
                mov1_sx_data.loc[2:, "V"] = scanner.coarse_input("velocity")
                mov1_sx_data.loc[2:, "TO"] = scanner.coarse_input("time_out")
                mov1_sx_data.loc[2:, "MOVELJ"] = scanner.coarse_input("movement_type")
                mov1_sx_data.loc[2:, "FORCE"] = scanner.coarse_input("force")
                mov1_sx_data.to_csv(dest_path+f"/mov1_s{basket_num+1}.csv", index=False)
                #_
                mov2_sx_data.loc[0, "PX"] = calc_px/1000
                mov2_sx_data.loc[0, "PY"] = calc_py/1000
                mov2_sx_data.loc[0, "PZ"] = calc_pz/1000
                mov2_sx_data.loc[0:, "RX"] = calc_rx
                mov2_sx_data.loc[0:, "RY"] = calc_ry
                mov2_sx_data.loc[0:, "RZ"] = calc_rz
                mov2_sx_data.loc[0:, "V"] = scanner.coarse_input("velocity")
                mov2_sx_data.loc[0:, "TO"] = scanner.coarse_input("time_out")
                mov2_sx_data.loc[0:, "MOVELJ"] = scanner.coarse_input("movement_type")
                mov2_sx_data.loc[0:, "FORCE"] = scanner.coarse_input("force")

                mov2_sx_data.loc[1, "PX"] = calc_px/1000
                mov2_sx_data.loc[1, "PY"] = calc_py/1000
                mov2_sx_data.loc[1:, "RX"] = calc_rx
                mov2_sx_data.loc[1:, "RY"] = calc_ry
                mov2_sx_data.loc[1:, "RZ"] = calc_rz
                mov2_sx_data.loc[1:, "V"] = scanner.coarse_input("velocity")
                mov2_sx_data.loc[1:, "TO"] = scanner.coarse_input("time_out")
                mov2_sx_data.loc[1:, "MOVELJ"] = scanner.coarse_input("movement_type")
                mov2_sx_data.loc[1:, "FORCE"] = scanner.coarse_input("force")

                mov2_sx_data.to_csv(dest_path+f"/mov2_s{basket_num+1}.csv", index=False)

                mov2_sx_home = mov2_sx_data.iloc[[-1]]
                mov2_sx_home.to_csv(dest_path+f"/mov2_s{basket_num+1}_home.csv", index=False)

                mov2_sx_out = mov2_sx_data[0:-1]
                mov2_sx_out.to_csv(dest_path+f"/mov2_s{basket_num+1}_out.csv", index=False)

                drop1_sx_data.loc[0, "PX"] = calc_px/1000
                drop1_sx_data.loc[0, "PY"] = calc_py/1000
                drop1_sx_data.loc[0, "PZ"] = calc_pz/1000
                drop1_sx_data.loc[0:, "RX"] = calc_rx
                drop1_sx_data.loc[0:, "RY"] = calc_ry
                drop1_sx_data.loc[0:, "RZ"] = calc_rz
                drop1_sx_data.loc[0:, "V"] = scanner.coarse_input("velocity")
                drop1_sx_data.loc[0:, "TO"] = scanner.coarse_input("time_out")
                drop1_sx_data.loc[0:, "MOVELJ"] = scanner.coarse_input("movement_type")
                drop1_sx_data.loc[0:, "FORCE"] = scanner.coarse_input("force")

                drop1_sx_data.loc[1, "PX"] = calc_px/1000
                drop1_sx_data.loc[1, "PY"] = calc_py/1000
                drop1_sx_data.loc[1:, "RX"] = calc_rx
                drop1_sx_data.loc[1:, "RY"] = calc_ry
                drop1_sx_data.loc[1:, "RZ"] = calc_rz
                drop1_sx_data.loc[1:, "V"] = scanner.coarse_input("velocity")
                drop1_sx_data.loc[1:, "TO"] = scanner.coarse_input("time_out")
                drop1_sx_data.loc[1:, "MOVELJ"] = scanner.coarse_input("movement_type")
                drop1_sx_data.loc[1:, "FORCE"] = scanner.coarse_input("force")
                drop1_sx_data.to_csv(dest_path+f"/drop1_s{basket_num+1}.csv", index=False)
                
            return True, "Calibration successful"
        except Exception as msg:
            return False, msg