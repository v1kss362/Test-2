from pygame import *

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, player_size_x, player_size_y):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (player_size_x,player_size_y))
        self.speed_x = player_speed
        self.speed_y = player_speed
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image,(self.rect.x, self.rect.y))
    def update3(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y
class Player(GameSprite):
    def update1(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < win_width - 80:
            self.rect.y += self.speed
    def update2(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_width - 80:
            self.rect.y += self.speed

window = display.set_mode((800, 500))
win_width = 800
win_height = 500
clock = time.Clock()
background = transform.scale(
    image.load('1.png'),(800, 500)
)
ball = GameSprite('2.png',300, 400, 1, 50, 50)
player1 = Player('3.jpg',750, 100, 5, 25, 125)
player2 = Player('3.jpg',50, 100, 5, 25, 125)
speed_x = 5
speed_y = 5

game = True
finish = False

font.init()
font1 = font.Font(None, 35)
lose2 = font1.render('Player 1 lose', True, (180, 0, 0))
lose3 = font1.render('Player 2 lose', True, (180, 0, 0))

while game != False :
    if finish == False :


        window.blit(background, (0,0))
        clock.tick(60)
        player1.update2()
        player1.reset()
        player2.update1()
        player2.reset()
        ball.update3()
        ball.reset()
        if ball.rect.y > win_height - 50 or ball.rect.y < 0:
            ball.speed_y *= -1
        if sprite.collide_rect(ball, player1) or sprite.collide_rect(ball, player2):
            ball.speed_x *= -1
    if ball.rect.x < 0:
        finish = True
        window.blit(lose2, (400, 250))
    if ball.rect.x > 800:
        finish = True
        window.blit(lose3, (400, 250))
    for e in event.get():
        if e.type == QUIT:
            game = False
        if e.type == KEYDOWN:
            if e.key == K_r:
                finish = False
                ball = GameSprite('2.png',300, 400, 0, 50, 50)
            if e.key == K_SPACE:
                ball = GameSprite('2.png', 300, 400, 1, 50, 50)
            if e.key == K_n:
                ball.speed_x *= 2
                ball.speed_y *= 2
            if e.key == K_m:
                ball.speed_x /= 2
                ball.speed_y /= 2
    display.update()
