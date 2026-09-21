## =============================================================================
## TEST AUTOMÁTICO: recorrido completo del prólogo
## =============================================================================
## Un `testcase` es un "jugador robot": hace clic por ti y comprueba que todo
## funcione. NO se ejecuta cuando alguien juega; solo cuando tú lo pides.
##
## Cómo ejecutarlo:
##   - Launcher: abre el proyecto una vez ("Ejecutar proyecto"), pulsa
##     "Recargar" y aparecerá el botón "Run Testcases".
##   - Terminal (macOS):
##       RENPY_PLATFORM=mac-universal /Applications/renpy-8.5.3-sdk/renpy.sh \
##           /Users/Matias/Proyectos/aethernia-novel test recorrido_prologo
##
## Úsalo después de cada cambio grande: si una línea del guion rompe el juego
## (una imagen mal escrita, un sonido que no existe...), el test falla y te
## dice en qué línea.
##
## Complemento: `lint` (Launcher -> "Comprobar script (Lint)") revisa el
## código SIN jugarlo; este test lo JUEGA. Usa los dos.
## =============================================================================

testcase recorrido_prologo:

    ## Esperamos a que el menú principal termine su transición de entrada:
    ## si "hacemos clic" antes, la orden se pierde.
    pause 4.0
    run Start()
    pause 4.0

    ## advance = un clic.  until = repetir hasta que se cumpla la condición.
    ## timeout = segundos máximos antes de dar el test por fallido.
    ##
    ## Las condiciones miran el ESTADO del juego (una variable, un texto en
    ## pantalla). En nuestras pruebas, `until label ...` no detectó las
    ## escenas a las que se entra con `call`, por eso no lo usamos.
    advance until eval espada_desperto timeout 300.0
    advance until "Fin del prólogo" timeout 120.0
    advance until screen "main_menu" timeout 60.0
