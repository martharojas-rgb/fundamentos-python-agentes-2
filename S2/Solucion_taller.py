import datetime

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
    historial_chat=[] 
    mensaje = ""

    while sistema_activo:
        cmd = input("PseudoAgente>: ").lower()  # salir        
        if cmd == "salir":
            mensaje = "Se ha solicitado  terminar la sesión."
            print("[PseudoAgente] Apagando sistemas...")
            sistema_activo = False
        elif cmd == "ping":
            print("pong~")
            mensaje = "Se envió un ping y se devuelve un pong." 
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
            mensaje = f"La palabra ingresada fue {pal} y se obtuvo como resultado: Vocales - {tot_vocales} | Consonantes {tot_cons} siendo el total: {tot_letras} "

        elif cmd == "fecha":
            if rol == "admin":    
                mensaje =f"Fecha y hora actual: {datetime.datetime.now()}"
                print("[PseudoAgente]" + mensaje)
            else:
                mensaje = "[Acceso Denegado] Este comando requiere privilegios de administrador."
                print("[PseudoAgente]" + mensaje)

        elif cmd == "contraseña":
            contrasena = input("Ingrese una opción de contraseña").lower()
            if len(contrasena) >= 8 and contrasena != usuario:
                print("Contraseña válida.")
                mensaje = "Se ha ingreado la contraseña correctamente"
            else:
                mensaje="La contraseña ingresada no cumple con las condiciones"
                print(
                    "Debe tener al menos 8 caracteres y no ser igual al nombre de usuario."
                )

        elif cmd == "historial":
            activo= True        
           
            while activo:
                historial = input("Ingrese una de las siguientes opciones: \nHistorial\nHistorial all\nHistorial clear\n o salir ").lower()
                
                if historial == "historial":
                    pal =input("Ingrese palabra clave para la busqueda ").lower()
                    resultado=[]
                    #Se genera un for para que recorra todas las posiciones del arreglo
                    for i in historial_chat:
                        #Para validar si una palabra se encuentra en el mensaje (descripcion) utilicé (in) el cual valida que la palabra ingresada por el usuario (pal) se encuentre dentro de la posición (i)
                        #Adicional use el .lower() que convierte las palabras en minusculas, sin importar si las hubiese ingresado en mayusculas, apliando de esta manera la busqueda.
                        if pal.lower() in i["descripcion"].lower():
                            resultado.append(i)
                    if len(resultado)== 0:   
                        print("[PseudoAgente] No encontré registros que coincidan con esa palabra.") 
                        mensaje="No se encontró información en historial"  
                    else:
                        print(f"Total de registros que coninciden:  {len(resultado)}")
                        print(f"Detalle de registros:  {resultado}")
                        mensaje="Detalle de registros"

                elif historial =="historial all":
                    print(f"El historial es:  {historial_chat}")
                    mensaje="Mostró todos los registros"
                elif historial == "historial clear":
                    historial_chat.clear()               
                    print(f"Se ha eliminado el historial:{historial_chat}")
                    mensaje="Eliminó todos los registros"

                elif historial == "salir":
                    activo =False
                else:    
                    print("No eligió una opción valida.") 
                    mensaje="No ingreso opción valida"    
   

        elif cmd == "calculadora":
            # Se convierte los valores ingresados a float porque input() siempre devuelve texto (string). Y si no se realiza, al realizar la operación en la ejecución genera error por el tipo de dato, el cual debe se int o float.
            # Error generado: TypeError: unsupported operand type(s) for /: 'float' and 'str'
            numero_uno = float(input("Ingrese el primer número:"))
            operador = input("Ingrese el operador (+, -, *, /):")
            numero_dos = float(input("Ingrese el segundo número:"))

            if operador == "+":
                print(f"El resultado de la suma es: {numero_uno + numero_dos}")
                mensaje="Se realizo la suma"
            elif operador == "-":
                print(f"El resultado de la resta es: {numero_uno - numero_dos}")
                mensaje="Se realizo la resta"
            elif operador == "*":
                print(f"El resultado de la multiplicación es: {numero_uno * numero_dos}")
                mensaje="Se realizo la multiplicacion"
                
            elif operador == "/":
                if numero_dos != 0:
                    print(f"El resultado de la división es: {numero_uno / numero_dos}")
                    mensaje="Se realizo la division"
                else:
                    print("No se puede dividir entre cero.")
                    mensaje="Se intento dividir entre cero"
        else:
            mensaje ="Comando desconocido, intente de nuevo."
            print("[PseudoAgente]" + mensaje)


        #TO-DO: Taller de la semana - Búsqueda de memoria
        d_log = {"timestamp": datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                "cmd": cmd,
                "rol": rol,
                "descripcion": mensaje}
        
        historial_chat.append(d_log)



# Sí el usuario agotó los tres intenos en el Login, se muestra mensaje de cuenta bloqueada.
else:
    print("Acceso denegado. Cuenta bloqueada.")
    mensaje= "Se intento igresar a la cuenta con data errada"


print("-----------Fin del taller--------------------")