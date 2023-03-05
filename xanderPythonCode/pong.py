import pygame
from pygame.locals import *
pygame.init()
screen = pygame.display.set_mode((500, 500))
# create the ball
ball = pygame.Rect(250, 250, 10, 10)
ball_speed = [3, 3]

# create the paddles
paddle_1 = pygame.Rect(10, 225, 10, 50)
paddle_2 = pygame.Rect(480, 225, 10, 50)
paddle_speed = 5
while True:
  # update the positions of the ball and paddles
  ball.x += ball_speed[0]
  ball.y += ball_speed[1]
  # check for key press events to move the paddles
  for event in pygame.event.get():
    if event.type == KEYDOWN:
      if event.key == K_UP:
        paddle_1.y -= paddle_speed
      elif event.key == K_DOWN:
        paddle_1.y += paddle_speed
  # check for ball-paddle collisions
  if ball.colliderect(paddle_1) or ball.colliderect(paddle_2):
    ball_speed[0] = -ball_speed[0]
  # check for ball-wall collisions
  if ball.top < 0 or ball.bottom > 500:
    ball_speed[1] = -ball_speed[1]
  # redraw the screen
  screen.fill((0, 0, 0))
  pygame.draw.rect(screen, (255, 255, 255), ball)
  pygame.draw.rect(screen, (255, 255, 255), paddle_1)
  pygame.draw.rect(screen, (255, 255, 255), paddle_2)
  pygame.display.flip()
