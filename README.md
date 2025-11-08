# Olá! Bem-vindo ao Blockchain-101

Este repositório contem o conteúdo principal do trabalho apresentado por Victor Luis Romão, Lucas Pimentel Nunes, Ana Laura Brito, Eloisa Pajehú para a disciplina de Gestão de Projetos ministrada pelo professor Ayrton.

Você já se perguntou como o Bitcoin ou o Ethereum realmente funcionam "por baixo dos panos"? O blockchain pode parecer um conceito complexo, mas na verdade é construído a partir de algumas ideias simples e poderosas.

Este projeto é uma **biblioteca de blockchain em Python, criada do zero**, com um objetivo principal: **ser uma ferramenta educacional**.

A ideia aqui não é criar a próxima grande criptomoeda, mas sim desmistificar a tecnologia, mostrando de forma clara e objetiva os pilares que a sustentam.

## O que este código faz?

Esta biblioteca simula as funcionalidades centrais de uma blockchain básica. Com ela, você pode:

* **Criar Blocos:** A unidade fundamental que armazena dados de forma segura.
* **Gerenciar Transações:** Permite a "transferência" de informações ou valores, com segurança garantida por assinaturas digitais.
* **Construir a Cadeia (Blockchain):** Encadeia os blocos usando criptografia (hashes), tornando-a imutável.
* **Minerar Blocos (Proof-of-Work):** Simula o processo de "Prova de Trabalho" (como no Bitcoin) para validar novos blocos e adicioná-los à cadeia.
* **Validar a Integridade:** Contém funções para verificar se a cadeia é válida e não foi adulterada.

## Como Executar

Para ver a blockchain em ação, siga estes passos:

1.  **Clone o repositório:**
    ```bash
    git clone [https://github.com/dev-vromao/blockchain-101.git](https://github.com/dev-vromao/blockchain-101.git)
    cd blockchain-101
    ```

2.  **Instale as dependências:**
    *(É provável que você precise de algumas bibliotecas. Elas estão listadas no `requirements.txt`)*
    ```bash
    pip install -r requirements.txt
    ```

3.  **Veja a mágica acontecer!**
    Para rodar uma demonstração, execute o arquivo principal:
    ```bash
    python main.py
    ```
    *Dica: Dê uma olhada também nos arquivos `demos.py` e `examples.py` para ver outros cenários de uso.*

## O que tem em cada arquivo?

Para facilitar o estudo, o código foi dividido por responsabilidade:

* `blockchain.py`: O coração do projeto. É a classe que gerencia a cadeia de blocos, adiciona novos blocos e valida sua integridade.
* `block.py`: Define a "planta" de um Bloco (o que ele contém: transações, timestamp, o hash do bloco anterior, etc.).
* `transaction.py`: Define a estrutura de uma Transação (quem envia, quem recebe, valor) e o mais importante: como ela é assinada digitalmente.
* `miner.py`: Contém a lógica de mineração (Prova de Trabalho). É o código que "trabalha" para encontrar um hash válido e adicionar um novo bloco à cadeia.
* `crypto_utils.py`: Funções auxiliares de criptografia. É aqui que acontece a geração de chaves (pública/privada), o hashing (SHA-256) e a verificação de assinaturas.
* `main.py` / `demos.py` / `examples.py`: Arquivos de exemplo para executar e testar a blockchain na prática.
* `tests.py`: Testes automatizados para garantir que tudo funcione como esperado.

***

Sinta-se à vontade para explorar, modificar e aprender com este código!