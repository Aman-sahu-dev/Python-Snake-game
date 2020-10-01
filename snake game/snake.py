# SNAKE GAME
# -----DATE 26-JUN-2020------
# NOTE: To run this game you need install pygame module in your compiler by simply typing in command pront show below
# Type : "pip install pygame"
# Than you can run the code directly
#                                                     LET'S START

# import modules
import pygame
import random
import os

pygame.mixer.init()                                                               #---->for music and background image

pygame.init()                                                                     #---->intialise pygame module

# create game window
screen_width = 900                                                                #----->screen_width
screen_height = 500                                                               #----->screen_height
game_window = pygame.display.set_mode((screen_width,screen_height))               #-----> it will create a window or a canvas

#Colors
white = (255, 255, 255)                                                           #----->colors
red = (255, 0, 0)
black = (0, 0, 0)
sky_blue = (0,229,238)

#background image                              
bgimg = pygame.image.load("D:\\code\\snake game\\p3.webp")                                             #----->it will load image on your variable
bgimg = pygame.transform.scale(bgimg,(screen_width,screen_height)).convert_alpha()#-----> it will adjust or resize your image as your window size


# Game Title
pygame.display.set_caption("Snakes with AMAN")                                   #-----> title of the game
pygame.display.update()

# FONT
font = pygame.font.SysFont(None,30)                                              #------>font for text we put in window
clock = pygame.time.Clock()

def text_screen(text,color,x,y):                                                 #------>function for printing text sms on screen
    screen_text = font.render(text,True,color)
    game_window.blit(screen_text,[x,y])                                         #------> it will update screen

def plot_snake(game_window,color,snk_list,snake_size):                         #-----> function for ploting snake   
    for x,y in snk_list:
        pygame.draw.rect(game_window,color,[x,y, snake_size, snake_size])       #---->it will create intial snake rectangle
        
def welcome():                                                                  #---->it will show welcome page
    exit_game = False
    while not exit_game:
        game_window.fill((234,240,190))                                         #-----> it will fill color in your window
        text_screen("WELCOME TO SNAKES WITH AMAN", black,220,230)
        text_screen("Press Space Bar To Play", black,280,260)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    pygame.mixer.music.load("D:\\code\\snake game\\bm.mp3")
                    pygame.mixer.music.play()
                    game_loop()

        pygame.display.update()
        clock.tick(60)


# GAME LOOP
def game_loop():
    # game specific variables

    exit_game = False
    game_over = False

    snake_x = 45
    snake_y = 45
    snake_size = 10
    velocity_x = 0
    velocity_y = 0
    init_velocity = 3
    
    score = 0
    fps = 60
    food_x = random.randint(20,screen_width/2)
    food_y = random.randint(30,screen_height/2)
    
    snk_list= []
    snk_length = 1
    #check if high_score file already exist or not in the system
    if(not os.path.exists("high_score.txt")):                      #---->it will directly create high_score file if you dont have
        with open("high_score.txt",'w') as f:
            f.write("0")

    with open('high_score.txt','r') as f:                         #----->if you already have file then it will directly read the intial highscore
        hiscore = f.read()

    while not exit_game:                                         #-----> game starts
        if game_over:
            with open('high_score.txt','w') as f:                #---->if game over it will save your highscore
                f.write(str(hiscore))
            game_window.fill(sky_blue)
            text_screen("GAME OVER ! press enter to continue",red, 250,200)
            text_screen("SCORE :" + str(score),red, 280,250)
        
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True
                
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:           #---> it will take you to game start window
                        welcome()


        else:                                                  #----> if game is not over then it will take input by keyboard
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True
                
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        velocity_x = init_velocity
                        velocity_y =0

                    if event.key == pygame.K_LEFT:
                        velocity_x = -init_velocity
                        velocity_y =0

                    if event.key == pygame.K_UP:
                        velocity_y = -init_velocity
                        velocity_x =0

                    if event.key == pygame.K_DOWN:
                        velocity_y = init_velocity
                        velocity_x =0

            snake_x = snake_x + velocity_x                                       #----->snake will move with velocity given to it
            snake_y += velocity_y

            if abs(snake_x - food_x)<5 and abs(snake_y - food_y)<5:              #----> to eat food if it is approx cross eachother
                score+=10 
                text_screen("Score : " + str(score),red,5,5)                     #----> print your score on screen
                food_x = random.randint(0,screen_width/2)
                food_y = random.randint(0,screen_height/2)
                snk_length+=5                                                    #----> it will increse length everytime when it eat the food
                if score>int(hiscore):
                    hiscore = score


            game_window.fill(white)
            game_window.blit(bgimg,(0,0))                                       #---> it will fill white color in board
            text_screen("Score : " + str(score) + "  Highscore : " + str(hiscore),red,5,5)           #----> it will print score
            plot_snake(game_window,black,snk_list,snake_size)                    # it is function used for make snake

            head = []                                                            #--------->this is for intial head of a snake in snk_list
            head.append(snake_x)
            head.append(snake_y)
            snk_list.append(head)                                                #----> this will append coordinates as loop runs

            if len(snk_list)>snk_length:                                         # ---->  this will delete the head if its length of list is more than length of snake..
                del snk_list[0]
            
            if head in snk_list[:-1]:                                            #-----> it will gameover  when your head touch your body
                game_over = True
                pygame.mixer.music.load('D:\\code\\snake game\\gameover.mp3')                          #----->it will load song
                pygame.mixer.music.play()                                        #-----> it will play song

            
            if snake_x<0 or snake_x>screen_width or snake_y<0 or snake_y>screen_height:#----> it will gameover when your snake touches the boundaries
                game_over =True
                pygame.mixer.music.load('D:\\code\\snake game\\gameover.mp3')                          #----->it will load song
                pygame.mixer.music.play()                                        #----->it will play song


            pygame.draw.rect(game_window,red,[food_x, food_y, snake_size, snake_size])#----> it will create food
        pygame.display.update()
        clock.tick(fps)                                                           #---->manage clock time of frame rate per second
    pygame.quit()
    quit()

welcome()

#  .................THANKS FOR PLAYING GAME....................