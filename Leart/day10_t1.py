import pygame



def main():
    pygame.init()
    screen = pygame.display.set_mode((1800,1600))
    pygame.display.set_caption('大球吃小球')
    screen.fill((255,255,255))
    ball_image = pygame.image.load('./res/ball.png')
    #pygame.draw.circle(screen, (255,0,0), (100,100), 30, 0)
    screen.blit(ball_image, (50, 50))
    
    
    pygame.display.flip()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False


if __name__ == '__main__':
    main()

