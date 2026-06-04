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
topo=100

def draw_board(win, board,nivel_dificuldade):
    font = pygame.font.SysFont('comicsans', 60)
    if(nivel_dificuldade=="Fácil"):
        retanguloFundo = pygame.Rect(217, 5, 170, 60)
        pygame.draw.rect(win, (255, 255, 255), retanguloFundo,border_radius=15)

        texto_nivel_dificuldade = font.render(nivel_dificuldade, True, (69, 121, 217))
        win.blit(texto_nivel_dificuldade, (255, 17))
    if(nivel_dificuldade=="Médio"):
        retanguloFundo = pygame.Rect(217, 5, 170, 60)
        pygame.draw.rect(win, (255, 255, 255), retanguloFundo,border_radius=15)

        texto_nivel_dificuldade = font.render(nivel_dificuldade, True, (69, 121, 217))
        win.blit(texto_nivel_dificuldade, (244, 17))
    if(nivel_dificuldade=="Difícil"):
        retanguloFundo = pygame.Rect(217, 5, 170, 60)
        pygame.draw.rect(win, (255, 255, 255), retanguloFundo,border_radius=15)

        texto_nivel_dificuldade = font.render(nivel_dificuldade, True, (69, 121, 217))
        win.blit(texto_nivel_dificuldade, (244, 17))
    
    height = 600
    width = 600
    tamanho = 600/3

    

    for i in range(1, 3):
        pygame.draw.line(win, (0, 0, 0), (0, topo + i * tamanho),\
                        (width, topo + i * tamanho), 3)
        
        pygame.draw.line(win, (0, 0, 0), (i * tamanho, topo), \
                         (i * tamanho, height+topo), 3)
        
    for i in range(3):
        for j in range(3):
            font = pygame.font.SysFont('comicsans', 100)

            x = j * tamanho
            y = i * tamanho+topo

            text = font.render(board[i][j], 1, (0,0,0))
            win.blit(text, ((x + 75), (y + 75)))

def redraw_window(win, board,nivel_dificuldade):
    win.fill((69, 121, 217))
    draw_board(win, board,nivel_dificuldade)

def tela_inicial():
    win = pygame.display.set_mode((600, 700))
    win.fill((69, 121, 217))
    pygame.display.set_caption("Jogo da Velha")
    font = pygame.font.SysFont('comicsans', 60)
    texto= font.render("Escolha a dificuldade", True, (255, 255, 255))
    win.blit(texto, (105, 15))

    font = pygame.font.SysFont('comicsans', 50)
    botao_dificuldade_facil = pygame.Rect(217, 165, 175, 60)
    pygame.draw.rect(win, (255, 255, 255), botao_dificuldade_facil,border_radius=15)
    texto_dificuldade_facil = font.render("Fácil", True, (69, 121, 217))
    win.blit(texto_dificuldade_facil, (262, 179))

    botao_dificuldade_medio = pygame.Rect(217, 305, 175, 60)
    pygame.draw.rect(win, (255, 255, 255), botao_dificuldade_medio,border_radius=15)
    texto_dificuldade_medio = font.render("Médio", True, (69, 121, 217))
    win.blit(texto_dificuldade_medio, (253, 319))

    botao_dificuldade_dificil = pygame.Rect(217, 440, 175, 60)
    pygame.draw.rect(win, (255, 255, 255), botao_dificuldade_dificil,border_radius=15)
    texto_dificuldade_dificil = font.render("Difícil", True, (69, 121, 217))
    win.blit(texto_dificuldade_dificil, (253, 454))

    pygame.display.update()

    while(True):
        mousePosition=pygame.mouse.get_pos()
        if botao_dificuldade_facil.collidepoint(mousePosition) or botao_dificuldade_medio.collidepoint(mousePosition) \
        or botao_dificuldade_dificil.collidepoint(mousePosition):
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
        else:
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
        for evento in pygame.event.get():
            if (evento.type == pygame.QUIT):
                return
            
            if(evento.type==pygame.KEYDOWN):
                key=evento.key
                if(key==pygame.K_1 or key == pygame.K_KP1):
                    pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
                    main(movimentoIA_facil,win,"Fácil")
                    return
                if(key==pygame.K_2 or key == pygame.K_KP2):
                    pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
                    main(movimentoIA_medio,win,"Médio")
                    return
                if(key==pygame.K_3 or key == pygame.K_KP3):
                    pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
                    main(movimento_ia,win,"Difícil")
                    return

            if(evento.type==pygame.MOUSEBUTTONUP ):
                mousePosition=evento.pos
                if(botao_dificuldade_facil.collidepoint(mousePosition)):
                    pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
                    main(movimentoIA_facil,win,"Fácil")
                    return
                if(botao_dificuldade_medio.collidepoint(mousePosition)):
                    pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
                    main(movimentoIA_medio,win,"Médio")
                    return
                if(botao_dificuldade_dificil.collidepoint(mousePosition)):
                    pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
                    main(movimento_ia,win,"Difícil")
                    return



def main(funcaoMovimento,win,nivel_dificuldade):
    pygame.display.set_caption("Jogo da Velha")
    board = criar_board()

    redraw_window(win, board,nivel_dificuldade)
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
                        if pos[1] < topo:
                            continue
                        i = (pos[1]-topo) // tamanho
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

        redraw_window(win,board,nivel_dificuldade)
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
    pygame.draw.rect(win, (255, 255, 255), botao_reiniciar,border_radius=15)
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