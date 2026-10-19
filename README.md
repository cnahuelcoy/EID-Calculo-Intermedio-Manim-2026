
# EID – Cálculo Intermedio

## 1. Información del proyecto

- **Proyecto:** Teorema Fundamental del Cálculo – Parte I
- **Asignatura:** Cálculo Intermedio (MAT1188)
- **Universidad:** Universidad Católica de Temuco (UCT)
- **Evaluación:** Evaluación Integrada de Desempeño (EID)
- **Grupo:** 8
- **Año:** 2026
- **Tema:** Derivar una función de acumulación

**Pregunta central:** ¿Por qué la derivada de una acumulación recupera la función que se está acumulando?

## 2. Integrantes

| Nombre | GitHub |
|---|---|
| Carlos Nahuelcoy | [@cnahuelcoy](https://github.com/cnahuelcoy) |
| Rodrigo Sevilla | [@rsevilla1](https://github.com/rsevilla1) |
| Matías Salinas | [@matiassalinas2026-oss](https://github.com/matiassalinas2026-oss) |

## 3. Descripción y ejemplo matemático

El proyecto utiliza **Manim Community** para explicar la relación entre la integral definida y la derivada mediante una función de acumulación.

Se trabaja con la función continua:

$$
f(x)=2-x,\qquad x\in[0,4]
$$

Su función de acumulación es:

$$
A(x)=\int_0^x(2-t)\,dt=2x-\frac{x^2}{2}
$$

Al derivarla, se obtiene:

$$
A'(x)=2-x=f(x)
$$

Así se ilustra que **la derivada de la acumulación recupera la función original** en el interior del intervalo.

## 4. Organización del código

| Archivo | Responsable | Contenido |
|---|---|---|
| `escenas/carlos.py` | Carlos Nahuelcoy | Introducción, fundamentos y gráfica inicial (5 escenas) |
| `escenas/rodrigo.py` | Rodrigo Sevilla | Integral, gráfica y área con signo (3 escenas) |
| `escenas/matias.py` | Matías Salinas | Incremento, derivada, interpretación y créditos (4 escenas) |

**Orden del video:** Carlos → Rodrigo → Matías.

## 5. Requisitos e instalación

- **Python:** 3.12.10
- **Manim Community:** 0.22.0
- **Herramientas externas:** FFmpeg, LaTeX y `dvisvgm`.

Instalar las herramientas externas siguiendo la [guía oficial de Manim](https://docs.manim.community/en/stable/installation.html).

Clonar el proyecto y crear el entorno virtual:

```bash
git clone https://github.com/cnahuelcoy/EID-Calculo-Intermedio-Manim-2026.git
cd EID-Calculo-Intermedio-Manim-2026
python -m venv .venv
```

Activar el entorno en **Windows PowerShell**:

```powershell
.\.venv\Scripts\Activate.ps1
```

O en **Linux/macOS**:

```bash
source .venv/bin/activate
```

Instalar Manim:

```bash
python -m pip install "manim==0.22.0"
```

## 6. Generación de las animaciones

Desde la carpeta principal del repositorio, ejecutar:

```bash
manim -qh --fps 30 -a escenas/carlos.py
manim -qh --fps 30 -a escenas/rodrigo.py
manim -qh --fps 30 -a escenas/matias.py
```

Estos comandos generan las escenas en **1920 × 1080 a 30 FPS**. Los archivos se guardan en `media/videos/`. Para reproducir el video final se unen las escenas en el orden indicado y se incorporan las narraciones de los tres integrantes durante la edición.

## 7. Video final

- **Archivo:** `MAT1188_EID_G08_2026.mp4`
- **Duración:** 5 minutos y 20 segundos
- **Enlace:** [Ver video final en Google Drive](https://drive.google.com/file/d/1M_T0kTUDxF6cbX-dvAoLRpGABCmDk_m6/view?usp=sharing)

El MP4 y la ficha PDF se entregan por **Blackboard**, siguiendo la pauta del curso. El enlace de Drive permite consultar el video; debe comprobarse que los permisos permitan acceder al archivo.

## 8. Referencias y herramientas

1. Universidad Católica de Temuco. (s. f.). *Introducción a la integral: Apunte base común para el proyecto de investigación y visualización*. Material de Cálculo Intermedio.
2. Larson, R. y Edwards, B. H. (2010). *Cálculo 1 de una variable* (9.ª ed.). McGraw-Hill.
3. Strang, G. y Herman, E. (2016). *Calculus Volume 1*. OpenStax. https://openstax.org/books/calculus-volume-1
4. Manim Community. (s. f.). *Documentación oficial*. https://docs.manim.community/

## 9. Declaración de uso de IA

Se utilizó **ChatGPT (OpenAI)** como apoyo para resolver dudas matemáticas, organizar explicaciones y guiones y revisar código de las animaciones. Los integrantes son responsables de **verificar los cálculos con las fuentes citadas, comprobar los renderizados y revisar el contenido final** antes de la entrega.
