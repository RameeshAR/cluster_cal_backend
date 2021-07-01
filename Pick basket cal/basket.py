import pandas as pd
import numpy as np

class pick_basket:

    def basket1(point1,point2,point3,point4,rvalue,parameter,rest,path,basket,basket_set):
        
        point1 = list(map(float, point1))
        point2 = list(map(float, point2))
        point3 = list(map(float, point3))
        point4 = list(map(float, point4))
        parameter = list(map(float, parameter))
        basket = list(map(float, basket))
        basket_set = list(map(float, basket_set))

        px = (point1[0] - (parameter[0] / 2)) + parameter[4]
        py = (point1[1] + parameter[1]) - parameter[2]
        pz = point1[2] + parameter[3]
        
        rx = rvalue[0]
        ry = rvalue[1]
        rz = rvalue[2]

        #___
        px1 = (point1[0] - (parameter[0] / 2))
        py1 = (point1[1] + parameter[1])
        pz1 = point1[2]
        #___
        rx1 = rvalue[0]
        ry1 = rvalue[1]
        rz1 = rvalue[2]

        px2 = (point2[0] + (parameter[0] / 2))
        py2 = (point2[1] + parameter[1])
        pz2 = point2[2]
        #___
        rx2 = rvalue[0]
        ry2 = rvalue[1]
        rz2 = rvalue[2]

        px3 = (point3[0] + (parameter[0] / 2))
        py3 = (point3[1] - parameter[1])
        pz3 = point3[2]
        #___
        rx3 = rvalue[0]
        ry3 = rvalue[1]
        rz3 = rvalue[2]

        px4 = (point4[0] - (parameter[0] / 2))
        py4 = (point4[1] - parameter[1])
        pz4 = point4[2]
        #___
        rx4 = rvalue[0]
        ry4 = rvalue[1]
        rz4 = rvalue[2]

        df = pd.DataFrame({'PX':[px],'PY':[py],'PZ':[pz],'RX':[rx],'RY':[ry],'RZ':[rz]})

        df[['PX','PY','PZ']] = df[['PX','PY','PZ']] / 1000 #convert to mts

        df['V'] = rest[0]
        df['TO'] = rest[1]
        df['MOVELJ'] = rest[2]
        df['FORCE'] = rest[3]
        
        print('bref Values :',df[['PX','PY','PZ']])

        col_offset = ((px4 - px1) / basket[0]) * basket[3]
        row_offset = ((py2 - py1) / basket[1]) * basket[4]
        z_pick_offset_col = ((pz4-pz1) / basket[0]) * basket[3]
        z_pick_offset_row = ((pz2 - pz1) / basket[1]) * basket[4]
        
        print('col_offset : ',col_offset)
        print('row_offset : ',row_offset)
        print('z_pick_offset_col :',z_pick_offset_col)
        print('z_pick_offset_row :',z_pick_offset_row)
        
        df2= pd.DataFrame({'Row Offset':[row_offset],'Col Offset':[col_offset],'Z Pick Offset Col':[z_pick_offset_col],'Z Pick Offset Row':[z_pick_offset_row]})

        df2['Max Rows'] = basket_set[0]
        df2['Max Cols'] = basket_set[1]
        df2['Row Dist'] = basket_set[2]
        df2['Col Dist'] = basket_set[3]
        df2['Z Pick Speed'] = basket_set[4]
        df2['Z Place Speed'] = basket_set[5]
        df2['Z Pick Pos'] = basket_set[6]
        df2['Z Place Pos'] = basket_set[7]
        df2['Row Dir'] = basket_set[8]
        df2['Col Dir'] = basket_set[9]
        df2['Z Place Offset Col'] = basket_set[10]
        df2['Z Place Offset Row'] = basket_set[11]

        #print('Before conversion values : ',df2)

        df2[['Row Offset','Col Offset','Z Pick Offset Col','Z Pick Offset Row','Z Pick Pos','Row Dist','Col Dist']] = df2[['Row Offset','Col Offset','Z Pick Offset Col','Z Pick Offset Row','Z Pick Pos','Row Dist','Col Dist']] /1000

        

        df3=df2[['Max Rows','Max Cols','Row Dist','Col Dist','Z Pick Speed','Z Place Speed','Z Pick Pos','Z Place Pos','Row Dir','Col Dir','Row Offset','Col Offset','Z Pick Offset Col','Z Place Offset Col','Z Pick Offset Row','Z Place Offset Row']]
        
        #print('After conversion values : ',df3)

        return df.to_csv(path+'/bref2.csv',index=False),df3.to_csv(path+'/BasketSett2.csv',index=False)



trial = pick_basket.basket1(input("Enter a point 1 value : ").split(','),input("Enter a point 2 value : ").split(','),input("Enter a point 3 value : ").split(','),
input("Enter a point 4 value : ").split(','),input("Enter R values : "),input("Enter a 5 parameters : ").split(','),input("Enter a V,TO,MOVELJ,FORCE : ").split(','),
input('Enter your csv path : '),input("Basket Dimensions(LWHST) : ").split(','),input("Basket_set values : ").split(','))

print('CSV saved')

#points will have 3 value
# r values will have 3 values
# 4 parameters
# bref rest details
# csv path
#basket dimensions
#basket set values