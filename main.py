print("Porfavor ingrese los datos del libro: ")
name = input("Proporcione el nombre del libro: ")

id = int(input("Proporcione el ID del libro: "))

coste = float(input("Proporcione el precio del libro: "))

envio = input("Envio Gratis(True/False): ")

if envio=='True':
    envio = True
elif envio=='False':
    envio=False
else:
    envio = 'Valor incorrecto (True/False)'

print("El nombre del libro es: ",name)

print("El ID del libro es: ",id)

print("El costo del libro es: ",coste)

print("El envio del libro es: ",envio)