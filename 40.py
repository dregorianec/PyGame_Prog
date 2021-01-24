import pygame
class Button:
    def __init__(self, position, size, clr=(100, 100, 100), cngclr=None, func=None, text='', font="Segoe Print",
                 font_size=10, font_clr=(0, 0, 0)):
        self.clr = clr
        self.size = size/l9
        self.func = func
        self.surf = pygame.Surface(size)
        self.rect = self.surf.get_rect(center=position)

        if cngclr:
            self.cngclr = cngclr
        else:
            self.cngclr = clr

        if len(clr) == 4:
            self.surf.set_alpha(clr[3])
        self.font = pygame.font.SysFont(font, font_size)
        self.txt = text
        self.font_clr = font_clr
        self.txt_surf = self.font.render(self.txt, 1, self.font_clr)
        self.txt_rect = self.txt_surf.get_rect(center=[wh // 2 for wh in self.size])

    def draw(self, screen):
        self.mouseover()
        self.surf.fill(self.curclr)
        self.surf.blit(self.txt_surf, self.txt_rect)
        screen.blit(self.surf, self.rect)

    def mouseover(self):
        self.curclr = self.clr


elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                pos = pygame.mouse.get_pos()
                if pos[0] in range(enemy.coords()[0], enemy.coords()[0] + 72) and pos[1] in range(enemy.coords()[1],
                                                                                                  enemy.coords()[
                                                                                                      1] + 72) and pos[
                    0] in range(hero.coords()[0] - radius, hero.coords()[0] + radius + 72) and pos[1] in range(
                    hero.coords()[1] - radius, hero.coords()[1] + radius + 72) and shoot and k > 0:
                    h_e -= damage
                    k -= 1
                    shoot = False
                    f = True
                    # звук пердежа
                    hero.change_image()
                for b in button_list:
                    if b.rect.collidepoint(pos):
                        b.call_back()
