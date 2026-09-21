## =============================================================================
## PRÓLOGO
## =============================================================================
## Punto de vista: el rey Leofric, que narra en primera persona y en presente.
##   - Narración (líneas sin personaje) = lo que el rey ve, piensa y recuerda.
##   - rey "..."                        = lo que el rey dice en voz alta.
##
## Cada escena es un `label` que termina en `return`. El índice que las llama
## en orden está en script.rpy (label start).
##
## Regla de escritura: UNA idea por clic. Si una línea no entra cómodamente en
## dos renglones de la caja de diálogo, divídela.
## =============================================================================


## -----------------------------------------------------------------------------
## Escena 1 — La leyenda
## -----------------------------------------------------------------------------
## Objetivo: presentar el mundo, al rey y la espada en pocas líneas, y cerrar
## con una pregunta abierta ("el elegido") que invite a seguir leyendo.

label prologo_leyenda:

    scene black
    play music presagio fadein 4.0

    ## {w=2.0} espera 2 segundos; {nw} avanza solo, sin esperar un clic.
    titulo "Prólogo{w=2.0}{nw}"

    ## El reino aparece borroso, como un recuerdo: todavía estamos en la leyenda.
    show bg balcon_noche at fondo_leyenda
    show chispas_doradas
    with fundido_lento

    leyenda "El reino de Falcon se enorgullece de ser uno de los más prósperos y justos del mundo."

    leyenda "Lo gobierna el rey Leofric Eldric, portador de una espada sagrada:{w=0.5} la Luz de Eternia."

    leyenda "Un arma mística cuyo origen nadie conoce."

    leyenda "Se dice que fue forjada por los dioses de la antigüedad…{w=0.4} que tiene conciencia propia…"

    leyenda "…y que solo puede empuñarla {i}el elegido{/i}."

    hide chispas_doradas with fundido_lento

    return


## -----------------------------------------------------------------------------
## Escena 2 — El balcón
## -----------------------------------------------------------------------------
## Objetivo: pasar de la leyenda al presente y sembrar la inquietud.
## Técnica: la MISMA imagen pasa de borrosa a nítida ("enfoque de cámara"),
## así la leyenda se convierte en el presente sin un corte.

label prologo_balcon:

    show bg balcon_noche at enfocar(3.0)
    play ambiente viento_tormenta fadein 3.0 volume 0.7
    pause 3.0

    ## Primera línea de toda escena: ¿quién, dónde, cuándo? Ubica al lector.
    "Desde el balcón de la torre contemplo mi reino."

    "Esta noche se siente extrañamente agitada."

    "Una intranquilidad me oprime el pecho y no logro saber de dónde viene."

    "Es como si algo se aproximara."

    ## Relámpago: sonido y destello blanco al mismo tiempo.
    play sound trueno
    with relampago

    "El viento azota los estandartes sin descanso, y esa extraña tormenta que avanza desde el horizonte no hace más que empeorarlo todo."

    "No.{w=0.5} No es la tormenta."

    "Es algo más. Algo que no logro ver."

    "Es como si mi propio corazón intentara advertirme."

    return


## -----------------------------------------------------------------------------
## Escena 3 — Los mensajeros
## -----------------------------------------------------------------------------
## Objetivo: el conflicto llega a la puerta del rey (literalmente).
## Técnica: corte SECO (sin transición) + sacudida. Un corte abrupto
## sobresalta; un fundido suave tranquiliza. Elige según la emoción.

