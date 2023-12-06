from hearingg import *
from reactionGUI import *
from balance import *
from patterng import *
from guizero import *

app = App(title='TestMe')
blank1 = Text(app, size=60)
title = Text(app, size=60, text='TestMe')
blank2 = Text(app, size=60, align='bottom')

expo = Box(app, layout='grid', align='bottom')
explanat = Text(expo, grid=[0,5], text='TestMe is a simple game menu that is designed to test your senses and abilities through a variety of games', size=18)
select = Text(expo, grid=[0,0], text='Select a game below:', size=24)

game1 = PushButton(expo, grid=[0,1], text='SoundIt', command=sound_it)
game1.text_size = 24
game2 = PushButton(expo, grid=[0,2], text='ReactTest', command=reactionGUI)
game2.text_size=24
game3 = PushButton(expo, grid=[0,3], text='BalanceIt', command=blenca)
game3.text_size=24
game4 = PushButton(expo, grid=[0,4], text='PatternTest', command=pattern_game)

app.display()