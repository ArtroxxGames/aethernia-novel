## =============================================================================
## PERSONAJES
## =============================================================================
## Aquí se declaran TODOS los personajes que hablan en la historia.
##
## ¿Por qué `define` y no `default`?
##   `define` es para cosas que NO cambian durante la partida (constantes).
##   Un personaje siempre es el mismo: su nombre y su estilo no se guardan en
##   las partidas. Si mañana cambias el color del rey, los jugadores que ya
##   tienen partidas guardadas también verán el cambio. Eso es lo que queremos.
##
## Convención de nombres:
##   - Variable corta y en minúsculas: la vas a escribir cientos de veces.
##   - Nombre visible: es lo que el jugador lee en la caja de nombre.
## =============================================================================


## --- Narración ---------------------------------------------------------------
## Ren'Py YA incluye un narrador: cualquier línea sin personaje es narración.
##
##     "El viento sopla."      <- esto ya es narración, no hace falta declarar nada
##
## (Antes existía `narrador_vacio = Character("")`: funcionaba, pero era un
## personaje extra que hacía lo mismo que el narrador que ya viene incluido.)


## Voz de la LEYENDA: texto centrado, sin caja de diálogo, como la apertura de
## una película.
##   kind=centered  -> "hereda" todo del personaje `centered` que trae Ren'Py;
##                     solo sobrescribimos lo que queremos cambiar.
##   what_*         -> estilo del TEXTO (what = lo que se dice).
##   window_*       -> estilo del CONTENEDOR del texto.
define leyenda = Character(
    None,
    kind=centered,
    what_font="fonts/EBGaramond-Regular.ttf",
    what_size=46,
    what_color="#f3e6c4",
    what_outlines=[(2, "#000000aa", 0, 0)],
    what_line_spacing=6,
    window_xmaximum=1300,   # limita el ancho: las líneas largas cansan la vista
)

## Carteles de título ("Prólogo", "Capítulo 1"...). Reutiliza la voz de la
## leyenda, pero con la tipografía de títulos.
define titulo = Character(
    None,
    kind=leyenda,
    what_font="fonts/Cinzel-Regular.ttf",
    what_size=72,
    what_color="#e8c170",
)


## --- Personajes --------------------------------------------------------------
## El color de cada nombre ayuda a reconocer quién habla sin leer la etiqueta.

define rey = Character("Rey Leofric", color="#e8c170")        # dorado: realeza
define soldado = Character("Soldado", color="#9fb3c8")        # gris acero
define soldados = Character("Soldados", color="#9fb3c8")
define voces = Character("Voces tras la puerta", color="#b0a89a")

## Ailen todavía no aparece en el prólogo; la dejamos declarada para cuando le
## toque entrar en escena.
define ailen = Character("Ailen", color="#b9a3e3")
