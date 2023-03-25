import pygame
import math
from game import Game
pygame.init()
pygame.mixer.init()


# generer une fenetre
pygame.display.set_caption("Jay Bros")
screen = pygame.display.set_mode((1080, 600))

# importer un bg
background = pygame.image.load("assets/bg.png")

# charger le jeu
game = Game()

# creation du bouton pour aller a l'acceuille
quit_button = pygame.image.load('assets/remove.png')
quit_button = pygame.transform.scale(quit_button, (100, 50))
quit_button_rect = quit_button.get_rect()
quit_button_rect.x = math.ceil(screen.get_width() / 1.1)
quit_button_rect.y = math.ceil(screen.get_height() / 20)

# création d'un bouton restart
restart_button = pygame.image.load('assets/restart.png')
restart_button = pygame.transform.scale(restart_button, (100, 50))
restart_button_rect = restart_button.get_rect()
restart_button_rect.x = math.ceil(screen.get_width() / 2)
restart_button_rect.y = math.ceil(screen.get_height() / 2 + 75)

# CREER l'image du TEXTE
image_texte = pygame.image.load("assets/bulle.png")
image_texte_rect = image_texte.get_rect()
image_texte_rect.x = game.onde_sonor.rect.x - 175
image_texte_rect.y = game.onde_sonor.rect.y + 25


coeur = pygame.image.load("assets/coeur.png")
coeur = pygame.transform.scale(coeur, (25, 25))

running = True
clock = pygame.time.Clock()
time_back = 0

# definit image de fin quand tu gagne ou perd
game_over = pygame.image.load("assets/game-over.jpg")
game_over = pygame.transform.scale(game_over, (screen.get_width(), screen.get_height()))
game_over_rect = game_over.get_rect()
win = pygame.image.load("assets/win.jpg")
win = pygame.transform.scale(win, (screen.get_width(), screen.get_height()))
win_rect = win.get_rect()

# music du jeu
pygame.mixer.music.load(game.music)
pygame.mixer.music.play(-1)  # If the loops is -1 then the music will repeat indefinitely.

music_perdu = "music/perdu(Rayman OST - Game Over 2).mp3"
music_gagner = "music/win(One Piece Soundtrack - To The Grand Line HD).mp3"
while running:

    # mettre a jour le temps
    game.temps = pygame.time.get_ticks()

    # Applique un bg
    screen.blit(background, (0, 0))
    # screen.scroll(500,0)

    # mettre a jour la barre de jauge en fonction du temps
    if pygame.time. get_ticks() - time_back >= 1000:
        game.onde_sonor.vie -= pygame.time. get_ticks() - time_back
        time_back = pygame.time. get_ticks()
    # game.onde_sonor.update_time_bar(screen) applique la bare dé le debut du jeu

    # verifier si le joueur aller à gauche ou a droite ou monter ou descendre
    if game.pressed.get(pygame.K_RIGHT) and game.player.rect.x < 900:
        game.player.move_right()
    if game.pressed.get(pygame.K_LEFT) and game.player.rect.x > 0:
        game.player.move_left()
    if game.pressed.get(pygame.K_UP) and game.player.rect.y >= 30:
        game.player.monter()
    if game.pressed.get(pygame.K_DOWN) and game.player.rect.y < 500:
        game.player.descendre()

    # lancer des attaque
    game.onde_sonor.launch_attack()

    # recuperer les projectile de onde_sonor et les lancer en fonction  de la bare de vie de onde sonor
    for attack in game.onde_sonor.all_Onde_sonor_attack:
        game.onde_sonor.update_time_bar(screen, attack)
        attack.move()

    # applique les attack de onde_sonor
    game.onde_sonor.all_Onde_sonor_attack.draw(screen)

    # appliquer l'image de mon joueur
    screen.blit(game.player.image, game.player.rect)

    # appliquer l'enemie du niveau 1 et sa position
    if not game.onde_sonor.arriver:
        game.onde_sonor.descendre()
    if game.onde_sonor.arriver:
        game.onde_sonor.monter()
    screen.blit(game.onde_sonor.image, game.onde_sonor.rect)

    # applique le l'imge du texte APPRES 1 seconde
    if 1000 <= pygame.time.get_ticks() <= 5500:
        image_texte_rect.x = game.onde_sonor.rect.x - 350
        image_texte_rect.y = game.onde_sonor.rect.y - 125
        screen.blit(image_texte, image_texte_rect)

    # appliquer le bouton pour quitter
    screen.blit(quit_button, quit_button_rect)

    # appliquer les coeur en fonction de la vie du joueur
    if game.player.life >= 1:
        screen.blit(coeur, (0, 0))
        if game.player.life >= 2:
            screen.blit(coeur, (30, 0))
            if game.player.life >= 3:
                screen.blit(coeur, (60, 0))
                if game.player.life >= 4:
                    screen.blit(coeur, (90, 0))
                    if game.player.life == 5:
                        screen.blit(coeur, (120, 0))

    # quitter le jeu si le joueur n'a element de vie
    if game.player.life <= 0:
        # afficher l'image game over
        screen.blit(game_over, (0, 0))

        # mette la music quand tu perd
        game.update_music(music_perdu)

        # afficher l'image restart
        screen.blit(restart_button, (restart_button_rect.x, restart_button_rect.y))
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if restart_button_rect.collidepoint(event.pos):
                pygame.quit()
                exec(open("main.py").read())

    # quitter le jeu si le onde sonor n'a element de vie/temps
    if game.onde_sonor.vie <= 0:
        # afficher l'image win
        screen.blit(win, (0, 0))

        # mette la music quand tu gagne
        game.update_music(music_gagner)

        # afficher l'image restart
        screen.blit(restart_button, (restart_button_rect.x, restart_button_rect.y))
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if restart_button_rect.collidepoint(event.pos):
                pygame.quit()
                exec(open("main.py").read())

    # mettre a jour l'écran
    pygame.display.flip()

    # si le joueur ferme cette fenetre
    for event in pygame.event.get():
        # que si event est fermeture de fenetre
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            # exec(open("acceuille.py").close())
            print("fermeture de la fenetre")

        # detecter si un joueur lache une touche
        elif event.type == pygame.KEYDOWN:
            game.pressed[event.key] = True
        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False

        # revenir a l'acceulle quand on clique
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if quit_button_rect.collidepoint(event.pos):
                pygame.quit()
                exec(open("acceuille.py").read())
                print("fermeture de la fenetre")
