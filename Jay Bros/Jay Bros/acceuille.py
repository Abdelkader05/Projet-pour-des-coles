import math
import sys
import pygame
pygame.mixer.init()
pygame.init()


pygame.display.set_caption("'A school game' by Jaybros")
screen = pygame.display.set_mode((1080, 600))

background = pygame.image.load('assets/background.jpg')

play_button = pygame.image.load('assets/start-button.png')
play_button = pygame.image.load('assets/start-button.png')
play_button = pygame.transform.scale(play_button, (200, 100))
play_button_rect = play_button.get_rect()
play_button_rect.x = math.ceil(screen.get_width() / 2.5)
play_button_rect.y = math.ceil(screen.get_height() / 2)
quit_button = pygame.image.load('assets/remove.png')
quit_button = pygame.transform.scale(quit_button, (100, 50))
quit_button_rect = quit_button.get_rect()
quit_button_rect.x = math.ceil(screen.get_width() / 1.1)
quit_button_rect.y = math.ceil(screen.get_height() / 20)

#aide pour le deplacement
deplacement_image = pygame.image.load("assets/deplacement.png")

running = True
#music du menu
pygame.mixer.music.load("music/menu(One Piece OST Overtaken).mp3")
pygame.mixer.music.play(-1)  # If the loops is -1 then the music will repeat indefinitely.
while running:

    screen.blit(background, (-500, -300))
    screen.blit(deplacement_image, (play_button_rect.x-40, play_button_rect.y+ 75))
    screen.blit(play_button, play_button_rect)
    screen.blit(quit_button, quit_button_rect)
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if play_button_rect.collidepoint(event.pos):
                pygame.quit()
                exec(open("main.py").read())
            if quit_button_rect.collidepoint(event.pos):
                pygame.quit()
                exec(open("main.py").close())
                sys.exit()
