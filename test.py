from socket import *

sock = socket(AF_INET, SOCK_STREAM)
sock.bind(('', 8888))
sock.close()