label prologo_mensajeros:

    ## Una lista en `play` reproduce los archivos uno detrás de otro:
    ## aquí, dos rondas de golpes seguidas.
    play sound [golpes_puerta, golpes_puerta]

    ## El ambiente cambia con el lugar: afuera viento, adentro fuego.
    play ambiente chimenea fadeout 1.5 fadein 1.5 volume 0.8

    scene bg puerta_aposentos
    with hpunch

    voces "¡Majestad!{w=0.3} ¡Majestad!"

    "Los golpes me arrancan de mis pensamientos."

    rey "Adelante."

    ## `queue` espera a que termine el sonido anterior: primero la puerta,
    ## después los pasos.
    play sound puerta_abre
    queue sound armaduras_pasos
    scene bg aposentos_soldados with dissolve

    "Tres soldados de la guardia real entran casi sin aliento."

    soldado "¡Majestad! Disculpe que irrumpamos así en sus aposentos…"

    soldado "…pero traemos malas noticias."

    soldado "En el Bosque de la Niebla aparecieron unas bestias extrañas.{w=0.3} Deformes."

    soldado "Atacaron el campamento de uno de los destacamentos que custodian el bosque."

    soldado "Son mucho más rápidas y fuertes que nosotros…{w=0.4} y usan una magia que jamás habíamos visto."

    soldado "Por favor, majestad.{w=0.3} Denos sus órdenes."

    ## --- Del guion base: el rey recuerda la leyenda del bosque ---
    ## La escena "se aleja" mientras piensa: desenfoque + viñeta oscura.
    show bg aposentos_soldados at introspeccion
    show vineta
    with dissolve

    "El Bosque de la Niebla…"

    "Desde tiempos antiguos se dice que resguarda un sello:{w=0.3} un camino hacia el mundo de los espíritus."

    "Muchos aventureros lo buscaron, aun cuando su búsqueda está prohibida por decreto."

    "Siempre creí que eran leyendas vacías, inventadas por algún charlatán."

    "Pero lo cierto es que ese bosque siempre tuvo un aura distinta…"

    "…y una niebla que jamás se disipa, sin importar la hora, el día o la estación del año."

    ## De vuelta al presente.
    show bg aposentos_soldados at fin_introspeccion
    hide vineta
    with dissolve

    ## La música cambia en el momento en que el rey DECIDE: el sonido acompaña
    ## el giro emocional de la escena, no solo el cambio de lugar.
    play music llamado_a_las_armas fadeout 2.0 fadein 1.0

    rey "De acuerdo.{w=0.3} Iré de inmediato."

    rey "Reúnan a la armada y síganme."

    soldados "¡Como ordene, majestad!"

    play sound armaduras_pasos
    "Hacen una última reverencia y salen corriendo a cumplir mis órdenes."

    return


## -----------------------------------------------------------------------------
## Escena 4 — La espada despierta
## -----------------------------------------------------------------------------
## Objetivo: el clímax del prólogo. Algo que NUNCA pasó, pasa.
## Técnica: silencio antes del clímax. La música se va y queda solo el
## zumbido de la espada; el contraste hace que el momento pese más.
##
## (No hay ilustración de la espada todavía: la sugerimos con luz sobre la
## habitación en penumbra. Cuando tengas la imagen, reemplaza el bloque del
## resplandor por un `show` de esa ilustración.)

label prologo_espada:

    ## Me quedo solo frente a la puerta: el rey está "a punto de salir de sus
    ## aposentos", tal como dice el guion base.
    scene bg puerta_aposentos at penumbra
    with fundido_negro

    "Me coloco la armadura a toda prisa y tomo mi espada."

    "Estoy a punto de salir cuando lo siento:{w=0.4} una vibración extraña en la empuñadura."

    stop music fadeout 3.0
    play audio espada_resonancia fadein 2.0
    show bg puerta_aposentos at penumbra, temblor(3, 14)

    "La desenvaino."

    play sound desenvainar
    show resplandor_dorado at pulso_dorado
    show chispas_doradas
    with destello_dorado

    ## Registramos el suceso en el estado de la partida (ver variables.rpy).
    $ espada_desperto = True

    "La hoja brilla con un resplandor dorado…"

    show resplandor_dorado at resplandor_creciente
    "…que se vuelve más intenso a cada instante."

    "Es la primera vez que sucede algo así."

    "Esta espada carga con la leyenda de haber sido otorgada por los mismos dioses, pero yo nunca la vi como algo más que una reliquia familiar."

    "Aunque es cierto que siempre fue especial.{w=0.3} Además de un filo incomparable y una durabilidad excepcional, tiene una cualidad única…"

    "…se repara sola."

    "No hay forma de desgastarla, y aunque alguien lo lograra, bastarían unos minutos para que la hoja volviera a quedar como nueva."

    "Pero esto…{w=0.5} que brille así no tiene precedentes."

    ## Eco: repite la idea de la escena del balcón ("mi corazón intentaba
    ## advertirme"). Los ecos unen escenas y hacen que la historia se sienta
    ## pensada, no improvisada.
    "Es como si ella también intentara advertirme de algo."

    ## Cierre: el sonido se apaga mientras se lee la última línea.
    stop audio fadeout 4.0
    stop ambiente fadeout 4.0

    "Tengo un mal presentimiento."

    return
