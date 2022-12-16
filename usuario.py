class Usuario():
    
    lista_usuarios = []
    
    def __init__(self, nombre, apellido, cedula, edad):
        self.nombre = nombre
        self.apellido = apellido
        self.cedula = cedula
        self.edad = int(edad)
        
        self.lista_usuarios.append ({'nombre':nombre, 
                                    'apellido':apellido,
                                    'cedula': cedula,
                                    'edad': edad})

    def mostrarUsuarios(self, cedula):
        for p in self.lista_usuarios:
            if (p['cedula'] == cedula):
                print("\n|--------------------------------------------------|")
                print("| Nombre:" , p['nombre'] , p['apellido'])
                print("| Cedula:" , p['cedula'])
                print("| Edad:" , p['edad'])
            else :
                print("El numero de identificacion " + cedula + " no existe.")
