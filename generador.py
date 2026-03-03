import random

inicio = ["Tech", "Data", "Neo", "Smart", "Innova", "Cyber", "Auto", "Meta"]
medio = ["Solutions", "Labs", "Systems", "Works", "Soft", "Logic", "Dynamics"]
final = ["AI", "Pro", "X", "Hub", "Net", "Plus"]

print("🎯 Generador de Nombres IA\n")

cantidad = int(input("¿Cuántos nombres querés generar? "))

nombres_generados = set()

while len(nombres_generados) < cantidad:
    nombre = f"{random.choice(inicio)} {random.choice(medio)} {random.choice(final)}"
    nombres_generados.add(nombre)

for nombre in nombres_generados:
    print("-", nombre)