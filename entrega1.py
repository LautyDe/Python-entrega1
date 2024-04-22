""" registro de usuario
usuario: nombre y contrasenia
almacenado en diccionario 
hacer funcion de loguin de usuarios
""" 

users = {'lautaro': '123456', 'matias': '123456'}



def createUser():
  username = input("Ingrese su nombre de usuario: ")
  password = input("Ingrese su contrasenia: ")
  users[username] = password
  print("Usuario guardado con exito")

def seeUsers():
  print(users)

def login(username, password):
  contador = 1
  while (not username in users):
    if(contador < 3): 
      print("Usuario o contrasenia incorrectos, por favor ingreselos de nuevo 1: ")
      username = input("Ingrese su nombre de usuario: ")
      password = input("Ingrese su contrasenia: ")
      contador += 1
    else:
      print('HOLA')
      return False
  else:
    if users[username] != password:
      print("Usuario o contrasenia incorrectos, por favor ingreselos de nuevo 2: ")
      username = input("Ingrese su nombre de usuario: ")
      password = input("Ingrese su contrasenia: ")
      contador += 1
    else:
      return True
    



def main():
  opcion = 0
  while(opcion != 4):
    print("Ingrese 1 para agregar un usuario")
    print("Ingrese 2 para ver los usuarios")
    print("Ingrese 3 para loguearse")
    print("Ingrese 4 para finalizar")
    opcion = int(input("Ingrese la opcion seleccionada: "))
    if(opcion == 1):
      createUser()
    elif(opcion == 2):
      seeUsers()
    elif(opcion == 3):
      username = input("Ingrese su nombre de usuario: ")
      password = input("Ingrese su contrasenia: ")
      loginOk = login(username, password)
      if not loginOk:
        print("Credenciales invalidas, cerrando ejecucion")
        break
      else :
        print("Logueo completo!")
        break
    elif(opcion == 4):
      print("Hasta pronto!")
      break



main()
