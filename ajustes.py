import pygame
from constantes import *
from funciones import *


def mostrar_pantalla_ajustes(
    pantalla: pygame.Surface, musica_activada: bool = True, volumen_musica: int = 100
):
    pantalla.fill(COLOR_NEGRO)

    ## TITULO
    fuente = pygame.font.Font(FUENTE, 50)
    texto = fuente.render("Ajustes", True, COLOR_BLANCO)
    texto_rect = texto.get_rect(center=(VENTANA_ANCHO // 2, 100))
    pantalla.blit(texto, texto_rect)

    ## SUBTITULO ESTADO MUSICA
    fuente_sub = pygame.font.Font(FUENTE, 32)
    estado = "ON" if musica_activada else "OFF"
    texto_sub = fuente_sub.render(f"MUSICA: {estado}", True, COLOR_BLANCO)
    texto_sub_rect = texto_sub.get_rect(center=(VENTANA_ANCHO // 2, 150))
    pantalla.blit(texto_sub, texto_sub_rect)

    ## SUBTITULO VOLUMEN
    texto_vol = fuente_sub.render(f"VOLUMEN: {volumen_musica}", True, COLOR_BLANCO)
    texto_vol_rect = texto_vol.get_rect(center=(VENTANA_ANCHO // 2, 190))
    pantalla.blit(texto_vol, texto_vol_rect)

    ## BOTONES DE MUSICA
    ancho_boton = 100
    alto_boton = 100
    espacio_entre = 30
    total_ancho = ancho_boton * 2 + espacio_entre
    x_inicio = (VENTANA_ANCHO - total_ancho) // 2
    y_botones = 230

    crear_superficie(
        pantalla=pantalla,
        pos_x=x_inicio,
        pos_y=y_botones,
        ancho=ancho_boton,
        alto=alto_boton,
        borde_radio=20,
        color=COLOR_BLANCO,
        texto="",
        fuente_tamaño=28,
        icono="assets/musica_silenciada.png",
        icono_ancho=70,
        icono_alto=70,
    )

    crear_superficie(
        pantalla=pantalla,
        pos_x=x_inicio + ancho_boton + espacio_entre,
        pos_y=y_botones,
        ancho=ancho_boton,
        alto=alto_boton,
        borde_radio=20,
        color=COLOR_BLANCO,
        texto="",
        fuente_tamaño=28,
        icono="assets/musica_activa.png",
        icono_ancho=70,
        icono_alto=70,
    )

    ## BOTONES DE VOLUMEN
    y_botones_vol = y_botones + alto_boton + 40

    crear_superficie(
        pantalla=pantalla,
        pos_x=x_inicio,
        pos_y=y_botones_vol,
        ancho=ancho_boton,
        alto=alto_boton,
        borde_radio=20,
        color=COLOR_BLANCO,
        texto="",
        fuente_tamaño=28,
        icono="assets/volumen_bajo.png",
        icono_ancho=70,
        icono_alto=70,
    )

    crear_superficie(
        pantalla=pantalla,
        pos_x=x_inicio + ancho_boton + espacio_entre,
        pos_y=y_botones_vol,
        ancho=ancho_boton,
        alto=alto_boton,
        borde_radio=20,
        color=COLOR_BLANCO,
        texto="",
        fuente_tamaño=28,
        icono="assets/volumen_alto.png",
        icono_ancho=70,
        icono_alto=70,
    )

    ## VOLVER AL MENU
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
        "boton_volver": boton_volver,
        "boton_musica_off": pygame.Rect(x_inicio, y_botones, ancho_boton, alto_boton),
        "boton_musica_on": pygame.Rect(
            x_inicio + ancho_boton + espacio_entre, y_botones, ancho_boton, alto_boton
        ),
        "boton_volumen_bajo": pygame.Rect(
            x_inicio, y_botones_vol, ancho_boton, alto_boton
        ),
        "boton_volumen_alto": pygame.Rect(
            x_inicio + ancho_boton + espacio_entre,
            y_botones_vol,
            ancho_boton,
            alto_boton,
        ),
    }
