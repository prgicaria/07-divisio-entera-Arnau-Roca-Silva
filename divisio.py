# Demanem valors enters per a divisor(n2) i dividend(n1):
n2=int(input("Introdueix el divisor"))
n1=int(input("Introdueix el dividend"))

#Calculem el residu i el quocient:
residu=n1%n2
quocient=n1//n2

#Mostrem per pantalla de manera ordenada:
print(f"Divisió: {n1}/{n2}")
print(f"Quocient: {quocient}")
print(f"Residu: {residu}")