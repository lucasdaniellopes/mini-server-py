from http.server import BaseHTTPRequestHandler, HTTPServer
import json

alunos = [
    {"id": 1, "nome": "João", "idade": 20},
    {"id": 2, "nome": "Maria", "idade": 21},
    {"id": 3, "nome": "Pedro", "idade": 22},
    {"id": 4, "nome": "Lucas", "idade": 22},
    {"id": 5, "nome": "Kaio", "idade": 19},
    {"id": 6, "nome": "Pablo", "idade": 35}]

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()
            self.wfile.write(b"<html><body><h1>Servidor Online!</h1></body></html>")
        
        elif self.path == '/data':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()
            self.wfile.write(json.dumps(alunos).encode())

def run(server_class=HTTPServer, handler_class=SimpleHTTPRequestHandler):
    server_address = ('', 8080)
    httpd = server_class(server_address, handler_class)
    print('Servidor HTTP rodando na porta 8080...')
    httpd.serve_forever()

if __name__ == '__main__':
    run()