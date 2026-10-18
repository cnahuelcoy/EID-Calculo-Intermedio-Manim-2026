from manim import *

config.background_color = "#10141C"
config.pixel_width = 1920
config.pixel_height = 1080
config.frame_rate = 30
COLOR_F, COLOR_A, COLOR_H = BLUE, GREEN, ORANGE


def f(u):
    return 2 - u


def A(u):
    return 2 * u - u**2 / 2


def encabezado(texto):
    return Text(texto, font_size=34).to_edge(UP)


def nota(texto, tamano=23, margen=0.35):
    return Text(texto, font_size=tamano).to_edge(DOWN, buff=margen)


def ecuacion(tex, posicion=ORIGIN, tamano=34, ancho=12.4, color=WHITE):
    """Ajusta la fórmula al espacio disponible sin cambiar su contenido."""
    expresion = MathTex(tex, font_size=tamano, color=color)
    if expresion.width > ancho:
        expresion.scale_to_fit_width(ancho)
    return expresion.move_to(posicion)


def grafica_f(ancho=5.2, alto=3.8, tamano=20, lateral=True):
    """Comparte los ejes y la función entre incremento, cociente y límite."""
    ejes = Axes(
        x_range=[0, 4, 1], y_range=[-2, 2, 1],
        x_length=ancho, y_length=alto,
        axis_config={"font_size": tamano}, tips=False,
    )
    if lateral:
        ejes.to_edge(LEFT, buff=0.8)
    ejes.shift(DOWN * 0.2)
    # Se omite el número 1 para dejar sitio a las marcas x y x+h.
    ejes.add_coordinates([0, 2, 3, 4], [-2, -1, 1, 2])
    etiquetas = ejes.get_axis_labels(
        MathTex("t", font_size=tamano + 6),
        MathTex("f(t)", font_size=tamano + 6),
    )
    return ejes, etiquetas, ejes.plot(f, x_range=[0, 4], color=COLOR_F)


def area_extra(ejes, curva, x, h):
    if h <= 0:
        return VGroup()
    return ejes.get_area(curva, x_range=[x, x + h], color=COLOR_H, opacity=0.5)


def vertical(ejes, x, color=COLOR_H, discontinua=False):
    tipo = DashedLine if discontinua else Line
    return tipo(ejes.c2p(x, 0), ejes.c2p(x, f(x)), color=color)


def marca(ejes, texto, x, color, tamano=26, margen=0.1):
    return MathTex(texto, font_size=tamano, color=color).next_to(
        ejes.c2p(x, 0), DOWN, buff=margen)


def intervalo_h(ejes, x, h, punta=0.08):
    return DoubleArrow(ejes.c2p(x, -0.65), ejes.c2p(x + h, -0.65),
                       color=COLOR_H, buff=0, tip_length=punta)


def cerrar(escena):
    """Detiene los actualizadores antes de desvanecer los objetos."""
    for objeto in escena.mobjects:
        objeto.clear_updaters()
    escena.play(*[FadeOut(objeto) for objeto in escena.mobjects])


