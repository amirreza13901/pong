import pygame
import sys
from paddle import paddle
from ball import ball 
from bot import bot
pygame.init()
pygame.mixer.init()
#music
pygame.mixer.music.load("assets/bgm.mp3")
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(0.5)
player_score = 0
bot_score = 0
sound = pygame.mixer.Sound('assets/hitting.wav')

#window
win_w, win_h = 1000,600
win = pygame.display.set_mode((win_w, win_h))
pygame.display.set_caption('PONG')
ball_cords_x, ball_cords_y=496, 252

paddle1 = paddle(948, 250,win)
ball = ball(win, ball_cords_x, ball_cords_y, 18, sound)
bot1 = bot(38, 250, win)
#photos
bg = pygame.image.load('assets/bg.png').convert_alpha()
score_font = pygame.font.Font('assets/font.ttf', 20)

def show_bg():
    bg_transform = pygame.transform.scale(bg, (win_w,win_h))
    win.blit(bg_transform, (0,0))



def bg_remove(win_w, win_h):
    fill_object = pygame.Rect(0, 0, win_w, win_h)
    pygame.Surface.fill(win, (255,255,255), fill_object)

    

def board_text(text, font, text_color, x, y):
    text_to_img = font.render(text, True, text_color)
    win.blit(text_to_img, (x, y))






def ball_go_over_player(win_width):
    con = False
    if ball.ball_base.x >= win_width:
        con=True
        ball.reset=True

        
    return con
def ball_go_over_bot(win_width):
    con = False
    if ball.ball_base.x <= 0:
        con=True
        ball.reset=True

        
    return con

def check_who_won(player_score, bot_score):
    if player_score>=5:
        pygame.display.set_caption('PLAYER WON')
        return 1
    if bot_score>=5:
        pygame.display.set_caption('BOT WON')
        return 2



clock = pygame.time.Clock()
fps = 60


#game loop
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    paddle1.move(win_w,win_h,win)
    ball.move(win_w, win_h, paddle1, bot1)
    bot1.move(win_w, win_h, ball)
    show_bg()
    if ball_go_over_player(win_w):
        player_score+=1
        ball.ball_reset_check(ball_cords_x, win_h)

    if ball_go_over_bot(win_w):
        bot_score+=1
        ball.ball_reset_check(ball_cords_x, win_h)
    




    result = check_who_won(player_score, bot_score)
    if result==1 or result==2:
        bg_remove(win_w, win_h)
        if result==1:
            board_text(str(f'player won {player_score} to {bot_score}'), score_font, (0,0,0), win_w//2 , win_h // 12)
        if result==2:
            board_text(str(f'bot won {bot_score} to {player_score}'), score_font, (0,0,0), win_w//2 , win_h // 12)



    paddle1.draw(win)
    ball.draw(win)
    bot1.draw(win)
    board_text(str(player_score), score_font, (255,255,255), win_w-120 , win_h / 12)
    board_text(str(bot_score), score_font, (255,255,255), 120 , win_h / 12)




    pygame.display.update()
    if result == 1 or result==2:
        pygame.time.wait(3000)
        run = False



    clock.tick(fps)

pygame.quit()