#nombre del afiliado y su deposito, se crea la cuenta con un deposito igual o superior a $15000

# Función para crear una cuenta con un depósito inicial mínimo de $15,000
def crear_cuenta():
    nombre = input("Ingrese su nombre: ")
    deposito_inicial = float(input("Ingrese el monto del depósito inicial (debe ser igual o superior a $15,000): "))
    
    if deposito_inicial >= 15000:
        cuenta = {
            'nombre': nombre,
            'saldo': deposito_inicial
        }
        return cuenta
    else:
        print("El depósito inicial debe ser igual o superior a $15,000. Intente nuevamente.")
        return None

# Función para abonar a la cuenta
def abonar_cuenta(cuenta):
    monto_abono = float(input("Ingrese el monto que desea abonar a la cuenta: "))
    cuenta['saldo'] += monto_abono
    print(f"Se han abonado ${monto_abono} a la cuenta.")
    mostrar_saldo(cuenta)

# Función para mostrar el saldo actual de la cuenta
def mostrar_saldo(cuenta):
    print(f"El saldo actual de la cuenta de {cuenta['nombre']} es: ${cuenta['saldo']}")

# Función para retirar dinero de la cuenta
def retirar(cuenta):
    monto_retiro = float(input("Ingrese el monto que desea retirar de la cuenta: "))
    if cuenta['saldo'] >= monto_retiro:
        cuenta['saldo'] -= monto_retiro
        print(f"Se han retirado ${monto_retiro} de la cuenta.")
        mostrar_saldo(cuenta)
    else:
        print("Saldo insuficiente para realizar el retiro.")

# Función principal que ejecuta el menú
def main():
    cuenta = None
    while True:
        print("\nBienvenido a Bancosena\n")
        print("1. Crear cuenta")
        print("2. Abonar a la cuenta")
        print("3. Mostrar saldo")
        print("4. Retirar")
        print("5. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            cuenta = crear_cuenta()
            if cuenta:
                print("Cuenta creada exitosamente.")
                mostrar_saldo(cuenta)
        elif opcion == '2':
            if cuenta:
                abonar_cuenta(cuenta)
            else:
                print("Primero debe crear una cuenta.")
        elif opcion == '3':
            if cuenta:
                mostrar_saldo(cuenta)
            else:
                print("Primero debe crear una cuenta.")
        elif opcion == '4':
            if cuenta:
                retirar(cuenta)
            else:
                print("Primero debe crear una cuenta.")
        elif opcion == '5':
            print("Gracias por usar Bancosena. ¡Hasta luego!")
            break
        else:
            print("Opción inválida. Por favor, seleccione una opción válida (1-5).")

if __name__ == "__main__":
    main()
