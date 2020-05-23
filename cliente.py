import socket,psutil,pickle

# AF_INET = IPv4
# SOCK_STREAM = TCP

host = socket.gethostname()
porta = 9991
destino = (host,porta)
# Usado para UDP
servidor = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

# Arquivo a ser enviado
disco = psutil.disk_usage('/')
disco_lista = {'Disco Total': (disco.total / 1024 ** 3, "GB"), 'Disco Usado': (disco.used / 1024 ** 3,"GB"), 'Disco Livre': (disco.free / 1024 ** 3,"GB")}

try :
    informacao_bytes = pickle.dumps(disco_lista)
    # Enviar informação para o cliente
    servidor.sendto(informacao_bytes,destino)
    # Encerra a conexao
    servidor.close()

    # Biblioteca padrao Exception
except Exception as erro:
    print(str(erro))