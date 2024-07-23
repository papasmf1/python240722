import pygame
import sys
import random

# 초기화
pygame.init()

# 색상 정의
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# 화면 크기 설정
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("블록 깨기 게임")

# 패들 설정
paddle_width = 400
paddle_height = 10
paddle = pygame.Rect(screen_width // 2 - paddle_width // 2, screen_height - 40, paddle_width, paddle_height)

# 공 설정
ball_radius = 10
ball_speed = [random.choice([-4, 4]), -4]
ball = pygame.Rect(screen_width // 2, screen_height // 2, ball_radius * 2, ball_radius * 2)

# 벽돌 설정
brick_rows = 5
brick_cols = 10
brick_width = screen_width // brick_cols
brick_height = 30
bricks = []
for row in range(brick_rows):
    for col in range(brick_cols):
        brick = pygame.Rect(col * brick_width, row * brick_height, brick_width, brick_height)
        bricks.append(brick)

# 게임 루프
running = True
clock = pygame.time.Clock()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 패들 이동
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and paddle.left > 0:
        paddle.move_ip(-6, 0)
    if keys[pygame.K_RIGHT] and paddle.right < screen_width:
        paddle.move_ip(6, 0)

    # 공 이동
    ball.move_ip(ball_speed)

    # 공 충돌 처리
    if ball.left <= 0 or ball.right >= screen_width:
        ball_speed[0] = -ball_speed[0]
    if ball.top <= 0:
        ball_speed[1] = -ball_speed[1]
    if ball.colliderect(paddle):
        ball_speed[1] = -ball_speed[1]

    # 벽돌 충돌 처리
    for brick in bricks[:]:
        if ball.colliderect(brick):
            ball_speed[1] = -ball_speed[1]
            bricks.remove(brick)
            break

    # 화면 그리기
    screen.fill(BLACK)
    pygame.draw.rect(screen, WHITE, paddle)
    pygame.draw.ellipse(screen, RED, ball)
    for brick in bricks:
        pygame.draw.rect(screen, BLUE, brick)
    pygame.display.flip()

    # 게임 종료 조건
    if ball.bottom >= screen_height:
        running = False

    clock.tick(60)

pygame.quit()
sys.exit()
