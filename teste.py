import telnetlib

#Declarando a variável que aponta para o device remoto
HOST = "192.168.73.131"
user = input("Por favor, indique um usuário válido: ")
password = input("Dígite a senha: ")

#Associando a variável HOST à função
tn = telnetlib.Telnet(HOST)

tn.read_until(b"Username: ")
tn.write(user.encode('ascii') + b"\n")

if password:
    tn.read_until(b"Password: ")
    tn.write(password.encode('ascii') + b"\n")

#Associando a sintaxe de execução com os atributos IOS

tn.write(b"enable\n")
tn.write(b"thiago\n")
tn.write(b"conf t\n")
tn.write(b"no hostname R1-ALFA\n")
tn.write(b"hostname R1-ALFA\n")
tn.write(b"end\n")
tn.write(b"copy running-config startup-config\n")
tn.write(b"\n")
tn.write(b"exit\n")

print(tn.read_all().decode('ascii'))
