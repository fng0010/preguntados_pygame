import pygame
import random
import csv
import json
import os
from datetime import datetime
from constantes import *


def crear_superficie(
    pantalla: pygame.Surface,
    pos_x: int,
    pos_y: int,
    ancho: int,
    alto: int,
    borde_radio: int,
    color: str,
    texto: str,
    fuente_tamaño: int = 30,
    icono: str = None,
    icono_ancho: int = None,
    icono_alto: int = None,
) -> pygame.Rect:
    boton_surface = pygame.Surface((ancho, alto), pygame.SRCALPHA)
    boton_surface.set_alpha(200)

    pygame.draw.rect(
        surface=boton_surface,
        color=color,
        rect=(0, 0, ancho, alto),
        border_radius=borde_radio,
    )

    if icono:
        imagen = pygame.image.load(icono).convert_alpha()
        imagen = pygame.transform.scale(imagen, (icono_ancho, icono_alto))
        imagen_rect = imagen.get_rect(center=(ancho // 2, alto // 2))
        boton_surface.blit(imagen, imagen_rect)
    else:
        fuente = pygame.font.Font(FUENTE, fuente_tamaño)
        texto_surface = fuente.render(texto, True, COLOR_NEGRO)
        texto_rect = texto_surface.get_rect(center=(ancho // 2, alto // 2))
        boton_surface.blit(texto_surface, texto_rect)

    pantalla.blit(boton_surface, (pos_x, pos_y))

    return pygame.Rect(pos_x, pos_y, ancho, alto)


def calcular_pos_y_boton(
    indice: int, base: int = 120, espacio: int = 130, mover: int = 20
) -> int:
    return VENTANA_ALTO - (base + indice * espacio) - mover


def cargar_preguntas(preguntas_csv: str) -> list[dict]:
    preguntas = []
    try:
        with open(preguntas_csv, mode="r", newline="", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            for linea in reader:
                pregunta = {
                    "pregunta": linea["pregunta"],
                    "respuesta_1": linea["respuesta_1"],
                    "respuesta_2": linea["respuesta_2"],
                    "respuesta_3": linea["respuesta_3"],
                    "respuesta_4": linea["respuesta_4"],
                    "respuesta_correcta": linea["respuesta_correcta"],
                    "categoria": linea["categoria"],
                }
                preguntas.append(pregunta)
    except Exception:
        print("Hubo un problema con preguntas.csv")
    random.shuffle(preguntas)
    return preguntas


def wrap_text(text, font, max_width):
    words = text.split(" ")
    lines = []
    actual_line = ""
    for word in words:
        test_line = actual_line + (" " if actual_line else "") + word
        if font.size(test_line)[0] <= max_width:
            actual_line = test_line
        else:
            if actual_line:
                lines.append(actual_line)
            actual_line = word
    if actual_line:
        lines.append(actual_line)
    return lines


def render_text(screen, lines, font, x, y, width, height, color):
    total_height = len(lines) * font.get_height() + (len(lines) - 1) * 5
    y_text = y + (height - total_height) // 2
    for line in lines:
        text_surface = font.render(line, True, color)
        text_ancho = text_surface.get_width()
        x_text = x + (width - text_ancho) // 2
        screen.blit(text_surface, (x_text, y_text))
        y_text += font.get_height() + 5


def crear_item(
    pantalla: pygame.Surface,
    pos_x: int,
    pos_y: int,
    ancho: int,
    alto: int,
    borde_radio: int,
    valor: int,
    valor_pos_x: int,
    valor_pos_y: int,
    icono_path: str,
    icono_pos_x: int,
    icono_pos_y: int,
    icono_ancho: int,
    icono_alto: int,
    fuente_tamano: int,
):
    superficie = pygame.Surface((ancho, alto), pygame.SRCALPHA)
    superficie.set_alpha(200)

    pygame.draw.rect(
        surface=superficie,
        color=COLOR_BLANCO,
        rect=(0, 0, ancho, alto),
        border_radius=borde_radio,
    )

    icono = pygame.image.load(icono_path).convert_alpha()
    icono = pygame.transform.scale(icono, (icono_ancho, icono_alto))
    superficie.blit(icono, (icono_pos_x, icono_pos_y))

    fuente = pygame.font.Font(FUENTE, fuente_tamano)
    texto_surface = fuente.render(str(valor), True, COLOR_NEGRO)
    superficie.blit(texto_surface, (valor_pos_x, valor_pos_y))

    pantalla.blit(superficie, (pos_x, pos_y))


def guardar_partida(nombre, puntaje):
    partidas_ruta = "partidas.json"

    datos = {
        "nombre": nombre,
        "puntaje": puntaje,
        "fecha": datetime.now().strftime("%Y-%m-%d"),
    }

    partidas = []

    try:
        with open(partidas_ruta, "r", encoding="utf-8") as f:
            partidas = json.load(f)
    except Exception:
        partidas = []

    partidas.append(datos)

    with open(partidas_ruta, "w", encoding="utf-8") as f:
        json.dump(partidas, f, indent=2)


def guardar_pregunta_csv(pregunta, r1, r2, r3, r4, correcta):
    archivo = "preguntas.csv"
    agregar_salto = False

    if os.path.exists(archivo):
        with open(archivo, "rb") as f:
            contenido = f.read()
            if contenido and contenido[-1:] not in [b"\n", b"\r"]:
                agregar_salto = True
    with open(archivo, "a", encoding="utf-8", newline="") as f:
        if agregar_salto:
            f.write("\n")
        writer = csv.writer(f)
        writer.writerow([pregunta, r1, r2, r3, r4, correcta, "otros"])


def obtener_respuestas_bomba(pregunta):
    respuestas = ["respuesta_1", "respuesta_2", "respuesta_3", "respuesta_4"]
    correcta = f"respuesta_{pregunta['respuesta_correcta']}"

    incorrectas = []

    for respuesta in respuestas:
        if respuesta != correcta:
            incorrectas.append(respuesta)

    visible_incorrecta = random.choice(incorrectas)
    return [correcta, visible_incorrecta]


def reiniciar_comodines(datos_juego):
    datos_juego["comodin_bomba_activo"] = False
    datos_juego["comodin_x2_activo"] = False
    datos_juego["comodin_doble_chance_activo"] = False
    datos_juego["comodin_pasar_activo"] = False

    if "doble_chance_segunda_oportunidad" in datos_juego:
        del datos_juego["doble_chance_segunda_oportunidad"]
