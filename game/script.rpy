## =============================================================================
## PUNTO DE ENTRADA DEL JUEGO
## =============================================================================
## Ren'Py siempre empieza en `label start`. Úsalo como un ÍNDICE: no escribas
## la historia aquí, solo llama a cada escena en orden. Así:
##   - ves la estructura completa de un vistazo,
##   - reordenar escenas es mover una línea,
##   - puedes probar una escena suelta desde la consola (Shift+O):
##         jump prologo_espada
##
## ¿Dónde está cada cosa?
##   definiciones/  -> personajes, imágenes, audio, efectos y variables
##   historia/      -> el guion, un archivo por capítulo
##
## `call` salta a una escena y, cuando esa escena hace `return`, vuelve aquí
## y sigue con la línea siguiente. `jump` salta y NO vuelve.
## =============================================================================

label start:

    ## Prólogo (historia/prologo.rpy)
    call prologo_leyenda
    call prologo_balcon
    call prologo_mensajeros
    call prologo_espada

    ## Capítulo 1 (próximamente, en historia/capitulo_01.rpy)
    # call capitulo_01_...

    jump fin_de_la_demo


label fin_de_la_demo:

    scene black with fundido_lento

    titulo "Fin del prólogo"

    leyenda "{i}Continuará…{/i}"

    ## Un `return` sin ningún `call` pendiente termina el juego y vuelve al
    ## menú principal.
    return
