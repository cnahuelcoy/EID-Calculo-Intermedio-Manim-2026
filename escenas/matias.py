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




class InterpretacionAcumulacion(Scene):
    def construct(self):
        presentar_estructura(
            self,
            "Interpretación de la acumulación",
            "Estructura inicial: crecimiento, máximo y decrecimiento.",
        )

class ConclusionYCreditos(Scene):
     def construct(self):
        presentar_estructura(
            self,
            "Conclusión y créditos",
            "Estructura inicial: respuesta central y cierre del grupo.",
        )

