## Echo server program
import socket
import subprocess


def get_routing_table():
  completed_proc = subprocess.run(['ip route'], shell=True, stdout=subprocess.PIPE)
  return completed_proc.stdout


HOST = ''                 # Symbolic name meaning all available interfaces
PORT = 50008              # Arbitrary non-privileged port
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen()
conn, addr = s.accept()
if conn:
  print('Connected by', addr)
  while True:
    data = conn.recv(1024)
    print(data.decode())
    if not data: break
    elif data.decode('utf-8') == 'get route table':
      data_to_send = get_routing_table()
      conn.sendall(data_to_send)





