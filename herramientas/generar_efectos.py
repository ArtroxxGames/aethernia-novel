"""
Generador de imágenes de efectos para Aethernia.

¿Por qué un script y no imágenes "sueltas"?
    Porque así los efectos son REPRODUCIBLES: si quieres un dorado más cálido
    o una viñeta más oscura, cambias un número aquí y lo vuelves a ejecutar.
    Nadie tiene que acordarse de "cómo hice esa imagen en Photoshop".

Uso (desde la raíz del proyecto):
    python3 herramientas/generar_efectos.py

Requisitos:
    pip install pillow

Genera en game/images/efectos/:
    - resplandor_dorado.png  -> luz radial dorada (se dibuja con mezcla aditiva)
    - chispa.png             -> partícula de luz pequeña y difusa
    - vineta.png             -> bordes oscuros para escenas introspectivas
"""

from pathlib import Path

from PIL import Image, ImageFilter

# Resolución del juego (tiene que coincidir con gui.init en gui.rpy).
ANCHO, ALTO = 1920, 1080

DESTINO = Path(__file__).resolve().parent.parent / "game" / "images" / "efectos"


def gradiente_radial(ancho, alto, centro, radio, color, potencia=2.0, alfa_max=255):
    """Crea un círculo de color que se desvanece hacia afuera.

    `potencia` controla la curva: valores altos = centro más concentrado.
    """
    img = Image.new("RGBA", (ancho, alto), (0, 0, 0, 0))
    px = img.load()
    cx, cy = centro
    r, g, b = color
    for y in range(alto):
        for x in range(ancho):
            d = ((x - cx) ** 2 + (y - cy) ** 2) ** 0.5 / radio
            if d < 1.0:
                intensidad = (1.0 - d) ** potencia
                px[x, y] = (r, g, b, int(alfa_max * intensidad))
    return img


def generar_resplandor():
    # Centrado un poco abajo del medio: ahí "estaría" la espada en manos del rey.
    # Mismo truco que la viñeta: calculamos a 1/4 de resolución y escalamos.
    e = 4
    img = gradiente_radial(
        ANCHO // e, ALTO // e, centro=(ANCHO // (2 * e), int(ALTO * 0.62) // e),
        radio=900 // e, color=(255, 196, 92), potencia=2.2, alfa_max=235,
    )
    img = img.resize((ANCHO, ALTO), Image.BICUBIC)
    img.save(DESTINO / "resplandor_dorado.png", optimize=True)


def generar_chispa():
    # Se dibuja grande y se achica: así el borde queda suave (antialiasing).
    grande = gradiente_radial(96, 96, centro=(48, 48), radio=46,
                              color=(255, 226, 150), potencia=1.8)
    chica = grande.resize((24, 24), Image.LANCZOS)
    chica.save(DESTINO / "chispa.png", optimize=True)


def generar_vineta():
    # Viñeta = negro en los bordes, transparente en el centro.
    # Trabajamos en baja resolución y escalamos (mucho más rápido, y el
    # resultado es un degradado igual de suave).
    escala = 8
    w, h = ANCHO // escala, ALTO // escala
    mascara = Image.new("L", (w, h), 0)
    px = mascara.load()
    cx, cy = w / 2, h / 2
    for y in range(h):
        for x in range(w):
            # Distancia "elíptica": respeta la forma 16:9 de la pantalla.
            d = (((x - cx) / cx) ** 2 + ((y - cy) / cy) ** 2) ** 0.5
            valor = max(0.0, min(1.0, (d - 0.55) / 0.6))
            px[x, y] = int(230 * valor ** 1.6)
    mascara = mascara.resize((ANCHO, ALTO), Image.BICUBIC).filter(ImageFilter.GaussianBlur(6))
    negro = Image.new("RGBA", (ANCHO, ALTO), (0, 0, 0, 255))
    negro.putalpha(mascara)
    negro.save(DESTINO / "vineta.png", optimize=True)


if __name__ == "__main__":
    DESTINO.mkdir(parents=True, exist_ok=True)
    generar_chispa()
    generar_vineta()
    generar_resplandor()
    print(f"Efectos generados en {DESTINO}")
