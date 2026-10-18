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
        formula = MathTex(r"A(x)=2x-\frac{x^{2}}{2}", font_size=44, color=COLOR_A)
        formula.next_to(titulo, DOWN, buff=0.35)
        self.play(Write(titulo))
        self.play(Write(formula))
        self.wait(1)

        # Calculo de los cinco puntos: A(x) se evalua con la funcion de Python,
        # asi el numero mostrado siempre coincide con la formula.
        filas = VGroup()
        for x in range(5):
            valor = f"{A(x):g}"  # 0, 1.5, 2, 1.5, 0
            calculo = MathTex(
                rf"A({x})=2({x})-\frac{{{x}^{{2}}}}{{2}}={valor}", font_size=36
            )
            calculo[0][:4].set_color(COLOR_A)
            coordenada = MathTex(rf"\rightarrow\ ({x},\,{valor})", font_size=36, color=YELLOW)
            filas.add(VGroup(calculo, coordenada).arrange(RIGHT, buff=0.4))
        filas.arrange(DOWN, aligned_edge=LEFT, buff=0.25)
        filas.next_to(formula, DOWN, buff=0.45)
        # Alinear las flechas en una misma columna
        borde = max(fila[0].get_right()[0] for fila in filas) + 0.4
        for fila in filas:
            fila[1].shift(RIGHT * (borde - fila[1].get_left()[0]))

        for fila in filas:
            self.play(Write(fila[0]), run_time=1.2)
            self.play(FadeIn(fila[1], shift=LEFT * 0.2), run_time=0.6)
        self.wait(2)

        # Grafica de A(x) en el intervalo [0, 4]
        self.play(FadeOut(filas), formula.animate.to_corner(UR).shift(DOWN * 0.9))
        ejes = Axes(
            x_range=[0, 4.5, 1], y_range=[0, 2.5, 0.5], x_length=8, y_length=4.4,
            axis_config={"include_numbers": True, "font_size": 24}, tips=False,
        ).shift(DOWN * 0.6)
        etiquetas = ejes.get_axis_labels(x_label=MathTex("x"), y_label=MathTex("A(x)"))
        curva = ejes.plot(A, x_range=[0, 4], color=COLOR_A, stroke_width=5)
        self.play(Create(ejes), Write(etiquetas))
        self.play(Create(curva), run_time=3)

        # Los cinco puntos calculados, cada uno con su coordenada
        direcciones = [UL, UL, UP, UR, UR]
        puntos = VGroup()
        for x, d in zip(range(5), direcciones):
            punto = Dot(ejes.c2p(x, A(x)), color=YELLOW, radius=0.09)
            texto = MathTex(rf"({x},\,{A(x):g})", font_size=28, color=YELLOW)
            texto.next_to(punto, d, buff=0.3 if x == 2 else 0.12)
            puntos.add(VGroup(punto, texto))
            self.play(FadeIn(punto, scale=1.5), Write(texto), run_time=0.6)
        self.wait(1)

        # Maximo en (2, 2)
        guia_x = DashedLine(ejes.c2p(2, 0), ejes.c2p(2, 2), color=YELLOW)
        guia_y = DashedLine(ejes.c2p(0, 2), ejes.c2p(2, 2), color=YELLOW)
        anillo = Circle(radius=0.2, color=YELLOW).move_to(ejes.c2p(2, 2))
        maximo = Text("máximo: A(2) = 2", font_size=24, color=YELLOW)
        maximo.next_to(puntos[2][1], UP, buff=0.15)
        self.play(Create(guia_x), Create(guia_y), Create(anillo), FadeIn(maximo))
        self.wait(2)

        # Donde la acumulacion aumenta y donde disminuye
        sube = Arrow(ejes.c2p(0.55, 0.45), ejes.c2p(1.45, 1.15), buff=0, color=WHITE)
        baja = Arrow(ejes.c2p(2.55, 1.15), ejes.c2p(3.45, 0.45), buff=0, color=WHITE)
        txt_sube = Text("A crece", font_size=24).next_to(sube, DOWN, buff=0.1)
        txt_baja = Text("A decrece", font_size=24).next_to(baja, DOWN, buff=0.1)
        self.play(GrowArrow(sube), FadeIn(txt_sube))
        self.wait(1)
        self.play(GrowArrow(baja), FadeIn(txt_baja))
        self.wait(3)

        self.play(*[FadeOut(m) for m in self.mobjects])


