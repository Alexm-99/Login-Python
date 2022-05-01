from pymongo import MongoClient

class Sesion():
    def __init__(self):
        self.client = MongoClient('localhost' , 27017)
        self.db = self.client['datos']
        self.coleccion= self.db['login']

    def insertar(self, datos):
        
        self.coleccion.insert_one(datos)

    def consulta(self, usuario, passwd):
        datos = {'usuario':usuario, 'clave': passwd}
        consulta = self.db.login.find_one(datos)
        return consulta
        #for i in consulta:
            #print(i)

if __name__== '__main__':
    dato = Sesion()
    #x = dato.consulta({'usuario':'admin02', 'clave': '12345'})
    #print(x)
    #dato.insertar({'usuario':'admin01', 'clave': 'd404559f602eab6fd602ac7680dacbfaadd13630335e951f097af3900e9de176b6db28512f2e000b9d04fba5133e8b1c6e8df59db3a8ab9d60be4b97cc9e81db'})