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


def ecuacion(*partes):
    """Linea del desarrollo: 'A(x) =' fijo a la izquierda + lado derecho."""
    return MathTex(r"A(x)", "=", *partes, font_size=58)


def nota(texto):
    """Texto explicativo en la parte inferior de la pantalla."""
    return Text(texto, font_size=26).to_edge(DOWN, buff=0.8)


class ResolucionIntegral(Scene):
    """Escena 1: calculo paso a paso de A(x)."""

    def construct(self):
        titulo = titulo_escena("Resolución de la integral")
        self.play(Write(titulo))

        # 1. Integral de acumulacion (continua desde la escena de Carlos)
        paso1 = ecuacion(r"\int_{0}^{x}", r"(2-t)\,dt")
        paso1[0].set_color(COLOR_A)
        paso1[3].set_color(COLOR_F)
        self.play(Write(paso1))
        self.wait(1)

        # 2. Limites: glifos de la integral -> [0] simbolo, [1] x, [2] 0
        lim_sup, lim_inf = paso1[2][1], paso1[2][2]
        txt_inf = Text("límite inferior fijo", font_size=24, color=YELLOW)
        txt_sup = Text("límite superior variable", font_size=24, color=YELLOW)
        txt_inf.next_to(paso1, DOWN, buff=0.9).shift(LEFT * 2)
        txt_sup.next_to(paso1, UP, buff=0.9).shift(LEFT * 2)
        flecha_inf = Arrow(txt_inf.get_top(), lim_inf.get_bottom(), buff=0.1, color=YELLOW)
        flecha_sup = Arrow(txt_sup.get_bottom(), lim_sup.get_top(), buff=0.1, color=YELLOW)

        self.play(lim_inf.animate.set_color(YELLOW), GrowArrow(flecha_inf), FadeIn(txt_inf))
        self.wait(1.5)
        self.play(lim_sup.animate.set_color(YELLOW), GrowArrow(flecha_sup), FadeIn(txt_sup))
        self.wait(1.5)
        self.play(FadeOut(VGroup(txt_inf, txt_sup, flecha_inf, flecha_sup)))

        # 3. Reglas de integracion aplicadas termino a termino
        reglas = VGroup(
            MathTex(r"\int 2\,dt = 2t", font_size=40),
            MathTex(r"\int t\,dt = \frac{t^{2}}{2}", font_size=40),
        ).arrange(RIGHT, buff=1.2).next_to(paso1, DOWN, buff=0.8)
        texto = nota("Integramos término a término (regla de la potencia)")
        self.play(FadeIn(reglas, shift=UP * 0.3), FadeIn(texto))
        self.wait(2.5)

        # 4. Antiderivada evaluada entre 0 y x
        paso2 = ecuacion(r"\left[\,2t-\frac{t^{2}}{2}\,\right]_{0}^{x}")
        paso2[0].set_color(COLOR_A)
        self.play(TransformMatchingTex(paso1, paso2), FadeOut(reglas))
        self.wait(2)

        # 5. Evaluacion de los limites: valor en x menos valor en 0
        paso3 = ecuacion(
            r"\left(2x-\frac{x^{2}}{2}\right)", "-",
            r"\left(2\cdot 0-\frac{0^{2}}{2}\right)",
        )
        paso3[0].set_color(COLOR_A)
        texto2 = nota("Evaluamos: valor en x menos valor en 0")
        self.play(TransformMatchingTex(paso2, paso3), ReplacementTransform(texto, texto2))
        self.wait(2.5)

        paso4 = ecuacion(r"\left(2x-\frac{x^{2}}{2}\right)", "-", "0")
        paso4[0].set_color(COLOR_A)
        self.play(TransformMatchingTex(paso3, paso4))
        self.wait(1.5)

        # 6. Resultado final destacado
        resultado = ecuacion(r"2x-\frac{x^{2}}{2}").set_color(COLOR_A)
        caja = SurroundingRectangle(resultado, color=COLOR_A, buff=0.3)
        texto3 = nota("Esta es la función de acumulación")
        self.play(TransformMatchingTex(paso4, resultado), ReplacementTransform(texto2, texto3))
        self.play(Create(caja))
        self.wait(3)
        self.play(FadeOut(VGroup(titulo, resultado, caja, texto3)))


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