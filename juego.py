import pygame
from constantes import *
from funciones import *


def mostrar_pantalla_juego(
    pantalla: pygame.Surface,
    pregunta_con_estado: dict,
    vidas: int,
    puntaje: int,
    tiempo: int = 5,
    racha: int = 0,
):
    pantalla.fill(COLOR_NEGRO)

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

    cuadro_racha = crear_item(
        pantalla=pantalla,
        pos_x=((VENTANA_ANCHO - 700) + 100) // 2,
        pos_y=calcular_pos_y_boton(0, base=900, espacio=130, mover=0),
        ancho=70,
        alto=40,
        borde_radio=5,
        valor=racha,
        valor_pos_x=45,
        valor_pos_y=10,
        icono_path="./assets/racha.png",
        icono_pos_x=5,
        icono_pos_y=5,
        icono_ancho=32,
        icono_alto=32,
        fuente_tamano=20,
    )

    cuadro_tiempo = crear_item(
        pantalla=pantalla,
        pos_x=((VENTANA_ANCHO - 700) + 250) // 2,
        pos_y=calcular_pos_y_boton(0, base=900, espacio=130, mover=0),
        ancho=90,
        alto=40,
        borde_radio=5,
        valor=tiempo,
        valor_pos_x=45,
        valor_pos_y=10,
        icono_path="./assets/tiempo.png",
        icono_pos_x=5,
        icono_pos_y=5,
        icono_ancho=32,
        icono_alto=32,
        fuente_tamano=20,
    )

    cuadro_vidas = crear_item(
        pantalla=pantalla,
        pos_x=((VENTANA_ANCHO - 700) + 100) // 2,
        pos_y=calcular_pos_y_boton(0, base=926, espacio=130, mover=20),
        ancho=70,
        alto=40,
        borde_radio=5,
        valor=vidas,
        valor_pos_x=45,
        valor_pos_y=10,
        icono_path="./assets/vidas.png",
        icono_pos_x=0,
        icono_pos_y=-6,
        icono_ancho=50,
        icono_alto=50,
        fuente_tamano=20,
    )

    cuadro_puntaje = crear_item(
        pantalla=pantalla,
        pos_x=((VENTANA_ANCHO - 700) + 250) // 2,
        pos_y=calcular_pos_y_boton(0, base=926, espacio=130, mover=20),
        ancho=90,
        alto=40,
        borde_radio=5,
        valor=puntaje,
        valor_pos_x=40,
        valor_pos_y=10,
        icono_path="./assets/puntaje.png",
        icono_pos_x=6,
        icono_pos_y=4,
        icono_ancho=32,
        icono_alto=32,
        fuente_tamano=20,
    )

    ## COMODIN BOMBA
    color_bomba = COLOR_BLANCO
    disponible_bomba = True

    if "datos_juego" in pregunta_con_estado:
        bomba_ya_usado = (
            "bomba_respuestas_visibles" in pregunta_con_estado["datos_juego"]
        )
        disponible_bomba = not bomba_ya_usado

    if not disponible_bomba:
        color_bomba = COLOR_GRIS

    boton_comodin_bomba = crear_superficie(
        pantalla=pantalla,
        pos_x=((VENTANA_ANCHO - 700) + 520) // 2,
        pos_y=calcular_pos_y_boton(0, base=926, espacio=130, mover=20),
        ancho=100,
        alto=90,
        icono="./assets/bomba.png",
        icono_ancho=64,
        icono_alto=64,
        borde_radio=5,
        color=color_bomba,
        texto="",
        fuente_tamaño=28,
    )

    ## COMODIN X2
    color_x2 = COLOR_BLANCO
    disponible_x2 = True

    if "datos_juego" in pregunta_con_estado:
        x2_ya_usado = pregunta_con_estado["datos_juego"].get("x2_usado", False)
        disponible_x2 = not x2_ya_usado

    if not disponible_x2:
        color_x2 = COLOR_GRIS

    boton_comodin_x2 = crear_superficie(
        pantalla=pantalla,
        pos_x=((VENTANA_ANCHO - 700) + 740) // 2,
        pos_y=calcular_pos_y_boton(0, base=926, espacio=130, mover=20),
        ancho=100,
        alto=90,
        icono="./assets/x2.png",
        icono_ancho=64,
        icono_alto=64,
        borde_radio=5,
        color=color_x2,
        texto="",
        fuente_tamaño=28,
    )

    ## COMODIN DOBLE CHANCE
    color_doble_chance = COLOR_BLANCO
    disponible_doble_chance = True

    if "datos_juego" in pregunta_con_estado:
        doble_chance_ya_usado = pregunta_con_estado["datos_juego"].get(
            "doble_chance_usado", False
        )
        disponible_doble_chance = not doble_chance_ya_usado

    if not disponible_doble_chance:
        color_doble_chance = COLOR_GRIS

    boton_comodin_doble_chance = crear_superficie(
        pantalla=pantalla,
        pos_x=((VENTANA_ANCHO - 700) + 960) // 2,
        pos_y=calcular_pos_y_boton(0, base=926, espacio=130, mover=20),
        ancho=100,
        alto=90,
        icono="./assets/doble_chance.png",
        icono_ancho=64,
        icono_alto=64,
        borde_radio=5,
        color=color_doble_chance,
        texto="",
        fuente_tamaño=28,
    )

    ## COMODIN PASAR
    color_pasar = COLOR_BLANCO
    disponible_pasar = True

    if "datos_juego" in pregunta_con_estado:
        pasar_ya_usado = pregunta_con_estado["datos_juego"].get("pasar_usado", False)
        disponible_pasar = not pasar_ya_usado

    if not disponible_pasar:
        color_pasar = COLOR_GRIS

    boton_comodin_pasar = crear_superficie(
        pantalla=pantalla,
        pos_x=((VENTANA_ANCHO - 700) + 1180) // 2,
        pos_y=calcular_pos_y_boton(0, base=926, espacio=130, mover=20),
        ancho=100,
        alto=90,
        icono="./assets/pasar.png",
        icono_ancho=64,
        icono_alto=64,
        borde_radio=5,
        color=color_pasar,
        texto="",
        fuente_tamaño=28,
    )

    ## CUADRO DE PREGUNTAS:
    fuente = pygame.font.Font(FUENTE, 28)
    lineas = wrap_text(pregunta_con_estado["pregunta"], fuente, 660)

    cuadro_pregunta = crear_superficie(
        pantalla=pantalla,
        pos_x=(VENTANA_ANCHO - 700) // 2,
        pos_y=calcular_pos_y_boton(0, base=820, espacio=130, mover=20),
        ancho=700,
        alto=400,
        borde_radio=30,
        color=COLOR_BLANCO,
        texto="",
        fuente_tamaño=28,
    )

    cuadro_x = (VENTANA_ANCHO - 700) // 2
    cuadro_y = calcular_pos_y_boton(0, base=820, espacio=130, mover=20)
    cuadro_ancho = 700
    cuadro_alto = 400

    render_text(
        pantalla,
        lineas,
        fuente,
        cuadro_x,
        cuadro_y,
        cuadro_ancho,
        cuadro_alto,
        COLOR_NEGRO,
    )

    ## BOTONES DE RESPUESTA
    botones_respuestas = {}
    visibles = None

    if "comodin_bomba_activo" in pregunta_con_estado and pregunta_con_estado.get(
        "comodin_bomba_activo", False
    ):
        visibles = pregunta_con_estado.get("bomba_respuestas_visibles", [])
    elif "datos_juego" in pregunta_con_estado:
        dj = pregunta_con_estado["datos_juego"]
        if dj.get("comodin_bomba_activo", False):
            visibles = dj.get("bomba_respuestas_visibles", [])

    indice = 1

    for respuesta in ["respuesta_1", "respuesta_2", "respuesta_3", "respuesta_4"]:
        mostrar = True
        if visibles is not None and respuesta not in visibles:
            mostrar = False
        if mostrar:
            botones_respuestas[respuesta] = crear_superficie(
                pantalla=pantalla,
                pos_x=(VENTANA_ANCHO - 700) // 2,
                pos_y=calcular_pos_y_boton(
                    0, base=500 - (indice * 100), espacio=130, mover=20
                ),
                ancho=700,
                alto=90,
                borde_radio=30,
                color=COLOR_BLANCO,
                texto=pregunta_con_estado[respuesta],
                fuente_tamaño=28,
            )
            indice += 1
        else:
            botones_respuestas[respuesta] = pygame.Rect(0, 0, 0, 0)

    resultado = {
        "boton_volver": boton_volver,
        "boton_comodin_bomba": boton_comodin_bomba,
        "boton_comodin_x2": boton_comodin_x2,
        "boton_comodin_doble_chance": boton_comodin_doble_chance,
        "boton_comodin_pasar": boton_comodin_pasar,
        "cuadro_tiempo": cuadro_tiempo,
        "cuadro_racha": cuadro_racha,
        "cuadro_vidas": cuadro_vidas,
        "cuadro_puntaje": cuadro_puntaje,
        "cuadro_pregunta": cuadro_pregunta,
    }

    resultado.update(botones_respuestas)

    return resultado


