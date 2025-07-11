import pygame
import pygame
from constantes import *
from funciones import *


def mostrar_pantalla_agregar_pregunta(pantalla: pygame.Surface, texto_pregunta=""):
    pantalla.fill(COLOR_NEGRO)

    ## TITULO
    fuente_titulo = pygame.font.Font(FUENTE, 50)
    texto_titulo = fuente_titulo.render("Agregar pregunta", True, COLOR_BLANCO)
    texto_titulo_rect = texto_titulo.get_rect(center=(VENTANA_ANCHO // 2, 80))
    pantalla.blit(texto_titulo, texto_titulo_rect)

    ## SUBTITULO
    fuente_subtitulo = pygame.font.Font(FUENTE, 36)
    texto_subtitulo = fuente_subtitulo.render("Pregunta:", True, COLOR_BLANCO)
    text_subtitulo_rect = texto_subtitulo.get_rect(center=(VENTANA_ANCHO // 2, 180))
    pantalla.blit(texto_subtitulo, text_subtitulo_rect)

    ## CUADRO PARA INGRESAR PREGUNTA
    cuadro_ancho = 600
    cuadro_alto = 250
    cuadro_x = (VENTANA_ANCHO - cuadro_ancho) // 2
    cuadro_y = 220
    cuadro_surface = pygame.Surface((cuadro_ancho, cuadro_alto), pygame.SRCALPHA)
    cuadro_surface.set_alpha(200)

    pygame.draw.rect(
        cuadro_surface,
        COLOR_BLANCO,
        (0, 0, cuadro_ancho, cuadro_alto),
        border_radius=15,
    )

    fuente_texto_ingresado = pygame.font.Font(FUENTE, 32)
    lineas = wrap_text(texto_pregunta, fuente_texto_ingresado, cuadro_ancho - 30)
    y_texto = 10

    for linea in lineas:
        texto_linea = fuente_texto_ingresado.render(linea, True, COLOR_NEGRO)
        cuadro_surface.blit(texto_linea, (15, y_texto))
        y_texto += fuente_texto_ingresado.get_height() + 5

    pantalla.blit(cuadro_surface, (cuadro_x, cuadro_y))

    ## BOTON SIGUIENTE
    fuente_boton = pygame.font.Font(FUENTE, 36)
    texto_boton = "Siguiente"
    ancho_boton = 300
    alto_boton = 60
    boton_x = (VENTANA_ANCHO - ancho_boton) // 2
    boton_y = cuadro_y + cuadro_alto + 40

    boton_surface = pygame.Surface((ancho_boton, alto_boton), pygame.SRCALPHA)
    boton_surface.set_alpha(200)

    pygame.draw.rect(
        boton_surface,
        COLOR_BLANCO,
        (0, 0, ancho_boton, alto_boton),
        border_radius=15,
    )

    texto_boton_render = fuente_boton.render(texto_boton, True, COLOR_NEGRO)
    texto_boton_rect = texto_boton_render.get_rect(
        center=(ancho_boton // 2, alto_boton // 2)
    )

    boton_surface.blit(texto_boton_render, texto_boton_rect)
    pantalla.blit(boton_surface, (boton_x, boton_y))

    ## BOTON VOLVER
    boton_volver = crear_superficie(
        pantalla=pantalla,
        pos_x=(VENTANA_ANCHO - 700) // 2,
        pos_y=calcular_pos_y_boton(0, base=926, espacio=130, mover=20),
        ancho=40,
        alto=40,
        borde_radio=5,
        color=COLOR_BLANCO,
        texto="<-",
        fuente_tamaño=20,
    )

    return {
        "boton_siguiente": pygame.Rect(boton_x, boton_y, ancho_boton, alto_boton),
        "boton_volver": boton_volver,
    }


def mostrar_pantalla_respuesta(pantalla: pygame.Surface, texto_respuesta="", numero=1):
    pantalla.fill(COLOR_NEGRO)

    ## TITULO
    fuente_titulo = pygame.font.Font(FUENTE, 50)
    texto_titulo = fuente_titulo.render("Agregar pregunta", True, COLOR_BLANCO)
    texto_titulo_rect = texto_titulo.get_rect(center=(VENTANA_ANCHO // 2, 80))
    pantalla.blit(texto_titulo, texto_titulo_rect)

    ## SUBTITULO
    fuente_label = pygame.font.Font(FUENTE, 36)
    texto_label = fuente_label.render(f"Respuesta {numero}:", True, COLOR_BLANCO)
    texto_label_rect = texto_label.get_rect(center=(VENTANA_ANCHO // 2, 180))
    pantalla.blit(texto_label, texto_label_rect)

    ## CUADRO PARA INGRESAR RESPUESTa
    cuadro_ancho = 600
    cuadro_alto = 100
    cuadro_x = (VENTANA_ANCHO - cuadro_ancho) // 2
    cuadro_y = 220

    cuadro_surface = pygame.Surface((cuadro_ancho, cuadro_alto), pygame.SRCALPHA)
    cuadro_surface.set_alpha(200)

    pygame.draw.rect(
        cuadro_surface,
        COLOR_BLANCO,
        (0, 0, cuadro_ancho, cuadro_alto),
        border_radius=15,
    )

    fuente_texto_ingresado = pygame.font.Font(FUENTE, 32)
    lineas = wrap_text(texto_respuesta, fuente_texto_ingresado, cuadro_ancho - 30)
    y_texto = 10

    for linea in lineas:
        texto_input = fuente_texto_ingresado.render(linea, True, COLOR_NEGRO)
        cuadro_surface.blit(texto_input, (15, y_texto))
        y_texto += fuente_texto_ingresado.get_height() + 5
    pantalla.blit(cuadro_surface, (cuadro_x, cuadro_y))

    ## BOTON SIGUIENTE
    fuente_boton = pygame.font.Font(FUENTE, 36)
    texto_boton = "Siguiente"
    ancho_boton = 300
    alto_boton = 60
    boton_x = (VENTANA_ANCHO - ancho_boton) // 2
    boton_y = cuadro_y + cuadro_alto + 40

    boton_surface = pygame.Surface((ancho_boton, alto_boton), pygame.SRCALPHA)
    boton_surface.set_alpha(200)

    pygame.draw.rect(
        boton_surface,
        COLOR_BLANCO,
        (0, 0, ancho_boton, alto_boton),
        border_radius=15,
    )

    texto_boton_render = fuente_boton.render(texto_boton, True, COLOR_NEGRO)
    texto_boton_rect = texto_boton_render.get_rect(
        center=(ancho_boton // 2, alto_boton // 2)
    )

    boton_surface.blit(texto_boton_render, texto_boton_rect)
    pantalla.blit(boton_surface, (boton_x, boton_y))

    ## BOTON VOLVER
    boton_volver = crear_superficie(
        pantalla=pantalla,
        pos_x=(VENTANA_ANCHO - 700) // 2,
        pos_y=calcular_pos_y_boton(0, base=926, espacio=130, mover=20),
        ancho=40,
        alto=40,
        borde_radio=5,
        color=COLOR_BLANCO,
        texto="<-",
        fuente_tamaño=20,
    )

    return {
        "boton_siguiente": pygame.Rect(boton_x, boton_y, ancho_boton, alto_boton),
        "boton_volver": boton_volver,
    }


def mostrar_pantalla_respuesta_correcta(pantalla: pygame.Surface, texto_correcta=""):
    pantalla.fill(COLOR_NEGRO)

    ## TITULO
    fuente_titulo = pygame.font.Font(FUENTE, 50)
    texto_titulo = fuente_titulo.render("Respuesta correcta", True, COLOR_BLANCO)
    texto_titulo_rect = texto_titulo.get_rect(center=(VENTANA_ANCHO // 2, 80))
    pantalla.blit(texto_titulo, texto_titulo_rect)

    ## SUBTITULO
    fuente_label = pygame.font.Font(FUENTE, 36)
    texto_label = fuente_label.render("Respuesta correcta (1-4):", True, COLOR_BLANCO)
    texto_label_rect = texto_label.get_rect(center=(VENTANA_ANCHO // 2, 180))
    pantalla.blit(texto_label, texto_label_rect)

    ## CUADRO PARA INGRESAR RESPUESTA CORRECTA
    cuadro_ancho = 200
    cuadro_alto = 80
    cuadro_x = (VENTANA_ANCHO - cuadro_ancho) // 2
    cuadro_y = 240

    cuadro_surface = pygame.Surface((cuadro_ancho, cuadro_alto), pygame.SRCALPHA)
    cuadro_surface.set_alpha(200)

    pygame.draw.rect(
        cuadro_surface,
        COLOR_BLANCO,
        (0, 0, cuadro_ancho, cuadro_alto),
        border_radius=15,
    )

    fuente_texto_ingresado = pygame.font.Font(FUENTE, 48)
    texto_input = fuente_texto_ingresado.render(texto_correcta, True, COLOR_NEGRO)
    texto_input_rect = texto_input.get_rect(
        center=(cuadro_ancho // 2, cuadro_alto // 2)
    )

    cuadro_surface.blit(texto_input, texto_input_rect)
    pantalla.blit(cuadro_surface, (cuadro_x, cuadro_y))

    ## BOTON FINALIZAR
    fuente_boton = pygame.font.Font(FUENTE, 36)
    texto_boton = "Finalizar"
    ancho_boton = 300
    alto_boton = 60
    boton_x = (VENTANA_ANCHO - ancho_boton) // 2
    boton_y = cuadro_y + cuadro_alto + 40

    boton_surface = pygame.Surface((ancho_boton, alto_boton), pygame.SRCALPHA)
    boton_surface.set_alpha(200)

    pygame.draw.rect(
        boton_surface,
        COLOR_BLANCO,
        (0, 0, ancho_boton, alto_boton),
        border_radius=15,
    )

    texto_boton_render = fuente_boton.render(texto_boton, True, COLOR_NEGRO)
    texto_boton_rect = texto_boton_render.get_rect(
        center=(ancho_boton // 2, alto_boton // 2)
    )

    boton_surface.blit(texto_boton_render, texto_boton_rect)
    pantalla.blit(boton_surface, (boton_x, boton_y))

    ## BOTON VOLVER
    boton_volver = crear_superficie(
        pantalla=pantalla,
        pos_x=(VENTANA_ANCHO - 700) // 2,
        pos_y=calcular_pos_y_boton(0, base=926, espacio=130, mover=20),
        ancho=40,
        alto=40,
        borde_radio=5,
        color=COLOR_BLANCO,
        texto="<-",
        fuente_tamaño=20,
    )

    return {
        "boton_finalizar": pygame.Rect(boton_x, boton_y, ancho_boton, alto_boton),
        "boton_volver": boton_volver,
    }


def ingresar_texto_pregunta(cola_eventos, texto_actual, max_len=120):
    for evento in cola_eventos:
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_BACKSPACE:
                texto_actual = texto_actual[:-1]
            else:
                if len(texto_actual) < max_len:
                    char = evento.unicode
                    if char.isprintable():
                        texto_actual += char
    return texto_actual


def ingresar_texto_correcta(cola_eventos, texto_actual):
    for evento in cola_eventos:
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_BACKSPACE:
                texto_actual = ""
            elif evento.key == pygame.K_RETURN:
                pass
            else:
                char = evento.unicode
                if char in ["1", "2", "3", "4"]:
                    texto_actual = char
    return texto_actual
