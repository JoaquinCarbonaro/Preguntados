'''
nombre: Joaquin
apellido: Carbonaro
'''
import pygame
from datos import lista
from constantes import *

# Inicializar pygame
pygame.init()

# Configuración de la ventana
ventana = pygame.display.set_mode((ANCHO_VENTANA, ALTO_VENTANA))
pygame.display.set_caption("Preguntados - Joaquín Carbonaro")  

# Configuración de música
pygame.mixer.music.load("piano.mp3")
pygame.mixer.music.play(-1) 

# Configuración de imágenes
logo = pygame.image.load("logo_preguntados.png")  
logo = pygame.transform.scale(logo, (160, 160))  

# Configuración de fuente de texto
fuente_titulo = pygame.font.SysFont("monospace", 40)
fuente_score = pygame.font.SysFont("impact", 30)
fuente_pregunta = pygame.font.SysFont("Arial", 25)
fuente_opciones = pygame.font.SysFont("Arial", 30)

# Datos de las preguntas (organizados en listas separadas)
preguntas = []  
opciones_a = []  
opciones_b = []  
opciones_c = []  
respuestas_correctas = []  

# Recorrer los datos de las preguntas y guardar en listas separadas
for elemento in lista:
    pregunta = elemento['pregunta']
    opcion_a = elemento['a'].capitalize() #primera letra mayuscula
    opcion_b = elemento['b'].capitalize()
    opcion_c = elemento['c'].capitalize()
    respuesta_correcta = elemento['correcta']

    preguntas.append(pregunta)
    opciones_a.append(opcion_a)
    opciones_b.append(opcion_b)
    opciones_c.append(opcion_c)
    respuestas_correctas.append(respuesta_correcta)

# Variables del juego
score = 0  
indice_pregunta = -1 
mostrar_opciones = False  # Variable para controlar la visualización de opciones
mostrar_pregunta = False # Variable para controlar la visualización de preguntas
intentos_restantes = 2  # Número de intentos permitidos por pregunta

# Bucle principal del juego
bandera_ejecutar = True
while bandera_ejecutar:  # se ejecuta el juego
    lista_eventos = pygame.event.get()  # se guarda las acciones en una tupla
    for evento in lista_eventos:
        if evento.type == pygame.QUIT:  # cerrar juego con la "X"
            bandera_ejecutar = False

        if evento.type == pygame.MOUSEBUTTONDOWN:  #click del mouse 
            posicion_click = list(evento.pos)  # guardo la posicion de click (tupla) en lista 
            x = posicion_click[0]
            y = posicion_click[1]

            # Botón "Pregunta": Mostrar pregunta y opciones
            if (x > 280 and x < 520) and (y > 40 and y < 140): 
                mostrar_opciones = True
                mostrar_pregunta = True
                indice_pregunta += 1
                intentos_restantes = 2

                # Al llegar al final de las preguntas, reinicia el índice
                if indice_pregunta >= len(preguntas):
                    indice_pregunta = 0
                    intentos_restantes = 2
                    score = 0 

            # Botón "Reiniciar": Reiniciar el juego (puntaje y pregunta)
            elif (x > 280 and x < 520) and (y > 460 and y < 560):
                indice_pregunta = 0
                score = 0
                mostrar_opciones = True
                mostrar_pregunta = True
                intentos_restantes = 2

            # Manejo de opciones
            elif mostrar_opciones:
                respuesta_correcta = respuestas_correctas[indice_pregunta]

                # Comprobar si se hizo clic en una opción
                if (x > 40 and x < 260) and (y > 340 and y < 400):  # Primera opción
                    if respuesta_correcta == 'a':
                        score += 10  
                        mostrar_opciones = False
                    else:
                        intentos_restantes -= 1  

                elif (x > 290 and x < 510) and (y > 340 and y < 400):  # Segunda opción
                    if respuesta_correcta == 'b':
                        score += 10
                        mostrar_opciones = False
                    else:
                        intentos_restantes -= 1

                elif (x > 540 and x < 760) and (y > 340 and y < 400):  # Tercera opción
                    if respuesta_correcta == 'c':
                        score += 10
                        mostrar_opciones = False
                    else:
                        intentos_restantes -= 1

            # Si se agotaron los intentos, no mostrar opciones
            if intentos_restantes == 0:
                mostrar_opciones = False
                mostrar_pregunta = True

    # Dibujar pantalla
    ventana.fill(COLOR_TURQUES)
    ventana.blit(logo, (20, 20)) 

    # Dibujar rectángulos
    pygame.draw.rect(ventana, COLOR_AMARILLO, POSICION_RECTANGULO_PREGUNTA)
    pygame.draw.rect(ventana, COLOR_NARANJA, POSICION_RECTANGULO_SCORE)
    pygame.draw.rect(ventana, COLOR_AMARILLO, POSICION_RECTANGULO_REINICIAR)

    # Renderizar y mostrar texto en los rectángulos
    texto_titulo_render = fuente_titulo.render(TEXTO_PREGUNTA_STR, True, COLOR_NEGRO)
    ventana.blit(texto_titulo_render, POSICION_TEXTO_PREGUNTA)

    texto_score_render = fuente_score.render(TEXTO_SCORE_STR + str(score), True, COLOR_NEGRO)
    ventana.blit(texto_score_render, POSICION_TEXTO_SCORE)

    texto_reiniciar_render = fuente_titulo.render(TEXTO_REINICIAR_STR, True, COLOR_NEGRO)
    ventana.blit(texto_reiniciar_render, POSICION_TEXTO_REINICIAR)

    if mostrar_pregunta:  # Mostrar la pregunta actual     
        pregunta_actual = preguntas[indice_pregunta]
        pygame.draw.rect(ventana, COLOR_LAVANDA, POSICION_RECTANGULO_PREGUNTA_ACTUAL)
        texto_pregunta = fuente_pregunta.render(pregunta_actual, True, COLOR_NEGRO)
        ventana.blit(texto_pregunta, POSICION_TEXTO_PREGUNTA_ACTUAL)

    if mostrar_opciones:   # Mostrar opciones
        pygame.draw.rect(ventana, COLOR_LAVANDA, POSICION_RECTANGULO_OPCION_A)
        texto_opcion_a = fuente_opciones.render(opciones_a[indice_pregunta], True, COLOR_NEGRO)
        ventana.blit(texto_opcion_a, POSICION_TEXTO_OPCION_A)

        pygame.draw.rect(ventana, COLOR_LAVANDA, POSICION_RECTANGULO_OPCION_B)
        texto_opcion_b = fuente_opciones.render(opciones_b[indice_pregunta], True, COLOR_NEGRO)
        ventana.blit(texto_opcion_b, POSICION_TEXTO_OPCION_B)

        pygame.draw.rect(ventana, COLOR_LAVANDA, POSICION_RECTANGULO_OPCION_C)
        texto_opcion_c = fuente_opciones.render(opciones_c[indice_pregunta], True, COLOR_NEGRO)
        ventana.blit(texto_opcion_c, POSICION_TEXTO_OPCION_C)

    pygame.display.flip()  # Actualizar info

pygame.quit()  # Salir del juego