def manejar_eventos_juego(mouse_pos, botones_respuesta, pregunta, datos_juego):
    if mouse_pos:
        if botones_respuesta["boton_volver"].collidepoint(mouse_pos):
            if "bomba_respuestas_visibles" in datos_juego:
                del datos_juego["bomba_respuestas_visibles"]
            if "x2_usado" in datos_juego:
                del datos_juego["x2_usado"]
            if "pasar_usado" in datos_juego:
                del datos_juego["pasar_usado"]
            if "doble_chance_usado" in datos_juego:
                del datos_juego["doble_chance_usado"]
            if "doble_chance_segunda_oportunidad" in datos_juego:
                del datos_juego["doble_chance_segunda_oportunidad"]
            return "volver_menu"

        if botones_respuesta["boton_comodin_bomba"].collidepoint(mouse_pos):
            bomba_usado = "bomba_respuestas_visibles" in datos_juego

            if not bomba_usado and not datos_juego.get("comodin_bomba_activo", False):
                datos_juego["comodin_bomba_activo"] = True
                datos_juego["bomba_respuestas_visibles"] = obtener_respuestas_bomba(
                    pregunta
                )
            return None

        if botones_respuesta["boton_comodin_x2"].collidepoint(mouse_pos):
            x2_usado = datos_juego.get("x2_usado", False)

            if not x2_usado and not datos_juego.get("comodin_x2_activo", False):
                datos_juego["comodin_x2_activo"] = True
                datos_juego["x2_usado"] = True  # Marcar que ya fue usado
            return None

        if botones_respuesta["boton_comodin_pasar"].collidepoint(mouse_pos):
            pasar_usado = datos_juego.get("pasar_usado", False)

            if not pasar_usado:
                datos_juego["pasar_usado"] = True
                return "pasar"
            return None

        if botones_respuesta["boton_comodin_doble_chance"].collidepoint(mouse_pos):
            doble_chance_usado = datos_juego.get("doble_chance_usado", False)

            if not doble_chance_usado:
                datos_juego["comodin_doble_chance_activo"] = True
                datos_juego["doble_chance_usado"] = True
            return None

        correcta = pregunta["respuesta_correcta"]

        if datos_juego.get("comodin_bomba_activo", False):
            visibles = datos_juego.get("bomba_respuestas_visibles", [])

            for r in visibles:
                if botones_respuesta[r].collidepoint(mouse_pos):
                    if r == f"respuesta_{correcta}":
                        return "correcta"
                    else:
                        if datos_juego.get(
                            "comodin_doble_chance_activo", False
                        ) and not datos_juego.get(
                            "doble_chance_segunda_oportunidad", False
                        ):
                            datos_juego["doble_chance_segunda_oportunidad"] = True
                            return None
                        return "incorrecta"
            return None

        for i in range(1, 5):
            if botones_respuesta[f"respuesta_{i}"].collidepoint(mouse_pos):
                if correcta == str(i):
                    return "correcta"
                else:
                    if datos_juego.get(
                        "comodin_doble_chance_activo", False
                    ) and not datos_juego.get(
                        "doble_chance_segunda_oportunidad", False
                    ):
                        datos_juego["doble_chance_segunda_oportunidad"] = True
                        return None
                    return "incorrecta"

    return None
