# Coloca el código de tu juego en este archivo.

# Declara los personajes usados en el juego como en el ejemplo:

define e = Character("Ailen")
define rey = Character("Rey Leofric Eldric")
define narrador = Character("...")


# El juego comienza aquí.

label start:

    scene black_cuadros
    narrador "El reino de Falcon, un reino próspero que se enorgullece de ser uno de los más ricos , prósperos y justos del mundo, está gobernado por el rey Leofric Eldric."

    narrador "El monarca es conocido por portar la sagrada espada Luz de Eternia, un arma mística, el cual se desconoce su origen."

    narrador "Se dice que fue forjada por los mismos Dioses de la antigüedad, según los rumores posee conciencia propia y que únicamente puede ser empuñada por \"el elegido\"."

    scene noche_estrellada_1
    rey "Esta noche, se siente extrañamente agitada, no logro identificar que es lo que da esta sensación de inquietud en mi ser que hace que mi corazón lata intranquilo como si se tratase de un criminal esperando su sentencia."

    rey " Serán las turbulencias del viento que se encuentran extrañamente alborotadas esta noche?, O tal vez la extraña tormenta que se aproxima con las nubes?, no, eso no, es algo mas que no logro vislumbrar, es como si mi corazón me estuviese alertando de algo."


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
