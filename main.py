import pygame
from constantes import *
from menu import *
from juego import *
from puntajes import *
from agregar_pregunta import *
from ajustes import *
from funciones import *
from fin_juego import *
from tiempo import *


pygame.init()
pygame.mixer.init()

## CONFIGURACION DEL JUEGO:
pantalla = pygame.display.set_mode(VENTANA_DIMENSIONES)
icono = pygame.image.load(VENTANA_ICONO)
pygame.display.set_caption(VENTANA_TITULO)
pygame.display.set_icon(icono)

## ESTADOS DEL JUEGO:
corriendo = True
datos_juego = {
    "indice_pregunta": 0,
    "estado_juego": "menu",
    "vidas": 5,
    "racha_correctas": 0,
    "puntaje": 0,
    "nombre_jugador": "",
    "tiempo_pregunta": 5,
    "timer_activo": False,
    "volumen_musica": 20,
    "musica_activada": True,
    "comodin_bomba_activo": False,
    "comodin_x2_activo": False,
    "comodin_doble_chance_activo": False,
    "comodin_pasar_activo": False,
}

# ESTADOS PARA LA PANTALLA DE AGREGAR PREGUNTAS
agregar_pregunta_opcion = "pregunta"
texto_pregunta = ""
texto_respuesta_1 = ""
texto_respuesta_2 = ""
texto_respuesta_3 = ""
texto_respuesta_4 = ""
texto_correcta = ""

