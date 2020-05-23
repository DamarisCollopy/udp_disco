import socket,psutil,pickle

# AF_INET = IPv4
# SOCK_STREAM = TCP

host = socket.gethostname()
porta = 9991

# Usado para UDP
servidor = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

servidor.bind((host, porta))
print((f"Servidor {host} experando conexao na porta {porta}"))

while True:
    # Diferente do TCP o UDP recebe a mensagem primeiro do cliente
    bytes, endereco = servidor.recvfrom(1024)

    # Recebe um conjunto de bytes, preciso tratar a lista uso pickle
    # Converter bytes em uma lista
    lista = pickle.loads(bytes)
    print(lista)

    servidor.close()


