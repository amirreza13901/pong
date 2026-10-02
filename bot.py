import pygame

class bot:
    def __init__(self, x, y, surface):
        self.bot_base = pygame.Rect(x, y, 25, 100)
    
    
    
    def move(self, win_width, win_height, ball):
        distance = ball.ball_base.centery - self.bot_base.centery
        add_y=distance * 0.09
        speed=10
        # dead_zone = 50
        bg_space_top = 28
        bg_space_bottom_with_win_height = win_height-46


        #ai logic
        # if ball.ball_base.centery >= self.bot_base.centery+ dead_zone:
        #     add_y+=speed


        # if ball.ball_base.centery < self.bot_base.centery - dead_zone:
        #     add_y-=speed

        if add_y > speed:
             add_y=speed

        if add_y < -speed:
             add_y=-speed


        #boundary logic     
        if self.bot_base.top <=bg_space_top:
            self.bot_base.top =bg_space_top
             
             
        if self.bot_base.bottom>=bg_space_bottom_with_win_height:
            self.bot_base.bottom=bg_space_bottom_with_win_height

    


             
        #add all             
        self.bot_base.y+=add_y
             

    def draw(self, surface):
            pygame.draw.rect(surface, (240,240,240), self.bot_base)
