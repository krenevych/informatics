#T21_22
#Зображує точки та кола. Використовує параметри з файлу конфігурації 

from t21_21_config_dict import *
from T19.t19_01_objvirt_abstract import *
import random

# встановити параметри за угодою
params = {'points_num': 3,
          'circles_num': 5,
          'minxy': -100,
          'maxxy': 100,
          'maxr': 30,
          'color': 'blue',
          'color2': 'green'}

# отримати параметри з конфігураційного файлу
conf = ConfigDict('turtleconfig.txt', params)
params = conf.getconfig()


drawer = TurtleDraw()
# встановити колір зображення точок 
drawer.color = params['color']

# зобразити точки
for i in range(params['points_num']):
    x = random.randrange(params['minxy'], params['maxxy']+1)
    y = random.randrange(params['minxy'], params['maxxy']+1)
    p = Point(x,y,TurtleDraw)
    p.switchon()

# встановити колір зображення кіл 
drawer.color = params['color2']

# зобразити кола
for i in range(params['circles_num']):
    x = random.randrange(params['minxy'], params['maxxy']+1)
    y = random.randrange(params['minxy'], params['maxxy']+1)
    r = random.randrange(1, params['maxr'])
    c = Circle(x,y,r,TurtleDraw)
    c.switchon()





