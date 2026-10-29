import pygame
pygame.init()
screen=pygame.display.set_mode((450,600))
done=True
while done:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            done=False
    pygame.draw.circle(screen,(0,255,0),(200,200),50)
    pygame.draw.circle(screen,(0,255,0),(300,300),50,20)
    pygame.display.flip()
