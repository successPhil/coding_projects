import pygame # import pygame lib and get exit from sys for while loop
from sys import exit
from random import randint

#Create function for movement
def obstacle_movement(obstacle_list):
   if obstacle_list:
     for obstacle_rect in obstacle_list:
         obstacle_rect.x -= 5
         if obstacle_rect.bottom == 300: screen.blit(blue_ball_surf, obstacle_rect)
         else: screen.blit(red_ball_surf, obstacle_rect)

     obstacle_list = [obstacle for obstacle in obstacle_list if obstacle.x > 0]
     return obstacle_list
   else:
       return []
   

#Create function for score
def display_score():
  current_time = int(pygame.time.get_ticks()/ 1000) - start_time #gets time in milliseconds
  #since current time is an integer and render expects a string for the first parameter
  #we convert current time into an f string
  #first need font to render text, then surface/rectangle to put text on
  score_font = pygame.font.Font(None, 30)
  score_surf = score_font.render(f'{current_time}', False, '#FEE511')
  score_rect = score_surf.get_rect(center = (400, 30))
  screen.blit(score_surf, score_rect)
  return current_time
pygame.init()

game_active = True #Use to allow on-off between game and menu
start_time = 0 #We will update this to the time game_active becomes false
screen = pygame.display.set_mode((800, 400)) #Create display surface **important**
pygame.display.set_caption('Runner') # Set caption for display
clock = pygame.time.Clock()
# import images, use .convert() / .convert_alpha() as needed
# quickly made these images for tutorial purposes using paint S
background_surf = pygame.image.load('pygametutorial_imgs/back_img.png').convert()
ground_surf = pygame.image.load('pygametutorial_imgs/ground_img.png').convert()
# create font for text surface if needed
#Create text rectangle for score

#Variable used to store initial load space of red ball and our bird object
#Create rectangles for bird and red ball
#Creating Enemy Objects

#Obstacle rect list
obstacle_rect_list = []
blue_ball_surf = pygame.image.load('pygametutorial_imgs/blue_ball_img.png').convert_alpha()
blue_ball_rect = blue_ball_surf.get_rect(midbottom = (700, 300))

red_ball_surf = pygame.image.load('pygametutorial_imgs/red_ball_img.png').convert_alpha()
red_ball_rect = red_ball_surf.get_rect(midbottom = (600, 220))
#Creating Player Objects
bird_surf = pygame.image.load('pygametutorial_imgs/player_bird_img.png').convert_alpha()
bird_rect = bird_surf.get_rect(midbottom = (50, 215))
#Intro screen
big_bird = pygame.transform.rotozoom(bird_surf, 0, 5)
big_bird_rect = big_bird.get_rect(center = (400, 160))

score = 0
text_font = pygame.font.Font(None, 50)
game_name = text_font.render('Clucky or not!', False, '#A811FE' )
game_name_rect = game_name.get_rect(center = (400, 60))
game_message = text_font.render('Press space to run', False, '#A811FE')
game_message_rect = game_message.get_rect(center = (400, 360))
#Initially set player gravity to 0 for 'jump' mechanic
bird_gravity = 0

# Timer
obstacle_timer = pygame.USEREVENT + 1
pygame.time.set_timer(obstacle_timer, 1400)



# Create a loop that is always true to write code in for game
while True:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pygame.quit()
        exit()
    # draw all our elements here
    # if game is active allow 'space' or 'click' on character to 'jump'
      if game_active:
          if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and bird_rect.bottom >= 220:
              bird_gravity = -15

          if event.type == pygame.MOUSEBUTTONDOWN:
            if bird_rect.collidepoint(event.pos) and bird_rect.bottom >= 220: 
              bird_gravity = -20
      else:
          if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
             game_active = True
             start_time = int(pygame.time.get_ticks() / 1000)
        
    if event.type == obstacle_timer and game_active:
       if randint(0,2):
         obstacle_rect_list.append(blue_ball_surf.get_rect(midbottom = (randint(900, 1100), 400)))
       else:
         obstacle_rect_list.append(red_ball_surf.get_rect(midbottom = (randint(900, 1100), 135)))
    if game_active:
      screen.blit(background_surf, (0,0))
      screen.blit(ground_surf, (0, 210))
      screen.blit(bird_surf, (bird_rect))
      #screen.blit(blue_ball_surf, blue_ball_rect)
      #screen.blit(red_ball_surf, (red_ball_rect))
      score = display_score()

    #Obstacle movement
      obstacle_rect_list = obstacle_movement(obstacle_rect_list)
      
  
      bird_gravity += 1
      bird_rect.y += bird_gravity
  
  #Pretty cool way to draw line to mouse
      #pygame.draw.line(screen, 'Gold', (0, 0), pygame.mouse.get_pos(), 10)
      #Decreasing moves left, increasing moves right
      #red_ball_rect.left -= 4
      #bird_rect.left += 0
      #Updates position once red ball leaves screen
      if blue_ball_rect.left < -100: blue_ball_rect.left = 1000
      if red_ball_rect.left < -100: red_ball_rect.left = 800
      if bird_rect.left > 900: bird_rect.left = -100
      if bird_rect.bottom >= 220: bird_rect.bottom = 220
       #screen.blit(score_surf, (score_rect))
#Collision
      if red_ball_rect.colliderect(bird_rect):
        game_active = False
        
    
    else:
      screen.fill('#33F8FF')
      screen.blit(big_bird, big_bird_rect)
      screen.blit(game_name, game_name_rect)
      #Create message to start game or update user with best score
      if score == 0:
        screen.blit(game_message, game_message_rect)
      else:
        score_message = text_font.render(f'Your best score was {score}', False, '#A811FE')
        score_message_rect = score_message.get_rect(center = (400, 360))
        screen.blit(score_message, score_message_rect)
        


    pygame.display.update()
    clock.tick(60)