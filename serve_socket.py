import socket


def start_server():
    # Criação do socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Define o endereço e a porta do servidor
    server_address = ('localhost', 65432)
    # Associa o socket ao endereço e porta
    server_socket.bind(server_address)
    # Aguarda conexões (o argumento 1 especifica o número de conexões pendentes permitidas)
    server_socket.listen(2)

    print('Aguardando uma conexão...')

    # Aceita uma conexão
    connection, client_address = server_socket.accept()

    print(socket.gethostname())
    print("=-=-----------=-=--=-=-=-")

    try:
        print(f'Conexão estabelecida com {client_address}')

        # Recebe a mensagem do cliente
        while True:
            data = connection.recv(1024)
            print(f'Mensagem recebida: {data.decode()}')
            if data.decode() == 'sair':
                break

    finally:
        # Fecha a conexão
        connection.close()


if __name__ == "__main__":
    start_server()


# import socket
# #Referencia: https://blog.4linux.com.br/socket-em-python/ ---- https://medium.com/@urapython.community/introdu%C3%A7%C3%A3o-a-sockets-em-python-44d3d55c60d0 --- https://realpython.com/python-sockets/
# host = '127.0.0.1'
# port = 1234
# addr = (host, port)

# #Determina qual será o protocolo de comunicação AF_INET == IPV4 e SOCK_STREAM == TCP na camada de transporte (Nessa camada diz como irá tratar a entrega de dados.)
# serv_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# serv_socket.bind(addr)  #Associa o socket ao servidor
# serv_socket.listen(10)

# print ('aguardando conexao' )
# con, cliente = serv_socket.accept()
# print ('conectado' )
# print ("Aguardando mensagem")

# msg = ""

# try:
#     while True:
#         recebe = con.recv(1024) #A quantidade maxima de bytes que um paote pode ter
#         recebe = recebe.decode('utf-8')#Transforma de bit para str
#         msg += recebe
#         print(recebe)
#         if f'{recebe}' == "0":
#             break
#     print (f'mensagem recebida: {msg}')
#     con.sendall(msg.encode('utf-8'))

# except:
#   print('An exception occurred')

# serv_socket.close()
