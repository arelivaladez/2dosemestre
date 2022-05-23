class tenis:
	ID = 4005
	Marca = "Adidas"
	Precio= 1000
	Color = "Azul"

	def tenismarca(self):
		pass

	def teniscolor(self):
	return self.Marca 


	def precioten(self):
		if self.precio() > 1000:
			print("Son originales")
		else:
			print("No son originales")

Persona = tenis()
Persona.precioten()
Persona.teniscolor="Rojo"
Persona.precio=1500
print(Persona.precio)
Persona.precioten()