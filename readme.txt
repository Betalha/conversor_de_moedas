Esta aplicação é um conversor de moedas que mostra a implementação de uma Arquitetura Orientada a Serviços (SOA) de forma simples. 

Aqui está um breve resumo com ênfase na arquitetura:

A aplicação segue os princípios da SOA, dividindo a funcionalidade em serviços independentes e interoperáveis:

- Serviço de Taxa de Câmbio: Responsável por obter as taxas de câmbio atualizadas de uma API externa.
- Serviço de Conversão: Utiliza as taxas de câmbio para realizar os cálculos de conversão entre moedas.
- Aplicação Principal: Atua como orquestrador, integrando os serviços e fornecendo uma interface web.

Componentes Principais:
- API Gateway (app.py): Gerencia as requisições HTTP e coordena a comunicação entre a interface do usuário e os serviços internos.
- Serviços (services/): Implementados como módulos Python separados, encapsulando lógicas específicas.
- Interface do Usuário (index.html): Uma página web simples..
- Lógica da interface web (script.js): Responsável pela implementação de lógicas e por interagir com o backend via requisições AJAX.