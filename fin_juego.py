import pygame
from constantes import *
from funciones import *


def mostrar_pantalla_fin_juego(
    pantalla: pygame.Surface, puntaje: int, nombre_jugador: str = ""
):
    pantalla.fill(COLOR_NEGRO)

    fuente_titulo = pygame.font.Font(FUENTE, 50)
    texto = fuente_titulo.render("Fin de la partida", True, COLOR_BLANCO)
    texto_rect = texto.get_rect(center=(VENTANA_ANCHO // 2, VENTANA_ALTO // 2 - 350))
    pantalla.blit(texto, texto_rect)

    fuente_mensaje = pygame.font.Font(FUENTE, 36)
    texto_mensaje = fuente_mensaje.render(
        f"Usted obtuvo {puntaje} puntos!", True, COLOR_BLANCO
    )
    texto_mensaje_rect = texto_mensaje.get_rect(
        center=(VENTANA_ANCHO // 2, VENTANA_ALTO // 2 - 100)
    )
    pantalla.blit(texto_mensaje, texto_mensaje_rect)

    cuadro_ancho = 400
    cuadro_alto = 60
    cuadro_pos_x = (VENTANA_ANCHO - cuadro_ancho) // 2
    cuadro_pos_y = VENTANA_ALTO // 2 - 30

    cuadro_superficie = pygame.Surface((cuadro_ancho, cuadro_alto), pygame.SRCALPHA)
    cuadro_superficie.set_alpha(200)

    pygame.draw.rect(
        cuadro_superficie,
        COLOR_BLANCO,
        (0, 0, cuadro_ancho, cuadro_alto),
        border_radius=15,
    )

    fuente_cuadro_nombre = pygame.font.Font(FUENTE, 36)
    texto_nombre = fuente_cuadro_nombre.render(nombre_jugador, True, COLOR_NEGRO)
    texto_nombre_rect = texto_nombre.get_rect(
        center=(cuadro_ancho // 2, cuadro_alto // 2)
    )

    cuadro_superficie.blit(texto_nombre, texto_nombre_rect)
    pantalla.blit(cuadro_superficie, (cuadro_pos_x, cuadro_pos_y))

    boton_guardar = crear_superficie(
        pantalla=pantalla,
        pos_x=(VENTANA_ANCHO - 200) // 2,
        pos_y=cuadro_pos_y + cuadro_alto + 40,
        ancho=200,
        alto=60,
        borde_radio=15,
        color=COLOR_BLANCO,
        texto="Guardar",
        fuente_tamaño=32,
    )
    return {
        "boton_guardar": boton_guardar,
        "cuadro_nombre": pygame.Rect(
            cuadro_pos_x, cuadro_pos_y, cuadro_ancho, cuadro_alto
        ),
    }


def ingresar_texto(cola_eventos, nombre_actual, max_len=8):
    for evento in cola_eventos:
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_BACKSPACE:
                nombre_actual = nombre_actual[:-1]
            elif evento.key == pygame.K_RETURN:
                pass
            else:
                if len(nombre_actual) < max_len:
                    char = evento.unicode
                    if char.isalpha():
                        nombre_actual += char
    return nombre_actual
