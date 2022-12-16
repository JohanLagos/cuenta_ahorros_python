from cuenta import Cuenta

class Beneficiario(Cuenta):
    
    def __init__(self, nombre, apellido, cedula, edad, cant_dineroAhorrado):
        super().__init__(nombre, apellido, cedula, edad, cant_dineroAhorrado)
        self.beneficiario = False

    def esBeneficiario(self, cedula):
        for p in self.lista_usuarios:
            if (p['cedula'] == cedula):
                if(p['edad']>=18 and p['edad']<28):
                    self.beneficiario = True
                    
                    p['beneficiario'] = "Si"
                    self.calcularBeneficio(cedula)
                    
                else:
                    p['beneficiario'] = "No"
                    
        return self.beneficiario
