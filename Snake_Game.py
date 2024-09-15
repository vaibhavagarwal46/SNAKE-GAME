import pygame
import random

def initialize_pygame():
    try:
        pygame.init()
        pygame.display.set_mode((1, 1))
    except Exception as e:
        print(f"Failed to initialize pygame: {e}")
        quit()

def create_game_window(width, height):
    try:
        screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption('Snake Game')
        return screen
    except Exception as e:
        print(f"Failed to create game window: {e}")
        quit()

def load_fonts():
    try:
        font_style = pygame.font.SysFont("calibri", 50)
        score_font = pygame.font.SysFont("calibri", 20)
        return font_style, score_font
    except Exception as e:
        print(f"Failed to load fonts: {e}")
        quit()

def Your_score(score, screen, score_font):
    try:
        value = score_font.render("Your Score: " + str(score), True, (0, 0, 0))
        screen.blit(value, [0, 0])
    except Exception as e:
        print(f"Failed to display score: {e}")

def snake(snake_block, snake_list, screen):
    try:
        for x in snake_list:
            pygame.draw.rect(screen, (0, 255, 0), [x[0], x[1], snake_block, snake_block])
    except Exception as e:
        print(f"Failed to draw snake: {e}")

def message(msg, color, screen, font_style, width, height):
    try:
        mesg = font_style.render(msg, True, color)
        screen.blit(mesg, [width / 6, height / 3])
    except Exception as e:
        print(f"Failed to display message: {e}")

def handle_events(x1_change, y1_change):
    try:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False, x1_change, y1_change
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    return True, -10, 0
                elif event.key == pygame.K_RIGHT:
                    return True, 10, 0
                elif event.key == pygame.K_UP:
                    return True, 0, -10
                elif event.key == pygame.K_DOWN:
                    return True, 0, 10
        return True, x1_change, y1_change
    except Exception as e:
        print(f"Failed to handle events: {e}")
        return False, x1_change, y1_change

def generate_food_position(width, height, snake_block):
    try:
        foodx = round(random.randrange(0, width - snake_block) / 10.0) * 10.0
        foody = round(random.randrange(0, height - snake_block) / 10.0) * 10.0
        return foodx, foody
    except Exception as e:
        print(f"Failed to generate food position: {e}")

def gameLoop():
    try:
        width, height = 600, 400
        screen = create_game_window(width, height)
        font_style, score_font = load_fonts()
        clock = pygame.time.Clock()

        snake_block = 10
        snake_speed = 15

        game_close = False

        x1 = width / 2
        y1 = height / 2
        x1_change = 0
        y1_change = 0

        snake_List = []
        Length_of_snake = 1

        foodx, foody = generate_food_position(width, height, snake_block)

        while True:
            while game_close:
                screen.fill((0, 0, 0))
                message("You Lost!", (255, 0, 0), screen, font_style, width, height)
                Your_score(Length_of_snake - 1, screen, score_font)
                pygame.display.update()

                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_q:
                            pygame.quit()
                            quit()
                        elif event.key == pygame.K_c:
                            gameLoop()

            running, x1_change, y1_change = handle_events(x1_change, y1_change)
            if not running:
                break

            x1 += x1_change
            y1 += y1_change

            if x1 >= width:
                x1 = 0
            elif x1 < 0:
                x1 = width - snake_block

            if y1 >= height:
                y1 = 0
            elif y1 < 0:
                y1 = height - snake_block

            screen.fill((255, 255, 255))

            pygame.draw.rect(screen, (0, 0, 0), [foodx, foody, snake_block, snake_block])

            snake_Head = [x1, y1]
            snake_List.append(snake_Head)
            if len(snake_List) > Length_of_snake:
                del snake_List[0]

            for x in snake_List[:-1]:
                if x == snake_Head:
                    game_close = True

            snake(snake_block, snake_List, screen)
            Your_score(Length_of_snake - 1, screen, score_font)

            pygame.display.update()

            if x1 == foodx and y1 == foody:
                foodx, foody = generate_food_position(width, height, snake_block)
                Length_of_snake += 1

            clock.tick(snake_speed)

    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        pygame.quit()

if __name__ == "__main__":
    initialize_pygame()
    gameLoop()
