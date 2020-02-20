class calcuAreaTri:
    def areatriangulo(self):
        print ("CALCULAR EL AREA DE UN TRIANGULO")
        b=input("CUAL ES LA BASE: ")
        a=input("CUAL ES LA ALTURA: ")
        area=int (b) * int (a) / 2.0
        print ("El área es: " + str (area))
        
calcular = calcuAreaTri()
calcular.areatriangulo()  
