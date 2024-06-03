import { getAlunos } from "./requests"

listaAlunos = document.getElementsByClassName("listaAlunos")
btn = document.getElementsByClassName("attBtn")

console.log(await getAlunos())
