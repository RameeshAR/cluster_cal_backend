from lxml import etree
from os.path import exists

class scanner:
    def coarse_input(x):
        try:
            file_obj = etree.parse("XMLTemplates/scanner_input.xml")
            root_tag = file_obj.getroot()
            basket_dims = root_tag.find("coarse_input")
            if basket_dims.find(x).attrib["type"] == 'float':
                var = float(basket_dims.find(x).attrib["value"])
            elif basket_dims.find(x).attrib["type"] == 'int':
                var = int(basket_dims.find(x).attrib["value"])
            return var
        except Exception as msg:
            print(x+" Given Parameter Empty\n"+ str(msg))
    def fine_input(x):
        try:  
            file_obj = etree.parse("XMLTemplates/scanner_input.xml")
            root_tag = file_obj.getroot()
            arm = root_tag.find("fine_input")
            if arm.find(x).attrib["type"] == 'float':
                var = float(arm.find(x).attrib["value"])
            elif arm.find(x).attrib["type"] == 'int':
                var = int(arm.find(x).attrib["value"])
            return var
        except Exception as msg:
            print(x+" Given Parameter Empty\n"+ str(msg))