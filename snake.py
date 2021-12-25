import pygame, sys, time, random


snake_speed = 15


#game window size
window_size_x = 1380
window_size_y = 840


# a debug tester
check_errors = pygame.init()

# making an exception if error

if (check_errors[1] > 0):
    print("error " + check_errors[1])
else:
    print("game works")


# window title
pygame.display.set_caption("Snake Python")

#making window with sizes

game_window = pygame.display.set_mode((window_size_x, window_size_y))


#color intialization

black = pygame.Color(0,0,0)
white = pygame.Color(255,255,255)
red = pygame.Color(255,0,0)
green = pygame.Color(0,255,0)
blue = pygame.Color(0,0,255)

# ... todo
fps_control = pygame.time.Clock()

square_size = 60


#function to initiaz the vars

def init_vars():
    global head_pos,snake_body,food_pos,food_spawn,score,direction
    #not sure .. todo
    direction = "RIGHT"
    # todo, fix
    head_pos = [120,60]
    snake_body = [[120,60]]
    food_pos = [random.randrange(1,(window_size_x // square_size) * square_size),
                random.randrange(1,(window_size_y // square_size) * square_size)]
    food_spawn = True
    #starting score
    score = 0


init_vars()



#need to show score

def show_score(choice, color,font,size):
    score_font = pygame.font.SysFont(font,size)
    score_surface = score_font.render("Score: " + str(score) , True, color)
    score_rect = score_surface.get_rect()


    # check choices

    if choice == 1:
        score_rect.midtop = (window_size_x / 10, 15)

    else:
        score_rect.midtop = (window_size_x / 2, window_size_y/1.25)

    game_window.blit(score_surface, score_rect)


# game loop



while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if ( event.key  == pygame.K_UP or event.key == ord("w")
                and direction != "DOWN"):
                direction = "UP"
            elif ( event.key  == pygame.K_DOWN or event.key == ord("s")
                    and direction != "UP"):
                    direction = "DOWN"
            elif ( event.key  == pygame.K_LEFT or event.key == ord("a")
                    and direction != "RIGHT"):
                    direction = "LEFT"
            elif ( event.key  == pygame.K_RIGHT or event.key == ord("d")
                    and direction != "LEFT"):
                    direction = "RIGHT"

    if direction == "UP":
        head_pos[1] -= square_size

    elif direction == "DOWN":
        head_pos[1] += square_size
    elif direction == "LEFT":
        head_pos[0] -= square_size
    else:
        head_pos[0] += square_size
        
    if head_pos[0] < 0:
        head_pos[0] = window_size_x - square_size
    elif head_pos[0] > window_size_x - square_size:
        head_pos[0] = 0
    elif head_pos[1] < 0:
        head_pos[1] = window_size_y - square_size
    elif head_pos[1] > window_size_y - square_size:
        head_pos[1] = 0

    # eat apple
    snake_body.insert(0, list(head_pos))
    if head_pos[0] == food_pos[0] and head_pos[1] == food_pos[1]:
        score += 1
        #todo check if possible
        food_spawn = False
    else:
        snake_body.pop()


    #spawn food 
    if not food_spawn:
        food_pos = [random.randrange(1, (window_size_x // square_size)) * square_size,
                    random.randrange(1, (window_size_y // square_size)) * square_size]
        food_spawn

    #graphics

    game_window.fill(black)

    for pos in snake_body:
        pygame.draw.rect(game_window, green,pygame.Rect(pos[0] + 2, pos[1] + 2. square_size - 2, square_size -2))

    pygame.draw.rect(game_window,red,pygame.Rect(food_pos[0] , food_pos[1], square_size,square_size))

    #game over conditions

    for block in snake_body[1:]:
        if head_pos[0] == block[0] and head_pos[1] == block[1]:
            init_vars()
    

    show_score(1,white,'.....' , 20)
    pygame.display.update()
    fps_control.tick(snake_speed)

        