while corriendo:
    mouse_pos = None
    cola_eventos = pygame.event.get()

    for evento in cola_eventos:
        if evento.type == pygame.QUIT:
            corriendo = False
        if evento.type == pygame.MOUSEBUTTONDOWN:
            if evento.button == 1:
                mouse_pos = evento.pos

    ## PANTALLA DE MENU
    if datos_juego["estado_juego"] == "menu":
        datos_juego["indice_pregunta"] = 0
        datos_juego["vidas"] = 5
        datos_juego["racha_correctas"] = 0
        datos_juego["puntaje"] = 0
        datos_juego["nombre_jugador"] = ""
        preguntas = cargar_preguntas("preguntas.csv")
        datos_juego["tiempo_pregunta"] = 5
        datos_juego["timer_activo"] = False
        parar_timer()
        reiniciar_comodines(datos_juego)
        botones_menu = mostrar_menu(pantalla)
        pygame.mixer.music.stop()
        if pygame.mixer.get_init():
            pygame.mixer.music.stop()
        if mouse_pos:
            datos_juego["estado_juego"], corriendo = manejar_eventos_menu(
                mouse_pos, botones_menu, datos_juego["estado_juego"], corriendo
            )

    ## PANTALLA DE JUEGO
    elif datos_juego["estado_juego"] == "jugar":
        if datos_juego["musica_activada"]:
            if not pygame.mixer.music.get_busy():
                porcentaje_volumen = datos_juego["volumen_musica"] / 100
                pygame.mixer.music.load("assets/musica.mp3")
                pygame.mixer.music.set_volume(porcentaje_volumen)
                pygame.mixer.music.play(-1)
        else:
            if pygame.mixer.get_init():
                pygame.mixer.music.stop()
            pass

        if datos_juego["vidas"] <= 0:
            datos_juego["estado_juego"] = "fin_juego"
            datos_juego["timer_activo"] = False
            parar_timer()
        else:
            pregunta_actual = preguntas[datos_juego["indice_pregunta"]]
            pregunta_con_estado = dict(pregunta_actual)
            pregunta_con_estado["datos_juego"] = datos_juego
            botones_respuesta = mostrar_pantalla_juego(
                pantalla,
                pregunta_con_estado,
                datos_juego["vidas"],
                datos_juego["puntaje"],
                datos_juego["tiempo_pregunta"],
                datos_juego["racha_correctas"],
            )

            if not datos_juego["timer_activo"]:
                comenzar_timer(5)
                datos_juego["timer_activo"] = True

            for evento in cola_eventos:
                if evento.type == evento_tiempo:
                    datos_juego["tiempo_pregunta"] -= 1

                    if datos_juego["tiempo_pregunta"] <= 0:
                        if datos_juego["puntaje"] > 0:
                            datos_juego["puntaje"] -= 1
                        datos_juego["vidas"] -= 1
                        datos_juego["racha_correctas"] = 0
                        datos_juego["indice_pregunta"] += 1
                        datos_juego["tiempo_pregunta"] = 5
                        datos_juego["timer_activo"] = False
                        reiniciar_comodines(datos_juego)
                        parar_timer()

            if mouse_pos:
                opcion = manejar_eventos_juego(
                    mouse_pos, botones_respuesta, pregunta_actual, datos_juego
                )
                if opcion == "correcta":
                    puntos = 5
                    if datos_juego.get("comodin_x2_activo", False):
                        puntos = 10
                    datos_juego["puntaje"] += puntos
                    datos_juego["racha_correctas"] += 1
                    if datos_juego["racha_correctas"] == 5:
                        datos_juego["vidas"] += 1
                        datos_juego["racha_correctas"] = 0
                    datos_juego["indice_pregunta"] += 1
                    datos_juego["tiempo_pregunta"] = 5
                    datos_juego["timer_activo"] = False
                    reiniciar_comodines(datos_juego)
                    parar_timer()
                elif opcion == "incorrecta":
                    if datos_juego["puntaje"] > 0:
                        datos_juego["puntaje"] -= 1
                    datos_juego["vidas"] -= 1
                    datos_juego["racha_correctas"] = 0
                    datos_juego["indice_pregunta"] += 1
                    datos_juego["tiempo_pregunta"] = 5
                    datos_juego["timer_activo"] = False
                    reiniciar_comodines(datos_juego)
                    parar_timer()
                elif opcion == "pasar":
                    datos_juego["indice_pregunta"] += 1
                    datos_juego["tiempo_pregunta"] = 5
                    datos_juego["timer_activo"] = False
                    reiniciar_comodines(datos_juego)
                    parar_timer()
                elif opcion == "volver_menu":
                    datos_juego["estado_juego"] = "menu"
                    datos_juego["timer_activo"] = False
                    reiniciar_comodines(datos_juego)
                    parar_timer()

    ## PANTALLA DE AJUSTES
    elif datos_juego["estado_juego"] == "ajustes":
        elementos_ajustes = mostrar_pantalla_ajustes(
            pantalla, datos_juego["musica_activada"], datos_juego["volumen_musica"]
        )

        if mouse_pos:
            if elementos_ajustes["boton_volver"].collidepoint(mouse_pos):
                datos_juego["estado_juego"] = "menu"

            elif elementos_ajustes["boton_musica_off"].collidepoint(mouse_pos):
                datos_juego["musica_activada"] = False
                if pygame.mixer.get_init():
                    pygame.mixer.music.set_volume(0)

            elif elementos_ajustes["boton_musica_on"].collidepoint(mouse_pos):
                datos_juego["musica_activada"] = True
                if pygame.mixer.get_init():
                    pygame.mixer.music.set_volume(datos_juego["volumen_musica"] / 100)

            elif elementos_ajustes["boton_volumen_bajo"].collidepoint(mouse_pos):
                if datos_juego["volumen_musica"] > 0:
                    datos_juego["volumen_musica"] -= 5
                    if datos_juego["volumen_musica"] < 0:
                        datos_juego["volumen_musica"] = 0
                    if pygame.mixer.get_init():
                        pygame.mixer.music.set_volume(
                            datos_juego["volumen_musica"] / 100
                        )

            elif elementos_ajustes["boton_volumen_alto"].collidepoint(mouse_pos):
                if datos_juego["volumen_musica"] < 100:
                    datos_juego["volumen_musica"] += 5
                    if datos_juego["volumen_musica"] > 100:
                        datos_juego["volumen_musica"] = 100
                    if pygame.mixer.get_init():
                        pygame.mixer.music.set_volume(
                            datos_juego["volumen_musica"] / 100
                        )

    ## PANTALLA DE FIN JUEGO (donde se guarda el nombre del jugador)
    elif datos_juego["estado_juego"] == "fin_juego":
        datos_juego["timer_activo"] = False
        parar_timer()

        if pygame.mixer.get_init():
            pygame.mixer.music.stop()

        datos_juego["nombre_jugador"] = ingresar_texto(
            cola_eventos, datos_juego["nombre_jugador"]
        )

        elementos_fin = mostrar_pantalla_fin_juego(
            pantalla, datos_juego["puntaje"], datos_juego["nombre_jugador"]
        )

        if mouse_pos:
            if elementos_fin["boton_guardar"].collidepoint(mouse_pos):
                if (
                    datos_juego["nombre_jugador"]
                    and len(datos_juego["nombre_jugador"]) >= 3
                ):
                    guardar_partida(
                        datos_juego["nombre_jugador"], datos_juego["puntaje"]
                    )
                    datos_juego["estado_juego"] = "menu"

    ## PANTALLA DE PUNTAJES
    elif datos_juego["estado_juego"] == "puntajes":
        elementos_puntajes = mostrar_pantalla_puntajes(pantalla)
        if mouse_pos:
            if elementos_puntajes["boton_volver"].collidepoint(mouse_pos):
                datos_juego["estado_juego"] = "menu"

    ## PANTALLA DE AGREGAR PREGUNTA
    elif datos_juego["estado_juego"] == "agregar_pregunta":
        if agregar_pregunta_opcion == "pregunta":
            texto_pregunta = ingresar_texto_pregunta(cola_eventos, texto_pregunta)
            elementos = mostrar_pantalla_agregar_pregunta(pantalla, texto_pregunta)
            if mouse_pos:
                if elementos["boton_volver"].collidepoint(mouse_pos):
                    datos_juego["estado_juego"] = "menu"
                    agregar_pregunta_opcion = "pregunta"
                    texto_pregunta = ""
                    texto_respuesta_1 = ""
                    texto_respuesta_2 = ""
                    texto_respuesta_3 = ""
                    texto_respuesta_4 = ""
                    texto_correcta = ""
                elif elementos["boton_siguiente"].collidepoint(mouse_pos):
                    agregar_pregunta_opcion = "respuesta1"
        elif agregar_pregunta_opcion == "respuesta1":
            texto_respuesta_1 = ingresar_texto_pregunta(cola_eventos, texto_respuesta_1)
            elementos = mostrar_pantalla_respuesta(pantalla, texto_respuesta_1, 1)
            if mouse_pos:
                if elementos["boton_siguiente"].collidepoint(mouse_pos):
                    agregar_pregunta_opcion = "respuesta2"
        elif agregar_pregunta_opcion == "respuesta2":
            texto_respuesta_2 = ingresar_texto_pregunta(cola_eventos, texto_respuesta_2)
            elementos = mostrar_pantalla_respuesta(pantalla, texto_respuesta_2, 2)
            if mouse_pos:
                if elementos["boton_siguiente"].collidepoint(mouse_pos):
                    agregar_pregunta_opcion = "respuesta3"
        elif agregar_pregunta_opcion == "respuesta3":
            texto_respuesta_3 = ingresar_texto_pregunta(cola_eventos, texto_respuesta_3)
            elementos = mostrar_pantalla_respuesta(pantalla, texto_respuesta_3, 3)
            if mouse_pos:
                if elementos["boton_siguiente"].collidepoint(mouse_pos):
                    agregar_pregunta_opcion = "respuesta4"
        elif agregar_pregunta_opcion == "respuesta4":
            texto_respuesta_4 = ingresar_texto_pregunta(cola_eventos, texto_respuesta_4)
            elementos = mostrar_pantalla_respuesta(pantalla, texto_respuesta_4, 4)
            if mouse_pos:
                if elementos["boton_siguiente"].collidepoint(mouse_pos):
                    agregar_pregunta_opcion = "correcta"
        elif agregar_pregunta_opcion == "correcta":
            texto_correcta = ingresar_texto_correcta(cola_eventos, texto_correcta)
            elementos = mostrar_pantalla_respuesta_correcta(pantalla, texto_correcta)
            if mouse_pos:
                if elementos["boton_finalizar"].collidepoint(mouse_pos):
                    if texto_correcta in ["1", "2", "3", "4"]:
                        guardar_pregunta_csv(
                            texto_pregunta,
                            texto_respuesta_1,
                            texto_respuesta_2,
                            texto_respuesta_3,
                            texto_respuesta_4,
                            texto_correcta,
                        )
                        agregar_pregunta_opcion = "pregunta"
                        texto_pregunta = ""
                        texto_respuesta_1 = ""
                        texto_respuesta_2 = ""
                        texto_respuesta_3 = ""
                        texto_respuesta_4 = ""
                        texto_correcta = ""
                        datos_juego["estado_juego"] = "menu"

    ## PANTALLA DE AJUSTES
    elif datos_juego["estado_juego"] == "ajustes":
        elementos_ajustes = mostrar_pantalla_ajustes(
            pantalla, datos_juego["musica_activada"], datos_juego["volumen_musica"]
        )
        if mouse_pos:
            if elementos_ajustes["boton_volver"].collidepoint(mouse_pos):
                datos_juego["estado_juego"] = "menu"
            elif elementos_ajustes["boton_musica_off"].collidepoint(mouse_pos):
                datos_juego["musica_activada"] = False
                if pygame.mixer.get_init():
                    pygame.mixer.music.set_volume(0)
            elif elementos_ajustes["boton_musica_on"].collidepoint(mouse_pos):
                datos_juego["musica_activada"] = True
                if pygame.mixer.get_init():
                    pygame.mixer.music.set_volume(datos_juego["volumen_musica"] / 100)
            elif elementos_ajustes["boton_volumen_bajo"].collidepoint(mouse_pos):
                if datos_juego["volumen_musica"] > 0:
                    datos_juego["volumen_musica"] -= 5
                    if datos_juego["volumen_musica"] < 0:
                        datos_juego["volumen_musica"] = 0
                    if pygame.mixer.get_init():
                        pygame.mixer.music.set_volume(
                            datos_juego["volumen_musica"] / 100
                        )
            elif elementos_ajustes["boton_volumen_alto"].collidepoint(mouse_pos):
                if datos_juego["volumen_musica"] < 100:
                    datos_juego["volumen_musica"] += 5
                    if datos_juego["volumen_musica"] > 100:
                        datos_juego["volumen_musica"] = 100
                    if pygame.mixer.get_init():
                        pygame.mixer.music.set_volume(
                            datos_juego["volumen_musica"] / 100
                        )

    pygame.display.flip()

pygame.quit()
