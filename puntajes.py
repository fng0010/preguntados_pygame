import pygame
import json
from constantes import *


def mostrar_pantalla_puntajes(pantalla: pygame.Surface):
    pantalla.fill(COLOR_NEGRO)

    ## TITULO DE PANTALLA
    fuente_titulo = pygame.font.Font(FUENTE, 50)
    texto_titulo = fuente_titulo.render("Partidas", True, COLOR_BLANCO)
    texto_titulo_rect = texto_titulo.get_rect(center=(VENTANA_ANCHO // 2, 100))

    pantalla.blit(texto_titulo, texto_titulo_rect)

    ## LISTA DE PUNTAJES
    partidas = []
    try:
        with open("partidas.json", "r", encoding="utf-8") as f:
            partidas = json.load(f)
    except Exception:
        partidas = []

    for i in range(len(partidas)):
        for j in range(i + 1, len(partidas)):
            if partidas[j]["puntaje"] > partidas[i]["puntaje"]:
                partidas[i], partidas[j] = partidas[j], partidas[i]

    fuente_lista = pygame.font.Font(FUENTE, 32)
    y = 180
    x = VENTANA_ANCHO // 2
    espacio = 45

    for indice in range(min(10, len(partidas))):
        partida = partidas[indice]
        texto = (
            "["
            + str(indice + 1)
            + "] "
            + partida["nombre"]
            + " :: "
            + str(partida["puntaje"])
            + "pts. :: "
            + partida["fecha"]
        )
        texto_render = fuente_lista.render(texto, True, COLOR_BLANCO)
        texto_rect = texto_render.get_rect(center=(x, y + indice * espacio))
        pantalla.blit(texto_render, texto_rect)

    ## BOTON PARA VOLVER AL MENU
    fuente_boton = pygame.font.Font(FUENTE, 36)
    texto_boton = "Volver"
    ancho_boton, alto_boton = 200, 60
    boton_x = (VENTANA_ANCHO - ancho_boton) // 2
    boton_y = y + 10 * espacio + 40

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

    return {"boton_volver": pygame.Rect(boton_x, boton_y, ancho_boton, alto_boton)}
