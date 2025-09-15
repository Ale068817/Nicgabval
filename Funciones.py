# Definimos dimensiones
ciudades = ["Libertad", "SantaElena", "Salinas"]
dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
semanas = 2
temperaturas = [
    [ #"Libertad"
        [#"1",
            {"dia":"Lunes","temperatura":70},
            {"dia":"Martes","temperatura":73},
            {"dia":"Miercoles","temperatura":79},
            {"dia":"Jueves","temperatura":88},
            {"dia":"Viernes","temperatura":74},
            {"dia":"Lunes","temperatura":70},
            {"dia":"Lunes","temperatura":70}
        ],
        [#"2",
            {"dia": "Lunes", "temperatura": 81},
            {"dia": "Martes", "temperatura": 83},
            {"dia": "Miercoles", "temperatura":77},
            {"dia": "Jueves", "temperatura": 80},
            {"dia": "Viernes", "temperatura": 84},
            {"dia": "Lunes", "temperatura": 79},
            {"dia": "Lunes", "temperatura": 83}
        ],
    ],
    [ #"SantaElena"
        [#"1",
            {"dia":"Lunes","temperatura":74},
            {"dia":"Martes","temperatura":76},
            {"dia":"Miercoles","temperatura":89},
            {"dia":"Jueves","temperatura":71},
            {"dia":"Viernes","temperatura":83},
            {"dia":"Lunes","temperatura":82},
            {"dia":"Lunes","temperatura":70}
        ],
        [#"2",
            {"dia": "Lunes", "temperatura": 80},
            {"dia": "Martes", "temperatura": 86},
            {"dia": "Miercoles", "temperatura":79},
            {"dia": "Jueves", "temperatura": 85},
            {"dia": "Viernes", "temperatura": 84},
            {"dia": "Lunes", "temperatura": 77},
            {"dia": "Lunes", "temperatura": 89}
        ],
    ],
    [# "Salinas"
        [ #"1",
            {"dia":"Lunes","temperatura":78},
            {"dia":"Martes","temperatura":72},
            {"dia":"Miercoles","temperatura":80},
            {"dia":"Jueves","temperatura":79},
            {"dia":"Viernes","temperatura":77},
            {"dia":"Lunes","temperatura":82},
            {"dia":"Lunes","temperatura":85}
        ],
        [#"2",
            {"dia": "Lunes", "temperatura":88},
            {"dia": "Martes", "temperatura":83},
            {"dia": "Miercoles", "temperatura":78},
            {"dia": "Jueves", "temperatura":82},
            {"dia": "Viernes", "temperatura":87},
            {"dia": "Lunes", "temperatura": 79},
            {"dia": "Lunes", "temperatura":90}
        ],
    ],
]
for i, ciudad in enumerate(ciudades):
    print(f"\nCiudad: {ciudad}")
    for semana in range(semanas):
        datos_semana = temperaturas[i][semana]
        suma = sum(d["temperatura"] for d in datos_semana)
        promedio = suma / len(datos_semana)
        print(f"  Semana {semana+1}: promedio = {promedio:.2f}")




def calcular_promedios(ciudades, semanas, temperaturas):
    resultados = {}
    for i in range(len(ciudades)):  # Recorre ciudades
        ciudad = ciudades[i]
        resultados[ciudad] = {}

        for j in range(semanas):  # Recorre semanas
            suma = 0
            contador = 0
            for k in range(len(temperaturas[i][j])):  # Recorre días
                suma += temperaturas[i][j][k]["temperatura"]
                contador += 1

            promedio = suma / contador
            resultados[ciudad][f"Semana {j+1}"] = round(promedio, 2)

    return resultados