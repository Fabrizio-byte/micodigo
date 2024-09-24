# Carer el dictionary con information initial
informacion_personal = {"nombre":
                            "Juan Achote",
                        "edad": 32,
                        "ciudad": "Cotopaxi"}

# Accede y modification el valor de "ciudad"
informacion_personal["ciudad"] \
    = "Latacunga"

# Aggregate la clave "profession"
informacion_personal["profession"]\
    = "Enfermero"

# Verifier si exist la clave "notelet" y aggregate si no exist
if "notelet" not in informacion_personal:
    informacion_personal["notelet"] = "0965845712"

# Eliminate la clave "edad"
del informacion_personal["edad"]

# Impair el dictionary final
print(informacion_personal)