define reportera=Character("Elena")
define camarada=Character("Matvey", color="#FF0000")

label start:
    image vnoticiero = "Noticiero.png"
    image vpresentadora = "Presentadora.png"

    scene vnoticiero
    with fade
    show vpresentadora
    with dissolve

    reportera "Muy buenos días tengan todos los televidentes."
    reportera "El pronóstio de hoy es un nuevo día de expansionismo para nuestro querido sistema."
    reportera "Yendo a las noticias..."
    reportera "El día de ayer, Alemania firmó su rendición después de que nuestras tropas diezmaran sus defensas en Berlín."
    reportera "'Germany took a huge L in this war, 💀.' declaró el primer ministro Churchil desde Gran Bretaña." 

    hide vpresentadora
    with dissolve

    image vinicial = "Oficina inicial.png"
    scene vinicial
    with fade

    play sound "audio/teléfono.mp3"
    "Hey, no sé qué, ve"
    "Pepe"
