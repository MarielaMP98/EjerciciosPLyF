"""
	https://www.computrabajo.com.mx/ofertas-de-trabajo/oferta-de-trabajo-de-desarrollador-batch-exp-sistemas-abiertos-en-queretaro-601BC72F6CEBB0F761373E686DCF3405
	En una empresa solicitan Lic./Ing. en Sistemas, Computación o afín.
	con los siguientes requisitos:
	• Oracle BBDD

	• SQL y PL/SQL

	• Linux

	• Unix

	• Shell (Linux - Unix)

	• C++, Proc*C y Tuxedo V12 o anteriores

	• Visual Basic 6.0

	• Java (Frameworks) , Web Services y Micro Servicios APIs
	
	Realizar un programa que realice preguntas al usuario
	y que apartir de sus respuestas evalue si es cadidato o no
	
	(usen conjuntos)
"""

Requisitos = {
	"Oracle","SQL/PL","Linux","Unix","Shell","C++",
	"Proc*C","TuxedoV12", "VB6", "Java","WebServices","MicroServicios"
} 

print(Requisitos)

print("Tiene experiencia en las siguientes cuestiones")
print("Responda SI o NO")

def esCandidato():
	R1 = input("\n Oracle BBDD   : ").upper()
	R2 = input(" SQL y PL/SQL  : ").upper()
	R3 = input(" Linux         : ").upper()
	R4 = input(" Unix          : ").upper()
	R5 = input(" Shell (Linux - Unix) : ").upper()
	R6 = input(" C++           : ").upper()
	R7 = input(" Proc*C        : ").upper()
	R8 = input(" TuxedoV12     : ").upper()
	R9 = input(" VB6           : ").upper()
	R10 = input(" Java          : ").upper()
	R11 = input(" WebServices   : ").upper()
	R12 = input(" MicroServicios: ").upper()
	Resp = set()
	if R1 == "SI":
		Resp.add("Oracle")
	if R2 == "SI":
		Resp.add("SQL/PL")
	if R3 == "SI":
		Resp.add("Linux")
	if R4 == "SI":
		Resp.add("Unix")
	if R5 == "SI":
		Resp.add("Shell")
	if R6 == "SI":
		Resp.add("C++")
	if R7 == "SI":
		Resp.add("Proc*C")
	if R8 == "SI":
		Resp.add("TuxedoV12")
	if R9 == "SI":
		Resp.add("VB6")
	if R10 == "SI":
		Resp.add("Java")
	if R11 == "SI":
		Resp.add("WebServices")
	if R12 == "SI":
		Resp.add("MicroServicios")
	Diferencia = Requisitos - Resp
	Interseccion = Requisitos & Resp
	print("\nExperiencia Del Usuario ",Resp)
	print("\nHabilidades Que No Tiene El Usuario ",Diferencia)
	Req = len(Requisitos)
	Exp = len(Interseccion)
	Req_minimos = Req - 4
	if Exp >= Req_minimos:
		return "\nEs candidato"
	else:
		return "\nNO es Candidato"

print(esCandidato())
