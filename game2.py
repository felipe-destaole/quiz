import pygame as pg
import os
from settings import *
from util import Alternativas, Botao, Pergunta


pg.init()


class Game:
    def __init__(self):
        pg.init()
        self.w = WIDTH
        self.h = HEIGHT
        self.win = pg.display.set_mode((self.w, self.h))
        pg.display.set_caption(TITULO)
        self.clock = pg.time.Clock()
        self.running = True

        self.perguntas = [Pergunta("pergunta1", "resposta1", Alternativas.A)]
        self.numero_pergunta = 0
        self.pergunta_atual = self.perguntas[0]
        self.botoes_aletrnativa = [
            Botao("alternativa1", 40, 490),
            Botao("alternativa1", 40, 685),
            Botao("alternativa1", 460, 490),
            Botao("alternativa1", 460, 685),
        ]

        self.font_name = pg.font.match_font(FONT_NAME)

    def new(self):
        self.run()

    def run(self):
        # Game Loop
        self.playing = True
        while self.playing:
            self.clock.tick(FPS)
            self.events()
            self.draw()

    def events(self):
        # Game Loop - events
        for event in pg.event.get():
            # check for closing window
            if event.type == pg.QUIT:
                if self.playing:
                    self.playing = False
                self.running = False
            if event.type == pg.MOUSEBUTTONUP:
                pos = pg.mouse.get_pos()
                alternativa = self.escolher_respota(pos)
                self.verificar_resposta(alternativa)
                
    def draw(self):
        self.win.fill(BRANCO)

        self.pergunta_atual.draw(self.win)
        
        for botao in self.botoes_aletrnativa:
            botao.draw(self.win)
            
        pg.display.update()
        
    def escolher_respota(self, mouse_pos):
        x, y = mouse_pos
        if 40 <= x <= 440 and 490 <= y <= 665:
            return Alternativas.A
        if 460 <= x <= 860 and 490 <= y <= 665:
            return Alternativas.B
        if 40 <= x <= 440 and 685 <= y <= 860:
            return Alternativas.C
        if 460 <= x <= 860 and 685 <= y <= 860:
            return Alternativas.D
        
    def verificar_resposta(self, alternativa):
        if alternativa == self.pergunta_atual.resposta:
            print("resposta correta")
        else:
            print("resposta errada")

    def show_start_screen(self):
        # game splash/start screen
        self.win.fill(BGCOLOR)
        self.draw_text('MÉTODOS DE ESTUDO', 48, BRANCO, WIDTH / 2, HEIGHT / 4)
        self.draw_text("Aperte qualquer tecla para começar", 22, BRANCO, WIDTH / 2, HEIGHT * 3 / 4)
        pg.display.flip()
        self.wait_for_key()
        
    def draw_text(self, text, size, color, x, y):
        font = pg.font.Font(self.font_name, size)
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect()
        text_rect.midtop = (x, y)
        self.win.blit(text_surface, text_rect)
    
    def wait_for_key(self):
        waiting = True
        while waiting:
            self.clock.tick(60)
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    waiting = False
                    self.running = False
                if event.type == pg.KEYUP:
                    waiting = False
                    
if __name__ == "__main__":
    game = Game()
    game.show_start_screen()
    while game.running:
        print(game.running)
        game.new()
        # game.show_go_screen()
    pg.quit()