class IncrementoExtremoSuperior(Scene):
    def construct(self):
        titulo = encabezado("Incremento del extremo superior")
        formula = MathTex(r"A(x)=\int_0^x(2-t)\,dt", font_size=40, color=COLOR_A)
        formula.next_to(titulo, DOWN, buff=0.25)
        ejes, etiquetas, curva = grafica_f(9, 3.6, 22, lateral=False)
        nombre_f = MathTex("f(t)=2-t", font_size=34, color=COLOR_F)
        nombre_f.move_to(ejes.c2p(2.9, 1.4))
        x = 1  # Rodrigo termina en x=1.
        h = ValueTracker(0)
        area = ejes.get_area(curva, x_range=[0, x], color=COLOR_A, opacity=0.4)
        linea_x = vertical(ejes, x, COLOR_A, discontinua=True)
        etiqueta_x = marca(ejes, "x=1", x, COLOR_A, tamano=28, margen=0.15)
        rotulo_area = MathTex("A(x)", font_size=28, color=COLOR_A)
        rotulo_area.move_to(ejes.c2p(0.45, 0.55))
        extra = always_redraw(lambda: area_extra(ejes, curva, x, h.get_value()))
        extremo = always_redraw(lambda: vertical(ejes, x + h.get_value()))

        self.play(Write(titulo), Write(formula))
        self.play(Create(ejes), Write(etiquetas), Create(curva), Write(nombre_f))
        self.play(FadeIn(area), Create(linea_x), Write(etiqueta_x), Write(rotulo_area))
        self.wait(2)
        self.add(extra, extremo)
        self.bring_to_front(ejes, etiquetas, curva, linea_x, etiqueta_x, rotulo_area)
        self.play(h.animate.set_value(0.5), run_time=3)
        extra.clear_updaters()
        extremo.clear_updaters()

        etiqueta_final = marca(ejes, "x+h", x + h.get_value(), COLOR_H,
                               tamano=28, margen=0.15)
        segmento_h = intervalo_h(ejes, x, h.get_value(), punta=0.1)
        etiqueta_h = MathTex("h", font_size=28, color=COLOR_H)
        etiqueta_h.next_to(segmento_h, DOWN, buff=0.1)
        rotulo_extra = MathTex(r"\Delta A", font_size=24, color=COLOR_H)
        rotulo_extra.move_to(ejes.c2p(x + h.get_value() / 2, 0.35))
        self.play(Write(etiqueta_final), GrowArrow(segmento_h), Write(etiqueta_h))
        self.play(Write(rotulo_extra))
        cambio = MathTex(r"\Delta A", "=", "A(x+h)-A(x)", font_size=38)
        cambio.to_edge(DOWN, buff=0.95)
        cambio[0].set_color(COLOR_H)
        cambio[2].set_color(COLOR_A)
        self.play(Write(cambio))
        self.wait(3)
        self.play(FadeIn(nota(
            "Si f es negativa, su aporte a la acumulación es negativo.", 22, 0.3)))
        self.wait(3)
        cerrar(self)


