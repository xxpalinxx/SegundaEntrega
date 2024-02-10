
class Cliente:
    def __init__(self,nombre,email,edad,direccion):
        self.nombre = nombre
        self.email = email
        self.edad = edad
        self.direccion = direccion

    def __str__(self):
        return f"El nombre del cliente es {self.nombre}"
    
    def imprimir_datos(self):
        datos = {"Nombre":self.nombre,"E-mail":self.email,"Edad":self.edad,"Dirección":self.direccion}
        for etiqueta, dato in datos.items():
            print(f"{etiqueta}: {dato}")
    
    def comprar(self,producto,local):
        self.producto = producto
        self.local = local
        print(f"Usted compro {self.producto} en el local {self.local}")
        self.realizar_envio()
        self.mandar_email()
    
    def realizar_envio(self):
        while True:
            try:
                eleccion = int(input("1- Retirar en local\n2- Envio a domicilio\nEscoja como obtener su producto: "))
                if eleccion == 1:
                    print(f"Usted puede retirar su producto ({self.producto}) en el local de {self.local}")
                    break
                elif eleccion == 2:
                    print(f"Su producto ({self.producto}) será enviado a {self.direccion}")
                    break
            except ValueError:
                print("Por favor, introducir valor valido")
    
    def mandar_email(self):
        print(f"La informacion de su compra se ha mandado a {self.email}")