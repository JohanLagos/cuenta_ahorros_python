from os import system
from usuario import Usuario

class Cuenta (Usuario):
    
    def __init__(self, nombre, apellido, cedula, edad, cant_dineroAhorrado):
        # Herencia
        super().__init__(nombre, apellido, cedula, edad)
        
        # Atributo
        self.saldo = cant_dineroAhorrado
        
        for p in self.lista_usuarios:
            if (p['cedula'] == cedula):
                p['saldo'] = self.saldo

    def setSaldo(self, cedula, nuevo_saldo):
        for p in self.lista_usuarios:
            if (p['cedula'] == cedula):
                if(p['beneficiario'] == 'Si'):
                    p['saldo'] = nuevo_saldo
                    self.calcularBeneficio(cedula)
                else:
                    p['saldo'] = nuevo_saldo
    
    def getSaldo(self, cedula):
        for p in self.lista_usuarios:
            if (p['cedula'] == cedula):
                if(p['beneficiario'] == 'Si'):
                    saldo_total = p['saldoTotal']
                else:
                    saldo_total = p['saldo']
        return saldo_total
    
    def ingresar(self, cedula, din_ingresar):
        if(din_ingresar < 0):
            print("\n Valores Negativos no son Aceptados.")
            print(" Intenta de nuevo.")
        else:
            for p in self.lista_usuarios:
                if (cedula == p['cedula']):
                    saldo_nuevo = self.getSaldo(cedula) 
                    saldo_nuevo += din_ingresar
                    self.setSaldo(cedula, saldo_nuevo)
                    print("\n Consignacion Exitosa \n")
                    print("| El nuevo estado de su cuenta es: \n")
                    self.mostrarUsuarios(cedula)
    
    def retirar(self, cedula, din_retirar):
        if(din_retirar < 0):
            print("\n Valores Negativos no son Aceptados.\n")
        else:
            for p in self.lista_usuarios:
                if (cedula == p['cedula']):
                    saldo_cuenta = self.getSaldo(cedula) 
                    if(din_retirar > saldo_cuenta):
                        print("\n Saldo insuficiente....\n")
                    else:
                        saldo_cuenta -= din_retirar
                        self.setSaldo(cedula, saldo_cuenta)
                        print("\n Retiro Exitoso \n")
                        print("| El nuevo estado de su cuenta es:")
                        self.mostrarUsuarios(cedula)
    
    def calcularBeneficio(self, cedula):
        for p in self.lista_usuarios:
            if (p['cedula'] == cedula):
                interes = int((p['saldo']) * 0.05)
                saldo_total = int(p['saldo']) + interes
                
                p['interes'] = interes
                p['saldoTotal'] = saldo_total

    def revisar_cunta(self):
        system("cls")
        print("\n|------------------------ ESTADO DE CUENTA ------------------------|")
        print("|")
        cc_usuario= input("| Digite su numero de identificacion: ")
        self.mostrarUsuarios(cc_usuario)
    

    def mostrarUsuarios(self, cedula):
        
        for p in self.lista_usuarios:
            if (p['cedula'] == cedula):
                if(p['beneficiario'] == 'Si'):
                    print("\n|--------------------------------------------------|")
                    print("| Nombre:" , p['nombre'] , p['apellido'])
                    print("| Cedula:" , p['cedula'])
                    print("| Edad:" , p['edad'])
                    print("|")
                    print("| Beneficiario-Joven:" , p['beneficiario'])
                    print("|")
                    print("| Saldo: $" + '{:,}'.format(p['saldo']).replace(',' , '.'))
                    print("| Interes Beneficiario-Joven: $" + '{:,}'.format(p['interes']).replace(',' , '.'))
                    print("|")
                    print("| Saldo Total: $" + '{:,}'.format(p['saldoTotal']).replace(',' , '.'))
                    print("|")
                    print("|--------------------------------------------------|\n")
                else :
                    print("\n|--------------------------------------------------|")
                    print("| Nombre:" , p['nombre'] , p['apellido'])
                    print("| Cedula:" , p['cedula'])
                    print("| Edad:" , p['edad'])
                    print("|")
                    print("| Beneficiario-Joven:" , p['beneficiario'])
                    print("| Saldo: $" + '{:,}'.format(p['saldo']).replace(',' , '.'))
                    print("|")
                    print("|--------------------------------------------------|\n")