class CocienteIncrementalYDerivada(Scene):
    def construct(self):
        titulo = encabezado("Razón de cambio promedio")
        formula = MathTex(r"A(x)=\int_0^x(2-t)\,dt", font_size=38, color=COLOR_A)
        formula.next_to(titulo, DOWN, buff=0.25)
        x, h = 1, 0.5
        delta_a = A(x + h) - A(x)
        ejes, etiquetas, curva = grafica_f()
        nombre_f = MathTex("f(t)=2-t", font_size=30, color=COLOR_F)
        nombre_f.move_to(ejes.c2p(2.8, 1.4))
        area = ejes.get_area(curva, x_range=[0, x], color=COLOR_A, opacity=0.25)
        extra = area_extra(ejes, curva, x, h)
        limites = VGroup(
            vertical(ejes, x, COLOR_A, discontinua=True),
            vertical(ejes, x + h, COLOR_H, discontinua=True),
        )
        marcas = [
            marca(ejes, "x", x, COLOR_A, tamano=24),
            marca(ejes, "x+h", x + h, COLOR_H, tamano=24),
        ]
        ancho = intervalo_h(ejes, x, h)
        etiqueta_h = MathTex("h", font_size=26, color=COLOR_H)
        etiqueta_h.next_to(ancho, DOWN, buff=0.1)
        datos = MathTex(rf"x={x:g},\quad h={h:g}>0", font_size=28)
        datos.next_to(ejes, DOWN, buff=0.35)
        posicion = RIGHT * 3 + UP * 0.8
        cambio, integral, cociente = [ecuacion(tex, posicion, ancho=5.6) for tex in (
            r"\Delta A=A(x+h)-A(x)",
            r"A(x+h)-A(x)=\int_x^{x+h}(2-t)\,dt",
            r"\frac{A(x+h)-A(x)}{h}=\frac{1}{h}\int_x^{x+h}(2-t)\,dt",
        )]
        condicion = MathTex(r"h\ne0", font_size=28, color=COLOR_H)
        condicion.move_to(RIGHT * 3 + DOWN * 0.15)
        detalle = nota("La región naranja mide el cambio de acumulación.")
        promedio = nota("Dividir por h da la razón de cambio promedio.")
        ejemplo = MathTex(rf"\frac{{{delta_a:g}}}{{{h:g}}}={delta_a / h:g}",
                          font_size=46, color=COLOR_H)
        ejemplo.move_to(RIGHT * 3 + DOWN * 1.3)

        self.play(Write(titulo), Write(formula))
        self.play(Create(ejes), Write(etiquetas), Create(curva), Write(nombre_f))
        self.play(FadeIn(area), FadeIn(extra), Create(limites))
        self.play(*[Write(m) for m in marcas], GrowArrow(ancho), Write(etiqueta_h))
        self.play(Write(datos), Write(cambio), FadeIn(detalle))
        self.wait(2)
        # Aditividad: al restar queda el tramo adicional entre x y x+h.
        self.play(TransformMatchingTex(cambio, integral), Indicate(extra, color=COLOR_H))
        self.wait(2)
        self.play(TransformMatchingTex(integral, cociente), Indicate(ancho, color=COLOR_H))
        self.play(Write(condicion), ReplacementTransform(detalle, promedio))
        self.wait(2)
        self.play(Write(ejemplo))
        self.wait(4)
        cerrar(self)
        self.mostrar_derivada()

    def mostrar_derivada(self):
        titulo = encabezado("Del cociente a la derivada")
        condiciones = MathTex(r"0<x<4,\quad h\ne0,\quad x+h\in[0,4]",
                              font_size=28, color=COLOR_H)
        condiciones.next_to(titulo, DOWN, buff=0.3)
        base = MathTex(r"A(x)=2x-\frac{x^2}{2}", font_size=40, color=COLOR_A)
        base.move_to(UP * 1.3)
        paso = ecuacion(r"A'(x)=\lim_{h\to0}\frac{A(x+h)-A(x)}{h}",
                        DOWN * 0.3, tamano=42)
        detalle = nota("Usamos la definición de derivada.", 24, 0.65)
        self.play(Write(titulo), Write(condiciones), Write(base))
        self.play(Write(paso), FadeIn(detalle))
        self.wait(1)
        pasos = [
            (r"A(x+h)=2(x+h)-\frac{(x+h)^2}{2}",
             "Evaluamos la acumulación en x+h."),
            (r"A(x+h)-A(x)=\left[2(x+h)-\frac{(x+h)^2}{2}\right]"
             r"-\left[2x-\frac{x^2}{2}\right]",
             "Restamos la acumulación anterior, conservando los signos."),
            (r"A(x+h)-A(x)=2x+2h-\frac{x^2+2xh+h^2}{2}-2x+\frac{x^2}{2}",
             "Desarrollamos el cuadrado y distribuimos el signo menos."),
            (r"A(x+h)-A(x)=2h-xh-\frac{h^2}{2}",
             "Cancelamos los términos iguales y reducimos."),
            (r"A(x+h)-A(x)=h\left(2-x-\frac{h}{2}\right)",
             "Factorizamos el incremento h."),
            (r"\frac{A(x+h)-A(x)}{h}=2-x-\frac{h}{2}",
             "Dividimos por h, que es distinto de cero."),
        ]
        for tex, explicacion in pasos:
            siguiente = ecuacion(tex, DOWN * 0.3, tamano=42)
            nueva_nota = nota(explicacion, 24, 0.65)
            self.play(TransformMatchingTex(paso, siguiente),
                      ReplacementTransform(detalle, nueva_nota))
            self.wait(1)
            paso, detalle = siguiente, nueva_nota
        cerrar(self)
        self.mostrar_limite()

    def mostrar_limite(self):
        titulo = encabezado("Cuando h tiende a cero")
        x = 1
        h = ValueTracker(0.5)
        ejes, etiquetas, curva = grafica_f()
        referencia = DashedLine(ejes.c2p(0, f(x)), ejes.c2p(4, f(x)),
                                color=COLOR_F, stroke_opacity=0.5)
        punto = Dot(ejes.c2p(x, f(x)), color=COLOR_F)
        datos = MathTex(r"x=1,\quad f(1)=1", font_size=30, color=COLOR_F)
        datos.next_to(ejes, DOWN, buff=0.35)
        extra = always_redraw(lambda: area_extra(ejes, curva, x, h.get_value()))
        extremo = always_redraw(lambda: vertical(ejes, x + h.get_value()))
        promedio = always_redraw(lambda: DashedLine(
            ejes.c2p(0, f(x) - h.get_value() / 2),
            ejes.c2p(4, f(x) - h.get_value() / 2), color=COLOR_H))
        ancho = always_redraw(lambda: Line(ejes.c2p(x, -0.65),
            ejes.c2p(x + h.get_value(), -0.65), color=COLOR_H, stroke_width=5))
        etiqueta_h = MathTex("h", font_size=26, color=COLOR_H)
        etiqueta_h.add_updater(lambda m: m.next_to(ancho, DOWN, buff=0.1))
        limite = MathTex(r"A'(x)=\lim_{h\to0}\left(2-x-\frac{h}{2}\right)",
                         font_size=36).scale_to_fit_width(5.7)
        limite.move_to(RIGHT * 3 + UP * 1.2)
        valor_h = DecimalNumber(0.5, num_decimal_places=3, font_size=32, color=COLOR_H)
        valor_tasa = DecimalNumber(0.75, num_decimal_places=3, font_size=32, color=COLOR_H)
        valor_h.add_updater(lambda m: m.set_value(h.get_value()))
        valor_tasa.add_updater(lambda m: m.set_value(f(x) - h.get_value() / 2))
        lecturas = VGroup(
            VGroup(MathTex("h=", font_size=32), valor_h).arrange(RIGHT, buff=0.2),
            VGroup(MathTex(r"\frac{\Delta A}{h}=", font_size=32), valor_tasa)
                .arrange(RIGHT, buff=0.2),
        ).arrange(DOWN, buff=0.35, aligned_edge=LEFT)
        lecturas.move_to(RIGHT * 3 + DOWN * 0.8)
        rotulo = Text("Tasa promedio", font_size=24, color=COLOR_H)
        rotulo.next_to(lecturas, UP, buff=0.3)
        detalle = nota("Figura: h>0. El álgebra también vale para h<0.")

        self.play(Write(titulo), Create(ejes), Write(etiquetas), Create(curva))
        self.add(extra, extremo, promedio, ancho, etiqueta_h)
        self.bring_to_front(ejes, etiquetas, curva)
        self.play(Create(referencia), FadeIn(punto), Write(datos), Write(limite))
        self.play(FadeIn(lecturas), FadeIn(rotulo), FadeIn(detalle))
        self.wait(1)
        for destino, pausa in [(0.1, 1), (0.02, 2)]:
            self.play(h.animate.set_value(destino), run_time=3)
            self.wait(pausa)
        cerrar(self)
        resultado = MathTex(r"A'(x)=2-x=f(x)", font_size=60, color=COLOR_A)
        caja = SurroundingRectangle(resultado, color=COLOR_A, buff=0.3)
        continuidad = Text("f(t)=2-t es continua en [0,4]: "
                           "se cumplen las condiciones del TFC I.", font_size=25)
        continuidad.next_to(resultado, DOWN, buff=0.8)
        interior = MathTex("0<x<4", font_size=30).next_to(continuidad, DOWN, buff=0.35)
        self.play(Write(resultado), Create(caja))
        self.play(FadeIn(continuidad), Write(interior))
        self.wait(3)
        cerrar(self)


