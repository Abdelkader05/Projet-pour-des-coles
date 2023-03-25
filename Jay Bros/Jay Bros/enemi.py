import pygame
from random import *


class Onde_sonor(pygame.sprite.Sprite):
    def __init__(self,game):
        super(Onde_sonor, self).__init__()
        self.nb_max_attack = 50
        self.game = game
        self.vie = 60000
        self.max_vie = 60000
        self.vitesse = 3
        self.all_Onde_sonor_attack = pygame.sprite.Group()
        self.image = pygame.image.load("assets/ennemie1.png")
        self.rect = self.image.get_rect()
        self.rect.x = 950
        self.rect.y = 0
        self.arriver = False
        self.time_launch_attack = 0




    def update_time_bar(self,surface,attack):
        bar_widht = self.vie / 100
        max_bar_widht = self.max_vie / 100

        # definir uune couleur pour la jauge devie
        bar_color = (111, 210, 46)

        # definir la position de la jauge de vie et sa largeur et son épaisseur
        bar_position = [480, 0, bar_widht, 20]

        # definir une couleur pour la jauge de vie en fonction du pourcentage de la bar (vert, jaune ,rouge )
        if bar_position[2] <= max_bar_widht:
            bar_color = (0, 255, 0)
        if bar_position[2] <= max_bar_widht * 0.75:
            bar_color = (255, 255, 0)
            Onde_sonor_attack.upgrade_speed(attack, "Jaune")
        if bar_position[2] <= max_bar_widht * 0.40:
            bar_color = (255, 0, 0)
            Onde_sonor_attack.upgrade_speed(attack, "Rouge")

        # DEFINIR le bg de la jauge
        bar_bg_color = (60, 63, 60)
        bar_bg_position = [480, 0, max_bar_widht, 20]

        # dessiner le bg de la jauge de vie
        pygame.draw.rect(surface, bar_bg_color, bar_bg_position)

        # desiner la barre de vie
        pygame.draw.rect(surface, bar_color, bar_position)



    def launch_attack(self):
        # APPLIQUE l'attack une fois sur deux
        #aleatoire = self.game.temps / 100 #".0" in str(aleatoire) or ".51" in str(aleatoire)
        if len(self.all_Onde_sonor_attack) <= self.nb_max_attack and pygame.time.get_ticks() - self.time_launch_attack >= 1000 :
            self.time_launch_attack = pygame.time.get_ticks()
            self.all_Onde_sonor_attack.add(Onde_sonor_attack(self, self.game))

    def monter(self):
        self.rect.y -= self.vitesse
        if self.rect.y == 0 :
            self.arriver = False

    def descendre(self):
        self.rect.y += self.vitesse
        if self.rect.y == 450 :
            self.arriver = True



class Onde_sonor_attack(pygame.sprite.Sprite):
    def __init__(self,Onde_sonor,game):
        super().__init__()
        self.game = game
        self.speed = 5
        self.speed_default = 5
        self.onde_sonor = Onde_sonor
        self.image = pygame.image.load("assets/ennemie1_attack.png")
        self.rect = self.image.get_rect()
        self.image = pygame.transform.scale(self.image,(50,50))
        self.rect.x = Onde_sonor.rect.x
        self.rect.y = Onde_sonor.rect.y + 25



    def remove(self) :
        self.onde_sonor.all_Onde_sonor_attack.remove(self)

    def upgrade_speed(self, couleur):
        if couleur == "Jaune":
            self.speed = self.speed_default * 1.5
        elif couleur == "Rouge" :
            self.speed = self.speed_default * 2


    def move(self):
        if not self.game.check_collision(self, self.game.all_player):
            self.rect.x -= self.speed

        elif self.game.check_collision(self, self.game.all_player):
            self.remove()
            self.game.player.life -= 1

        #condition pour verifier si le l'attack est toujous sur l'ecran
        if self.rect.x < 0  :
            #supprimer l'attack
            self.remove()