# Dia 2 - Estructuras de control
## while, for | match/case**
# Estructura y lógica: while
## while condicion:
#   ...
#   ...
#   if(....):
#       break
#   Cuidado los bucles infinitos! Truco? La actualización/gestión de la condición

# nom_per = input("¿Cuál es tu nombre?: ")
# print(f"Hola {nom_per}, adiós~")


# Previa para el taller de la semana: Hacer un pseudoagente estilo consola
## - ¿Qué podrá hacer este pseudoagente por medio de comandos?
### - Terminar la sesión - salir
### - Responder un ping con un pong - ping
### - Contar letras en una palabra: Total, vocales y consonantes - contar


rol = ""
i = 0
# Para evaluar los intentos se define el ciclo while, ya que sé cuantos intentos voy a realizar, la variable i inicia en 0 y se va a ir incrementando hasta llegar a 3 cada vez que se ingresa mal el usuario o contraseña.
# Seguido por la solicitud de usuario y contraseña.
# Si el usuario y contraseña son validos el ciclo se rompe y guarda el rol en la variable rol.

while i < 3:
    usuario = input("Ingresa tu usuario: ")
    contrasena = input("Ingresa tu contraseña: ")

    if usuario == "invitado" and contrasena == "1234":
        print("Bienvenido, invitado.")
        rol = "invitado"
        break
    elif usuario == "admin" and contrasena == "admin123":
        print("Bienvenido, admin.")
        rol = "admin"
        break
    # Contador que se va incrementando cada vez que el usuario ingresa un usuario o contraseña incorrectos.
    i += 1

if rol == "invitado" or rol == "admin":
    print("-----------Iniciando el pseudoagente estilo consola--------------------")

    # Banderas/Banderines - Booleanos
    cmd = ""
    sistema_activo = True
    while sistema_activo:
        cmd = input("PseudoAgente>: ").lower()  # salir
        if cmd == "salir":
            sistema_activo = False
        elif cmd == "ping":
            print("pong~")
        elif cmd == "contar":
            pal = input("Ingrese una palabra: ").strip().lower()
            tot_letras = len(pal)
            # Conteo
            tot_vocales = 0
            tot_cons = 0
            for p in pal:
                if p in "aeiou":
                    tot_vocales += 1
                else:
                    tot_cons += 1
            # Resultados del conteo
            print(f"Palabra ingresada: {pal}")
            print(f"Total de vocales: {tot_vocales}")
            print(f"Total de consonantes: {tot_cons}")
            print(f"Total de letras: {tot_letras}")
        elif cmd == "fecha":
            if rol == "admin":
                from datetime import datetime

                print(f"Fecha y hora actual: {datetime.now()}")
            else:
                print(
                    "[Acceso Denegado] Este comando requiere privilegios de administrador."
                )

        elif cmd == "contraseña":
            contrasena = input("Ingrese una opción de contraseña").lower()
            if len(contrasena) >= 8 and contrasena != usuario:
                print("Contraseña válida.")
            else:
                print(
                    "Debe tener al menos 8 caracteres y no ser igual al nombre de usuario."
                )

        elif cmd == "calculadora":
            # Se convierte los valores ingresados a float porque input() siempre devuelve texto (string). Y si no se realiza, al realizar la operación en la ejecución genera error por el tipo de dato, el cual debe se int o float.
            # Error generado: TypeError: unsupported operand type(s) for /: 'float' and 'str'
            numero_uno = float(input("Ingrese el primer número:"))
            operador = input("Ingrese el operador (+, -, *, /):")
            numero_dos = float(input("Ingrese el segundo número:"))

            if operador == "+":
                print(f"El resultado de la suma es: {numero_uno + numero_dos}")
            elif operador == "-":
                print(f"El resultado de la resta es: {numero_uno - numero_dos}")
            elif operador == "*":
                print(
                    f"El resultado de la multiplicación es: {numero_uno * numero_dos}"
                )
            elif operador == "/":
                if numero_dos != 0:
                    print(f"El resultado de la división es: {numero_uno / numero_dos}")
                else:
                    print("No se puede vividir entre cero.")
        else:
            print("Comando desconocido, intente de nuevo.")

# Sí el usuario agotó los tres intenos en el Login, se muestra mensaje de cuenta bloqueada.
else:
    print("Acceso denegado. Cuenta bloqueada.")


print("-----------Fin del taller--------------------")


# Falta colocar (Tarea autónoma):
# - Mostrar el saldo disponible
# - Indicar al usuario que ya no dispone de saldo para continuar
# - Gestionar el saldo negativo
saldo = 100
while saldo > 0:
    print("""
 Prendas disponibles y con stock:
#     - Vestido (50)
#     - Zapatos (50)
#     - Jeans (30)
#     - Camiseta (20)
#     - Medias/Calcetines (5)
#     """)
    op = input("Selecciona una prenda: ").lower()  # vestido, VESTIDO, vEStido, vstido
    if op.startswith("v") or op.startswith("z"):
        if saldo>=50:
            saldo -= 50
        else:
            print("No cuenta con saldo suficiente.")
        print(f"El saldo disponible es: {saldo}")
    elif op.startswith("j"):
        if saldo>=30:
            saldo -= 30
        else: 
            print("No cuenta con saldo suficiente.")   
        print(f"El saldo disponible es: {saldo}")
    elif op.startswith("c"):
        if saldo>=20:
            saldo -= 20
        else:
            print("No cuenta con saldo suficiente.")
        print(f"El saldo disponible es: {saldo}")
    elif op.startswith("m"):
        if saldo>=5:
            saldo -= 5
        else:
            print("No cuenta con saldo suficiente.")
        print(f"El saldo disponible es: {saldo}")
    else:
        print("Selección inválida, intente de nuevo")

print("No cuenta con mas saldo disponible.")