class InterpretacionAcumulacion(Scene):
    def construct(self):
        titulo = encabezado("Interpretación de la acumulación")
        relacion = MathTex(r"A'(x)=f(x)=2-x", color=COLOR_F, font_size=40)
        relacion.next_to(titulo, DOWN, buff=0.25)
        estilo = {"x_range": [0, 4, 1], "x_length": 5.2, "tips": False,
                  "axis_config": {"include_numbers": True, "font_size": 20}}
        ejes_f = Axes(y_range=[-2, 2, 1], y_length=3.4, **estilo)
        ejes_f.to_edge(LEFT, buff=0.8).shift(DOWN * 0.2)
        ejes_a = Axes(y_range=[0, 2.5, 1], y_length=2.125, **estilo).to_edge(RIGHT, buff=0.8)
        ejes_a.shift(UP * (ejes_f.c2p(0, 0)[1] - ejes_a.c2p(0, 0)[1]))
        curvas = VGroup(ejes_f.plot(f, x_range=[0, 4], color=COLOR_F),
                        ejes_a.plot(A, x_range=[0, 4], color=COLOR_A))
        etiquetas = VGroup(
            ejes_f.get_axis_labels(
                MathTex("x", font_size=24), MathTex("f(x)", font_size=24),
            ),
            ejes_a.get_axis_labels(
                MathTex("x", font_size=24), MathTex("A(x)", font_size=24),
            ),
        )
        nombre_a = MathTex(r"A(x)=2x-\frac{x^2}{2}", color=COLOR_A, font_size=30)
        nombre_a.move_to(ejes_a.c2p(2.2, 2.65))
        self.play(Write(titulo), Write(relacion))
        self.play(Create(ejes_f), Create(ejes_a), Create(curvas),
                  Write(etiquetas), Write(nombre_a), run_time=2)
        casos = [
            (1, r"0<x<2:\quad A'(x)=f(x)>0", "A crece: la pendiente es positiva."),
            (2, r"x=2:\quad A'(2)=0,\quad A(2)=2",
             "La pendiente cambia de positiva a negativa: máximo."),
            (3, r"2<x<4:\quad A'(x)=f(x)<0", "A decrece; su valor todavía es positivo."),
        ]
        for x, tex, explicacion in casos:
            # El segmento sobre A tiene pendiente f(x), también cuando es cero.
            tangente = Line(
                ejes_a.c2p(x - 0.35, A(x) - 0.35 * f(x)),
                ejes_a.c2p(x + 0.35, A(x) + 0.35 * f(x)),
                color=COLOR_F, stroke_width=6,
            )
            marcas = VGroup(
                Dot(ejes_f.c2p(x, f(x)), color=COLOR_F),
                Dot(ejes_a.c2p(x, A(x)), color=COLOR_A),
                tangente,
            )
            expresion = MathTex(tex, font_size=34).move_to(DOWN * 2.65)
            grupo = VGroup(marcas, expresion, nota(explicacion, 24, 0.3))
            self.play(FadeIn(grupo))
            self.wait(3)
            self.play(FadeOut(grupo))
        cerrar(self)


