import sys, pygame

pygame.init()
 
size = width, height = 640, 480

screen = pygame.display.set_mode(size)
 
caves = pygame.image.load("danger.gif")
cavesrect = caves.get_rect()

friendly = pygame.image.load("friendlydragon.gif")
friendlyrect = pygame.Rect(59,292,50,50)

bad = pygame.image.load("baddragon.png")
badrect = pygame.Rect(269,292,50,50)

robber = pygame.image.load("robberdragon.gif")
robberrect = pygame.Rect(471,292,50,50)

screen.blit(caves, cavesrect)

pygame.display.flip()
while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key==pygame.K_1:
                print ('you pressed 1')
                screen.blit(friendly,friendlyrect)
            elif event.key==pygame.K_2:
                print('you pressed 2 ')
                screen.blit(bad,badrect)
            elif event.key==pygame.K_3:
                print('you pressed 3 ')
                screen.blit(robber,robberrect)
            pygame.display.update()