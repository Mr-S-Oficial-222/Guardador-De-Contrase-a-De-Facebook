print("guardador de contraseñas 3000")

face = input("tienes facebook (y/n)")

if face == "y":

    facecon = input("pon tu contraseña de facebook| ")
    faceuser = input("escribe tu nombre de usario de facebook| ")

def escribir():
    with open("Leer.txt", "a") as f:
        f.write(f"tu nombre de usuario de facebook es {faceuser} \n")
        f.write(f"tu contraseña de facebook es {facecon} \n")
        f.write("------------------------------------------------------")
escribir()    
