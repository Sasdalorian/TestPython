# Hola Mundo!
'''
Hola 
esto es un 
comentario
'''


print("hello world")

my_string = "Hola soy un string"
my_other_string = "Hola cambie el string"

# No se require definir como variable ni constante
print(type(my_string))
print(my_string)

my_int = 6 #Tipado dinámico

print(type(my_int))
print(my_int)


my_int = 3
my_int = 6
my_bool = True
my_bool = False

print(type(my_bool))
print(my_bool)

print("El valor de mi entero es: " + str(my_int) + ", y el valor de mi bool es: " + str(my_bool) + ".")

print(f"El valor de mi entero es: {my_int}, y el valor de mi bool es: {my_bool}.")

my_list = [ my_string, my_int, my_other_string, my_bool]
print(type(my_list))
print(my_list)
print(my_list[2])

# La clave debe ser unica
my_dict = {"String": my_string, "Int": my_int, "Other_String": my_other_string, "Nombre": "Sas"}
print(type(my_dict))
print(my_dict)
print(my_dict["Nombre"])

my_int = 1
my_bool = True

if my_int == 1 and my_bool == True:
  print("El valo es 1 y el bool es True")
elif my_int == 2:
  print("El valor es 2")
else:
  print("El valor no es 1 ni 2")