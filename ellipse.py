import pygame as pg 

pg.init()
try:
    n = int(input())
except:
    print('ошибка')
    exit()

W, H = 500, 500
sc = pg.display.set_mode((W, H))
step = W/(n * 2)
x_move = 0

while True: 
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            exit()
#######################изм положения

    x_move+=1
    if x_move > W//2:
        x_move = - W//2
 
    
   
#######################отрисовка
    
    sc.fill((0, 0, 0))
    for i in range(n):
        x_y= i * step
        width_height = W-2 * x_y
        pg.draw.ellipse(sc, (255, 255, 255),(x_move + x_y, 0, width_height, H), 1)
        pg.draw.ellipse(sc, (255, 255, 255),(x_move + 0,x_y, W ,width_height), 1)
    pg.display.update()

    ################WAIT################## милисикунды
    pg.time.delay(50)