
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

        grupo = Text(
            "Calculo Intermedio - Grupo 8",
            font_size=24
        )

        integrantes = VGroup(
            Text("Carlos Nahuelcoy", font_size=23),
            Text("Rodrigo Sevilla", font_size=23),
            Text("Matias Salinas", font_size=23)
        ).arrange(DOWN, buff=0.2)

        portada = VGroup(
            titulo, subtitulo, grupo, integrantes
        ).arrange(DOWN, buff=0.4)

        self.play(Write(titulo))
        self.play(FadeIn(subtitulo))
        self.play(FadeIn(grupo))
        self.play(FadeIn(integrantes))
        self.wait(2)
        self.play(FadeOut(portada))

        pregunta = Text(
            "¿Por que la derivada de una acumulacion\n"
            "recupera la funcion que se esta acumulando?",
            font_size=29,
            line_spacing=1.3
        )

        self.play(Write(pregunta))
        self.wait(3)
        self.play(FadeOut(pregunta))
