import requests

def fetch_content(url):
    response = requests.get(url)
    if response.status_code == 200:
        print("Resposta do Servidor:")
        print(response.text)
    else:
        print(f"Falha ao acessar {url}. Status code: {response.status_code}")

if __name__ == '__main__':
    url = 'http://localhost:8080'
    fetch_content(url)