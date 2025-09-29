informacion_personal =  {
    "nombre":"Alejandro Gonzalez",
    "edad":"60",
    "ciudad":"La Libertad",
    "estudios":"bachiller",
   }

#Accedemos a la clave ciudad para modificar
informacion_personal["ciudad"] = "santa elena"

#creamos una nueva clave
informacion_personal["ocupación"] = "chofer"

#Verifica si la clave teléfono existe en el diccionario. Si no existe, agrégala con un número de teléfono ficticio.
if "teléfono" not in informacion_personal:
    informacion_personal["teléfono"] = "0946667788"

#Elimina la clave "edad" del diccionario, ya que esa información no es necesaria.
informacion_personal.pop("edad")

for clave, valor in informacion_personal.items():
    print(f"{clave}, {valor}")







