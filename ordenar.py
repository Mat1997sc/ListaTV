ARCHIVO = "ListaAPP"

with open(ARCHIVO, "r", encoding="utf-8") as f:
    lineas = [linea.strip() for linea in f if linea.strip()]

encabezado = ""
canales = []
bloque_actual = []

for linea in lineas:
    if linea.startswith("#EXTM3U"):
        encabezado = linea
    elif linea.startswith("#EXTINF"):
        if bloque_actual:
            canales.append(bloque_actual)
        bloque_actual = [linea]
    else:
        bloque_actual.append(linea)

if bloque_actual:
    canales.append(bloque_actual)

# Extrae el nombre del canal (lo que va después de la última coma en #EXTINF) y ordena
canales.sort(key=lambda c: c[0].split(",")[-1].strip().lower())

with open(ARCHIVO, "w", encoding="utf-8") as f:
    if encabezado:
        f.write(encabezado + "\n")
    for canal in canales:
        f.write("\n".join(canal) + "\n")
