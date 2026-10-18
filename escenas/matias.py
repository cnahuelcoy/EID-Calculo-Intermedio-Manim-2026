from manim import *

#parte 3: Matias Salinas
#Etapa 1 estructura inicial

config.background_color= "#10141C"
config.pixel_width= 1920
config.pixel_height= 1080
config.frame_rate= 30 

#Colores acordados 
COLOR_F = BLUE
COLOR_A = GREEN
COLOR_H = ORANGE

def presentar_estructura(escena, titulo, descripcion):
    encabezado = Text(titulo, font_size=36)
    detalle = Text(descripcion, font_size=25)

    contenido = VGroup(
        encabezado,
        detalle,
    ). arrange(DOWN, buff=0.5)

    escena.play(Write(encabezado), run_time=1)
    escena.play(FadeIn(detalle), run_time=0.6)
    escena.wait(2)
    escena.play(FadeOut(contenido), run_time=0.6)

class IncrementoExtremoSuperior(Scene):
    def construct(self):
        titulo = Text(
            "Incremento del extremo superior", font_size=34,
        ).to_edge(UP)

        formula = MathTex(
            r"A(x)=\int_0^x(2-t)\,dt",
            font_size=40, color=COLOR_A,
        ).next_to(titulo, DOWN, buff=0.25)

        ejes = Axes(
            x_range=[0, 4, 1],
            y_range=[-2, 2, 1],
            x_length=9,
            y_length=3.6,
            axis_config={"font_size": 22},
            tips=False,
        ).shift(DOWN * 0.2)

        # Dejamos espacio para la etiqueta x=1.
        ejes.add_coordinates([0, 2, 3, 4], [-2, -1, 1, 2])

        etiquetas = ejes.get_axis_labels(
            x_label=MathTex("t", font_size=28),
            y_label=MathTex("f(t)", font_size=28),
        )

        curva = ejes.plot(
            lambda t: 2 - t, x_range=[0, 4], color=COLOR_F,
        )
        nombre_f = MathTex(
            r"f(t)=2-t", font_size=34, color=COLOR_F,
        ).move_to(ejes.c2p(2.9, 1.4))

        # Rodrigo termina en x=1; continuamos desde ahí.
        x = 1
        h = ValueTracker(0)

        area = ejes.get_area(
            curva, x_range=[0, x], color=COLOR_A, opacity=0.4,
        )
        linea_x = DashedLine(
            ejes.c2p(x, 0), ejes.c2p(x, 2 - x), color=COLOR_A,
        )
        etiqueta_x = MathTex(
            "x=1", font_size=28, color=COLOR_A,
        ).next_to(ejes.c2p(x, 0), DOWN, buff=0.15)

        rotulo_area = MathTex(
            "A(x)", font_size=28, color=COLOR_A,
        ).move_to(ejes.c2p(0.45, 0.55))

        def crear_area_extra():
            if h.get_value() <= 0:
                return VGroup()

            return ejes.get_area(
                curva,
                x_range=[x, x + h.get_value()],
                color=COLOR_H,
                opacity=0.5,
            )

        extra = always_redraw(crear_area_extra)
        extremo = always_redraw(lambda: Line(
            ejes.c2p(x + h.get_value(), 0),
            ejes.c2p(x + h.get_value(), 2 - x - h.get_value()),
            color=COLOR_H,
        ))

        self.play(Write(titulo), Write(formula))
        self.play(
            Create(ejes), Write(etiquetas),
            Create(curva), Write(nombre_f),
        )
        self.play(
            FadeIn(area), Create(linea_x),
            Write(etiqueta_x), Write(rotulo_area),
        )
        self.wait(2)

        self.add(extra, extremo)
        self.bring_to_front(
            ejes, etiquetas, curva, linea_x, etiqueta_x, rotulo_area,
        )
        self.play(h.animate.set_value(0.5), run_time=3)

        extra.clear_updaters()
        extremo.clear_updaters()

        etiqueta_final = MathTex(
            "x+h", font_size=28, color=COLOR_H,
        ).next_to(ejes.c2p(x + h.get_value(), 0), DOWN, buff=0.15)

        segmento_h = DoubleArrow(
            ejes.c2p(x, -0.65),
            ejes.c2p(x + h.get_value(), -0.65),
            color=COLOR_H, buff=0, tip_length=0.1,
        )
        etiqueta_h = MathTex(
            "h", font_size=28, color=COLOR_H,
        ).next_to(segmento_h, DOWN, buff=0.1)

        rotulo_extra = MathTex(
            r"\Delta A", font_size=24, color=COLOR_H,
        ).move_to(ejes.c2p(x + h.get_value() / 2, 0.35))

        self.play(
            Write(etiqueta_final),
            GrowArrow(segmento_h),
            Write(etiqueta_h),
        )
        self.play(Write(rotulo_extra))

        cambio = MathTex(
            r"\Delta A", "=", r"A(x+h)-A(x)", font_size=38,
        ).to_edge(DOWN, buff=0.95)

        cambio[0].set_color(COLOR_H)
        cambio[2].set_color(COLOR_A)

        self.play(Write(cambio))
        self.wait(3)

        nota = Text(
            "Si f es negativa, su aporte a la acumulación es negativo.",
            font_size=22,
        ).to_edge(DOWN, buff=0.3)

        self.play(FadeIn(nota))
        self.wait(3)
        self.play(*[FadeOut(objeto) for objeto in self.mobjects])

