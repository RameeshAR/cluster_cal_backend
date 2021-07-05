from lxml import etree
from os.path import exists

class pick_basket:
    def xml_value():
    try:
        FilePath = "/home/adminspin/Downloads/slide_pick_basket.xml"
        File = etree.parse(FilePath)
        rootTag  = File.getroot()
        print("\nBasket Dimensions")
        for stags in rootTag.iter("basket_dimensions"):
            for subTag in stags:
                if subTag.tag == "height":
                    print("height : ", subTag.attrib['value'])
                elif subTag.tag == "width":
                    print("width : ", subTag.attrib['value'])
                elif subTag.tag == "length":
                    print("length : ", subTag.attrib['value'])
                elif subTag.tag == "column_distance":
                    print("column_distance : ", subTag.attrib['value'])
                elif subTag.tag == "row_distance":
                    print("row_distance : ", subTag.attrib['value'])
                elif subTag.tag == "max_row_count":
                    print("max_row_count : ", subTag.attrib['value'])
                elif subTag.tag == "max_col_count":
                    print("max_col_count : ", subTag.attrib['value'])
        print("\nRobot Movement Parameters -")
        for arm in rootTag.iter("robot_movement_parameters"):
            for subTag in arm:
                if subTag.tag == "time_out":
                    print("time_out : ", subTag.attrib['value'])
                elif subTag.tag == "velocity":
                    print("velocity:: ", subTag.attrib['value'])
                elif subTag.tag == "rx":
                    print("Rx : ", subTag.attrib['value'])
                elif subTag.tag == "velocity":
                    print("velocity:: ", subTag.attrib['value'])
                elif subTag.tag == "ry":
                    print("ry : ", subTag.attrib['value'])
                elif subTag.tag == "velocity":
                    print("velocity : ", subTag.attrib['value'])
                elif subTag.tag == "Rx":
                    print("Rx : ", subTag.attrib['value'])
                elif subTag.tag == "rz":
                    print("rz : ", subTag.attrib['value'])
                elif subTag.tag == "movement_type":
                    print("movement_type : ", subTag.attrib['value'])
                elif subTag.tag == "force":
                    print("force : ", subTag.attrib['value'])
                elif subTag.tag == "z_pick_speed":
                    print("z_pick_speed : ", subTag.attrib['value'])
                elif subTag.tag == "z_place_speed":
                    print("z_place_speed : ", subTag.attrib['value'])
                elif subTag.tag == "z_place_pos":
                    print("z_place_pos : ", subTag.attrib['value'])
                elif subTag.tag == "row_direction":
                    print("row_direction : ", subTag.attrib['value'])
                elif subTag.tag == "column_direction":
                    print("column_direction : ", subTag.attrib['value'])
                elif subTag.tag == "gripper_width":
                    print("gripper_width : ", subTag.attrib['value'])
                elif subTag.tag == "gripper_jaw_thickness":
                    print("gripper_jaw_thickness : ", subTag.attrib['value'])
                elif subTag.tag == "column_slot_distance":
                    print("column_slot_distance : ", subTag.attrib['value'])
                elif subTag.tag == "z_offset_distance":
                    print("z_offset_distance : ", subTag.attrib['value'])
                elif subTag.tag == "row_division_distance":
                    print("row_division_distance : ", subTag.attrib['value'])
        var = basket_dimensions.find("height").attrib["value"]
        print(var)
    except Exception as msg:
        print("Exception "" ERROR 404 " + str(msg))
        return False

pick_basket.xml_value()
