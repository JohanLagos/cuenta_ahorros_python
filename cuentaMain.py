from os import system
import os
from beneficiario import Beneficiario

class CuentaMain():
    
    def __init__(self):
        self.menu()
    
    def registrar_usuario(self):
        
        system("cls") # Limpiar Ventana
        
        # Menú de registro de usuario
        print("\n|------------------ REGISTRO DE NUEVA CUENTA ----------------|\n")
        print("|--------- Datos Personales ---------|")
        print("|")
        cedula = input("| Digite su número de identificación: ")
        nombre = input("| Digite su Nombre: ")
        apellido = input("| Digite su Apellido: ")
        edad = int(input("| Digite su Edad: "))
        print("|")
        print("|------ Saldo Inicial -------")
        print("|")
        saldo_inicial = int(input('| Digite el Saldo Inicial : $ '))
        if saldo_inicial < 0 :
            print("\n Valores negativos no Aceptados")
            print(" Registro Invalido... \n")
        else:
            # Creación de un nuevo Usuario
            self.nueva_cuenta = Beneficiario(nombre, apellido, cedula, edad,  saldo_inicial)
    
            #Verificacion si es apto para Beneficiario-Joven
            self.nueva_cuenta.esBeneficiario(cedula)
            
            print("\n|---------------**** REGISTRO EXITOSO ****--------------------|\n")
    
    def realizar_movimiento(self):
        
        system("cls")
        
        print("\n|------------------ REALIZAR UN MOVIMIENTO ----------------|\n")
        print(" 1. Consinar.")
        print(" 2. Retirar.")
        print(" 3. Volver al Menu.\n")
            
        op = int(input("| -- Digite una opción: "))
            
        match op:
            case 1:
                print("\n|")
                cc_usuario= input("| Digite su cedula: ")
                for p in self.nueva_cuenta.lista_usuarios:
                    if (cc_usuario == p['cedula']):
                        print("|")
                        print("| Hola" , p['nombre'] , p['apellido'])
                        print("|")
                        din_ingresar= int(input("| Digite la cantidad de dinero que desea consignar: $ "))
                        self.nueva_cuenta.ingresar(cc_usuario,din_ingresar)
                        print("\n")
            case 2:
                print("\n|")
                cc_usuario= input("| Digite su cedula: ")
                for p in self.nueva_cuenta.lista_usuarios:
                    if (cc_usuario == p['cedula']):
                        print("|")
                        print("| Hola" , p['nombre'] , p['apellido'])
                        print("|")
                        din_retirar= int(input("| Digite la cantidad de dinero a retirar: $ "))
                        self.nueva_cuenta.retirar(cc_usuario, din_retirar)
                        print("\n")
            case 3:
                self.menu()
            case _:
                self.realizar_movimiento()
    
    
    def mostrarCuentas(self):
        
        system("cls") # Limpiar pantalla
        
        print("\n|------------------------ LISTADO DE CUENTAS ------------------------|")
        print("|")
        for p in self.nueva_cuenta.lista_usuarios:
            self.nueva_cuenta.mostrarUsuarios(p['cedula'])
    
    def menu(self):
        
        system("cls")
        
        active = True
        
        while (active):
            print("\n|------------------ CAJERO AUTOMATICO ----------------|\n")
            print(" 1. Registrar Nueva Cuenta.")
            print(" 2. Realizar Un Movimiento.")
            print(" 3. Revisar Estado de Cuenta.")
            print(" 4. Cuentas.")
            print(" 5. Salir.\n")
            opcion = int(input(" Por Favor, Digite una Opcion: "))
            
            match opcion: 
                case 1:
                    self.registrar_usuario()
                    os.system("pause")
                case 2:
                    self.realizar_movimiento()
                    os.system("pause")
                case 3:
                    self.nueva_cuenta.revisar_cunta()
                    os.system("pause")
                case 4:
                    self.mostrarCuentas()
                    os.system("pause")
                case 5:
                    active = False
                    print("Finalizando......")
                case _:
                    print("\n Opcion no valida, Vuelva a intentar.\n")

if __name__ == "__main__": 
    CuentaMain()