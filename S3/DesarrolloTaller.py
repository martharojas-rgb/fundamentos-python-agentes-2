import datetime
from typing import Dict, List


"""Alias de Tipos: Sirven para ponerle un nombre único a una estructura de datos (como una lista de diccionarios), 
haciendo que el código sea más fácil de leer y documentar. 
Esto ayuda a la IA porque le define reglas exactas sobre qué datos debe procesar previniendo errores o confusiones."""

Recuerdo = Dict[str, str]
MemoriaAgente = List[Recuerdo]

def gestionarHistorial(accion: str, memoria: MemoriaAgente) -> str:
    """
        Ejecuta cada acción elegida por el usuario y devuelve un mensaje con la respuesta.
    """
    if accion == "historial":
        pal = input("Ingrese palabra clave para la busqueda: ").lower()
        resultado = []
        
        for i in memoria:
            if pal in i["descripcion"].lower():
                resultado.append(i)
        
        if len(resultado) == 0:
            return "[PseudoAgente] No encontré registros que coincidan con esa palabra."
        else:
            return f"Total de registros: {len(resultado)} | Detalle: {resultado}"

    elif accion == "historial all":
        return f"El historial es: {memoria}"

    elif accion == "historial clear":
        memoria.clear() 
        return "Se ha eliminado el historial correctamente."

    elif accion == "salir":
        return "salir" 

    else:
        return "No eligió una opción válida."



def contarLetras(pal: str) -> str:
    """
    Cuenta el total de letras, vocales y consonantes de una palabra.
    Recibe como parametro el string o palabra ingresada por el usuario y retornaun string con el mensaje para la respuesta.
    """
    tot_letras = len(pal)
    tot_vocales = 0
    tot_cons = 0
    for p in pal:
        if p in "aeiou":
            tot_vocales += 1
        else:
            tot_cons += 1
  
    return f"Palabra: {pal} | Vocales: {tot_vocales} | Consonantes: {tot_cons} | Total: {tot_letras}"




def ejecutarCalculadora(num1: float, operacion: str, num2: float) -> str:
    """
    Realiza la operación de matemáticas solicitada por el usuario.
    Recibe como parametros dos float para la operación y un string para identificar el tipo de operación a realizar y 
    retorna un string con el resultado de la operación o error.
    """
     
    if operacion == "+":
        return f"El resultado de la suma es: {num1 + num2}"
    elif operacion == "-":
        return f"El resultado de la resta es: {num1 - num2}"
    elif operacion == "*":
        return f"El resultado de la multiplicación es: {num1*num2}"
    elif operacion == "/":
        if num2 != 0:
            return f"El resultado de la división es: {num1 / num2}"
        else:
            return "No se puede dividir entre cero."
    else:
        raise ValueError("Operador no válido.")
   
    
def mostrarFecha(rol: str)-> str:
    if rol == "admin":    
        return f"Fecha y hora actual: {datetime.datetime.now()}"        
    else:
        """raise: Es una instrucción que detiene la ejecución normal para generar un error controlado cuando ocurre algo no permitido dentro de la función.
        El error viaja "hacia afuera" de la función buscando un bloque except en el programa principal donde se llamada dicha función que genero la exception,
        si lo encuentra, el error se captura y el programa muestra un mensaje en lugar de cerrarse el programa."""
        raise PermissionError("[Acceso Denegado] Este comando requiere privilegios de administrador.")
 



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
            mensaje=contarLetras(pal)
            print(f"[PseudoAgente] {mensaje}") 


        elif cmd == "fecha":
            try:
                mensaje=mostrarFecha(rol)
                print(f"[PseudoAgente] {mensaje}")
            except PermissionError as e:
                print(e)    



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
                
                respuesta = gestionarHistorial(historial, historial_chat)
                if respuesta == "salir":
                    activo = False
                else:
                    print(f"[PseudoAgente] {respuesta}")
                    mensaje = respuesta
                  
   

        elif cmd == "calculadora":
            # Se convierte los valores ingresados a float porque input() siempre devuelve texto (string). Y si no se realiza, al realizar la operación en la ejecución genera error por el tipo de dato, el cual debe se int o float.
            # Error generado: TypeError: unsupported operand type(s) for /: 'float' and 'str'
            try:
                numero_uno = float(input("Ingrese el primer número:"))
                operador = input("Ingrese el operador (+, -, *, /):")
                numero_dos = float(input("Ingrese el segundo número:"))

                mensaje=ejecutarCalculadora(numero_uno, operador, numero_dos)
                print(f"[PseudoAgente] {mensaje}")

            except ValueError as e:
                print(e) 


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

