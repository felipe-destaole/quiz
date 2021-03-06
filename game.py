import pygame as pg
import os
from data.settings import *
from data.util import Alternativas, Botao, Pergunta

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

        self.perguntas = [
            Pergunta("pergunta1", Alternativas.A),
            Pergunta("pergunta2", Alternativas.B),
            Pergunta("pergunta3", Alternativas.D),
            Pergunta("pergunta4", Alternativas.A),
            Pergunta("pergunta5", Alternativas.C),
            Pergunta("pergunta6", Alternativas.B),
            Pergunta("pergunta7", Alternativas.D),
            Pergunta("pergunta8", Alternativas.A),
            Pergunta("pergunta9", Alternativas.A),
            Pergunta("pergunta10", Alternativas.B),
        ]
        
        self.numero_pergunta = 0
        self.pontuacao = 0
        self.pergunta_atual = self.perguntas[0]
        self.botoes_aletrnativa = [
            Botao("A", MARGEM_BOTAO, ALTURA_ENUNCIADO + MARGEM_BOTAO, LARGURA_BOTAO, ALTURA_BOTAO),
            Botao("B", 1.5*MARGEM_BOTAO + LARGURA_BOTAO, ALTURA_ENUNCIADO + MARGEM_BOTAO, LARGURA_BOTAO, ALTURA_BOTAO),
            Botao("C", MARGEM_BOTAO, ALTURA_ENUNCIADO + 1.5*MARGEM_BOTAO + ALTURA_BOTAO, LARGURA_BOTAO, ALTURA_BOTAO),
            Botao("D", 1.5*MARGEM_BOTAO + LARGURA_BOTAO, ALTURA_ENUNCIADO + 1.5*MARGEM_BOTAO + ALTURA_BOTAO, LARGURA_BOTAO, ALTURA_BOTAO),
        ]

        self.font_name = pg.font.match_font(FONT_NAME)

    def run(self):
        # Game Loop
        self.playing = True
        self.acertou = -1
        while self.playing:
            self.clock.tick(FPS)
            self.events()
            self.draw()
        return self.acertou

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

            if event.type == RESPOSTA_CERTA:
                self.pontuacao += 1
                self.acertou = 1
                self.playing = False
                self.proxima_questao()

            if event.type == RESPOSTA_ERRADA:
                self.acertou = 0
                self.playing = False
                self.proxima_questao()

    def draw(self):
        self.win.fill(BGCOLOR)

        self.pergunta_atual.draw(self.win)
        self.draw_text(f"Pontua????o: {self.pontuacao}", 22, BRANCO, WIDTH - 60, 5)

        for botao in self.botoes_aletrnativa:
            botao.draw(self.win)

        pg.display.update()

    def escolher_respota(self, mouse_pos):
        x, y = mouse_pos
        if MARGEM_BOTAO <= x <= MARGEM_BOTAO + LARGURA_BOTAO and ALTURA_ENUNCIADO + MARGEM_BOTAO <= y <= HEIGHT - 1.5*MARGEM_BOTAO - ALTURA_BOTAO:
            return Alternativas.A
        if 1.5*MARGEM_BOTAO + LARGURA_BOTAO <= x <= WIDTH - MARGEM_BOTAO and ALTURA_ENUNCIADO + MARGEM_BOTAO <= y <= HEIGHT - 1.5*MARGEM_BOTAO - ALTURA_BOTAO:
            return Alternativas.B
        if MARGEM_BOTAO <= x <= MARGEM_BOTAO + LARGURA_BOTAO and HEIGHT - MARGEM_BOTAO - ALTURA_BOTAO <= y <= HEIGHT - MARGEM_BOTAO:
            return Alternativas.C
        if 1.5*MARGEM_BOTAO + LARGURA_BOTAO <= x <= WIDTH - MARGEM_BOTAO and HEIGHT - MARGEM_BOTAO - ALTURA_BOTAO <= y <= HEIGHT - MARGEM_BOTAO:
            return Alternativas.D

    def verificar_resposta(self, alternativa):
        if not alternativa:
            return
        if alternativa == self.pergunta_atual.resposta:
            pg.event.post(pg.event.Event(RESPOSTA_CERTA))
        else:
            pg.event.post(pg.event.Event(RESPOSTA_ERRADA))

    def proxima_questao(self):
        self.numero_pergunta += 1
        if self.numero_pergunta >= len(self.perguntas):
            self.running = False
            return
        self.pergunta_atual = self.perguntas[self.numero_pergunta]

    def tela_comeco(self):
        # game splash/start screen
        self.win.fill(BGCOLOR)
        self.draw_text("M??TODOS DE ESTUDO", 48, BRANCO, WIDTH / 2, HEIGHT / 4)
        self.draw_text("Regras: acerte as perguntas", 22, BRANCO, WIDTH / 2, HEIGHT * 3 / 5)
        self.draw_text("Grupo: Felip??o, Davi, Dosseau, Ot??vio e Beri Beri", 22, BRANCO, WIDTH / 2, HEIGHT * 3 / 5 + 30)
        self.draw_text("Objetivo: entender sobre boas praticas de estudo e conhecer novos m??todos de estudo", 22, BRANCO, WIDTH / 2, HEIGHT * 3 / 5 + 60)
        self.draw_text(
            "Aperte qualquer tecla para come??ar", 22, BRANCO, WIDTH / 2, HEIGHT * 3 / 4
        )
        pg.display.flip()
        self.wait_for_key()

    def tela_prox_pergunta(self, acertou=False):
        # game splash/start screen
        cor = VERDE if acertou else VERMELHO
        frase = (
            "Parabens, voc?? acertou! Continue assim"
            if acertou
            else "Que pena, voc?? errou, tente novamente"
        )
        self.win.fill(cor)
        self.draw_text("M??TODOS DE ESTUDO", 48, BRANCO, WIDTH / 2, HEIGHT / 4)
        self.draw_text(frase, 22, BRANCO, WIDTH / 2, HEIGHT * 2 / 4)
        self.draw_text(
            "Aperte qualquer tecla para ir para a proxima quest??o",
            22,
            BRANCO,
            WIDTH / 2,
            HEIGHT * 3 / 4,
        )
        pg.display.flip()
        self.wait_for_key()

    def game_over(self):
        cor = (234, 195, 78)
        frase = f"Parabens, voc?? acertou {self.pontuacao} de {len(self.perguntas)}! Continue assim"
        self.win.fill(cor)
        self.draw_text("M??TODOS DE ESTUDO", 48, BRANCO, WIDTH / 2, HEIGHT / 4)
        self.draw_text(frase, 22, BRANCO, WIDTH / 2, HEIGHT * 2 / 4)
        self.draw_text(
            "Obrigado por jogar!",
            22,
            BRANCO,
            WIDTH / 2,
            HEIGHT * 3 / 4,
        )
        pg.display.flip()
        waiting = True
        while waiting:
            self.clock.tick(FPS)
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    waiting = False
                    self.running = False

    def draw_text(self, text, size, color, x, y):
        font = pg.font.Font(self.font_name, size)
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect()
        text_rect.midtop = (x, y)
        self.win.blit(text_surface, text_rect)

    def wait_for_key(self):
        waiting = True
        while waiting:
            self.clock.tick(FPS)
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    waiting = False
                    self.running = False
                if event.type == pg.KEYUP:
                    waiting = False


if __name__ == "__main__":
    game = Game()
    game.tela_comeco()
    while game.running:
        acertou = game.run()
        if acertou != -1:
            game.tela_prox_pergunta(acertou)
    game.game_over()
    pg.quit()
