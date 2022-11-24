"""Snake Game"""
import random
import pygame


pygame.init()
display_width = 800
display_height = 500
gameWindow = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption("Snake Game")
font = pygame.font.SysFont(None, 40)
clock = pygame.time.Clock()
bgimg = pygame.image.load("bg.jpg")
bgimg = pygame.transform.scale(bgimg, (display_width, display_height))


def dipslay_text(text, color, x_value, y_value):
    """This function display text at window"""
    screen_text = font.render(text, True, color)
    gameWindow.blit(screen_text, [x_value, y_value])


def plot_snake(gameWindow, color, snake_list, snake_size):
    """This function plot snake"""
    for x, y in snake_list:
        pygame.draw.rect(gameWindow, 'black', [x, y, snake_size, snake_size])


def welcome():
    """This function display welcome page"""
    exit_game = False
    while not exit_game:
        gameWindow.blit(bgimg, (0, 0))
        dipslay_text("Welcome! to Snake Game", 'darkgreen', 150, 50)
        dipslay_text("Press Space To Play", 'darkgreen', 150, 100)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    gameloop()
        pygame.display.update()
        clock.tick(60)


def gameloop():
    """This function run gameloop"""
    with open("highscore.txt", 'r') as hi_scr:
        highscore = hi_scr.read()
    exit_game = False
    game_over = False
    snake_x = 45
    snake_y = 55
    velocity_x = 0
    velocity_y = 0
    snake_size = 20
    score = 0
    inital_x_velocity = 3
    inital_y_velocity = 3

    food_x = random.randint(20, display_width-20)
    food_y = random.randint(20, display_height-20)

    snake_list = []
    snake_length = 1

    while not exit_game:
        if game_over:
            with open("highscore.txt", "w") as f:
                f.write(highscore)
            gameWindow.fill('white')
            gameWindow.blit(bgimg, (0, 0))
            dipslay_text("Score: "+str(score), 'red', 350, 100)
            dipslay_text("Game over! press Enter to Continue",
                         'red', 170, display_height/1.3)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        gameloop()
        else:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        velocity_x = inital_x_velocity
                        velocity_y = 0
                    if event.key == pygame.K_LEFT:
                        velocity_x = -inital_x_velocity
                        velocity_y = 0
                    if event.key == pygame.K_DOWN:
                        velocity_y = inital_y_velocity
                        velocity_x = 0
                    if event.key == pygame.K_UP:
                        velocity_y = -inital_y_velocity
                        velocity_x = 0

            snake_x += velocity_x
            snake_y += velocity_y

            # logic to eat food and incease score
            if abs(snake_x - food_x) < 15 and abs(snake_y - food_y) < 15:
                score += 10
                food_x = random.randint(20, display_width-20)
                food_y = random.randint(20, display_height-20)
                snake_length += 5
                if score > int(highscore):
                    highscore = str(score)

                # incease velocity 
                inital_x_velocity += 0.1       
                inital_y_velocity += 0.1
                # print(inital_x_velocity,inital_y_velocity)

            gameWindow.fill(color='White')
            gameWindow.blit(bgimg, (0, 0))
            dipslay_text("Score: "+str(score)+"   Highest: " +
                         highscore, "blue", 5, 5)

            head = []
            head.append(snake_x)
            head.append(snake_y)
            snake_list.append(head)

            if len(snake_list) > snake_length:
                del snake_list[0]

            if head in snake_list[:-1]: #logic to over game if snake touch itself
                game_over = True

            if snake_x < 0 or snake_x > display_width or snake_y < 0 or snake_y > display_height: #logic to game over if snake touch walls
                game_over = True

            plot_snake(gameWindow, "balck", snake_list, snake_size)
            pygame.draw.circle(gameWindow, 'red',
                               [food_x, food_y], 10, 0)
        pygame.display.update()
        clock.tick(60)

    pygame.quit()
    quit()


welcome()
