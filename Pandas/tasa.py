nombre = input('ingresa tu nombre: ')
mujer = input('Eres mujer? (si/no): ')
peso= int(input("ingresar peso: "))
altura= int(input("ingresar altura: "))
edad= int(input("ingresar edad: "))

constante_1 = 10
constante_2 = 6.25
constante_3 = 5
constante_mujer = 161


tmb_hombre = constante_1*peso + constante_2*altura - constante_3*edad 
tmb_mujer = tmb_hombre - 161

tmb = None
if mujer == "si":
    tmb = tmb_mujer
    print(f"""
    Hola {nombre}!
    Tu indice metabolico basal es de
    ---------
    {tmb}
    ---------
    """)
else:
    tmb = tmb_hombre
    print(f"""
    Hola {nombre}!
    Tu indice metabolico basal es de
    ---------
    {tmb}
    ---------
    """)

actividad_fisica = int(input(f"""Que tan activo eres?
1] Muy ligero: Poco o nada de ejercicio

2] Ligero: 1-3 veces ejercicio a la semana

3] Moderado: 3-5 veces ejercicio a la semana

4] Intenso: 6-7 veces ejercicio a la semana

5] Muy intensa" Deporte 2 horas todos los dias

Ingresa el numero de la opcion:
"""))

final = 0
if actividad_fisica == 1:
    final = tmb * 1.2
elif actividad_fisica == 2:
    final = tmb * 1.375
elif actividad_fisica == 3:
    final = tmb * 1.55
elif actividad_fisica == 4:
    final = tmb * 1.725
else:
    final = tmb * 1.9

print(f"""
Tu gasto diario real es de {final}
""")