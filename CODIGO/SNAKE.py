import pygame, sys, time, random

pygame.init()

ventana = pygame.display.set_mode((500, 500))

font = pygame.font.Font(None, 40) #elegimos el tipo de letra y tamnaño

fps = pygame.time.Clock()


def food():    
    random_pos = random.randint(0,49)*10
    food_pos = [random_pos, random_pos]  # posición en eje X e Y
    return food_pos


def main():

    cola = [100, 50] #ponemos donde vamos a comenzar la serpiente y definimos la variable 
    cuerpo = [[100,50],[90,50],[80,50]] #la longitud de el tamaño de la serpiente
    change = "RIGHT"
    run = True
    food_pos = food()
    score = 0

    while run:

        for event in pygame.event.get(): #le damos la dirreccion a las teclas
            if event.type == pygame.QUIT:
                run = False     # cierra el juego si el usuario sale
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    change = "RIGHT"  # cambiar dirección a la derecha
                if event.key == pygame.K_LEFT:
                    change = "LEFT"   # cambiar dirección a la izquierda
                if event.key == pygame.K_UP:
                    change = "UP"     # cambiar dirección hacia arriba
                if event.key == pygame.K_DOWN:
                    change = "DOWN"   # cambiar dirección hacia abajo
        if change == "RIGHT": #añadimos los pixeles que hacen ver como si se moviera
            cola[0] += 10 #Actualiza la posición de la cabeza de la serpiente según la dirección del movimiento.Se modifican las coordenadas en pasos de 10 píxeles para simular el desplazamiento en la pantalla.
        if change == "LEFT": 
            cola[0] -= 10
        if change == "UP":
            cola[1] -= 10
        if change == "DOWN":
            cola[1] += 10

        cuerpo.insert(0, list(cola)) #va eliminando conforme avanza en la pantalla la serpiente

        if cola == food_pos: #Verifica si la posición actual de la cabeza de la serpiente coincide con la posición de la comida. 
            food_pos = food() # si es así, se genera una nueva comida en otra posición y se incrementa el puntaje del jugador.
            score += 1
            print(score) #esto dice que mientras vaya sumando la comida va creciendo el taamaño
        else:
            cuerpo.pop() # elimina el ultimo movimientp
        
        head = cuerpo[-1]
        for i in range(len(cuerpo) - 1): 
            part = cuerpo[i]
            if head[0] == part[0] and head[1] == part[1]:
                run = False
                print("YOU LOSE")
# aqui escogi un color que me agrade para mi juego
        ventana.fill((178,140,200))

        for pos in cuerpo:
            pygame.draw.rect(ventana,(0,250,0), pygame.Rect(pos[0], pos[1], 10, 10)) #elegi el color de mi serpiente y el tamaño de nuestra serpiente       
        pygame.draw.rect(ventana,(169,6,6), pygame.Rect(food_pos[0], food_pos[1], 10, 10)) #elegimos el color de la comida
        
        text = font.render(str(score),0,(0,0,0)) #le damos el color a la puntuacion y el tipo de letra
        ventana.blit(text, (480,20))

        if score < 3: #vamos a poner la velocidad de la serpiennte
            fps.tick(3) # si es menor que 3 tiene una velocidad lenta y asi sucesivamente
        if score >= 3: # velocidad más rápida
            fps.tick (6)
   # Verifica si la serpiente choca con los límites de la pantalla y si la cabeza sale de los bordes, el juego termina.
        if cola[0] <= 0 or cola[0] >= 500:
            run = False
            print("YOU LOSE")
        if cola[1] <= 0 or cola[1] >= 500:
            run = False
            print("YOU LOSE")

        pygame.display.flip()

main()

pygame.quit()