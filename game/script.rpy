# Coloca el código de tu juego en este archivo.

# Declara los personajes usados en el juego como en el ejemplo:

define e = Character("Ailen")
define rey = Character("Rey Leofric Eldric")
define narrador_vacio = Character("")


image noche_estrellada_1 = Transform(
    "images/noche_estrellada_1.jpg",
    xysize=(1920, 1080)
)

# El juego comienza aquí.

label start:

    scene black_cuadros
    narrador_vacio "El reino de Falcon, un reino próspero que se enorgullece de ser uno de los más ricos , prósperos y justos del mundo, está gobernado por el rey Leofric Eldric."

    narrador_vacio "El monarca es conocido por portar la sagrada espada Luz de Eternia, un arma mística, el cual se desconoce su origen."

    narrador_vacio "Se dice que fue forjada por los mismos Dioses de la antigüedad, según los rumores posee conciencia propia y que únicamente puede ser empuñada por \"el elegido\"."

    scene noche_estrellada_1
    rey "Esta noche, se siente extrañamente agitada."

    rey "No logro identificar que es lo que me hace sentir esta sensación de intranquilidad, es como si algo se aproximase y no logro identificar que es."

    rey "Las turbulencias del viento solo ayudan a empeorar dicha sensacion, asi como esa extranha tormenta que se aproxima, no, eso no, es algo mas que no logro ver, es como si mi corazón me estuviese alertando de algo."


    # Muestra una imagen de fondo: Aquí se usa un marcador de posición por
    # defecto. Es posible añadir un archivo en el directorio 'images' con el
    # nombre "bg room.png" or "bg room.jpg" para que se muestre aquí.

    scene bg room

    # Muestra un personaje: Se usa un marcador de posición. Es posible
    # reemplazarlo añadiendo un archivo llamado "eileen happy.png" al directorio
    # 'images'.

    show eileen happy

    # Presenta las líneas del diálogo.

    e "Has creado un nuevo juego Ren'Py."

    e "Añade una historia, imágenes y música, ¡y puedes presentarlo al mundo!"

    # Finaliza el juego:

    return
