import pygame
from constantes import *
from funciones import *


def mostrar_menu(pantalla: pygame.Surface):
    imagen_cargada = pygame.image.load(MENU_FONDO).convert()
    fondo = pygame.transform.scale(imagen_cargada, VENTANA_DIMENSIONES)

    pantalla.blit(fondo, (0, 0))

    boton_jugar = crear_superficie(
        pantalla=pantalla,
        pos_x=(VENTANA_ANCHO - BOTON_ANCHO) // 2,
        pos_y=calcular_pos_y_boton(4, base=120, espacio=130, mover=20),
        alto=BOTON_ALTO,
        ancho=BOTON_ANCHO,
        borde_radio=BOTON_BORDE_RADIO,
        color=COLOR_BLANCO,
        texto="JUGAR",
    )

    boton_agregar_pregunta = crear_superficie(
        pantalla=pantalla,
        pos_x=(VENTANA_ANCHO - BOTON_ANCHO) // 2,
        pos_y=calcular_pos_y_boton(3, base=120, espacio=130, mover=20),
        alto=BOTON_ALTO,
        ancho=BOTON_ANCHO,
        borde_radio=BOTON_BORDE_RADIO,
        color=COLOR_BLANCO,
        texto="AGREGAR PREGUNTA",
    )

    boton_puntajes = crear_superficie(
        pantalla=pantalla,
        pos_x=(VENTANA_ANCHO - BOTON_ANCHO) // 2,
        pos_y=calcular_pos_y_boton(2, base=120, espacio=130, mover=20),
        alto=BOTON_ALTO,
        ancho=BOTON_ANCHO,
        borde_radio=BOTON_BORDE_RADIO,
        color=COLOR_BLANCO,
        texto="PUNTAJES",
    )

    boton_ajustes = crear_superficie(
        pantalla=pantalla,
        pos_x=(VENTANA_ANCHO - BOTON_ANCHO) // 2,
        pos_y=calcular_pos_y_boton(1, base=120, espacio=130, mover=20),
        alto=BOTON_ALTO,
        ancho=BOTON_ANCHO,
        borde_radio=BOTON_BORDE_RADIO,
        color=COLOR_BLANCO,
        texto="AJUSTES",
    )

    boton_salir = crear_superficie(
        pantalla=pantalla,
        pos_x=(VENTANA_ANCHO - BOTON_ANCHO) // 2,
        pos_y=calcular_pos_y_boton(0, base=120, espacio=130, mover=20),
        alto=BOTON_ALTO,
        ancho=BOTON_ANCHO,
        borde_radio=BOTON_BORDE_RADIO,
        color=COLOR_BLANCO,
        texto="SALIR",
    )

    return {
        "jugar": boton_jugar,
        "agregar pregunta": boton_agregar_pregunta,
        "puntajes": boton_puntajes,
        "ajustes": boton_ajustes,
        "salir": boton_salir,
    }


def manejar_eventos_menu(mouse_pos, botones_menu, estado_actual, corriendo):
    if mouse_pos:
        if botones_menu["jugar"].collidepoint(mouse_pos):
            return "jugar", corriendo
        if botones_menu["agregar pregunta"].collidepoint(mouse_pos):
            return "agregar_pregunta", corriendo
        if botones_menu["puntajes"].collidepoint(mouse_pos):
            return "puntajes", corriendo
        if botones_menu["ajustes"].collidepoint(mouse_pos):
            return "ajustes", corriendo
        if botones_menu["salir"].collidepoint(mouse_pos):
            return estado_actual, False
    return estado_actual, corriendo
