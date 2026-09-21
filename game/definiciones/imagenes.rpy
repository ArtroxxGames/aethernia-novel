## =============================================================================
## IMÁGENES
## =============================================================================
## Convención de nombres: "etiqueta atributo"
##
##     bg balcon_noche   -> etiqueta "bg", atributo "balcon_noche"
##
## Ren'Py agrupa las imágenes por ETIQUETA: al mostrar un "bg" nuevo, reemplaza
## automáticamente al anterior. Por eso todos los fondos empiezan con "bg".
## (Más adelante, los sprites seguirán la misma idea: "ailen feliz",
## "ailen triste"... y cambiar de expresión reemplaza la anterior.)
##
## Imágenes AUTOMÁTICAS: todo archivo dentro de game/images/ se define solo,
## usando su nombre sin extensión (las subcarpetas se ignoran). Por eso
## "chispa", "vineta" y "resplandor_dorado" (en images/efectos/) ya existen
## sin escribir nada. Solo definimos a mano las que necesitan ajustes.
## =============================================================================


## --- Fondos ------------------------------------------------------------------
## Las ilustraciones miden 1408x768 (proporción 1.83:1) y la pantalla 1920x1080
## (1.78:1). Hay dos formas de hacerlas encajar:
##
##   xysize solo   -> ESTIRA la imagen hasta que entre: queda deformada (~3%).
##   fit "cover"   -> la AGRANDA SIN deformar hasta cubrir la pantalla; lo que
##                    sobra (unos pocos píxeles a los costados) queda fuera.
##
## Como vamos a repetir lo mismo en cada fondo, lo encapsulamos en una función.
## (Regla DRY: si copias y pegas lo mismo tres veces, conviértelo en función.)

init python:

    def fondo(archivo):
        """Escala una ilustración para cubrir toda la pantalla sin deformarla."""
        return Transform(
            "images/fondos/" + archivo,
            fit="cover",
            xysize=(config.screen_width, config.screen_height),
        )

## Nota: `image` se ejecuta en init 500 y `init python` en init 0, así que la
## función `fondo` ya existe cuando se definen estas imágenes.
image bg balcon_noche = fondo("noche_estrellada_1.jpg")
image bg puerta_aposentos = fondo("tocan_puerta.jpg")
image bg aposentos_soldados = fondo("soldados_entrando.jpg")


## --- Fondos de los menús -----------------------------------------------------
## Se usan en gui.rpy (gui.main_menu_background / gui.game_menu_background).

## Menú principal: el balcón con un zoom lentísimo de ida y vuelta, para que
## la pantalla "respire" en lugar de ser una foto quieta.
image fondo_menu_principal:
    "bg balcon_noche"
    align (0.5, 0.5)
    zoom 1.0
    ease 25.0 zoom 1.06
    ease 25.0 zoom 1.0
    repeat

## Menús del juego (guardar, cargar, preferencias): el mismo balcón,
## desenfocado y oscurecido para que el texto se lea bien encima.
image fondo_menu_juego = Transform(
    "bg balcon_noche",
    blur=18,
    matrixcolor=TintMatrix("#6a6a6a"),   # 42% del brillo original
)


## --- Efectos -----------------------------------------------------------------
## Partículas de luz dorada que SUBEN (yspeed negativo). Aparecen en la leyenda
## y cuando despierta la espada: repetir el mismo efecto crea un MOTIVO visual
## y el jugador asocia "chispas doradas = poder de la espada" sin que nadie se
## lo explique.
##
## SnowBlossom(imagen, count=cantidad, xspeed=deriva lateral, yspeed=velocidad
##             vertical, fast=True para que arranquen repartidas por la pantalla)
image chispas_doradas = SnowBlossom(
    "chispa",
    count=36,
    border=40,
    xspeed=(-18, 18),
    yspeed=(-70, -25),
    fast=True,
)
