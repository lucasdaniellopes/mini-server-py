baseUrl = 'http://localhost:8080';
fetchData = {
    method: 'GET',
    headers: new Headers,
    body: ''
}

/* async function getAlunos() {
    response = await fetch(`${baseUrl}/data`)
    .then(resp => resp.json())
    return response
}

export {getAlunos}*/

async function getAlunos() {
    const response = await fetch(`${baseUrl}/`);
    const data = await response.json();
    return data;
}

export { getAlunos };