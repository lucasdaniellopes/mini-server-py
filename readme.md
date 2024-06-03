## Mini Servidor de Alunos - Frontend e Backend Simples

Este projeto demonstra um sistema básico de servidor e cliente para exibir uma lista de alunos.

### **Frontend:**

* **HTML (index.html):** Cria a estrutura da página web, incluindo:
    * Título da página.
    * Lista desordenada (`<ul>`) para exibir os alunos.
    * Botão para atualizar a lista (`<button>`).
* **CSS (style.css):** Define o estilo visual da página, incluindo formatação da lista e do botão.
* **JavaScript (script.js):**
    * Realiza requisições HTTP GET ao servidor para obter a lista de alunos.
    * Cria elementos HTML dinamicamente para cada aluno e os adiciona à lista na página.
    * Adiciona um evento de clique ao botão para atualizar a lista quando o usuário clicar.

### **Backend:**

* **Python (server.py):** Cria um servidor web simples usando Flask.
    * Define um endpoint (`/data`) que responde com uma lista de alunos em formato JSON.

### **Como Executar:**

1. **Instalar Flask:** Se você ainda não tiver o Flask instalado, execute o comando `pip install Flask` no seu terminal.
2. **Iniciar o servidor:** Execute o arquivo `server.py` no seu terminal.
3. **Abrir a página HTML:** Abra o arquivo `index.html` em um navegador web.

### **Como Funciona:**

1. O navegador carrega o arquivo `index.html` e executa o código JavaScript.
2. O JavaScript envia uma requisição GET ao servidor na URL `/data`.
3. O servidor responde com uma lista de alunos em formato JSON.
4. O JavaScript processa os dados JSON e cria elementos HTML para cada aluno.
5. Os elementos HTML são adicionados à lista na página web.
6. Ao clicar no botão "Atualizar Lista", o processo é repetido, atualizando a lista com dados do servidor.

### **Observações:**

* Este é um exemplo simples de um sistema cliente-servidor.
* Você pode estender o código para:
    * Adicionar funcionalidades de adicionar, editar ou remover alunos.
    * Implementar autenticação para acessar o servidor.
    * Criar uma interface gráfica mais sofisticada.
    * Usar um banco de dados para armazenar os dados dos alunos.
