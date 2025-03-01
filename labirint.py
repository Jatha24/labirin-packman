from pygame import *

back = (255, 255, 255)
window = display.set_mode((700, 500))
display.set_caption('Game labirin')
jam = time.Clock()

background = transform.scale(image.load('background.jpg'), (700, 500))
class GameSprite(sprite.Sprite):

    def __init__(self, sprite_image, x_cor, y_cor, size_x, size_y):
        sprite.Sprite.__init__(self)
        self.image = transform.scale(image.load(sprite_image), (size_x, size_y))

        self.rect = self.image.get_rect()
        self.rect.x = x_cor
        self.rect.y = y_cor

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
class Player(GameSprite):
    def __init__(self, sprite_image, x_cor, y_cor, size_x, size_y):
        GameSprite.__init__(self, sprite_image, x_cor, y_cor,size_x, size_y)
        self.x_speed = 0
        self.y_speed = 0
    def update(self):
        self.rect.x += self.x_speed
        self.rect.y += self.y_speed

class Musuh(GameSprite):
    def __init__(self, sprite_image, x_cor, y_cor, size_x, size_y):
        GameSprite.__init__(self, sprite_image, x_cor, y_cor,size_x, size_y)

class Dinding(GameSprite):
    def __init__(self, sprite_image, x_cor, y_cor, size_x, size_y):
        GameSprite.__init__(self, sprite_image, x_cor, y_cor,size_x, size_y)

class Koin(GameSprite):
    def __init__(self, sprite_image, x_cor, y_cor, size_x, size_y):
        GameSprite.__init__(self, sprite_image, x_cor, y_cor,size_x, size_y)

player1 = Player('packman.png', 50, 50, 75, 75)
musuh1 = Musuh('hantu.png', 550, 50, 75, 75)
koin1 = Koin('duit.png', 600, 400, 75, 75)
dinding1 = Dinding('dinding.png2.jpg', 400, 100, 50, 550)

run = True
finish = False
while run:
    
    for kejadian in event.get():
        if kejadian.type == QUIT:
            run = False
        elif kejadian.type == KEYDOWN:
            if kejadian.key == K_a:
                player1.x_speed = -5
            elif kejadian.key == K_d:
                player1.x_speed = 5
            elif kejadian.key == K_w:
                player1.y_speed = -5
            elif kejadian.key == K_s:
                player1.y_speed = 5
        elif kejadian.type == KEYUP:
            if kejadian.key == K_a:
                player1.x_speed = 0
            elif kejadian.key == K_s:
                player1.x_speed = 0
            elif kejadian.key == K_d:
                player1.y_speed = 0
            elif kejadian.key == K_w:
                player1.y_speed = 0
               
            

    if finish == False:
        window.fill(back)
        window.blit(background, (0,0))
        jam.tick()
        player1.reset()
        musuh1.reset()
        dinding1.reset()
        koin1.reset()
        if sprite.collide_rect(player1, musuh1):
            finish = True
            img = image.load('gameover.jpg')
            d = img.get_width() // img.get_height()
            window.fill((255, 255, 255))
            window.blit(transform.scale(img, (500 * d, 500)), (90, 0))
        
        if sprite.collide_rect(player1, koin1):
            finish = True
            img = image.load('win.jpg')
            d = img.get_width() // img.get_height()
            window.fill((255, 255, 255))
            window.blit(transform.scale(img, (500 * d, 500)), (0, 0))
        player1.update()
        
    
    
        
        
        display.update()
              

        
        
    
