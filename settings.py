import pygame as pg
import os

TITULO = "Quiz"
FONT_NAME = 'arial'
FPS = 60

BRANCO = (255, 255, 255)
VERMELHO = (255, 0, 0)
VERDE = (25,141,237)

BGCOLOR = (255, 0, 45)
WIDTH, HEIGHT = 900, 900

BOARD = pg.transform.scale(
    pg.image.load(os.path.join("assets", "pergunta1.png")), (WIDTH, HEIGHT)
)

# Eventos

RESPOSTA_CERTA = pg.USEREVENT + 1
RESPOSTA_ERRADA = pg.USEREVENT + 2