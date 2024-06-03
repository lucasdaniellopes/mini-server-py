const listaAlunos = document.querySelector(".listaAlunos");
const btn = document.querySelector(".attBtn");
const baseUrl = "http://localhost:8080/";
/* fetchData = {
    method: 'GET',
    headers: new Headers,
    body: ''
}*/

function getAlunos() {
  const response = fetch(`${baseUrl}data`).then((resp) => resp.json());
  return response;
}
/*async function getAlunos() {
  const response = await fetch(baseUrl);
  const data = await response.json();
  return data;
}*/

console.log(await getAlunos());

btn.addEventListener("click", async (event) => {
  listaAlunos.innerHTML = "";
  const alunos = await getAlunos();

  alunos.forEach((aluno) => {
    const li = document.createElement("li");
    const id = document.createElement("span");
    const nome = document.createElement("p");
    const idade = document.createElement("span");

    nome.innerHTML = `<b>Nome</b>: ${aluno.nome}`;
    id.innerHTML = `<b>ID</b>: ${aluno.id}`;
    idade.innerHTML = `<b>Idade</b>: ${aluno.idade}`;

    li.append(id, nome, idade);

    listaAlunos.appendChild(li);
  });
});
