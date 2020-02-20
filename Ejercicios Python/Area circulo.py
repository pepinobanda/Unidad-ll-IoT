class areaCircle:
  def areadelcirculo(self):
    print ("CALCULAR EL AREA DE UN CIRCULO")
    radio=input("CUAL ES EL RADIO: ")
    pi=3.1416
    area=float (pi) * int (radio) ** 2.0
    print("El área es: " + str (area))

area = areaCircle()
area.areadelcirculo()
