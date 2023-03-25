import pygame

#creer un classe pour le joueur
class Player (pygame.sprite.Sprite):
    def __init__(self,game):
        super().__init__()
        # pygame.sprite.Sprite.__init__(self)
        self.life = 5
        self.game = game
        self.speed = 5
        self.image = pygame.image.load("assets/player.png")
        self.image = pygame.transform.scale(self.image, (55, 75))
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 450
        self.jump = 3
        self.all_coeur = pygame.sprite.Group()


    def move_right(self):
        # si le joueur n'est pas en colision avk l'attack
        if not self.game.check_collision(self,self.game.onde_sonor.all_Onde_sonor_attack):
            self.rect.x += self.speed
    def move_left(self):
        if not self.game.check_collision(self, self.game.onde_sonor.all_Onde_sonor_attack):
         self.rect.x -= self.speed

    def monter(self):
        if not self.game.check_collision(self, self.game.onde_sonor.all_Onde_sonor_attack):
            self.rect.y -= self.speed

    def descendre(self):
        if not self.game.check_collision(self, self.game.onde_sonor.all_Onde_sonor_attack):
            self.rect.y += self.speed


