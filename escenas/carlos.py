
from manim import *


class Introduccion(Scene):
    def construct(self):
        titulo = Text(
            "Teorema Fundamental del Calculo",
            font_size=38
        )

        subtitulo = Text(
            "Parte I - Funciones de acumulacion",
            font_size=26
        )

        contenido = VGroup(
            titulo,
            subtitulo
        ).arrange(DOWN, buff=0.5)

        self.play(Write(titulo))
        self.play(FadeIn(subtitulo))
        self.wait(2)
        self.play(FadeOut(contenido))
