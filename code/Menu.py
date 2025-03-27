import pygame

from code.Const import WIN_WIDTH, COLOR_ORANGE, MENU_OPTION, COLOR_WHITE


class Menu:
    def __init__(self, window):
        pygame.init()
        pygame.font.init()
        pygame.mixer.init()

        self.window = window
        self.surf = pygame.image.load('./asset/MenuBg.png')
        self.rect = self.surf.get_rect(left=0, top=0)

    def run(self):
        pygame.mixer.music.load('./asset/Menu.mp3')
        pygame.mixer.music.play(-1)

        running = True
        while running:
            self.window.blit(self.surf, self.rect)
            self.menu_text(text_size=50, text="Mountain", text_color=COLOR_ORANGE, text_center_pos=((WIN_WIDTH / 2), 70))
            self.menu_text(text_size=50, text="Shooter", text_color=COLOR_ORANGE, text_center_pos=((WIN_WIDTH / 2), 120))

            for i in range(len(MENU_OPTION)):
                self.menu_text(text_size=20, text=MENU_OPTION[i], text_color=COLOR_WHITE, text_center_pos=((WIN_WIDTH / 2), 200 + 25 * i))

            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

        pygame.quit()
        quit()

    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: pygame.font.Font = pygame.font.SysFont("Lucida Sans Typewriter", text_size)
        text_surf: pygame.Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: pygame.Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(text_surf, text_rect)