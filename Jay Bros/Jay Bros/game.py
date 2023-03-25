import pygame
from player import Player
from enemi import Onde_sonor
from enemi import Onde_sonor_attack


# classe qui vas representer notre jeu
class Game():

    def __init__(self):
        #generer notre joueur
        self.player = Player(self)
        self.all_player =pygame.sprite.Group()
        self.all_player.add(self.player)
        self.pressed = {}
        self.onde_sonor = Onde_sonor(self)
        self.temps = pygame.time.get_ticks()
        self.onde_sonor_attack = Onde_sonor_attack
        self.music = "music/jeu(One Piece - Welcome To Wano Theme (Extended)).mp3"

    def check_collision(self,sprite,group):
        return pygame.sprite.spritecollide(sprite,group,False,pygame.sprite.collide_mask)

    def update_music(self,music):
        if music != self.music :
            self.music = music
            pygame.mixer.music.load(self.music)
            pygame.mixer.music.play(-1)  # If the loops is -1 then the music will repeat indefinitely.