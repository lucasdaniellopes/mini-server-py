from http.server import BaseHTTPRequestHandler, HTTPServer
import json

alunos = [
    {"id": 1, "nome": "João", "idade": 20},
    {"id": 2, "nome": "Maria", "idade": 21},
    {"id": 3, "nome": "Pedro", "idade": 22}]

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(b"<html><body><h1>Ola, Mundo!</h1></body></html>")
        elif self.path == '/data':
            # Se a URL for '/data', envia o arquivo JSON
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps(alunos).encode())

def run(server_class=HTTPServer, handler_class=SimpleHTTPRequestHandler):
    server_address = ('', 8080)
    httpd = server_class(server_address, handler_class)
    print('Servidor HTTP rodando na porta 8080...')
    httpd.serve_forever()

if __name__ == '__main__':
    run()