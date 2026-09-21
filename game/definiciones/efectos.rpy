## =============================================================================
## TRANSICIONES Y TRANSFORMS (ATL)
## =============================================================================
## - Una TRANSICIÓN dice CÓMO se pasa de una imagen a otra
##   (se usa con `with`).
## - Un TRANSFORM dice cómo se COMPORTA una imagen mientras está en pantalla:
##   posición, zoom, desenfoque, color, movimiento... (se usa con `at`).
##
##     scene bg balcon_noche with fundido_lento     <- transición
##     show bg balcon_noche at enfocar              <- transform
##
## Cómo leer un transform ATL:
##     propiedad valor                 -> valor inicial (instantáneo)
##     linear 2.0 propiedad valor      -> llega a ese valor en 2 s, velocidad constante
##     ease 2.0 ...                    -> igual, pero acelera y frena (más natural)
##     easein / easeout                -> solo frena al final / solo acelera al inicio
##     block: ... repeat               -> repite el bloque (para siempre o N veces)
##
## TRAMPA 1: `matrixcolor` solo se anima de forma suave si el valor inicial y
## el final son del mismo tipo. Si arranca en None (sin color), SALTA de golpe.
## Por eso cada transform declara su matrixcolor inicial explícitamente.
##
## TRAMPA 2: para OSCURECER usa TintMatrix, no BrightnessMatrix.
##   BrightnessMatrix(-0.3) RESTA 0.3 a cada color: todo lo que ya era oscuro
##                          se vuelve negro puro y se pierde el detalle.
##   TintMatrix("#8c8c8c")  MULTIPLICA cada color por 0.55 (8c = 140 de 255):
##                          oscurece de forma pareja y conserva las texturas.
## (Lo descubrimos probando: con BrightnessMatrix la puerta de la escena de
## la espada quedaba completamente negra.)
## =============================================================================


## --- Transiciones ------------------------------------------------------------

## Fundido cruzado lento: para momentos contemplativos.
define fundido_lento = Dissolve(2.0)

## A negro, pausa breve, desde negro: cambio de escena "con respiración".
define fundido_negro = Fade(1.0, 0.4, 1.0)

## Relámpago: la pantalla se pone blanca un instante y vuelve.
## Fade(ida, espera, vuelta, color=...)
define relampago = Fade(0.08, 0.0, 0.7, color="#ffffff")

## Destello dorado: el momento en que la espada se ilumina.
define destello_dorado = Fade(0.2, 0.1, 1.4, color="#ffe9b0")


## --- Cámara: leyenda y enfoque -----------------------------------------------

## Fondo de la leyenda: desenfocado, oscuro, desaturado y con un zoom
## lentísimo (efecto "Ken Burns", como en los documentales).
transform fondo_leyenda:
    subpixel True           # movimiento suave, sin saltos de píxel
    align (0.5, 0.5)        # el zoom se hace desde el centro
    blur 10
    matrixcolor TintMatrix("#707070") * SaturationMatrix(0.6)
    zoom 1.12
    linear 45.0 zoom 1.02

## "Enfoque de cámara": del recuerdo borroso al presente nítido.
## Arranca con los MISMOS valores del final de la leyenda para que no haya
## un salto, y luego los lleva a la normalidad.
transform enfocar(duracion=3.0):
    subpixel True
    align (0.5, 0.5)
    blur 10
    matrixcolor TintMatrix("#707070") * SaturationMatrix(0.6)
    easein duracion blur 0 matrixcolor TintMatrix("#ffffff") * SaturationMatrix(1.0) zoom 1.0


## --- Introspección: cuando el personaje se pierde en sus pensamientos --------

## La escena se aleja: un poco de desenfoque y oscuridad.
transform introspeccion:
    blur 0
    matrixcolor TintMatrix("#ffffff")
    ease 1.5 blur 4 matrixcolor TintMatrix("#a6a6a6")

## Vuelta al presente.
transform fin_introspeccion:
    blur 4
    matrixcolor TintMatrix("#a6a6a6")
    ease 1.0 blur 0 matrixcolor TintMatrix("#ffffff")


## --- La espada ---------------------------------------------------------------

## Penumbra: el rey queda solo; la habitación se oscurece para que la luz de
## la espada destaque. Es estático (sin animación), así que combinarlo con
## otros transforms (`at penumbra, temblor`) no produce saltos.
transform penumbra:
    blur 2
    matrixcolor TintMatrix("#8c8c8c") * SaturationMatrix(0.8)

## Vibración: sacudida lateral corta. `veces` = cuántas idas y vueltas.
## (Solo horizontal: el fondo es un poco más ancho que la pantalla, así que
## moverlo de costado no deja ver bordes negros.)
transform temblor(intensidad=4, veces=10):
    xoffset 0
    block:
        linear 0.04 xoffset intensidad
        linear 0.04 xoffset -intensidad
        repeat veces
    linear 0.04 xoffset 0

## Resplandor que "respira". `additive 1.0` = mezcla aditiva: SUMA luz a lo
## que hay debajo (como una luz real), en vez de pintar encima.
transform pulso_dorado:
    align (0.5, 0.5)
    additive 1.0
    alpha 0.0
    easein 2.0 alpha 0.55
    block:
        ease 1.4 alpha 0.8
        ease 1.4 alpha 0.55
        repeat

## El resplandor crece y se vuelve más intenso.
transform resplandor_creciente:
    align (0.5, 0.5)
    additive 1.0
    ease 2.0 alpha 1.0 zoom 1.25
    block:
        ease 1.1 alpha 0.85
        ease 1.1 alpha 1.0
        repeat
