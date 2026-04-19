import pygame

pygame.init()
pygame.display.set_mode((640, 480))
pygame.display.set_caption("ventana basica")

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()