class CocienteIncrementalYDerivada(Scene):
    def construct(self):
        titulo = Text(
            "Razón de cambio promedio", font_size=34,
        ).to_edge(UP)

        formula_a = MathTex(
            r"A(x)=\int_0^x(2-t)\,dt",
            font_size=38, color=COLOR_A,
        ).next_to(titulo, DOWN, buff=0.25)

        x = 1
        h = 0.5

        def A(u):
            return 2 * u - u**2 / 2

        
        delta_a = A(x + h) - A(x)
        tasa = delta_a / h

        ejes = Axes(
            x_range=[0, 4, 1],
            y_range=[-2, 2, 1],
            x_length=5.2,
            y_length=3.8,
            axis_config={"font_size": 20},
            tips=False,
        ).to_edge(LEFT, buff=0.8).shift(DOWN * 0.2)

        ejes.add_coordinates([0, 2, 3, 4], [-2, -1, 1, 2])

        etiquetas = ejes.get_axis_labels(
            x_label=MathTex("t", font_size=26),
            y_label=MathTex("f(t)", font_size=26),
        )
        curva = ejes.plot(
            lambda t: 2 - t, x_range=[0, 4], color=COLOR_F,
        )
        nombre_f = MathTex(
            r"f(t)=2-t", font_size=30, color=COLOR_F,
        ).move_to(ejes.c2p(2.8, 1.4))

        area_anterior = ejes.get_area(
            curva, x_range=[0, x], color=COLOR_A, opacity=0.25,
        )
        extra = ejes.get_area(
            curva, x_range=[x, x + h], color=COLOR_H, opacity=0.5,
        )
        limites = VGroup(
            DashedLine(
                ejes.c2p(x, 0),
                ejes.c2p(x, 2 - x),
                color=COLOR_A,
            ),
            DashedLine(
                ejes.c2p(x + h, 0),
                ejes.c2p(x + h, 2 - x - h),
                color=COLOR_H,
            ),
        )

        marca_x=  MathTex("x", font_size=24, color= COLOR_A)
        marca_x.next_to(ejes.c2p(x, 0), DOWN, buff=0.1)


        marca_final = MathTex("x+h", font_size=24, color=COLOR_H)
        marca_final.next_to(ejes.c2p(x + h, 0), DOWN, buff=0.1)

        ancho = DoubleArrow(
            ejes.c2p(x, -0.65),
            ejes.c2p(x + h, -0.65),
            color=COLOR_H, buff=0, tip_length=0.08,
        )
        etiqueta_h = MathTex("h", font_size=26, color=COLOR_H)
        etiqueta_h.next_to(ancho, DOWN, buff=0.1)

        datos = MathTex(
            rf"x={x:g},\quad h={h:g}>0",
            font_size=28,
        ).next_to(ejes, DOWN, buff=0.35)

        # Sustituimos las ecuaciones en la misma posición.
        def ecuacion(tex):
            expresion = MathTex(tex, font_size=34)
            if expresion.width > 5.6:
                expresion.scale_to_fit_width(5.6)
            return expresion.move_to(RIGHT * 3 + UP * 0.8)

        cambio = ecuacion(
            r"\Delta A=A(x+h)-A(x)"
        )
        integral = ecuacion(
            r"A(x+h)-A(x)=\int_x^{x+h}(2-t)\,dt"
        )
        cociente = ecuacion(
            r"\frac{A(x+h)-A(x)}{h}"
            r"=\frac{1}{h}\int_x^{x+h}(2-t)\,dt"
        )

        condicion = MathTex(
            r"h\ne0", font_size=28, color=COLOR_H,
        ).move_to(RIGHT * 3 + DOWN * 0.15)

        nota = Text(
            "La región naranja mide el cambio de acumulación.",
            font_size=23,
        ).to_edge(DOWN, buff=0.35)

        nota_promedio = Text(
            "Dividir por h da la razón de cambio promedio.",
            font_size=23,
        ).to_edge(DOWN, buff=0.35)

        ejemplo = MathTex(
            rf"\frac{{{delta_a:g}}}{{{h:g}}}={tasa:g}",
            font_size=46, color=COLOR_H,
        ).move_to(RIGHT * 3 + DOWN * 1.3)

        self.play(Write(titulo), Write(formula_a))
        self.play(
            Create(ejes), Write(etiquetas),
            Create(curva), Write(nombre_f),
        )
        self.play(
            FadeIn(area_anterior), FadeIn(extra), Create(limites),
        )
        self.play(
            Write(marca_x), Write(marca_final),
            GrowArrow(ancho), Write(etiqueta_h),
        )
        self.play(Write(datos), Write(cambio), FadeIn(nota))
        self.wait(2)

        # Aditividad: al restar, queda el tramo entre x y x+h.
        self.play(
            TransformMatchingTex(cambio, integral),
            Indicate(extra, color=COLOR_H),
        )
        self.wait(2)

        self.play(
            TransformMatchingTex(integral, cociente),
            Indicate(ancho, color=COLOR_H),
        )
        self.play(
            Write(condicion),
            ReplacementTransform(nota, nota_promedio),
        )
        self.wait(2)

        self.play(Write(ejemplo))
        self.wait(4)
        self.play(*[FadeOut(objeto) for objeto in self.mobjects])
        self.mostrar_derivada()

    def mostrar_derivada(self):
        titulo = Text(
            "Del cociente a la derivada", font_size=34,
        ).to_edge(UP)

        condiciones = MathTex(
            r"0<x<4,\quad h\ne0,\quad x+h\in[0,4]",
            font_size=28, color=COLOR_H,
        ).next_to(titulo, DOWN, buff=0.3)

        base = MathTex(
            r"A(x)=2x-\frac{x^2}{2}",
            font_size=40, color=COLOR_A,
        ).move_to(UP * 1.3)

        def formula(tex):
            expresion = MathTex(tex, font_size=42)
            if expresion.width > 12.4:
                expresion.scale_to_fit_width(12.4)
            return expresion.move_to(DOWN * 0.3)

        paso = formula(
            r"A'(x)=\lim_{h\to0}\frac{A(x+h)-A(x)}{h}"
        )
        nota = Text(
            "Usamos la definición de derivada.", font_size=24,
        ).to_edge(DOWN, buff=0.65)

        self.play(Write(titulo), Write(condiciones), Write(base))
        self.play(Write(paso), FadeIn(nota))
        self.wait(1)

        pasos = [
            (
                r"A(x+h)=2(x+h)-\frac{(x+h)^2}{2}",
                "Evaluamos la acumulación en x+h.",
            ),
            (
                r"A(x+h)-A(x)=\left[2(x+h)-\frac{(x+h)^2}{2}\right]"
                r"-\left[2x-\frac{x^2}{2}\right]",
                "Restamos la acumulación anterior, conservando los signos.",
            ),
            (
                r"A(x+h)-A(x)=2x+2h-\frac{x^2+2xh+h^2}{2}"
                r"-2x+\frac{x^2}{2}",
                "Desarrollamos el cuadrado y distribuimos el signo menos.",
            ),
            (
                r"A(x+h)-A(x)=2h-xh-\frac{h^2}{2}",
                "Cancelamos los términos iguales y reducimos.",
            ),
            (
                r"A(x+h)-A(x)=h\left(2-x-\frac{h}{2}\right)",
                "Factorizamos el incremento h.",
            ),
            (
                r"\frac{A(x+h)-A(x)}{h}=2-x-\frac{h}{2}",
                "Dividimos por h, que es distinto de cero.",
            ),
        ]

        for tex, explicacion in pasos:
            siguiente = formula(tex)
            nueva_nota = Text(
                explicacion, font_size=24,
            ).to_edge(DOWN, buff=0.65)

            self.play(
                TransformMatchingTex(paso, siguiente),
                ReplacementTransform(nota, nueva_nota),
            )
            self.wait(1)
            paso, nota = siguiente, nueva_nota

        self.play(*[FadeOut(objeto) for objeto in self.mobjects])

        titulo = Text(
            "Cuando h tiende a cero", font_size=34,
        ).to_edge(UP)

        x = 1
        h = ValueTracker(0.5)

        ejes = Axes(
            x_range=[0, 4, 1],
            y_range=[-2, 2, 1],
            x_length=5.2,
            y_length=3.8,
            axis_config={"font_size": 20},
            tips=False,
        ).to_edge(LEFT, buff=0.8).shift(DOWN * 0.2)

        ejes.add_coordinates([0, 2, 3, 4], [-2, -1, 1, 2])
        etiquetas = ejes.get_axis_labels(
            x_label=MathTex("t", font_size=26),
            y_label=MathTex("f(t)", font_size=26),
        )
        curva = ejes.plot(
            lambda t: 2 - t, x_range=[0, 4], color=COLOR_F,
        )

        referencia = DashedLine(
            ejes.c2p(0, 2 - x),
            ejes.c2p(4, 2 - x),
            color=COLOR_F, stroke_opacity=0.5,
        )
        punto = Dot(ejes.c2p(x, 2 - x), color=COLOR_F)

        datos = MathTex(
            r"x=1,\quad f(1)=1",
            font_size=30, color=COLOR_F,
        ).next_to(ejes, DOWN, buff=0.35)

        extra = always_redraw(lambda: ejes.get_area(
            curva,
            x_range=[x, x + h.get_value()],
            color=COLOR_H,
            opacity=0.5,
        ))
        extremo = always_redraw(lambda: Line(
            ejes.c2p(x + h.get_value(), 0),
            ejes.c2p(x + h.get_value(), 2 - x - h.get_value()),
            color=COLOR_H,
        ))
        promedio = always_redraw(lambda: DashedLine(
            ejes.c2p(0, 2 - x - h.get_value() / 2),
            ejes.c2p(4, 2 - x - h.get_value() / 2),
            color=COLOR_H,
        ))
        ancho = always_redraw(lambda: Line(
            ejes.c2p(x, -0.65),
            ejes.c2p(x + h.get_value(), -0.65),
            color=COLOR_H, stroke_width=5,
        ))

        etiqueta_h = MathTex("h", font_size=26, color=COLOR_H)
        etiqueta_h.add_updater(
            lambda m: m.next_to(ancho, DOWN, buff=0.1)
        )

        limite = MathTex(
            r"A'(x)=\lim_{h\to0}\left(2-x-\frac{h}{2}\right)",
            font_size=36,
        ).scale_to_fit_width(5.7).move_to(RIGHT * 3 + UP * 1.2)

        valor_h = DecimalNumber(
            0.5, num_decimal_places=3,
            font_size=32, color=COLOR_H,
        )
        valor_tasa = DecimalNumber(
            0.75, num_decimal_places=3,
            font_size=32, color=COLOR_H,
        )
        valor_h.add_updater(
            lambda m: m.set_value(h.get_value())
        )
        valor_tasa.add_updater(
            lambda m: m.set_value(2 - x - h.get_value() / 2)
        )

        lecturas = VGroup(
            VGroup(
                MathTex("h=", font_size=32), valor_h,
            ).arrange(RIGHT, buff=0.2),
            VGroup(
                MathTex(r"\frac{\Delta A}{h}=", font_size=32),
                valor_tasa,
            ).arrange(RIGHT, buff=0.2),
        ).arrange(DOWN, buff=0.35, aligned_edge=LEFT)

        lecturas.move_to(RIGHT * 3 + DOWN * 0.8)

        rotulo = Text(
            "Tasa promedio", font_size=24, color=COLOR_H,
        ).next_to(lecturas, UP, buff=0.3)

        nota = Text(
            "Figura: h>0. El álgebra también vale para h<0.",
            font_size=23,
        ).to_edge(DOWN, buff=0.35)

        self.play(
            Write(titulo), Create(ejes),
            Write(etiquetas), Create(curva),
        )
        self.add(extra, extremo, promedio, ancho, etiqueta_h)
        self.bring_to_front(ejes, etiquetas, curva)

        self.play(
            Create(referencia), FadeIn(punto),
            Write(datos), Write(limite),
        )
        self.play(FadeIn(lecturas), FadeIn(rotulo), FadeIn(nota))
        self.wait(1)

        self.play(h.animate.set_value(0.1), run_time=3)
        self.wait(1)
        self.play(h.animate.set_value(0.02), run_time=3)
        self.wait(2)

        for objeto in (
            extra, extremo, promedio, ancho,
            etiqueta_h, valor_h, valor_tasa,
        ):
            objeto.clear_updaters()

        self.play(*[FadeOut(objeto) for objeto in self.mobjects])

        resultado = MathTex(
            r"A'(x)=2-x=f(x)", font_size=60, color=COLOR_A,
        )
        caja = SurroundingRectangle(
            resultado, color=COLOR_A, buff=0.3,
        )
        continuidad = Text(
            "f(t)=2-t es continua en [0,4]: "
            "se cumplen las condiciones del TFC I.",
            font_size=25,
        ).next_to(resultado, DOWN, buff=0.8)

        interior = MathTex(
            r"0<x<4", font_size=30,
        ).next_to(continuidad, DOWN, buff=0.35)

        self.play(Write(resultado), Create(caja))
        self.play(FadeIn(continuidad), Write(interior))
        self.wait(3)
        self.play(*[FadeOut(objeto) for objeto in self.mobjects])
    

