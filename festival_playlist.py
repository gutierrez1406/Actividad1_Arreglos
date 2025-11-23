

# FESTIVAL PLAYLIST - ARREGLOS

nombres = []
artistas = []
duraciones = []
popularidades = []


def agregar_canciones():
    print("\n ~~~ AGREGAR CANCIONES ~~~ ")
    try:
        n = int(input("¿Cuántas canciones quieres agregar? "))
    except ValueError:
        print("Por favor ingresa un número válido.")
        return

    for i in range(n):
        print(f"\nCanción #{i+1}")

        nombre = input("Nombre de la canción: ")
        artista = input("Artista: ")

        while True:
            try:
                duracion = float(input("Duración en minutos: "))
                break
            except ValueError:
                print("Ingresa una duración válida (número).")

        while True:
            try:
                pop = int(input("Popularidad (1-100): "))
                if 1 <= pop <= 100:
                    break
                else:
                    print("Debe ser un valor entre 1 y 100.")
            except ValueError:
                print("Ingresa un número entero válido.")

        # Guardar datos en listas
        nombres.append(nombre)
        artistas.append(artista)
        duraciones.append(duracion)
        popularidades.append(pop)

    print("\n✔ Canciones agregadas con éxito.\n")


def generar_reportes():
    print("\n -- REPORTES DE LA PLAYLIST -- ")

    if len(nombres) == 0:
        print("Aún no hay canciones registradas.\n")
        return

    total_canciones = len(nombres)
    duracion_total = sum(duraciones)
    pop_max = max(popularidades)
    pop_min = min(popularidades)
    promedio_pop = sum(popularidades) / total_canciones

    cancion_popular = nombres[popularidades.index(pop_max)]
    cancion_menos_pop = nombres[popularidades.index(pop_min)]

    print(f"\nTotal de canciones: {total_canciones}")
    print(f"Duración total: {duracion_total:.2f} minutos")
    print(f"Canción más popular: {cancion_popular} (Popularidad: {pop_max})")
    print(f"Canción menos popular: {cancion_menos_pop} (Popularidad: {pop_min})")
    print(f"Promedio de popularidad: {promedio_pop:.2f}\n")


def buscar_canciones():
    print("\n ··· BÚSQUEDA DE CANCIONES ··· ")

    if len(nombres) == 0:
        print("No hay canciones para buscar.\n")
        return

    print("1. Buscar por artista")
    print("2. Buscar por rango de popularidad")

    opc = input("Elige una opción: ")

    if opc == "1":
        art = input("\nIngresa el nombre del artista: ")
        print(f"\nResultados para artista '{art}':\n")

        encontrados = False
        for i in range(len(nombres)):
            if artistas[i].lower() == art.lower():
                encontrados = True
                print(f"- {nombres[i]} (Popularidad: {popularidades[i]})")

        if not encontrados:
            print("No se encontraron canciones de ese artista.")

    elif opc == "2":
        try:
            minimo = int(input("Popularidad mínima: "))
            maximo = int(input("Popularidad máxima: "))
        except ValueError:
            print("Valores inválidos.")
            return

        print(f"\nResultados con popularidad entre {minimo} y {maximo}:\n")
        encontrados = False

        for i in range(len(nombres)):
            if minimo <= popularidades[i] <= maximo:
                encontrados = True
                print(f"- {nombres[i]} (Artista: {artistas[i]}, Popularidad: {popularidades[i]})")

        if not encontrados:
            print("No se encontraron canciones en ese rango.")

    else:
        print("Opción no válida.")

    print()


def playlist_recomendada():
    print("\n °· PLAYLIST RECOMENDADA ·° ")

    if len(nombres) == 0:
        print("No hay canciones registradas.\n")
        return

    promedio_pop = sum(popularidades) / len(popularidades)

    print(f"Popularidad promedio: {promedio_pop:.2f}")
    print("\nCanciones sugeridas:")

    encontradas = False
    for i in range(len(nombres)):
        if popularidades[i] > promedio_pop:
            encontradas = True
            print(f"- {nombres[i]} (Artista: {artistas[i]}, Pop: {popularidades[i]})")

    if not encontradas:
        print("No hay canciones por encima del promedio.")

    print()


# -------------------------------------------------------------
# MENÚ PRINCIPAL

while True:
    print(" ~~ FESTIVAL PLAYLIST ~~ ")
    print("1. Agregar canciones 🎵")
    print("2. Ver reportes 📊")
    print("3. Buscar canciones 🔍")
    print("4. Playlist recomendada ✔️")
    print("5. Salir ⬅️")

    opcion = input(" ⭐ Elige una opción: ")

    if opcion == "1":
        agregar_canciones()
    elif opcion == "2":
        generar_reportes()
    elif opcion == "3":
        buscar_canciones()
    elif opcion == "4":
        playlist_recomendada()
    elif opcion == "5":
        print("\n ✨ ¡Gracias por usar Festival Playlist! ¡Disfruta la música!\n")
        break
    else:
        print(" ✖️ Opción no válida. Intenta de nuevo.\n")
