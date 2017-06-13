import pygame

def main():
    pygame.init()
    pygame.display.set_mode([700,700])
    pygame.display.set_caption("Snake")
    sair = False

#Fazendo while para fechar ao pressionar o botão x na tela do pygame

    while sair != True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sair = True
    pygame.quit()

main()