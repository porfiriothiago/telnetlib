import getpass
import telnetlib

#Declarando a variável que aponta para o device remoto
HOST = "192.168.73.131"
user = input("Por favor, indique um usuário válido: ")
password = getpass.getpass()

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
tn.write(b"hostname R1-SP\n")
tn.write(b"int lo 0\n")
tn.write(b"ip add 200.0.0.1 255.255.255.255\n")
tn.write(b"int lo 1\n")
tn.write(b"ip add 200.0.0.2 255.255.255.255\n")
tn.write(b"int lo 2\n")
tn.write(b"ip add 200.0.0.3 255.255.255.255\n")
tn.write(b"int lo 3\n")
tn.write(b"ip add 200.0.0.4 255.255.255.255\n")
tn.write(b"end\n")
tn.write(b"copy running-config startup-config\n")
tn.write(b"\n")

print(tn.read_all().decode('ascii'))