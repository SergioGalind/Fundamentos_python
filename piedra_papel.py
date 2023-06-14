# Eleccion de maquina
import random

num_rand = random.randint(1,3)
if num_rand==1:
    choice_maq = 'Piedra'
elif num_rand ==2:
    choice_maq = 'Papel'
else: 
    choice_maq='Tijeras'
# Eleccion de usuario
choice_text = '''
Escribe una opcion:
    Piedra
    Papel   
    Tijeras
'''
choice_user = input(choice_text)
# imprime Selecion
print("usuario elige: ", choice_user)
print("Maquina elige: ", choice_maq)

#Define Ganador
if choice_user ==choice_maq:
    print("Es empate")
else:
    if choice_user == "Piedra" and choice_maq=="Papel":
        print("Gana maquina")
    elif choice_user == "Piedra" and choice_maq=="Tijeras":
        print("Gana usuario")
    elif choice_user == "Papel" and choice_maq=="Piedra":
        print("Gana usuario")
    elif choice_user == "Papel" and choice_maq=="Tijeras":
        print("Gana Maquina")
    elif choice_user == "Tijeras" and choice_maq=="Piedra":
        print("Gana Maquina")
    elif choice_user == "Tijeras" and choice_maq=="Papel":
        print("Gana Usuario")
    else:
        print("Escribe bien usuario")