class InterpretacionAcumulacion(Scene):
    def construct(self):
        def f(u):
            return 2 - u
        def A(u):
            return 2 * u - u**2 / 2

        titulo = Text("Interpretación de la acumulación", font_size=34).to_edge(UP)
        relacion = MathTex(r"A'(x)=f(x)=2-x", color=COLOR_F, font_size=40)
        relacion.next_to(titulo, DOWN, buff=0.25)
        estilo = {
            "x_range": [0, 4, 1], "x_length": 5.2, "tips": False,
            "axis_config": {"include_numbers": True, "font_size": 20},
        }
        ejes_f = Axes(y_range=[-2, 2, 1], y_length=3.4, **estilo)
        ejes_f.to_edge(LEFT, buff=0.8).shift(DOWN * 0.2)
        ejes_a = Axes(y_range=[0, 2.5, 1], y_length=2.125, **estilo)
        ejes_a.to_edge(RIGHT, buff=0.8)
        ejes_a.shift(UP * (ejes_f.c2p(0, 0)[1] - ejes_a.c2p(0, 0)[1]))
        curvas = VGroup(
            ejes_f.plot(f, x_range=[0, 4], color=COLOR_F),
            ejes_a.plot(A, x_range=[0, 4], color=COLOR_A),
        )
        etiquetas = VGroup(
            ejes_f.get_axis_labels(MathTex("x", font_size=24), MathTex("f(x)", font_size=24)),
            ejes_a.get_axis_labels(MathTex("x", font_size=24), MathTex("A(x)", font_size=24)),
        )
        nombre_a = MathTex(r"A(x)=2x-\frac{x^2}{2}", color=COLOR_A, font_size=30)
        nombre_a.move_to(ejes_a.c2p(2.2, 2.65))
        self.play(Write(titulo), Write(relacion))
        self.play(Create(ejes_f), Create(ejes_a), Create(curvas), Write(etiquetas), Write(nombre_a), run_time=2)

        casos = [
            (1, r"0<x<2:\quad A'(x)=f(x)>0",
             "A crece: la pendiente es positiva."),
            (2, r"x=2:\quad A'(2)=0,\quad A(2)=2",
             "La pendiente cambia de positiva a negativa: máximo."),
            (3, r"2<x<4:\quad A'(x)=f(x)<0",
             "A decrece; su valor todavía es positivo."),
        ]
        for x, tex, explicacion in casos:
            marcas = VGroup(
                Dot(ejes_f.c2p(x, f(x)), color=COLOR_F),
                Dot(ejes_a.c2p(x, A(x)), color=COLOR_A),
                Line(
                    ejes_a.c2p(x - 0.35, A(x) - 0.35 * f(x)),
                    ejes_a.c2p(x + 0.35, A(x) + 0.35 * f(x)),
                    color=COLOR_F, stroke_width=6,
                ),
            )
            expresion = MathTex(tex, font_size=34).move_to(DOWN * 2.65)
            nota = Text(explicacion, font_size=24).to_edge(DOWN, buff=0.3)
            grupo = VGroup(marcas, expresion, nota)
            self.play(FadeIn(grupo))
            self.wait(3)
            self.play(FadeOut(grupo))

        self.play(*[FadeOut(objeto) for objeto in self.mobjects])

class ConclusionYCreditos(Scene):
     def construct(self):
        presentar_estructura(
            self,
            "Conclusión y créditos",
            "Estructura inicial: respuesta central y cierre del grupo.",
        )

