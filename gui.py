import os
import sys

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

import pygame

from jogo_da_velha import criar_board, faz_movimento, get_input_valido, \
    print_board, verifica_ganhador, verica_movimento

from minimax import movimento_ia, movimentoIA_facil,movimentoIA_medio

pygame.mixer.init()
pygame.mixer.music.load('musica.mp3')
pygame.mixer.music.play()

pygame.font.init()

def draw_board(win, board):
    height = 600
    width = 600
    tamanho = 600/3

    for i in range(1, 3):
        pygame.draw.line(win, (0, 0, 0), (0, i * tamanho),\
                              (width, i * tamanho), 3)
        
        pygame.draw.line(win, (0, 0, 0), (i * tamanho, 0), \
                         (i * tamanho, height), 3)
        
    for i in range(3):
        for j in range(3):
            font = pygame.font.SysFont('comicsans', 100)

            x = j * tamanho
            y = i * tamanho

            text = font.render(board[i][j], 1, (0,0,0))
            win.blit(text, ((x + 75), (y + 75)))

def redraw_window(win, board):
    win.fill((69, 121, 217))
    draw_board(win, board)

def tela_inicial():
    win = pygame.display.set_mode((600, 600))
    win.fill((69, 121, 217))
    pygame.display.set_caption("Escolha a Dificuldade")
    
    font = pygame.font.SysFont('comicsans', 100)
    botao_dificuldade_facil = pygame.Rect(257, 303, 80, 55)
    pygame.draw.rect(win, (255, 255, 255), botao_dificuldade_facil)
    texto_dificuldade_facil = font.render("Facil!", True, (255, 255, 255))
    win.blit(texto_dificuldade_facil, (140, 230))

    botao_dificuldade_medio = pygame.Rect(257, 303, 80, 55)
    pygame.draw.rect(win, (255, 255, 255), botao_dificuldade_medio)
    texto_dificuldade_medio = font.render("Médio!", True, (255, 255, 255))
    win.blit(texto_dificuldade_medio, (140, 230))

    botao_dificuldade_dificil = pygame.Rect(257, 303, 80, 55)
    pygame.draw.rect(win, (255, 255, 255), botao_dificuldade_dificil)
    texto_dificuldade_dificil = font.render("Médio!", True, (255, 255, 255))
    win.blit(texto_dificuldade_dificil, (140, 230))

    pygame.display.update()

    while(True):
        pos = pygame.mouse.get_pos()
        if(dificuldade=="facil"):
            main(movimentoIA_facil)
            return
        if(dificuldade=="medio"):
            main(movimentoIA_medio)
            return
        main(movimento_ia)



def main(funcaoMovimento,win,nivel_dificuldade):
    pygame.display.set_caption("Jogo da Velha")
    font = pygame.font.SysFont('comicsans', 300)
    texto_nivel_dificuldade = font.render(nivel_dificuldade, True, (255, 255, 255))
    win.blit(texto_nivel_dificuldade, (140, 230))
    board = criar_board()

    redraw_window(win, board)
    pygame.display.update()

    jogador = 0
    ganhador = verifica_ganhador(board)

    while(not ganhador):
        i = None
        j = None
        

        if jogador == 0:
            jogou = False

            while(not jogou):
                for event in pygame.event.get():
                    if (event.type == pygame.QUIT):
                        return
                    elif (event.type == pygame.MOUSEBUTTONUP):
                        pos = pygame.mouse.get_pos()
                        tamanho = 600 // 3
                        i = pos[1] // tamanho
                        j = pos[0] // tamanho
                        if 0 <= i < 3 and 0 <= j < 3:
                            jogou = True
        else:
            i, j = funcaoMovimento(board, jogador)

        if verica_movimento(board, i, j):
            faz_movimento(board, i, j, jogador)
            ganhador = verifica_ganhador(board)
            if(not ganhador):
                jogador = (jogador + 1) % 2

        redraw_window(win, board)
        pygame.display.update()
        print_board(board)
    
    font = pygame.font.SysFont('comicsans', 100)
    texto=None
    if(ganhador=="EMPATE"):
        texto = font.render("EMPATE!", True, (255, 255, 255))
        win.blit(texto, (140, 230))
        
    else:
        texto = font.render("Vencedor: " + ganhador + " ", True, (255, 255, 255))
        win.blit(texto, (90, 230))
    
    botao_reiniciar = pygame.Rect(257, 303, 80, 55)
    pygame.draw.rect(win, (255, 255, 255), botao_reiniciar)
    imagem_reiniciar = pygame.image.load("reiniciar.png")
    imagem_reiniciar = pygame.transform.scale(
    imagem_reiniciar,
    (40, 40)
    )
    win.blit(imagem_reiniciar, (275, 310))
    pygame.display.update()

    while(True):
        pos = pygame.mouse.get_pos()

        if botao_reiniciar.collidepoint(pos):
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
        else:
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
        for event in pygame.event.get():
            if (event.type == pygame.QUIT):
                return
            elif event.type == pygame.MOUSEBUTTONUP:
                pos = event.pos

                if botao_reiniciar.collidepoint(pos):
                    pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
                    tela_inicial()   
                    return    

tela_inicial()