class ConclusionYCreditos(Scene):
    def construct(self):
        titulo = encabezado("Conclusión")
        resultado = MathTex(r"A'(x)=2-x=f(x)", font_size=54, color=COLOR_A).shift(UP * 0.7)
        mensaje = Text("La integral acumula aportes con signo.\n"
            "La derivada recupera la función continua\ncomo razón de cambio instantánea.",
            font_size=28, line_spacing=1.2).next_to(resultado, DOWN, buff=0.7)
        self.play(Write(titulo), run_time=1)
        self.play(Write(resultado), FadeIn(mensaje), run_time=1)
        self.wait(4)
        cerrar(self)

        def pantalla(texto, contenido, pausa):
            titulo = encabezado(texto)
            if contenido.width > 12.2:
                contenido.scale_to_fit_width(12.2)
            contenido.move_to(DOWN * 0.2)
            self.play(FadeIn(titulo), FadeIn(contenido), run_time=0.6)
            self.wait(pausa)
            self.play(FadeOut(titulo), FadeOut(contenido), run_time=0.6)

        apunte = MarkupText("Universidad Católica de Temuco. (s. f.).\n"
            "<i>Introducción a la integral: Apunte base común\n"
            "para el proyecto de investigación y visualización</i>.\nMaterial de Cálculo Intermedio.",
            font_size=28, line_spacing=0.4)
        pantalla("Referencias bibliográficas (1/2)", apunte, 8)
        libros = VGroup(
            MarkupText("Larson, R. y Edwards, B. H. (2010).\n"
                "<i>Cálculo 1 de una variable</i> (9.ª ed.). McGraw-Hill.",
                font_size=28, line_spacing=0.4),
            MarkupText("Strang, G. y Herman, E. (2016).\n<i>Calculus Volume 1</i>. OpenStax.",
                font_size=28, line_spacing=0.4),
        ).arrange(DOWN, buff=0.8)
        pantalla("Referencias bibliográficas (2/2)", libros, 10)
        declaracion = Text("«Se utilizó inteligencia artificial como herramienta\n"
            "de apoyo para resolver dudas puntuales y revisar\nerrores ortográficos en el informe.\n"
            "Los contenidos matemáticos fueron revisados\npor los integrantes del grupo».",
            font_size=28, line_spacing=0.4)
        pantalla("Declaración de uso de IA", declaracion, 11)
        proyecto = VGroup(
            Text("Herramienta de animación: Manim Community v0.22.0", font_size=28, color=COLOR_A),
            Text("Universidad Católica de Temuco", font_size=28),
            Text("Asignatura: Cálculo Intermedio", font_size=28),
            Text("Tema: Teorema Fundamental del Cálculo, Parte I", font_size=28),
        ).arrange(DOWN, buff=0.4)
        pantalla("Créditos finales", proyecto, 5)
