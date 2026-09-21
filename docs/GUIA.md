# Guía de Aethernia: cómo está hecho y cómo seguir

Esta guía explica **qué** se cambió en el proyecto, **por qué**, y cómo continuar por tu cuenta. Tu versión original del guion está en [`docs/antes/script_original.rpy`](antes/script_original.rpy): compárala con la nueva mientras lees.

---

## 0. Lo primero que debes saber

| Situación | Qué hacer |
| --- | --- |
| Probar el juego | Launcher → **Ejecutar proyecto** |
| Ver cambios sin reiniciar | Con el juego abierto: **Shift+R** (recarga el script) |
| Ir directo a una escena | **Shift+O** abre la consola → escribe `jump prologo_espada` |
| Revisar errores sin jugar | Launcher → **Comprobar script (Lint)** |
| Jugar todo automáticamente | Ejecuta el test (ver [sección 6](#6-probar-lint-tests-y-atajos)) |
| El texto aparece de golpe (sin efecto máquina de escribir) | Launcher → Acciones → **Eliminar datos persistentes**. Tu preferencia vieja (texto instantáneo) quedó guardada. |
| Una partida guardada vieja da error al cargarla | Bórrala. La estructura del guion cambió por completo; en un prototipo es normal. |

---

## 1. Estructura del proyecto

```text
aethernia-novel/
├── CREDITOS.md                  ← licencias de todos los recursos de terceros
├── docs/
│   ├── GUIA.md                  ← esta guía
│   └── antes/script_original.rpy← tu versión original, para comparar
├── herramientas/                ← scripts de Python para generar recursos
│   ├── generar_efectos.py       ← crea resplandor, chispa y viñeta
│   └── recolorear_gui.py        ← pasa la interfaz de rosa a dorado
└── game/
    ├── script.rpy               ← SOLO el índice: qué escenas se juegan y en qué orden
    ├── historia/
    │   └── prologo.rpy          ← el guion del prólogo (4 escenas)
    ├── definiciones/            ← todo lo que el guion USA
    │   ├── personajes.rpy       ← quién habla y cómo se ve
    │   ├── imagenes.rpy         ← fondos, fondos de menú, partículas
    │   ├── audio.rpy            ← canales y catálogo de sonidos
    │   ├── efectos.rpy          ← transiciones y transforms (ATL)
    │   └── variables.rpy        ← estado de la partida (default)
    ├── tests/
    │   └── recorrido_prologo.rpy← "jugador robot" que recorre el prólogo
    ├── images/{fondos,efectos}/
    ├── audio/{musica,ambiente,sfx}/
    ├── fonts/                   ← Cinzel y EB Garamond + sus licencias
    ├── gui.rpy, options.rpy, screens.rpy   ← plantilla de Ren'Py (con cambios marcados "Aethernia:")
    └── guion_base.md            ← tu guion en prosa (ya integrado)
```

**¿Por qué separar así?** Por la misma razón por la que en una obra no se mezclan los planos eléctricos con los de plomería: cada archivo tiene **una responsabilidad**. Cuando quieras cambiar el color del rey, sabes que está en `personajes.rpy`, no escondido entre 500 líneas de diálogo. Y cuando escribas, `historia/` contiene solo historia.

> Ren'Py carga **todos** los `.rpy` dentro de `game/`, en cualquier subcarpeta. Las carpetas son para ti, no para el motor.

---

## 2. Cómo fluye el juego

```text
Menú principal ──"Comenzar"──▶ label start (script.rpy)
                                  │
                                  ├─ call prologo_leyenda    ──┐
                                  ├─ call prologo_balcon       │  historia/prologo.rpy
                                  ├─ call prologo_mensajeros   │  (cada una termina en `return`)
                                  ├─ call prologo_espada     ──┘
                                  └─ jump fin_de_la_demo ──return──▶ Menú principal
```

- `call escena` → salta a la escena y, cuando esta hace `return`, **vuelve** a la línea siguiente.
- `jump escena` → salta y **no vuelve**.
- Un `return` sin ningún `call` pendiente termina el juego y vuelve al menú.

Con `start` como índice ves la estructura completa de un vistazo, y reordenar escenas es mover una línea.

> **Para cuando publiques:** en la pantalla "Construir distribuciones" del launcher, deja marcada la opción **"Añadir cláusulas 'from' a 'calls'"**. Así las partidas guardadas de los jugadores siguen funcionando aunque edites el índice.

---

## 3. Conceptos de Ren'Py que aparecen en el código

| Concepto | Dónde verlo | En una frase |
| --- | --- | --- |
| `define` vs `default` | `personajes.rpy`, `variables.rpy` | `define` = constante (no se guarda). `default` = valor inicial de algo que **cambia** y **se guarda** en la partida. |
| Narrador | `prologo.rpy` | Una línea sin personaje (`"texto"`) ya es narración. No hace falta un `Character("")`. |
| `Character(kind=...)` | `personajes.rpy` | Hereda de otro personaje y solo cambia lo que indicas. `what_*` = estilo del texto; `window_*` = estilo del contenedor. |
| Imagen "etiqueta atributo" | `imagenes.rpy` | `bg balcon_noche`: mostrar otro `bg` reemplaza al anterior automáticamente. |
| Imágenes automáticas | `images/efectos/` | Todo archivo en `game/images/` ya existe como imagen con su nombre (`chispa`, `vineta`...). |
| `fit="cover"` | `imagenes.rpy` | Escala **sin deformar** hasta cubrir la pantalla. Tu `xysize` solo estiraba las imágenes un ~3%. |
| `init python` + función | `imagenes.rpy` → `fondo()` | Si escribes lo mismo 3 veces, conviértelo en función (principio DRY). |
| Transición (`with`) | `efectos.rpy` | **Cómo** se pasa de una imagen a otra: `fundido_lento`, `relampago`, `hpunch`... |
| Transform ATL (`at`) | `efectos.rpy` | Cómo se **comporta** una imagen: zoom, desenfoque, color, temblor, pulso de luz. |
| `additive 1.0` | `pulso_dorado` | Mezcla aditiva: **suma** luz (como una lámpara real) en vez de pintar encima. |
| Canales de audio | `audio.rpy` | `music` (1 pista), `sound` (1 efecto), `audio` (efectos superpuestos), `ambiente` (nuestro, en loop). |
| `play` / `queue` / `stop` | `prologo.rpy` | `fadein`, `fadeout` y `volume` suavizan y mezclan. Una lista `[a, b]` reproduce en secuencia. |
| Etiquetas de texto | `prologo.rpy` | `{w=0.5}` pausa; `{nw}` avanza solo; `{i}...{/i}` cursiva. |
| `config.font_replacement_map` | `gui.rpy` | Usa los archivos reales de cursiva y negrita en lugar de "inventarlos". |
| `testcase` | `tests/` | Un jugador robot que juega por ti y avisa si algo se rompe. |

### Dos trampas que encontramos (y cómo las resolvimos)

1. **`BrightnessMatrix` oscurecía de más.** `BrightnessMatrix(-0.3)` **resta** brillo: lo que ya era oscuro se vuelve negro puro. La puerta de la escena de la espada quedó totalmente negra. Solución: `TintMatrix("#8c8c8c")`, que **multiplica** (×0.55) y conserva las texturas. Lo descubrimos sacando capturas del juego real, no mirando el código. **Prueba siempre lo que ves.**
2. **`matrixcolor` no se anima desde `None`.** Si un transform arranca sin color y termina con `TintMatrix`, el cambio es un salto brusco. Solución: declarar siempre el valor inicial (`matrixcolor TintMatrix("#ffffff")`).

---

## 4. De la prosa a la novela visual: qué cambió en el texto y por qué

Tu `guion_base.md` está escrito como **novela en prosa**. Una novela visual es otro formato: el lector avanza **clic a clic**, con imagen y sonido. Estas son las técnicas aplicadas.

### 4.1 Una idea por clic
En una novela, un párrafo largo funciona. En una caja de diálogo, más de dos renglones cansan y esconden el ritmo. El párrafo final de tu guion (unas 180 palabras) se convirtió en 13 líneas, y cada una tiene su momento.

### 4.2 La raya de diálogo y el verbo de habla desaparecen
La caja de nombre ya dice quién habla. Los "exclamé", "dijo", "exclamaron" sobran.

```text
ANTES (prosa):
—De acuerdo, iré de inmediato, reúnan a la armada y síganme —exclamé mientras preparaba mi armadura y mi espada para salir.

DESPUÉS (novela visual):
rey "De acuerdo.{w=0.3} Iré de inmediato."
rey "Reúnan a la armada y síganme."
...
"Me coloco la armadura a toda prisa y tomo mi espada."
```

### 4.3 Un solo punto de vista, un solo tiempo verbal
Tu guion mezclaba tiempos ("exclamé", "sentí" en pasado; "tengo un mal presentimiento" en presente). Como en una novela visual la escena ocurre **ahora** frente al jugador, todo el prólogo quedó en **primera persona, presente**, desde el rey. El pasado se reserva para lo que de verdad es pasado ("Siempre creí que eran leyendas").

- La **leyenda** usa otra voz (tercera persona, texto centrado sobre el reino desenfocado). El cambio visual marca el cambio de narrador.
- Los pensamientos del balcón, que antes eran `rey "..."` (hablando solo en voz alta), pasaron a **narración**: son lo que el rey piensa.

### 4.4 Ubica al lector en la primera línea de cada escena
¿Quién? ¿Dónde? ¿Cuándo? Por eso el balcón empieza con *"Desde el balcón de la torre contemplo mi reino."* Sin esa línea, el lector no sabe si el que narra es el rey.

### 4.5 Mostrar, no contar
```text
ANTES: "Estas criaturas nos superan enormemente en velocidad y fuerza, sin mencionar que realizan magia única."
DESPUÉS: "Son mucho más rápidas y fuertes que nosotros…{w=0.4} y usan una magia que jamás habíamos visto."
```
El soldado está asustado y sin aliento: habla en frases cortas, se corta, duda. "Realizan magia única" suena a informe; "una magia que jamás habíamos visto" suena a miedo.

### 4.6 El ritmo: frases largas y cortas, más pausas
Alternar da respiración: *"Un arma mística cuyo origen nadie conoce."* (corta, contundente) después de una frase larga. Las pausas `{w=0.5}` son los silencios de un actor: *"No.{w=0.5} No es la tormenta."*

### 4.7 Sin repeticiones
```text
ANTES: "No logro identificar que es lo que me hace sentir esta sensación de intranquilidad,
        es como si algo se aproximase y no logro identificar que es."
DESPUÉS: "Una intranquilidad me oprime el pecho y no logro saber de dónde viene."
         "Es como si algo se aproximara."
```
"No logro identificar" aparecía dos veces en la misma oración, y "sentir esta sensación" es redundante.

### 4.8 Ecos entre escenas
En el balcón: *"Es como si mi propio corazón intentara advertirme."* Con la espada: *"Es como si ella también intentara advertirme de algo."* Ese eco une las dos escenas y además refuerza algo de la leyenda: la espada "tiene conciencia propia". **Es la única línea que agregué y que no está en tu guion.** Si no te convence, bórrala.

### 4.9 El sonido también narra
- Afuera suena viento; adentro, fuego: el ambiente cambia con el lugar.
- La música cambia cuando el rey **decide**, no cuando cambia el fondo.
- Antes del clímax, la música **se apaga** y queda solo el zumbido de la espada. El silencio le da peso al momento.

### 4.10 Ortografía y gramática

| Original | Corregido | Regla |
| --- | --- | --- |
| extranha | extraña | La ñ no se reemplaza por "nh" (en Mac: Option+N y luego N). |
| sensacion, asi, tenia, hacia | sensación, así, tenía, hacía | Tildes: agudas terminadas en vocal, n o s; y el hiato -ía. |
| algo mas | algo más | "más" (cantidad) lleva tilde; "mas" sin tilde significa "pero". |
| no logro identificar que es | …qué es | Los interrogativos indirectos llevan tilde. |
| este brillando | esté brillando | "esté" (verbo) lleva tilde. |
| ricos , prósperos | ricos, prósperos | Sin espacio antes de la coma. |
| Esta noche, se siente agitada | Esta noche se siente agitada | No se pone coma entre sujeto ("esta noche") y verbo. |
| un arma mística, el cual se desconoce su origen | un arma mística cuyo origen nadie conoce | Relativo posesivo: "cuyo". |
| degastar, a parte de | desgastar, aparte de | Errata; "aparte" va junto. |
| los mismos Dioses | los dioses | Sustantivo común en minúscula (salvo que sea el nombre de un panteón concreto). |
| una vibración proviniendo de la empuñadura | una vibración en la empuñadura | Evitar el gerundio usado como adjetivo. |

### 4.11 Nombres visibles que cambié (fácil de revertir en `personajes.rpy`)

| Antes | Ahora | Motivo |
| --- | --- | --- |
| Rey Leofric Eldric | Rey Leofric | Los nombres cortos en la caja se leen mejor. El nombre completo aparece en la leyenda. |
| Soldado desconocido | Soldado | El rey conoce a su guardia: "desconocido" confunde. |
| Voces alteradas | Voces tras la puerta | Describe lo que el jugador **percibe**: voces que todavía no ve. |
| narrador_vacio | *(eliminado)* | Ren'Py ya trae un narrador. |
| e (Ailen) | ailen | Las variables se nombran por lo que representan. |

---

## 5. Recetas para seguir

### Agregar una escena
1. En `historia/prologo.rpy` (o en un archivo nuevo, como `historia/capitulo_01.rpy`):
   ```renpy
   label capitulo_01_bosque:
       scene bg bosque_niebla with fundido_lento
       "La niebla es tan espesa que apenas veo a mis hombres."
       return
   ```
2. En `script.rpy`, agrégala al índice: `call capitulo_01_bosque`.

### Agregar un fondo
1. Copia la imagen a `game/images/fondos/`.
2. En `imagenes.rpy`: `image bg bosque_niebla = fondo("bosque.jpg")`.

### Agregar un sonido
1. Copia el archivo a `game/audio/sfx/` (o `musica/`, `ambiente/`).
2. En `audio.rpy`: `define audio.aullido = "audio/sfx/aullido.ogg"`.
3. **Anota la licencia en `CREDITOS.md`** (y en `gui.about` si es CC-BY).
4. Úsalo: `play sound aullido`.

### Agregar un personaje con sprites
```renpy
## personajes.rpy
define ailen = Character("Ailen", color="#b9a3e3", image="ailen")

## Archivos: images/personajes/ailen neutral.png, ailen triste.png ...
## (se definen solos por su nombre)

## En el guion:
show ailen neutral at left with dissolve
ailen triste "No debiste venir."     # cambia la expresión y habla, todo junto
```

### Agregar una decisión con consecuencias
```renpy
## variables.rpy
default espero_refuerzos = False

## en el guion
menu:
    "¿Qué hago?"
    "Partir de inmediato con la guardia":
        rey "No hay tiempo que perder."
    "Esperar a que llegue la armada":
        $ espero_refuerzos = True
        rey "Iremos juntos. Solos no tenemos oportunidad."

## más adelante, la decisión TIENE que notarse:
if espero_refuerzos:
    "Llegamos tarde. El campamento ya no existe."
```
Una decisión que no cambia nada después se siente falsa. Guarda la elección en una variable `default` y úsala más adelante.

---

## 6. Probar: lint, tests y atajos

| Herramienta | Qué detecta | Cómo |
| --- | --- | --- |
| **Lint** | Imágenes o sonidos inexistentes, errores de sintaxis, personajes sin definir | Launcher → Comprobar script (Lint) |
| **Test** | Errores que solo aparecen al **jugar** | Launcher → "Run Testcases", o en la terminal: |

```bash
RENPY_PLATFORM=mac-universal /Applications/renpy-8.5.3-sdk/renpy.sh \
    /Users/Matias/Proyectos/aethernia-novel test recorrido_prologo
```

> En este Mac, `renpy.sh` necesita `RENPY_PLATFORM=mac-universal`; sin esa variable dice que no encuentra la plataforma.

Atajos con el juego abierto desde el launcher (modo desarrollador):
- **Shift+R**: recarga el script sin cerrar el juego.
- **Shift+O**: consola (`jump escena`, ver o cambiar variables).
- **Shift+D**: menú de desarrollador (visor de variables, director interactivo, lista de archivos...).

Los scripts de `herramientas/` se ejecutan desde la raíz del proyecto:
```bash
python3 herramientas/generar_efectos.py    # regenera resplandor, chispa y viñeta
python3 herramientas/recolorear_gui.py     # solo si restauras la GUI rosa original
```

---

## 7. Recursos y licencias: reglas de oro

1. **Verifica la licencia en la página del recurso**, no en un buscador.
2. Acepta **CC0**, **CC-BY** (con atribución) y **OFL** (fuentes). Evita **NC** (no comercial), **ND** (sin derivados) y "gratis para uso personal": te impedirían vender el juego.
3. Desconfía si el autor dice que el recurso "lo sacó de otro lado". Nos pasó con un sonido de golpes a la puerta: tenía CC0, pero el autor admitía que no era suyo. Lo cambiamos por otro de origen limpio.
4. Registra todo en `CREDITOS.md` en el momento en que agregas el recurso, no después.

---

## 8. Pendientes e ideas

- **El arte y el texto deben coincidir.** Tu fondo del balcón muestra un **eclipse y dos lunas**, y el texto no los menciona. Si es parte del mundo, el rey debería notarlo ("Esta noche el sol negro vuelve a asomarse..."). Si no, conviene cambiar la imagen: un detalle tan llamativo genera preguntas.
- **"Luz de Eternia" y "Aethernia"**: ¿el parecido es intencional? Si la espada y el mundo están relacionados, es un gran gancho. Si no, puede confundir.
- **Ilustración de la espada**: por ahora la escena la sugiere con luz. Cuando tengas la imagen, reemplaza el bloque del resplandor en `prologo_espada`.
- **Sonido de desenvainar**: es un cuchillo (pack de Kenney), lo más cercano con licencia libre. Vale la pena buscar uno de espada larga.
- **`images/fondos/black_cuadros.png`** ya no se usa (la leyenda ahora va sobre el reino desenfocado). Bórralo si no lo necesitas.
- **Sprites de personajes**: el soldado y el rey todavía no tienen. Ver la receta de la [sección 5](#agregar-un-personaje-con-sprites).
