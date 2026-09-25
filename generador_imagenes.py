"""
generador_imagenes.py
=====================
Genera imagenes lado a lado:
  - IZQUIERDA : el codigo HTML con resaltado de sintaxis (estilo Dracula oscuro)
  - DERECHA   : captura de pantalla real del archivo en el navegador Chromium

Uso:
    py generador_imagenes.py                       -> procesa todos los archivos de act6/
    py generador_imagenes.py act6/practica14.html  -> solo ese archivo
    py generador_imagenes.py act5/                 -> todos los archivos de act5/

Las imagenes se guardan en capturas/<nombre_sin_extension>.png
"""

import sys
import os
from pathlib import Path
from io import BytesIO

from PIL import Image, ImageDraw, ImageFont
from pygments import highlight
from pygments.lexers import HtmlLexer
from pygments.formatters import ImageFormatter
from playwright.sync_api import sync_playwright

# ------------------------------------
# CONFIGURACION VISUAL
# ------------------------------------
BROWSER_WIDTH  = 900   # ancho del viewport del navegador
BROWSER_HEIGHT = 600   # alto del viewport del navegador
CODE_WIDTH     = 900   # ancho del panel de codigo
PADDING        = 30    # espacio alrededor
GAP            = 20    # separacion entre los dos paneles
FONT_SIZE      = 15    # tamano de fuente en la imagen de codigo

# Colores del marco final
BG_COLOR       = (18, 18, 24)      # fondo oscuro del cartel
ACCENT_COLOR   = (94, 129, 238)    # azul para titulos y bordes
HEADER_HEIGHT  = 50                # altura de la barra de titulo superior

OUTPUT_DIR = Path("capturas")


# ------------------------------------
# FUNCIONES
# ------------------------------------

def generar_imagen_codigo(html_code: str, width: int) -> Image.Image:
    """Renderiza el codigo HTML con resaltado de sintaxis y devuelve un Image."""
    formatter = ImageFormatter(
        style="dracula",
        font_name="Consolas",
        font_size=FONT_SIZE,
        line_numbers=True,
        line_number_bg="#1e1e2e",
        line_number_fg="#7f849c",
        image_pad=12,
    )
    png_bytes = highlight(html_code, HtmlLexer(), formatter)
    img = Image.open(BytesIO(png_bytes)).convert("RGBA")
    if img.width > width:
        ratio = width / img.width
        img = img.resize((width, int(img.height * ratio)), Image.LANCZOS)
    return img


def capturar_navegador(html_path: Path, width: int, height: int) -> Image.Image:
    """Abre el archivo en Chromium headless y devuelve la captura de pantalla."""
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page(viewport={"width": width, "height": height})
        page.goto(html_path.resolve().as_uri())
        page.wait_for_timeout(600)
        screenshot_bytes = page.screenshot(full_page=False)
        browser.close()
    return Image.open(BytesIO(screenshot_bytes)).convert("RGBA")


def agregar_label(img: Image.Image, text: str, color: tuple) -> Image.Image:
    """Agrega una barra de etiqueta en la parte superior de un panel."""
    bar_h = 32
    out = Image.new("RGBA", (img.width, img.height + bar_h), (0, 0, 0, 0))
    bar = Image.new("RGBA", (img.width, bar_h), color + (255,))
    draw = ImageDraw.Draw(bar)
    try:
        font = ImageFont.truetype("arial.ttf", 14)
    except Exception:
        font = ImageFont.load_default()
    draw.text((10, 7), text, fill=(255, 255, 255), font=font)
    out.paste(bar, (0, 0))
    out.paste(img, (0, bar_h))
    return out


