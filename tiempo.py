import pygame

evento_tiempo = pygame.USEREVENT + 1


def comenzar_timer(segundos: int = 5):
    pygame.time.set_timer(evento_tiempo, 1000)
    return segundos


def parar_timer():
    pygame.time.set_timer(evento_tiempo, 0)
