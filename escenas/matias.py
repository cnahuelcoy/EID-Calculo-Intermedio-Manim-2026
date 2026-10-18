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
        presentar_estructura(self,
                             "Incremento del extremo superior",
                             "Estructura inicial: desplazamiento del extremo superior.")

class CocienteIncrementalYDerivada(Scene):
    def construct(self):
        presentar_estructura(self,
            "Cociente incremental y derivada",
            "Estructura inicial: razón de cambio, límite y derivada.",
        )

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
