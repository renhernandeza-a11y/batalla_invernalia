# import os
# os.system(cls)

# La Batalla de Invernalia 
# Contexto de la misión: El Rey de la Noche se acerca a Invernalia con su ejército de Caminantes Blancos. Jon Snow y Daenerys Targaryen te han nombrado su Consejero Táctico. Tu deber es crear un programa en Python que evalúe si las fuerzas aliadas sobrevivirán a la noche, calculando el tamaño del ejército, el armamento disponible y las condiciones climáticas.
# Requisitos del programa:
# 1. Define las siguientes CONSTANTES al inicio de tu código:
vidriagon_por_soldado = 3
temperatura_congelacion = -15
# •	VIDRIAGON_POR_SOLDADO: Cada soldado necesita exactamente 3 dagas de vidriagón para ser efectivo.
cantidad_inmaculados= int(input("ingrese la cantidad de soldados inmaculados\n"))
cantidad_dothrakis = int(input("ingrese cantidad de soldados dothrakis\n"))
vidriagon_disponible = int(input("ingresa la cantidad de dagas disponibles\n"))
temperatura_actual = float(input("ingrese temperatura actual en invernalia\n"))
existen_dragones = input("daenerys llevo sus dragones? si - no \n").lower()
# •	TEMPERATURA_CONGELACION: El punto crítico donde los soldados humanos pierden eficacia es a los -15 grados.
# 2. Solicita al usuario que ingrese las siguientes VARIABLES (o defínelas tú mismo en el código):
# •	Cantidad de soldados Inmaculados (número entero).
ejercito_total = cantidad_inmaculados + cantidad_dothrakis
vidriagon_necesario = ejercito_total * vidriagon_por_soldado 
deficit_de_armas = vidriagon_necesario - vidriagon_disponible
# •	Cantidad de soldados Dothrakis (número entero).
# •	Cantidad total de dagas de Vidriagón disponibles en el castillo (número entero).
# •	Temperatura actual en Invernalia (número entero o decimal).
# •	¿Daenerys trajo a sus dragones? (Puedes usar un booleano True/False o texto como "si" / "no").
# 3. Crea las VARIABLES AUXILIARES y usa OPERADORES MATEMÁTICOS para calcular:
# •	Ejército total: La suma de Inmaculados y Dothrakis.
if ejercito_total >=20000 and existen_dragones == "si" and vidriagon_disponible >= vidriagon_necesario:
    mensaje = "¡victoria absoluta! el rey de la noche ha sido derrotado sin problemas"
# •	Vidriagón necesario: El ejército total multiplicado por la constante de armas requeridas por soldado.
# •	Déficit de armas: Cuántas dagas de vidriagón faltan (vidriagón necesario menos el disponible).
# 4. Usa lógica condicional (if, elif, else) y OPERADORES LÓGICOS (and, or) para predecir el resultado de la batalla:
elif ejercito_total >=10000 and existen_dragones == "si" or temperatura_actual <= temperatura_congelacion or deficit_de_armas < 0:
    mensaje = f"Victoria Amarga: Sobrevivimos gracias al fuego de dragón, pero las bajas por el frío y la falta de armas fueron catastróficas. Faltaron {deficit_de_armas} dagas."
# •	Condición 1 (Victoria Absoluta): Si el ejército total es mayor o igual a 20.000 soldados Y tienen a los dragones Y el vidriagón disponible es mayor o igual al necesario.  Imprimir: "¡Victoria Absoluta! El Rey de la Noche ha sido derrotado sin problemas."
# •	Condición 2 (Victoria Amarga): Si el ejército total es mayor o igual a 10.000 Y tienen a los dragones, PERO la temperatura actual es menor o igual a la constante de congelación O hay un déficit de armas (faltan dagas).  Imprimir: "Victoria Amarga: Sobrevivimos gracias al fuego de dragón, pero las bajas por el frío y la falta de armas fueron catastróficas. Faltaron [Mostrar déficit de armas] dagas."
# •	Condición 3 (Retirada Táctica): Si el ejército es menor a 10.000 Y tienen a los dragones, Y la temperatura es mayor a la constante de congelación.  Imprimir: "Retirada Táctica: No somos suficientes, pero los dragones nos dieron tiempo para huir hacia el sur."
elif ejercito_total < 10000 and existen_dragones == "si" and temperatura_actual > temperatura_congelacion:
    mensaje = "Retirada Táctica: No somos suficientes, pero los dragones nos dieron tiempo para huir hacia el sur."

else:
    mensaje = "Derrota Total: Invernalia ha caído. Comienza la Larga Noche..."
# •	Condición 4 (Derrota Total): Para cualquier otro escenario (por ejemplo, si no hay dragones y no se cumplen las condiciones de tamaño del ejército).  Imprimir: "Derrota Total: Invernalia ha caído. Comienza la Larga Noche..."





