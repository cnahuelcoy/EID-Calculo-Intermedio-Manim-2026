"""
EID Calculo Intermedio - Grupo 8
Parte 2 (Rodrigo Sevilla): desarrollo matematico y
visualizacion de la funcion de acumulacion.

Ejemplo del informe:
    f(t) = 2 - t,   a = 0,   A(x) = integral de 0 a x de (2 - t) dt
"""

from manim import *

# Colores acordados por el grupo
COLOR_F = BLUE      # funcion original f
COLOR_A = GREEN     # funcion acumulada A
COLOR_H = ORANGE    # elementos de transicion / incrementos


def f(t):
    """Funcion original del ejemplo."""
    return 2 - t


def A(x):
    """Funcion de acumulacion ya integrada: A(x) = 2x - x^2/2."""
    return 2 * x - x**2 / 2


def titulo_escena(texto):
    """Titulo comun para las tres escenas (mismo estilo que carlos.py)."""
    return Text(texto, font_size=34).to_edge(UP)


class ResolucionIntegral(Scene):
    """Escena 1: calculo paso a paso de A(x)."""

    def construct(self):
        titulo = titulo_escena("Resolución de la integral")
        self.play(Write(titulo))
        self.wait(1)
        self.play(FadeOut(titulo))


class GraficaAcumulacion(Scene):
    """Escena 2: grafica de A(x) y sus cinco puntos."""

    def construct(self):
        titulo = titulo_escena("Gráfica de la función acumulada")
        self.play(Write(titulo))
        self.wait(1)
        self.play(FadeOut(titulo))


class AreaAcumulada(Scene):
    """Escena 3: area con signo bajo f(t) y extremo superior variable."""

    def construct(self):
        titulo = titulo_escena("Interpretación del área acumulada")
        self.play(Write(titulo))
        self.wait(1)
        self.play(FadeOut(titulo))