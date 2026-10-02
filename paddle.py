import pygame



class paddle:
    def __init__(self, x, y, surface):
        self.player_base = pygame.Rect(x, y, 25, 100)

    def move(self, win_width, win_height, surface):
        add_y=0
        speed=8
        bg_space_top = 28
        bg_space_bottom_with_win_height = win_height-46

        keyboard = pygame.key.get_pressed()
        if keyboard[pygame.K_UP]:
            if self.player_base.top>bg_space_top:
                add_y-=speed

        if keyboard[pygame.K_DOWN]:
            if self.player_base.bottom<bg_space_bottom_with_win_height:           
                add_y+=speed


        if self.player_base.top <=bg_space_top:
            self.player_base.top =bg_space_top


        if self.player_base.bottom>=bg_space_bottom_with_win_height:
            self.player_base.bottom=bg_space_bottom_with_win_height


        self.player_base.y+=add_y

    def draw(self, surface):
        pygame.draw.rect(surface, (240,240,240), self.player_base)


