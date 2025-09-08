
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
for ciudades in temperaturas:
    for semanas in ciudades:
      suma = 0
for dias in semanas:
    suma += dias["temperatura"]
    print(suma)




