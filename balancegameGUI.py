from guizero import *
from engi1020.arduino.api import *
from random import *
from time import *

def blenca():
    balance = App(title='BalanceIt')


    def balance_test():
        x = []
        y= []
        z = []
        prolem = []
        x.append(three_axis_get_accelX())
        y.append(three_axis_get_accelY())
        z.append(three_axis_get_accelZ())
        
        for i in range(30):
            x.append(three_axis_get_accelX())
            y.append(three_axis_get_accelY())
            z.append(three_axis_get_accelZ())
        
        deviancex = [max(x) - x[0], x[0] - min(x)]
        deviancey = [max(y) - y[0], y[0] - min(x)]
        deviancez = [max(z) - z[0], z[0] - min(z)]
        
        if abs(sum(deviancex)) <= .2 and sum(abs(deviancey))  <= .2 and abs(sum(deviancez)) <= .2:
            oled_print('Seems stable')
            prolem = 'None'
            issues.append(prolem)
        
        else:
            oled_print('Unstable')
            
            if deviancey[0] > deviancey[1]:
                prolem = 'right arm weakness'
                oled_print(prolem)
                issues.append(prolem)
            
            else:
                prolem = 'left arm weakness'
                oled_print(prolem)
                issues.append(prolem)
            
            if  deviancez[0] > deviancez[1]:
                prolem = 'raised too much'
                oled_print(prolem)
                issues.append(prolem)

            
            else:
                prolem = 'raised too much'
                oled_print(prolem)
                issues.append(prolem)
            
            if deviancex[0] >0 or deviancex[1]>0 :
                prolem = 'wrist instability'
                oled_print(prolem)
                issues.append(prolem)
            
        balanceprobs = Window(balance, title='What we found')
        resttl = Text(balanceprobs, size=60, text='Your balanceprobs')
        report = Picture(balanceprobs, image='report.png')
        problems = Text(balanceprobs, size=30, text=f'The following issues were found {issues}')
        blank2 = Text(balanceprobs, size=40)
        resexit = Text(balanceprobs, size=30, text='Close this window to play again')
        
            
        
            


    blnce = Box(balance, align = 'bottom', layout="grid")
    titular = Text(balance, 'ReactTest', size=80)
    start = PushButton(balance, text='Press to Start',command=balance_test, image='balance.png')
    sec1 = Text(blnce, 'The game will proceed as follows:', size=24, grid=[0,0])

    inste1 = Text(blnce, '1. Hold the Arduino on either side.',grid=[0,1], align='left', size=18)
    inste2 = Text(blnce, '2. Keep it as stable as you can.',grid=[0,2], align='left', size=18)
    inste3 = Text(blnce, '3. For 30 seconds, the Arduino will note all movement', grid=[0,3], align='left', size=18)
    inste4 = Text(blnce, '4. The data collected will be processed', grid=[0,4], align='left', size=18)
    inste5 = Text(blnce, '5. A new window will appear on your computer, along with any issues that were found',grid=[0,5], align='left', size=18)
    inste6 = Text(blnce, 'Press the Balance to Start', grid=[0,6], size=24)
            
            
     
