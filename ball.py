import pygame
import random
class ball:
    def __init__(self, surface, x, y, size, sound):
        self.ball_base = pygame.Rect(x, y, size, size)
        self.dx = random.choice([-4,4])
        self.dy = random.choice([-4,4])
        self.hit_bottom = False
        self.hit_top = False
        # self.player_score=0
        self.reset=False
        self.sound = sound




    def move(self, win_width, win_height, paddle, bot):
        self.ball_base.y+=self.dy
        self.ball_base.x+=self.dx
        bg_space_top = 28
        bg_space_bottom_with_win_height = win_height-46


        if self.ball_base.top <=bg_space_top:
                 self.ball_base.top =bg_space_top
                 self.dy *= -1


        if self.ball_base.bottom>=bg_space_bottom_with_win_height:
             self.ball_base.bottom=bg_space_bottom_with_win_height
             self.dy *= -1
        
        # Assuming your paddle is on the RIGHT side:
        if self.ball_base.colliderect(paddle.player_base):
            # Only bounce if the ball is moving RIGHT (dx > 0)
            if self.dx > 0: 
                self.dx *= -1 
                self.sound.play()
                # Snap the ball outside the paddle so it doesn't get stuck
                self.ball_base.right = paddle.player_base.left



        if self.ball_base.colliderect(bot.bot_base):
            # Only bounce if the ball is moving RIGHT (dx > 0)
            if self.dx < 0: 
                self.dx *= -1 
                self.sound.play()

                # Snap the ball outside the paddle so it doesn't get stuck
                self.ball_base.left = bot.bot_base.right
        
        


    def ball_reset_check(self,x,win_h):
        if self.reset:
            self.reset=False
            if self.ball_base.x > 500:
                self.dx = -4
            if self.ball_base.x <500:
                self.dx = 4   
            self.ball_base.y=random.randint(26, win_h-46)
            self.ball_base.x=x
            self.dy = random.choice([-4,4])
      
        

    # def get_player_score(self, win_width, x, y):
    #     if self.ball_base.x >= win_width-50:
    #         self.player_score+=1
    #         self.ball_reset(x, y)
    #         self.reset=True
    #     if self.reset:
    #          self.ball_reset(x, y)
    #          self.reset=False
        
    #     return self.player_score


         


    def draw(self, surface):
        pygame.draw.rect(surface, (240,240,240), self.ball_base)