class AreaAcumulada(Scene):
    """Escena 3: area con signo bajo f(t) y extremo superior variable."""

    def construct(self):
        titulo = titulo_escena("Interpretación del área acumulada")
        self.play(Write(titulo))

        # Funcion original f(t) = 2 - t en el panel izquierdo
        ejes_f = Axes(
            x_range=[0, 4.5, 1], y_range=[-2.5, 2.5, 1], x_length=5.0, y_length=4.4,
            axis_config={"include_numbers": True, "font_size": 22}, tips=False,
        ).to_edge(LEFT, buff=0.9).shift(DOWN * 0.4)
        etiquetas_f = ejes_f.get_axis_labels(x_label=MathTex("t"), y_label=MathTex("f(t)"))
        graf_f = ejes_f.plot(f, x_range=[0, 4], color=COLOR_F, stroke_width=5)
        formula_f = MathTex(r"f(t)=2-t", font_size=36, color=COLOR_F)
        formula_f.next_to(ejes_f, UP, buff=0.1).shift(RIGHT * 1.5)
        self.play(Create(ejes_f), Write(etiquetas_f))
        self.play(Create(graf_f), Write(formula_f))
        self.wait(1)

        # Region donde f >= 0 (aporte positivo) y donde f < 0 (aporte negativo)
        area_pos = ejes_f.get_area(graf_f, x_range=[0, 2], color=BLUE, opacity=0.35)
        area_neg = ejes_f.get_area(graf_f, x_range=[2, 4], color=RED, opacity=0.35)
        signo_pos = MathTex("+", font_size=48).move_to(ejes_f.c2p(0.65, 0.6))
        signo_neg = MathTex("-", font_size=48).move_to(ejes_f.c2p(3.35, -0.6))

        aporte_pos = MathTex(r"\int_{0}^{2}(2-t)\,dt=2", font_size=36, color=BLUE)
        aporte_neg = MathTex(r"\int_{2}^{4}(2-t)\,dt=-2", font_size=36, color=RED)
        texto_pos = Text("aporte positivo (f ≥ 0)", font_size=22, color=BLUE)
        texto_neg = Text("aporte negativo (f < 0)", font_size=22, color=RED)
        geometrica = MathTex(r"\text{Área geométrica}=2+2=4", font_size=34)
        neta = MathTex(r"\text{Acumulación neta}=A(4)=2+(-2)=0", font_size=34, color=COLOR_A)
        panel = VGroup(
            VGroup(aporte_pos, texto_pos).arrange(DOWN, buff=0.15),
            VGroup(aporte_neg, texto_neg).arrange(DOWN, buff=0.15),
            geometrica, neta,
        ).arrange(DOWN, buff=0.45).to_edge(RIGHT, buff=0.6).shift(DOWN * 0.3)

        self.play(FadeIn(area_pos), Write(signo_pos))
        self.bring_to_front(ejes_f, graf_f)
        self.play(Write(panel[0]))
        self.wait(1.5)
        self.play(FadeIn(area_neg), Write(signo_neg))
        self.bring_to_front(ejes_f, graf_f)  # numeros y curva sobre el relleno
        self.play(Write(panel[1]))
        self.wait(1.5)

        # Area geometrica (siempre positiva) frente a acumulacion con signo
        self.play(Write(geometrica))
        self.wait(1.5)
        self.play(Write(neta))
        self.wait(3)

        self.play(*[FadeOut(m) for m in self.mobjects])