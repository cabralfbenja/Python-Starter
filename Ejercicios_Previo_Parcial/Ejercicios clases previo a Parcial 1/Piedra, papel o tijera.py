import random

print("Juego de PIEDRA, PAPEL o TIJERA")

opciones = ("PIEDRA", "PAPEL", "TIJERA", "SPOCK", "LAGARTO")
print("Elija entre las opciones:\n0)Piedra\n1)Papel\n2)Tijera\n3)Spock\n4)Lagarto")
opc_usuario = int(input("Elección: "))

opc_pc = random.choice(opciones)
opc_usr = opciones[opc_usuario]
if opciones[opc_usuario] == opc_pc:
    ganador = "Empate!!"
else:
    if opc_usr == "PAPEL" and opc_pc == "PIEDRA" or opc_usr == "PIEDRA" and opc_pc == "TIJERA" or \
        opc_usr == "TIJERA" and opc_pc == "PAPEL" or opc_usr == "PAPEL" and opc_pc == "SPOCK" or \
            opc_usr == "PIEDRA" and opc_pc == "LAGARTO" or opc_usr == "TIJERA" and opc_pc == "LAGARTO"\
            or opc_usr == "LAGARTO" and opc_pc == "SPOCK" or opc_usr == "LAGARTO" and opc_pc == "PAPEL"\
            or opc_usr == "SPOCK" and opc_pc == "TIJERA" or opc_usr == "SPOCK" and opc_pc == "PIEDRA":
        ganador = "Ganaste!!"
    else:
        ganador = "Perdiste!!"

print("Elección de la PC:", opc_pc, "\tElección del usuario:", opc_usr)
print("El resultado fue:", ganador)
print("Fin del Juego")
