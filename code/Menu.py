import pygame

from code.Const import WIN_WIDTH, COLOR_BLACK, MENU_OPTION, COLOR_WHITE, COLOR_YELLOW


class Menu:
    def __init__(self, window):
        pygame.init()
        pygame.font.init()
        pygame.mixer.init()

        self.window = window
        self.surf = pygame.image.load('./asset/MenuBg.png').convert_alpha()
        self.rect = self.surf.get_rect(left=0, top=0)

    def run(self, ):
        menu_option = 0
        pygame.mixer.music.load('./asset/Menu.mp3')
        pygame.mixer.music.play(-1)

        running = True
        while running:
            self.window.blit(self.surf, self.rect)
            self.menu_text(text_size=50, text="Mountain", text_color=COLOR_BLACK, text_center_pos=((WIN_WIDTH / 2), 70))
            self.menu_text(text_size=50, text="War", text_color=COLOR_BLACK, text_center_pos=((WIN_WIDTH / 2), 120))

            for i in range(len(MENU_OPTION)):
                if i == menu_option:
                    self.menu_text(text_size=20, text=MENU_OPTION[i], text_color=COLOR_YELLOW, text_center_pos=((WIN_WIDTH / 2), 200 + 25 * i))
                else:
                    self.menu_text(text_size=20, text=MENU_OPTION[i], text_color=COLOR_WHITE, text_center_pos=((WIN_WIDTH / 2), 200 + 25 * i))

            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_DOWN:
                        if menu_option < len(MENU_OPTION) - 1:
                            menu_option += 1
                        else:
                            menu_option = 0
                    if event.key == pygame.K_UP:
                        if menu_option > 0:
                            menu_option -= 1
                        else:
                            menu_option = len(MENU_OPTION) - 1
                    if event.key == pygame.K_RETURN:
                        return MENU_OPTION[menu_option]

    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: pygame.font.Font = pygame.font.SysFont("Lucida Sans Typewriter", text_size)
        text_surf: pygame.Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: pygame.Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(text_surf, text_rect)