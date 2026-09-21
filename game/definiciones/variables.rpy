## =============================================================================
## ESTADO DE LA HISTORIA
## =============================================================================
## Aquí van las variables que CAMBIAN durante la partida: decisiones del
## jugador, objetos obtenidos, relaciones entre personajes, etc.
##
## ¿Por qué `default` y no `define`?
##   `default` declara el valor INICIAL de algo que puede cambiar. Ren'Py lo
##   guarda en cada partida, lo restaura al cargar y lo respeta al retroceder
##   (rollback). Si usaras `define` o `$ variable = ...` en `start`, al cargar
##   una partida vieja la variable podría no existir o tener un valor
##   incorrecto.
##
## Regla práctica:
##   ¿Cambia durante el juego?  -> default
##   ¿Es fija (personajes, rutas de archivos, configuración)?  -> define
## =============================================================================

## Se vuelve True cuando la Luz de Eternia brilla por primera vez (prólogo).
## Todavía nada la consulta, pero queda registrada para capítulos futuros:
##
##     if espada_desperto:
##         "La empuñadura todavía está tibia."
default espada_desperto = False
