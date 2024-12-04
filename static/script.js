async function carregarMoedas() {
    try {
        const response = await axios.get('/moedas');
        const moedas = response.data;
        const listaMoedas = document.getElementById('listaMoedas');
        const selectOrigem = document.getElementById('moedaOrigem');
        const selectDestino = document.getElementById('moedaDestino');

        moedas.forEach(moeda => {
            const li = document.createElement('li');
            li.textContent = moeda;
            listaMoedas.appendChild(li);

            const optionOrigem = document.createElement('option');
            optionOrigem.value = moeda;
            optionOrigem.textContent = moeda;
            selectOrigem.appendChild(optionOrigem);

            const optionDestino = document.createElement('option');
            optionDestino.value = moeda;
            optionDestino.textContent = moeda;
            selectDestino.appendChild(optionDestino);
        });
    } catch (error) {
        console.error('Erro ao carregar moedas:', error);
    }
}

document.getElementById('conversorForm').addEventListener('submit', async (e) => {
    e.preventDefault();
    const valor = document.getElementById('valor').value;
    const moedaOrigem = document.getElementById('moedaOrigem').value;
    const moedaDestino = document.getElementById('moedaDestino').value;

    try {
        const response = await axios.post('/converter', {
            valor: valor,
            moeda_origem: moedaOrigem,
            moeda_destino: moedaDestino
        });
        document.getElementById('resultado').innerText = `Resultado: ${response.data.resultado} ${moedaDestino}`;
    } catch (error) {
        document.getElementById('resultado').innerText = `Erro: ${error.response.data.erro}`;
    }
});
window.onload = carregarMoedas;