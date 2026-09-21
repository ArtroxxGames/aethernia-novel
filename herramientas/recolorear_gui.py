"""
Recolorea las imágenes de la GUI de Ren'Py: del rosa por defecto (#cc0066)
al dorado de Aethernia (#c9a45c).

Contexto:
    Cuando se crea un proyecto, el launcher de Ren'Py GENERA las imágenes de
    game/gui/ (barras, sliders, botones, fondos de menú) usando el "color de
    acento" elegido. Cambiar gui.accent_color en gui.rpy solo cambia los
    TEXTOS; las imágenes siguen del color viejo.

    La forma oficial de regenerarlas es: Launcher -> "Cambiar/Actualizar GUI"
    -> elegir color -> "Regenerar archivos de imagen". Este script hace lo
    mismo sobre las imágenes existentes, rotando el tono (hue) de los píxeles
    rosas hacia el dorado y dejando intactos los grises/negros.

Uso (desde la raíz del proyecto):
    python3 herramientas/recolorear_gui.py

Ojo: es IDEMPOTENTE solo en un sentido: una vez recoloreado, ya no hay
píxeles rosas, así que correrlo dos veces no cambia nada.
"""

import colorsys
from pathlib import Path

from PIL import Image

GUI = Path(__file__).resolve().parent.parent / "game" / "gui"

# Tono y saturación del dorado destino (#c9a45c -> h=40°, s=0.54).
TONO_DESTINO = 40 / 360
FACTOR_SATURACION = 0.54


def es_rosa(h, s):
    """Tono ~300°-360°/0°-7° con algo de saturación = el acento viejo."""
    return s > 0.12 and (h > 0.83 or h < 0.02)


def recolorear(ruta):
    img = Image.open(ruta).convert("RGBA")
    datos = list(img.getdata())
    cambiados = 0
    nuevos = []
    for r, g, b, a in datos:
        h, s, v = colorsys.rgb_to_hsv(r / 255, g / 255, b / 255)
        if a > 0 and es_rosa(h, s):
            r2, g2, b2 = colorsys.hsv_to_rgb(TONO_DESTINO, s * FACTOR_SATURACION, v)
            nuevos.append((round(r2 * 255), round(g2 * 255), round(b2 * 255), a))
            cambiados += 1
        else:
            nuevos.append((r, g, b, a))
    if cambiados:
        img.putdata(nuevos)
        img.save(ruta, optimize=True)
    return cambiados


if __name__ == "__main__":
    for ruta in sorted(GUI.rglob("*.png")):
        n = recolorear(ruta)
        if n:
            print(f"{ruta.relative_to(GUI.parent)}: {n} píxeles recoloreados")
