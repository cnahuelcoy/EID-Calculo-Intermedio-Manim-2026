
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


class FuncionAcumulacion(Scene):
    def construct(self):
        titulo = Text(
            "Funcion de acumulacion",
            font_size=36
        ).to_edge(UP)

        formula = MathTex(
            r"A(x)=\int_{a}^{x}f(t)\,dt",
            font_size=56
        )

        explicacion = Text(
            "La acumulacion depende del limite superior x",
            font_size=25
        ).next_to(formula, DOWN, buff=0.8)

        contenido = VGroup(formula, explicacion)

        self.play(Write(titulo))
        self.wait(1)

        self.play(Write(formula))
        self.wait(2)

        self.play(FadeIn(explicacion))
        self.wait(3)

        self.play(
            FadeOut(contenido),
            FadeOut(titulo)
        )


class SimbolosYCondiciones(Scene):
    def construct(self):
        titulo = Text(
            "Elementos de la funcion acumulada",
            font_size=32
        ).to_edge(UP)

        formula = MathTex(
            r"A(x)=\int_{a}^{x}f(t)\,dt",
            font_size=54
        ).shift(UP * 1.3)

        simbolos = [
            (r"A(x)", "Cantidad acumulada"),
            (r"a", "Limite inferior fijo"),
            (r"x", "Limite superior variable"),
            (r"f(t)", "Funcion que se integra"),
            (r"dt", "Diferencial de integracion")
        ]

        self.play(Write(titulo))
        self.play(Write(formula))
        self.wait(1)

        for simbolo, descripcion in simbolos:
            expresion = MathTex(
                simbolo,
                font_size=38,
                color=YELLOW
            )

            texto = Text(
                descripcion,
                font_size=26
            )

            explicacion = VGroup(
                expresion, texto
            ).arrange(RIGHT, buff=0.5)

            explicacion.next_to(
                formula, DOWN, buff=0.8
            )

            self.play(FadeIn(explicacion))
            self.wait(1)
            self.play(FadeOut(explicacion))

        self.play(FadeOut(formula))

        condicion = Text(
            "Condicion: f debe ser continua en [a, b]",
            font_size=29
        ).move_to(UP * 0.6)

        resultado = MathTex(
            r"A'(x)=f(x)",
            font_size=58,
            color=GREEN
        ).next_to(condicion, DOWN, buff=0.7)

        self.play(Write(condicion))
        self.wait(2)

        self.play(Write(resultado))
        self.wait(2)

        self.play(
            FadeOut(condicion),
            FadeOut(resultado),
            FadeOut(titulo)
        )


class PresentacionEjemplo(Scene):
    def construct(self):
        titulo = Text(
            "Nuestro ejemplo matematico",
            font_size=36
        ).to_edge(UP)

        funcion = MathTex(
            r"f(x)=2-x",
            font_size=64,
            color=BLUE
        )

        intervalo = MathTex(
            r"x\in[0,4]",
            font_size=44
        )

        continuidad = Text(
            "Es una funcion continua en [0,4]",
            font_size=27
        )

        datos = VGroup(
            funcion,
            intervalo,
            continuidad
        ).arrange(DOWN, buff=0.65)

        self.play(Write(titulo))
        self.wait(1)

        self.play(Write(funcion))
        self.wait(2)

        self.play(FadeIn(intervalo))
        self.wait(1)

        self.play(FadeIn(continuidad))
        self.wait(2)

        self.play(FadeOut(datos))

        acumulacion = MathTex(
            r"A(x)=\int_{0}^{x}(2-t)\,dt",
            font_size=58,
            color=GREEN
        )

        explicacion = Text(
            "El limite inferior permanece fijo en cero",
            font_size=26
        ).next_to(acumulacion, DOWN, buff=0.7)

        self.play(Write(acumulacion))
        self.wait(2)

        self.play(FadeIn(explicacion))
        self.wait(2)

        self.play(
            FadeOut(acumulacion),
            FadeOut(explicacion),
            FadeOut(titulo)
        )


class GraficaInicial(Scene):
    def construct(self):
        titulo = Text(
            "Representacion grafica de f(x)",
            font_size=33
        ).to_edge(UP)

        ejes = Axes(
            x_range=[0, 4, 1],
            y_range=[-2.5, 2.5, 1],
            x_length=8,
            y_length=4.5,
            axis_config={
                "include_numbers": True,
                "font_size": 24
            },
            tips=False
        ).shift(DOWN * 0.35)

        etiquetas = ejes.get_axis_labels(
            x_label=MathTex("x"),
            y_label=MathTex("f(x)")
        )

        funcion = ejes.plot(
            lambda x: 2 - x,
            x_range=[0, 4],
            color=BLUE,
            stroke_width=5
        )

        formula = MathTex(
            r"f(x)=2-x",
            color=BLUE,
            font_size=38
        ).to_corner(UR).shift(DOWN * 0.6)

        punto_inicial = Dot(
            ejes.c2p(0, 2),
            color=YELLOW
        )

        punto_cero = Dot(
            ejes.c2p(2, 0),
            color=YELLOW
        )

        punto_final = Dot(
            ejes.c2p(4, -2),
            color=YELLOW
        )

        self.play(Write(titulo))
        self.play(Create(ejes))
        self.play(Write(etiquetas))
        self.wait(1)

        self.play(Write(formula))
        self.play(Create(funcion), run_time=3)
        self.wait(1)

        self.play(
            FadeIn(punto_inicial),
            FadeIn(punto_cero),
            FadeIn(punto_final)
        )

        self.wait(2)

        explicacion = Text(
            "Ahora calcularemos la acumulacion",
            font_size=28
        ).to_edge(DOWN)

        self.play(FadeIn(explicacion))
        self.wait(2)

        self.play(
            FadeOut(titulo),
            FadeOut(ejes),
            FadeOut(etiquetas),
            FadeOut(funcion),
            FadeOut(formula),
            FadeOut(punto_inicial),
            FadeOut(punto_cero),
            FadeOut(punto_final),
            FadeOut(explicacion)
        )

        transicion = MathTex(
            r"A(x)=\int_{0}^{x}(2-t)\,dt",
            font_size=58,
            color=GREEN
        )

        self.play(Write(transicion))
        self.wait(3)
        self.play(FadeOut(transicion))
