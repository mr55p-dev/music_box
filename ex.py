import socket
import subprocess
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serversocket.bind(('localhost', 8089))
serversocket.listen(4)

def funct():
    print("It worked.")
    subprocess.call(['ffplay','-nodisp','-autoexit', './file.mp3'])
    return

# while True:
#     connection, address = serversocket.accept()
#     buf = connection.recv(64)
#     if len(buf) > 0:
#         print(buf)
#         funct()
#         serversocket.close()
#         break

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    sock.bind(('', 2000))
    sock.listen()
    host, port = sock.accept()
    with host:
        print("Connected by")
        print(host)
        # sock.send(b"""HTTP/1.1 200 OK\n
        #  Content-Type: text/html\n\n
        #  <html><body>Hello World</body></html>\n""")
        funct()
        # while True:
        #     data = host.recv(1024)
        #     if not data:
        #         break
    sock.close()
