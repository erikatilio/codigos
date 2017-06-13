import pygame

def main():
    #As definiçoes dos objetos
    x = pygame.init()
    tela = pygame.display.set_mode([1000,500])
    pygame.display.set_caption("SONIC BOOM")
    relogio = pygame.time.Clock()
    rect = pygame.Rect(500,450,90,50)

    #cores
    branco = (255,255,255)
    verde = (152,231,114)
    amarelo = (255,255,0)
    vermelho = (255,0,0)
    azul = (0,0,255)


    sair = False
    while sair != True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sair = True
            # movimentos com teclado
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    rect = rect.move(20,0)

                if event.key == pygame.K_LEFT:
                    rect = rect.move(-20,0)

        # frames
        relogio.tick(150)
        #preenchimento e chamar superficie
        tela.fill(branco)
        # mover objeto com mouse

        # desenhar objeto
        pygame.draw.rect(tela, vermelho, rect)
        # atualizar tela
        pygame.display.update()

    pygame.quit()

main()
