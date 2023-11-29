from guizero import *
from engi1020.arduino.api import *
from random import *
from time import *

print(three_axis_get_accelX())
print(three_axis_get_accelY())
print(three_axis_get_accelZ())

def balance_test():
    x = []
    y= []
    z = []
    x.append(three_axis_get_accelX())
    y.append(three_axis_get_accelY())
    z.append(three_axis_get_accelZ())
    
    for i in range(30):
        x.append(three_axis_get_accelX())
        y.append(three_axis_get_accelY())
        z.append(three_axis_get_accelZ())
    
    deviancex = max(x) - min(x)
    deviancey = max(y) - min(y)
    deviancez = max(z) - min(z)
    
    if deviancex >= .3 and deviance y>= .3 and deviancez>= .3:
        oled_print('Seems stable')
    
    else:
        oled_print('Unstable')
        
        if deviancey <0:
            oled_print('right arm instability')
        
        else:
            oled_print('left arm instability')
        
        if deviancez
 