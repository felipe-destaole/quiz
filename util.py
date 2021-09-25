import pygame as pg
import os
from enum import Enum
from settings import *


class Alternativas(Enum):
    A = 0
    B = 1
    C = 2
    D = 3
    
class Pergunta:
    def __init__(self, pergunta: str, alternativas: str, resposta: Alternativas):
        self.pergunta = pg.transform.scale(pg.image.load(os.path.join("assets", pergunta + '.png')), (WIDTH, 200))
        self.alternativas = pg.transform.scale(pg.image.load(os.path.join("assets", alternativas + '.png')), (WIDTH, 250))
        self.resposta = resposta

    def draw(self, win):
        win.blit(self.pergunta, (0,0))
        win.blit(self.alternativas, (0, 200))

class Botao():
    def __init__(self, image, x, y, width = 400, height = 175, certa = False):
        self.image = pg.transform.scale(pg.image.load(os.path.join("assets", image + '.png')), (width, height))
        self.x = x
        self.y = y
        self.width = width
        self.height = height
    
    def draw(self, win):
        win.blit(self.image, (self.x, self.y))

