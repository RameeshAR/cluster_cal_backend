from lxml import etree
from os.path import exists

class pick:
    def basket_dims(x):
        try:
            file_obj = etree.parse("/home/adminspin/office/cluster_cal_backend/XMLTemplates/slide_pick_basket.xml")
            root_tag = file_obj.getroot()
            basket_dims = root_tag.find("basket_dimensions")
            if basket_dims.find(x).attrib["type"] == 'float':
                var = float(basket_dims.find(x).attrib["value"])
            elif basket_dims.find(x).attrib["type"] == 'int':
                var = int(basket_dims.find(x).attrib["value"])
            return var
        except Exception as msg:
            print(x+" Given Parameter Empty\n"+ str(msg))
    def arm(x):
        try:  
            file_obj = etree.parse("/home/adminspin/office/cluster_cal_backend/XMLTemplates/slide_pick_basket.xml")
            root_tag = file_obj.getroot()
            arm = root_tag.find("robot_movement_parameters")
            if arm.find(x).attrib["type"] == 'float':
                var = float(arm.find(x).attrib["value"])
            elif arm.find(x).attrib["type"] == 'int':
                var = int(arm.find(x).attrib["value"])
            return var
        except Exception as msg:
            print(x+" Given Parameter Empty\n"+ str(msg))


