from guizero import *
from engi1020.arduino.api import *
from random import *
from time import *

def blenca():
    balance = App(title='BalanceIt')

    def balance_test():
        x = []
        y = []
        z = []
        issues = []

        for i in range(30):
            x.append(three_axis_get_accelX())
            y.append(three_axis_get_accelY())
            z.append(three_axis_get_accelZ())
            sleep(1)
        
        buzzer_frequency(5, 300)
        sleep(1)
        buzzer_stop(5)
        
        deviancex = [max(x) - x[0], x[0] - min(x)]
        deviancey = [max(y) - y[0], y[0] - min(x)]
        deviancez = [max(z) - z[0], z[0] - min(z)]
        
        print(abs(sum(deviancex)),'x')
        print(abs(sum(deviancey)),'y')
        print(abs(sum(deviancez)),'z')
        
        if abs(sum(deviancex)) <= .4 and abs(sum(deviancey))  <= .4 and abs(sum(deviancez)) <= .4:
            oled_clear()
            oled_print('Seems stable')
            problem = 'No issues found!'
            issues.append(problem)
        
        else:
            oled_clear()
            oled_print('Unstable')
            if abs(sum(deviancey)) > .4:
                if abs(deviancey[0]) < abs(deviancey[1]):
                    problem = 'right arm weakness'
                    oled_print(problem)
                    issues.append(problem)
                
                elif abs(deviancey[0]) > abs(deviancey[1]):
                    problem = 'left arm weakness'
                    oled_print(problem)
                    issues.append(problem)
            else:
                None
                
            if abs(sum(deviancez)) > .4:
                if abs(deviancez[0]) > abs(deviancez[1]):
                    problem = 'raised too much'
                    oled_print(problem)
                    issues.append(problem)
                
                else:
                    problem = 'dropped too much'
                    oled_print(problem)
                    issues.append(problem)
            else:
                None
            
            if abs(sum(deviancex)) > .4:
                if deviancex[0] >0 or deviancex[1]>0 :
                    problem = 'wrist instability'
                    oled_print(problem)
                    issues.append(problem)
            
            else:
                None
                
        balanceprobs = Window(balance, title='What we found')
        resttl = Text(balanceprobs, size=60, text='Your Balance Problems')
        report = Picture(balanceprobs, image='report.png')
        problems = Text(balanceprobs, size=30, text=f'The following issues were found:\n {issues}')
        blank2 = Text(balanceprobs, size=40)
        with open('resultats.txt', 'a') as r:
            for i in range(len(issues)):
                r.write(issues[i])
        resexit = Text(balanceprobs, size=30, text='Close this window to play again')


    blnce = Box(balance, align = 'bottom', layout="grid")
    titular = Text(balance, 'BalanceIt', size=80)
    start = PushButton(balance, text='Press to Start',command=balance_test, image='balance.png')
    sec1 = Text(blnce, 'The game will proceed as follows:', size=24, grid=[0,0])

    inste1 = Text(blnce, '1. Hold the Arduino on either side.',grid=[0,1], align='left', size=18)
    inste2 = Text(blnce, '2. Keep it as stable as you can.',grid=[0,2], align='left', size=18)
    inste3 = Text(blnce, '3. For ~30 seconds, the Arduino will note all movement', grid=[0,3], align='left', size=18)
    inste4 = Text(blnce, '4. The data collected will be processed', grid=[0,4], align='left', size=18)
    inste5 = Text(blnce, '5. A new window will appear on your computer, along with any issues that were found',grid=[0,5], align='left', size=18)
    inste6 = Text(blnce, 'Press the Balance twice to Start', grid=[0,6], size=24)
            
            
blenca()