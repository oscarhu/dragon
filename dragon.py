import random, time, sys, pygame

def displayIntro():
    print('You are in a land full of dragons. In front of you,')
    print('you see three caves. In one cave, the dragon is friendly')
    print('and will share his treasure with you. Another  dragon')
    print('is greedy and hungry, and will eat you on sight.')
    print('The last dragon is poor and takes your money.')
    print()

def chooseCave():
    cave = ''
    while cave != '1' and cave != '2' and cave != '3':
        print('Which cave will you go into? (1 or 2 or 3)')
        cave = raw_input()

    return cave

def checkCave(chosenCave):
    print('You approach the cave...')
    #time.sleep(2)
    print('It is dark and spooky...')
    #time.sleep(2)
    print('A large dragon jumps out in front of you! He opens his jaws and...')
    print()
    #time.sleep(2)

    friendlyCave = random.randint(1, 3)
    robberCave = friendlyCave -1
    if robberCave < 1:
       robberCave += 3
        
    badCave = friendlyCave +1
    if badCave >3:
        badCave -=3
        
    screen.blit(blackbox,allcaves[0])
    screen.blit(blackbox,allcaves[1])
    screen.blit(blackbox,allcaves[2])
    screen.blit(black2, black2Rect)
    
    if chosenCave == friendlyCave:
        print('Gives you his treasure!')
        screen.blit(friendly,allcaves[chosenCave-1])
        screen.blit(money,moneyRect)
    else:
        if chosenCave == robberCave:
            print('robs all your stuff')
            screen.blit(robber,allcaves[chosenCave-1])
            screen.blit(robbed,robbedRect)
        else:
            if chosenCave == badCave:
                print('Gobbles you down in one bite!')
                screen.blit(bad,allcaves[chosenCave-1])
                screen.blit(eaten,eatenRect)
    print('the friendly cave was ' + str(friendlyCave) )
    print('the robber cave was ' + str(robberCave) )
    print('the badcave was ' + str(badCave) )
    
displayIntro()

pygame.init()
 
size = width, height = 640, 480

screen = pygame.display.set_mode(size)
 
caves = pygame.image.load("danger.gif")
cavesrect = caves.get_rect()

blackbox = pygame.image.load("blackbox.gif")
black2 = pygame.image.load("black2.gif")
black2Rect = pygame.Rect(139, 373, 362, 100)

eaten = pygame.image.load("eaten.gif")
eatenRect = pygame.Rect(162,381, 316, 91)

money = pygame.image.load("money.gif")
moneyRect = pygame.Rect(141, 385, 359, 83)

robbed = pygame.image.load("robbed.gif")
robbedRect = pygame.Rect(196, 378, 249, 98)

friendly = pygame.image.load("friendlydragon.gif")
cave1 = pygame.Rect(59,292,50,50)

bad = pygame.image.load("baddragon.png")
cave2 = pygame.Rect(269,292,50,50)

robber = pygame.image.load("robberdragon.gif")
cave3 = pygame.Rect(471,292,50,50)

allcaves=[cave1,cave2,cave3]

screen.blit(caves, cavesrect)   

pygame.display.flip()

# Run the game
while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key==pygame.K_1:
                print ('you pressed 1')
                checkCave(1)
            elif event.key==pygame.K_2:
                print('you pressed 2 ')
                checkCave(2)
            elif event.key==pygame.K_3:
                print('you pressed 3 ')
                checkCave(3)
            pygame.display.update()