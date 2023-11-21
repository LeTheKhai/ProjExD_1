import sys
import pygame as pg


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((1600, 900))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("fig/pg_bg.jpg")
    kk_img = pg.image.load("fig/3.png")
    kk_img = pg.transform.flip(kk_img,True,False)
    kk_img = [kk_img, pg.transform.rotozoom(kk_img,10,1)]
    tmr = 0
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return
            
        screen.blit(bg_img, [0, 0])
        screen.blit(kk_img[1],[300, 200])
        pg.display.update()
        tmr += 1        
        clock.tick(10)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()