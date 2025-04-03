
naves_espaciales = [
    {"nombre": "Halcón Milenario", "longitud": 34.75, "tripulantes": 4, "pasajeros": 6},
    {"nombre": "X-Wing", "longitud": 12.5, "tripulantes": 1, "pasajeros": 0},
    {"nombre": "TIE Fighter", "longitud": 8.99, "tripulantes": 1, "pasajeros": 0},
    {"nombre": "Estrella de la Muerte", "longitud": 120000, "tripulantes": 265000, "pasajeros": 843342},
    {"nombre": "Slave I", "longitud": 21.5, "tripulantes": 1, "pasajeros": 6},
]

for nave in naves_espaciales:
    print(f"Nombre: {nave['nombre']}")
    print(f"Longitud: {nave['longitud']} metros")
    print(f"Tripulantes: {nave['tripulantes']}")
    print(f"Pasajeros: {nave['pasajeros']}")
    print("-" * 40)
    class NaveEspacial:
        def __init__(self, nombre, longitud, tripulantes, pasajeros):
            self.nombre = nombre
            self.longitud = longitud
            self.tripulantes = tripulantes
            self.pasajeros = pasajeros

        def __repr__(self):
            return f"{self.nombre} (Longitud: {self.longitud}, Tripulantes: {self.tripulantes}, Pasajeros: {self.pasajeros})"


    class FlotaEspacial:
        def __init__(self, naves):
            self.naves = [NaveEspacial(**nave) for nave in naves]

        def procesar_datos(self):
            # Ordenar la lista de naves por nombre de forma ascendente y por longitud de forma descendente
            naves_ordenadas_nombre = sorted(self.naves, key=lambda x: x.nombre)
            naves_ordenadas_longitud = sorted(self.naves, key=lambda x: x.longitud, reverse=True)

            # Mostrar información de las naves "Cometa Veloz" y "Titán del Cosmos"
            naves_cometa_titan = [nave for nave in self.naves if nave.nombre in ["Cometa Veloz", "Titán del Cosmos"]]
            print("Información de las naves 'Cometa Veloz' y 'Titán del Cosmos':")
            for nave in naves_cometa_titan:
                print(nave)

            # Determinar las cinco naves con mayor cantidad de pasajeros
            naves_mayor_pasajeros = sorted(self.naves, key=lambda x: x.pasajeros, reverse=True)[:5]
            print("Cinco naves con mayor cantidad de pasajeros:")
            for nave in naves_mayor_pasajeros:
                print(nave)

            # Indicar cuál es la nave que requiere la mayor cantidad de tripulación
            nave_mayor_tripulacion = max(self.naves, key=lambda x: x.tripulantes)
            print("Nave que requiere mayor cantidad de tripulación:")
            print(nave_mayor_tripulacion)

            # Mostrar todas las naves cuyo nombre comience con "GX"
            naves_gx = [nave for nave in self.naves if nave.nombre.startswith("GX")]
            print("Naves cuyo nombre comienza con 'GX':")
            for nave in naves_gx:
                print(nave)


    # Datos iniciales
    naves_espaciales = [
        {"nombre": "Halcón Milenario", "longitud": 34.75, "tripulantes": 4, "pasajeros": 6},
        {"nombre": "X-Wing", "longitud": 12.5, "tripulantes": 1, "pasajeros": 0},
        {"nombre": "TIE Fighter", "longitud": 8.99, "tripulantes": 1, "pasajeros": 0},
        {"nombre": "Estrella de la Muerte", "longitud": 120000, "tripulantes": 265000, "pasajeros": 843342},
        {"nombre": "Slave I", "longitud": 21.5, "tripulantes": 1, "pasajeros": 6},
    ]

    # Crear instancia de FlotaEspacial y procesar datos
    flota = FlotaEspacial(naves_espaciales)
    flota.procesar_datos()