## =============================================================================
## AUDIO
## =============================================================================
## Canales de audio (piensa en ellos como "pistas" de una mesa de mezcla):
##
##   music     -> la música. Solo suena UNA pista a la vez y se repite en loop.
##   sound     -> efectos puntuales (golpes, pasos). Uno a la vez: un sonido
##                nuevo corta al anterior.
##   audio     -> efectos que pueden SUPERPONERSE (varios a la vez).
##   ambiente  -> canal PROPIO (lo creamos abajo): sonido de fondo en loop
##                (viento, fuego) que convive con la música.
##
## Uso en el guion:
##   play music presagio fadein 3.0          (entra suave en 3 segundos)
##   play ambiente chimenea fadeout 1.5 fadein 1.5
##   play sound golpes_puerta
##   queue sound armaduras_pasos             (suena cuando termine el anterior)
##   stop music fadeout 2.0
## =============================================================================

init python:
    ## mixer="sfx" -> lo controla el volumen de "Sonido" en Preferencias.
    ## loop=True   -> todo lo que se reproduzca aquí se repite solo.
    renpy.music.register_channel("ambiente", mixer="sfx", loop=True)

## Al volver al menú principal, Ren'Py corta los canales de esta lista. Por
## defecto no incluye nuestro canal nuevo: sin esta línea, si sales al menú en
## medio del balcón, el viento seguiría sonando sobre el menú.
define config.main_menu_stop_channels = ["sound", "voice", "movie", "audio", "ambiente"]


## --- Catálogo de sonidos -----------------------------------------------------
## `define audio.nombre` crea un alias: en el guion escribes `presagio` en vez
## de la ruta completa. Si mañana cambias el archivo, cambias UNA línea aquí.
##
## (Ren'Py también crea alias automáticos para los archivos de game/audio/,
## pero declararlos a mano sirve de índice: ves todo el audio de un vistazo.)
##
## Licencias y autores: ver CREDITOS.md en la raíz del proyecto.

## Música
define audio.presagio = "audio/musica/presagio.mp3"
define audio.llamado_a_las_armas = "audio/musica/llamado_a_las_armas.ogg"

## Ambientes (en loop)
define audio.viento_tormenta = "audio/ambiente/viento_tormenta.mp3"
define audio.chimenea = "audio/ambiente/chimenea.mp3"

## Efectos
define audio.trueno = "audio/sfx/trueno.mp3"
define audio.golpes_puerta = "audio/sfx/golpes_puerta.mp3"
define audio.puerta_abre = "audio/sfx/puerta_abre.ogg"
define audio.armaduras_pasos = "audio/sfx/armaduras_pasos.mp3"
define audio.desenvainar = "audio/sfx/desenvainar.ogg"
define audio.espada_resonancia = "audio/sfx/espada_resonancia.mp3"

## Música del menú principal (la misma que abre el prólogo, así el paso del
## menú al juego se siente continuo).
define config.main_menu_music = audio.presagio