def componer_imagen(code_img: Image.Image, browser_img: Image.Image, title: str) -> Image.Image:
    """Combina codigo + captura en una sola imagen con encabezado."""
    max_h = max(code_img.height, browser_img.height)

    def pad_bottom(im: Image.Image, target_h: int) -> Image.Image:
        if im.height >= target_h:
            return im
        canvas = Image.new("RGBA", (im.width, target_h), (30, 30, 40, 255))
        canvas.paste(im, (0, 0))
        return canvas

    code_img    = pad_bottom(code_img,    max_h)
    browser_img = pad_bottom(browser_img, max_h)

    total_w = PADDING + code_img.width + GAP + browser_img.width + PADDING
    total_h = HEADER_HEIGHT + PADDING + max_h + PADDING

    canvas = Image.new("RGBA", (total_w, total_h), BG_COLOR + (255,))
    draw = ImageDraw.Draw(canvas)

    # Encabezado
    draw.rectangle([(0, 0), (total_w, HEADER_HEIGHT)], fill=ACCENT_COLOR + (255,))
    try:
        font_title = ImageFont.truetype("arialbd.ttf", 20)
    except Exception:
        try:
            font_title = ImageFont.truetype("arial.ttf", 20)
        except Exception:
            font_title = ImageFont.load_default()
    draw.text((PADDING, 13), title, fill=(255, 255, 255), font=font_title)

    # Separador vertical
    x_sep = PADDING + code_img.width + GAP // 2
    draw.line([(x_sep, HEADER_HEIGHT + 5), (x_sep, total_h - 5)], fill=ACCENT_COLOR + (180,), width=2)

    # Pegar paneles
    canvas.paste(code_img,    (PADDING,                        HEADER_HEIGHT + PADDING), code_img)
    canvas.paste(browser_img, (PADDING + code_img.width + GAP, HEADER_HEIGHT + PADDING), browser_img)

    return canvas.convert("RGB")


def procesar_archivo(html_path: Path):
    """Genera la imagen lado a lado para un unico archivo HTML."""
    print(f"  -> Procesando: {html_path}")

    html_code = html_path.read_text(encoding="utf-8", errors="replace")

    code_img    = generar_imagen_codigo(html_code, CODE_WIDTH)
    code_img    = agregar_label(code_img,    "Codigo HTML",          (40, 44, 78))

    browser_img = capturar_navegador(html_path, BROWSER_WIDTH, BROWSER_HEIGHT)
    browser_img = agregar_label(browser_img, "Vista en el navegador", (30, 80, 60))

    stem  = html_path.stem
    title = stem.replace("_", " ").replace("practica", "Practica ").title()
    final = componer_imagen(code_img, browser_img, title)

    OUTPUT_DIR.mkdir(exist_ok=True)
    out_path = OUTPUT_DIR / f"{stem}.png"
    final.save(out_path, "PNG")
    print(f"     OK -> {out_path}")


def resolver_targets():
    """Determina que archivos procesar segun los argumentos."""
    if len(sys.argv) < 2:
        return sorted(Path("act6").glob("*.html"))

    targets = []
    for arg in sys.argv[1:]:
        p = Path(arg)
        if p.is_dir():
            targets.extend(sorted(p.glob("*.html")))
        elif p.is_file() and p.suffix == ".html":
            targets.append(p)
        else:
            print(f"Advertencia: No se reconoce: {arg}")
    return targets


# ------------------------------------
# MAIN
# ------------------------------------
if __name__ == "__main__":
    targets = resolver_targets()

    if not targets:
        print("No se encontraron archivos HTML. Comprueba la ruta.")
        sys.exit(1)

    print(f"\nGenerando {len(targets)} imagen(es) en '{OUTPUT_DIR}/'...\n")
    errores = []
    for html_path in targets:
        try:
            procesar_archivo(html_path)
        except Exception as e:
            errores.append((html_path, e))
            print(f"     ERROR en {html_path}: {e}")

    print(f"\nCompletado. {len(targets) - len(errores)}/{len(targets)} imagenes generadas.")
    if errores:
        print("Errores encontrados:")
        for p, e in errores:
            print(f"  {p}: {e}")
