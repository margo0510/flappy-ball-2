import pgzrun
from random import randint

TITLE = "FLAPPY BALL"
HEIGHT = 600
WIDTH = 800

GRAVITY = 2000


class Ball():
    def __init__(self, initial_x, initial_y, radius):
        self.y = initial_y
        self.x = initial_x
        self.vx = 200
        self.vy = 0
        self.radius = radius
        self.color = (randint(0, 255), randint(0, 255), randint(0, 255)) 
    def draw(self):
        pos = (self.x, self.y)
        screen.draw.filled_circle(pos, self.radius, self.color)

    def update(self, dt):
        updated_y = self.vy
        self.vy += GRAVITY * dt
        self.y += (updated_y + self.vy) * 0.5 * dt
        if self.y > HEIGHT - self.radius:
            self.y = HEIGHT - self.radius
            self.vy = -self.vy * 0.9
        self.x += self.vx * dt
        if self.x > WIDTH - self.radius or self.x < self.radius:
            self.vx = -self.vx


ball_1 = Ball(50, 100, 30)
ball_2 = Ball(300, 100, 40)
ball_3 = Ball(500, 600, 60)
ball_4 = Ball(600, 0, 25)


def draw():
    screen.clear()
    screen.fill("navy")
    ball_1.draw()
    ball_2.draw()
    ball_3.draw()
    ball_4.draw()


def update(dt):
    ball_1.update(dt)
    ball_2.update(dt)
    ball_3.update(dt)
    ball_4.update(dt)


def on_key_down(key):
    if key == keys.LEFT:
        ball_2.vy = -600
    elif key == keys.RIGHT:
        ball_1.vy = -400
    elif key == keys.UP:
        ball_3.vy = -500
    elif key == keys.DOWN:
        ball_4.vy = -300


pgzrun.go()